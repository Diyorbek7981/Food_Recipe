from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'location']
    list_display_links = ['title', 'author', 'location']



@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ['recipe', 'text']
    list_display_links = ['recipe', 'text']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']
    list_display_links = ['category_name']


@admin.register(FoodComment)
class FoodCommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'recipe', ]
    list_display_links = ['author', 'recipe', ]


@admin.register(FoodLike)
class FoodLikeAdmin(admin.ModelAdmin):
    list_display = ['author', 'recipe', ]
    list_display_links = ['author', 'recipe', ]


@admin.register(CommentLike)
class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ['author', 'comment', ]
    list_display_links = ['author', 'comment', ]
