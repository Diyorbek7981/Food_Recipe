from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Recipes as Recipe
from .serializers import RecipeSerializer


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
