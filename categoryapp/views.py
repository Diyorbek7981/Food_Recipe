from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser

from .models import Category
from .serializers import CategorySerializer


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
