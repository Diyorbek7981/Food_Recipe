from django.urls import path
from .views import *

urlpatterns = [
    path('create_delete/foodlike/<int:pk>', FoodLikeApiView.as_view()),
    path('list/foodlike', FoodLikeListView.as_view()),
    path('create_delete/foodsave/<int:pk>', FoodSaveApiView.as_view()),
    path('list/foodsave', FoodSaveListView.as_view()),
    path('coment/list/<int:pk>', FoodCommentListView.as_view()),
    path('coment/create/<int:pk>', FoodCommentCreateView.as_view()),
    path('coment/update_delete/<int:pk>', CommentUpdateDeleteView.as_view()),
    path('create_delete/comentlike/<int:pk>', CommentLikeAPiView.as_view()),
    path('list/comentlike', CommentLikeListView.as_view()),
    path('list/recipes', RecipeListView.as_view()),
]
