from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser

from .models import Instructions
from .serializers import InstructionSerializer


class InstructionCreate(generics.CreateAPIView):
    queryset = Instructions.objects.all()
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = InstructionSerializer


class InstructionList(generics.ListAPIView):
    queryset = Instructions.objects.all()
    serializer_class = InstructionSerializer


class InstructionDetail(generics.RetrieveAPIView):
    queryset = Instructions.objects.all()
    serializer_class = InstructionSerializer


class InstructionUpdate(generics.UpdateAPIView):
    queryset = Instructions.objects.all()
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = InstructionSerializer


class InstructionDelete(generics.DestroyAPIView):
    queryset = Instructions.objects.all()
    serializer_class = InstructionSerializer
