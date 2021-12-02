from django.urls import path, include
from .views import SignUpView, TokenView, UserViewSet
from rest_framework.routers import SimpleRouter
from .views import CategoryViewSet, GenreViewSet, TitleViewSet


router = SimpleRouter()
router.register('users', UserViewSet)
router.register(r'users/me/', UserViewSet)
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register('titles', TitleViewSet, basename='titles')

urlpatterns = [
    path('v1/auth/signup/', SignUpView.as_view()),
    path('v1/auth/token/', TokenView.as_view()),
    path('v1/', include(router.urls)),
]
