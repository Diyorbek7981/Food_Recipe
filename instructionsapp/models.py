from django.db import models

from recipesapp.models import Recipes


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)


class Instructions(BaseModel):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    text = models.TextField()
    image_1 = models.ImageField(upload_to='media/instructions/')
    image_2 = models.ImageField(upload_to='media/instructions/')
    image_3 = models.ImageField(upload_to='media/instructions/')

    def __str__(self):
        return self.text[:20]
