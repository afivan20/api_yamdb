from rest_framework import generics, status, viewsets
from rest_framework import filters, mixins, viewsets
from .serializers import SignUpSerializer, UserTokenSerializer, UserSerializer
from reviews.models import User
from uuid import uuid1
from django.core.mail import send_mail
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from reviews.models import Category, Genre, Title
from .serializers import CategorySerializer
from .serializers import GenreSerializer
from .serializers import TitleSerializer, TitleSerializerView
from .permissions import IsAdminUserOrReadOnlyGenCat, IsAdmin


class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        username = serializer.data['username']
        secret = str(uuid1())
        User.objects.create(
            username=username,
            email=email,
            confirmation_code=secret
        )
        send_mail(
            'Confirmation code',
            f'Используйте этот код для входа в учетную запись - {secret}',
            'admin@yamdb.com',
            [email],
            fail_silently=False,
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class TokenView(APIView):
    def post(self, request):
        serializer = UserTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data['username']
        user = get_object_or_404(User, username=username)
        refresh = RefreshToken.for_user(user)
        return Response(
            {"access": str(refresh.access_token)},
            status=status.HTTP_200_OK,
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsAdmin)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('username',)
    lookup_field = 'username'
    pagination_class = PageNumberPagination

    @action(
        detail=False, methods=['PATCH', 'GET'],
        permission_classes=(IsAuthenticated,)
    )
    def me(self, request):
        serializer = UserSerializer(request.user,
                                    data=request.data,
                                    partial=True)

        if request.user.is_admin or request.user.is_moderator:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer.is_valid(raise_exception=True)
        serializer.save(role='user')
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin, viewsets.GenericViewSet):
    http_method_names = ['get', 'post']
    permission_classes = (IsAdminUserOrReadOnlyGenCat,)
    queryset = Category.objects.all().order_by('id')
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin, viewsets.GenericViewSet):
    http_method_names = ['get', 'post']
    permission_classes = (IsAdminUserOrReadOnlyGenCat,)
    queryset = Genre.objects.all().order_by('id')
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination


class TitleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUserOrReadOnlyGenCat,)
    queryset = Title.objects.all()

    def get_serializer_class(self):
        if (self.request.method == 'POST'
                or self.request.method == 'PATCH'
                or self.request.method == 'PUT'):
            return TitleSerializer
        return TitleSerializerView

    serializer_class = TitleSerializer
    pagination_class = None
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ('category__name', 'genre__slug', 'name', 'year',)
    ordering_fields = ('name', 'year')
    pagination_class = PageNumberPagination


class CategoriesDelete(generics.DestroyAPIView):
    lookup_field = 'slug'
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAdmin,)


class GenreDelete(generics.DestroyAPIView):
    lookup_field = 'slug'
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = (IsAdmin,)
