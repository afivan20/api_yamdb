from django.urls import path, include
from .views import SignUpView, TokenView, UserViewSet
from rest_framework.routers import SimpleRouter
from .views import CategoryViewSet, GenreViewSet, TitleViewSet
from .views import CategoriesDelete, GenreDelete
from .views import ReviewViewSet, CommentViewSet

router = SimpleRouter()
router.register('users', UserViewSet)
router.register(r'users/me/', UserViewSet)
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register('titles', TitleViewSet, basename='titles')
router.register(r'v1/titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='comments')
router.register(r'v1/titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
                CommentViewSet, basename='comments')


urlpatterns = [
    path('v1/auth/signup/', SignUpView.as_view()),
    path('v1/auth/token/', TokenView.as_view()),
    path('v1/categories/<slug:slug>/', CategoriesDelete.as_view()),
    path('v1/genres/<slug:slug>/', GenreDelete.as_view()),
    path('v1/', include(router.urls)),
]
