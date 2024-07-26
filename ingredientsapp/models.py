from django.db import models

from foodapp.models import Recipes


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)


class Ingredients(BaseModel):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:20]
