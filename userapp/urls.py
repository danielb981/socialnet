from django.urls import path
from userapp.views import *


urlpatterns = [
    path("list/", UserList.as_view(), name="user-list"),
    path('info/<int:pk>/', UserInfo.as_view())
]