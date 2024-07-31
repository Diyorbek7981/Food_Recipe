from django.contrib import admin
from .models import *

admin.site.register(Recipes)
admin.site.register(Comments)
admin.site.register(Category)
admin.site.register(Ingredients)
admin.site.register(Instructions)
