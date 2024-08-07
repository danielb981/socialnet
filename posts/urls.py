from django.urls import path, include
from posts.views import *
from rest_framework.routers import DefaultRouter


like_router = DefaultRouter()
like_router.register('', LikeViewSet)

dislike_router = DefaultRouter()
dislike_router.register(r'dislikes', DislikeViewSet)


urlpatterns = [
    path("list/", PublicationList.as_view(), name="posts-list"),
    path('info/<int:pk>/', PublicationDetail.as_view()),
    path('create/', PostCreate.as_view(), name='post-create'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='post-update'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='post-delete'),\

    path('likes/', include(like_router.urls)),
    path('', include(dislike_router.urls)),
]