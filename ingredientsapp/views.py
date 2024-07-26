from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Ingredients as Ingredient
from .serializers import IngredientSerializer


class IngredientCreate(generics.CreateAPIView):
    queryset = Ingredient.objects.all()
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = IngredientSerializer


class IngredientList(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientDetail(generics.RetrieveAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientUpdate(generics.UpdateAPIView):
    queryset = Ingredient.objects.all()
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = IngredientSerializer


class IngredientDelete(generics.DestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
