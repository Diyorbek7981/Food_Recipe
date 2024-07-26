from django.urls import path
from .views import *

urlpatterns = [
    path('instructions/', InstructionCreate.as_view(), name='instruction-create'),
    path('instructions/', InstructionList.as_view(), name='instruction-list'),
    path('instructions_detail/<int:pk>/', InstructionDetail.as_view(), name='instruction-detail'),
    path('instructions_update/<int:pk>/', InstructionUpdate.as_view(), name='instruction-update'),
    path('instructions_delete/<int:pk>/', InstructionDelete.as_view(), name='instruction-delete'),
]
