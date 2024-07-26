from django.db import models
from django.conf import settings

from categoryapp.models import Category

User = settings.AUTH_USER_MODEL


class Recipes(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/recipe/')
    cook_time = models.IntegerField()
    serves = models.IntegerField()
    views_number = models.ManyToManyField(User, verbose_name="ViewsNumber", related_name="recipes_views")
    location = models.CharField(max_length=100)
    likes = models.ManyToManyField(User, related_name='blogpost_like')
    recipe_owner = models.ForeignKey(User, related_name='recipe_owner', on_delete=models.CASCADE, verbose_name='Owner')
    category = models.ManyToManyField(Category, verbose_name='Categories', related_name='recipes_category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.ManyToManyField(User)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
