from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('index' , index , name = 'index'),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>',SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token), # to obtain the token
    path('message/', msg),
]