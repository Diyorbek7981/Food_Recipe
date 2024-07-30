from django.urls import path
from .views import *

urlpatterns = [
    path('recipes_like/create_delete/<int:pk>', FoodLikeApiView.as_view()),
    path('recipes_like/list', FoodLikeListView.as_view()),
    path('recipes_save/create_delete/<int:pk>', FoodSaveApiView.as_view()),
    path('recipes_save/list', FoodSaveListView.as_view()),
    path('coment/list/<int:pk>', FoodCommentListView.as_view()),
    path('coment/create/<int:pk>', FoodCommentCreateView.as_view()),
    path('coment/update_delete/<int:pk>', CommentUpdateDeleteView.as_view()),
    path('coment_like/create_delete/<int:pk>', CommentLikeAPiView.as_view()),
    path('coment_like/list/', CommentLikeListView.as_view()),
    path('recipes/list/', RecipeListView.as_view()),
]
