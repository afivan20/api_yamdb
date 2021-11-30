from django.shortcuts import render
from rest_framework import viewsets
from reviews.models import Category, Genre, Title


class CategoryViewSet(viewsets.ModelViewSet):
    pass


class GenreViewSet(viewsets.ModelViewSet):
    pass


class TitleViewSet(viewsets.ModelViewSet):
    pass
