from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *


# Register your models here.

class TaskAdmin():
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(CuisinesModel)
class CuisinesModelAdmin(TranslationAdmin, TaskAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    list_display_links = ['id', 'username']


@admin.register(UserConfirmation)
class UserConfirmationAdmin(admin.ModelAdmin):
    list_display = ['id', 'code']
    list_display_links = ['id', 'code']


@admin.register(DietaryModel)
class DietaryModelAdmin(TranslationAdmin, TaskAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']


@admin.register(FollowerModel)
class FollowerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'follower']
    list_display_links = ['id', 'author', 'follower']


@admin.register(FollowingModel)
class FollowingModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'following']
    list_display_links = ['id', 'author', 'following']
