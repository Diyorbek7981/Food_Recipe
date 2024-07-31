from django.urls import path
from .views import RecipeCreate, RecipeList, RecipeDetail, RecipeUpdate, RecipeDelete
from .views import CategoryCreate, CategoryList, CategoryDetail, CategoryUpdate, CategoryDelete
from .views import IngredientCreate, IngredientList, IngredientDetail, IngredientUpdate, IngredientDelete
from .views import InstructionCreate, InstructionList, InstructionDetail, InstructionUpdate, InstructionDelete

urlpatterns = [
    path('instructions/', InstructionCreate.as_view(), name='instruction-create'),
    path('instructions/', InstructionList.as_view(), name='instruction-list'),
    path('instructions_detail/<int:pk>/', InstructionDetail.as_view(), name='instruction-detail'),
    path('instructions_update/<int:pk>/', InstructionUpdate.as_view(), name='instruction-update'),
    path('instructions_delete/<int:pk>/', InstructionDelete.as_view(), name='instruction-delete'),
    path('ingredients/', IngredientCreate.as_view(), name='ingredient-create'),
    path('ingredients/', IngredientList.as_view(), name='ingredient-list'),
    path('ingredients_detail/<int:pk>/', IngredientDetail.as_view(), name='ingredient-detail'),
    path('ingredients_update/<int:pk>/', IngredientUpdate.as_view(), name='ingredient-update'),
    path('ingredients_delete/<int:pk>/', IngredientDelete.as_view(), name='ingredient-delete'),
    path('categories/', CategoryCreate.as_view(), name='category-create'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories_detail/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('categories_update/<int:pk>/', CategoryUpdate.as_view(), name='category-update'),
    path('categories_delete/<int:pk>/', CategoryDelete.as_view(), name='category-delete'),
    path('recipes/', RecipeCreate.as_view(), name='recipe-create'),
    path('recipes/', RecipeList.as_view(), name='recipe-list'),
    path('recipes_detail/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('recipes_update/<int:pk>/', RecipeUpdate.as_view(), name='recipe-update'),
    path('recipes_delete/<int:pk>/', RecipeDelete.as_view(), name='recipe-delete'),
]
