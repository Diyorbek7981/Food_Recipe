from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'location']
    list_display_links = ['id', 'title', 'author', 'location']


@admin.register(Instructions)
class InstructionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'recipe', 'text']
    list_display_links = ['id', 'recipe', 'text']


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ['id', 'recipe', 'text']
    list_display_links = ['id', 'recipe', 'text']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name']
    list_display_links = ['id', 'category_name']


@admin.register(FoodComment)
class FoodCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'recipe', ]
    list_display_links = ['id', 'author', 'recipe', ]


@admin.register(FoodLike)
class FoodLikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'recipe', ]
    list_display_links = ['id', 'author', 'recipe', ]


@admin.register(CommentLike)
class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'comment', ]
    list_display_links = ['id', 'author', 'comment', ]


@admin.register(SaveModel)
class SaveModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'recipe', ]
    list_display_links = ['id', 'author', 'recipe', ]
