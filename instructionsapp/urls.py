from django.urls import path
from .views import *

urlpatterns = [
    path('get_instructions/', InstructionsView.as_view()),
    path('create_instructions/', CreateInstructionsView.as_view()),
]
