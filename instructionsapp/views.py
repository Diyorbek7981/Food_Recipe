from django.shortcuts import render
from .serializers import *
from foodapp.models import *
from django.views import generic


class InstructionsView(generic.ListView):
    model = Instructions
    context_object_name = 'instructions'

    def get_queryset(self):
        return Instructions.objects.all()
