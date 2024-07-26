from django.urls import path
from .views import CategoryCreate, CategoryList, CategoryDetail, CategoryUpdate, CategoryDelete

urlpatterns = [
    path('categories/', CategoryCreate.as_view(), name='category-create'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories_detail/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('categories_update/<int:pk>/', CategoryUpdate.as_view(), name='category-update'),
    path('categories_delete/<int:pk>/', CategoryDelete.as_view(), name='category-delete'),
]
