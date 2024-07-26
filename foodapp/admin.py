from django.contrib import admin
from .models import *


# Register your models here.


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
