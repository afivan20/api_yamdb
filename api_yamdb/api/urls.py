from django.urls import path, include
from rest_framework import routers

from .views import CategoryViewSet, GenreViewSet, TitleViewSet

router = routers.DefaultRouter()
router.register(r'v1/categories/', CategoryViewSet, basename='categories')
router.register(r'v1/genres/', GenreViewSet, basename='genres')
router.register('v1/titles', TitleViewSet, basename='titles')


urlpatterns = [
    path('', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
