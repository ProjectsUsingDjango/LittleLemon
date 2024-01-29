from django.urls import path
from .views import *

urlpatterns = [
    path('index' , index , name = 'index'),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>',SingleMenuItemView.as_view()),
]