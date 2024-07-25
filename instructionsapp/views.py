from django.shortcuts import render
from .serializers import *
from foodapp.models import *
from django.views import generic


class InstructionsView(generic.ListView):
    model = Instructions
    serializer_class = InstructionsSerializer
    context_object_name = 'instructions'

    def get_queryset(self):
        return Instructions.objects.all()


class CreateInstructionsView(generic.edit.CreateView):
    model = Instructions
    serializer_class = InstructionsSerializer

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.save()
