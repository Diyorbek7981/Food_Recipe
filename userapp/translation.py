from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(CuisinesModel)
class CuisinesModelTranslation(TranslationOptions):
    fields = ['name']


@register(DietaryModel)
class DietaryModelTranslation(TranslationOptions):
    fields = ['name']
