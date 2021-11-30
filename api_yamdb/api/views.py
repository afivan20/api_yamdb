from django.shortcuts import render
from rest_framework import viewsets
from reviews.models import Category, Genre, Title
from .serializers import CategorySerializer
from .serializers import GenreSerializer
from .serializers import TitleSerializer
from .permissions import IsAuthorOrReadOnlyPermission
from .permissions import IsAdminUserOrReadOnly
from .permissions import IsAll


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAll,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


class GenreViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAll,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = None


class TitleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAll,)
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    pagination_class = None
