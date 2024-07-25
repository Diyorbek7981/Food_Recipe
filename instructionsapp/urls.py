from django.urls import path
from .views import *

urlpatterns = [
    path('instructions/', InstructionCreate.as_view(), name='instruction-create'),
    path('instructions/', InstructionList.as_view(), name='instruction-list'),
    path('instructions/<int:pk>/', InstructionDetail.as_view(), name='instruction-detail'),
    path('instructions/<int:pk>/', InstructionUpdate.as_view(), name='instruction-update'),
    path('instructions/<int:pk>/', InstructionDelete.as_view(), name='instruction-delete'),
]
