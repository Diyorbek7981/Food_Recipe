from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(CuisinesModel)
class HomeModelTranslation(TranslationOptions):
    fields = ['name']