from django.urls import path

from .views import *

urlpatterns = [
    path('create_delete/foodlike/<int:pk>', FoodLikeApiView.as_view()),
    path('list/foodlike', FoodLikeListView.as_view()),
]
