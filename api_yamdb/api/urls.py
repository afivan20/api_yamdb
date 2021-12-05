from django.urls import path, include
from .views import ReviewViewSet, SignUpView, TokenView, UserViewSet
from rest_framework.routers import SimpleRouter
from .views import CategoryViewSet, GenreViewSet, TitleViewSet
from .views import CategoriesDelete, GenreDelete


router = SimpleRouter()
router.register('users', UserViewSet)
router.register(r'users/me/', UserViewSet)
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register('titles', TitleViewSet, basename='titles')
router.register(
    r'titles/(?P<title_id>[^/.]+)/reviews',
    ReviewViewSet, basename='reviews'
)

urlpatterns = [
    path('v1/auth/signup/', SignUpView.as_view()),
    path('v1/auth/token/', TokenView.as_view()),
    path('v1/categories/<slug:slug>/', CategoriesDelete.as_view()),
    path('v1/genres/<slug:slug>/', GenreDelete.as_view()),
    path('v1/', include(router.urls)),
]
