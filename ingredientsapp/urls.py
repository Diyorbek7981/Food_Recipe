from django.urls import path
from .views import IngredientCreate, IngredientList, IngredientDetail, IngredientUpdate, IngredientDelete

urlpatterns = [
    path('ingredients/', IngredientCreate.as_view(), name='ingredient-create'),
    path('ingredients/', IngredientList.as_view(), name='ingredient-list'),
    path('ingredients_detail/<int:pk>/', IngredientDetail.as_view(), name='ingredient-detail'),
    path('ingredients_update/<int:pk>/', IngredientUpdate.as_view(), name='ingredient-update'),
    path('ingredients_delete/<int:pk>/', IngredientDelete.as_view(), name='ingredient-delete'),
]
