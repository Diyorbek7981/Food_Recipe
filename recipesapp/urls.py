from django.urls import path
from .views import RecipeCreate, RecipeList, RecipeDetail, RecipeUpdate, RecipeDelete

urlpatterns = [
    path('recipes/', RecipeCreate.as_view(), name='recipe-create'),
    path('recipes/', RecipeList.as_view(), name='recipe-list'),
    path('recipes_detail/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('recipes_update/<int:pk>/', RecipeUpdate.as_view(), name='recipe-update'),
    path('recipes_delete/<int:pk>/', RecipeDelete.as_view(), name='recipe-delete'),
]
