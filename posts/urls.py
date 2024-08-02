from django.urls import path
from .views import *

urlpatterns = [
    path('publications/', PublicationList.as_view(), name='publication-list'),
    path('info/<int:pk>/', PublicationDetail.as_view()),
    path('create/', PostCreate.as_view(), name='post-create'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='post-update'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='post-delete'),
]