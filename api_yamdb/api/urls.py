from django.urls import path, include
from rest_framework import routers

from .views import CategoryViewSet, GenreViewSet, TitleViewSet

router = routers.DefaultRouter()
router.register('v1/categories', CategoryViewSet, basename='categories')
router.register('v1/genres', GenreViewSet, basename='genres')
router.register('v1/titles', TitleViewSet, basename='titles')

# router.register(r'v1/posts/(?P<post_id>\d+)/comments',
#                 CommentViewSet, basename='comments')
# router.register(r'v1/groups', GroupViewSet)
# router.register(r'v1/follow', FollowViewSet, basename='follows')

urlpatterns = [
    path('', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
