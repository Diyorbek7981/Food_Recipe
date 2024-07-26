from rest_framework import serializers
from .models import Recipes as Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'image', 'cook_time', 'serves', 'views_number', 'location', 'likes',
                  'recipe_owner', 'category', 'created_at', 'updated_at', 'deleted_at']
        read_only_fields = ['views_number', 'likes', 'created_at', 'updated_at', 'deleted_at']
