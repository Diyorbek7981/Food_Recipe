from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Recipes as Recipe
from .models import *
from .serializers import *


class RecipeCreate(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = RecipeSerializer


class RecipeList(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetail(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeUpdate(generics.UpdateAPIView):
    queryset = Recipe.objects.all()
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = RecipeSerializer


class RecipeDelete(generics.DestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class CategoryCreate(generics.CreateAPIView):
    queryset = Category.objects.all()
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = CategorySerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdate(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDelete(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class IngredientCreate(generics.CreateAPIView):
    queryset = Ingredients.objects.all()
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = IngredientSerializer


class IngredientList(generics.ListAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer


class IngredientDetail(generics.RetrieveAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer


class IngredientUpdate(generics.UpdateAPIView):
    queryset = Ingredients.objects.all()
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = IngredientSerializer


class IngredientDelete(generics.DestroyAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer


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
