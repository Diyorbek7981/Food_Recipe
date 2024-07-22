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
class HomeModelAdmin(TranslationAdmin, TaskAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']


@admin.register(UserConfirmation)
class UserConfirmationAdmin(admin.ModelAdmin):
    list_display = ['id', 'code']
    list_display_links = ['id', 'code']


@admin.register(DietaryModel)
class DietaryModelAdmin(TranslationAdmin, TaskAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
