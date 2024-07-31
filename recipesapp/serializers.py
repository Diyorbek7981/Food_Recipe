from rest_framework import serializers
from foodapp.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'created_at', 'updated_at']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ['id', 'recipe', 'text', 'created_at', 'updated_at']


class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructions
        fields = ['id', 'recipe', 'text', 'image_1', 'image_2', 'image_3']
