from django.urls import include, path

from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'v1/posts', PostViewSet)
router.register(r'v1/groups', GroupViewSet)
router.register(r'v1/follow', FollowViewSet, basename='following')
router.register(
    r'v1/posts/(?P<post_pk>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('', include(router.urls))
]
