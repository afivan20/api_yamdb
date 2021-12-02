from rest_framework import viewsets
from reviews.models import Category, Genre, Title
from .serializers import CategorySerializer
from .serializers import GenreSerializer
from .serializers import TitleSerializer
# from .permissions import IsAuthorOrReadOnlyPermission
# from .permissions import IsAdminUserOrReadOnly
from .permissions import IsAll
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


class CategoryViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    permission_classes = (IsAll,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination


class GenreViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    permission_classes = (IsAll,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination


class TitleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAll,)
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    pagination_class = None
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ('category__name', 'genre', 'name', 'year',)
    ordering_fields = ('name', 'year')
    pagination_class = PageNumberPagination
