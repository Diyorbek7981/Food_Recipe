from rest_framework import serializers
from .models import *


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ['id', 'title', 'description', 'image', 'cook_time', 'serves', 'views_number', 'location', 'likes',
                  'recipe_owner', 'category', 'created_at', 'updated_at', 'deleted_at']
        read_only_fields = ['views_number', 'likes', 'created_at', 'updated_at', 'deleted_at']


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
