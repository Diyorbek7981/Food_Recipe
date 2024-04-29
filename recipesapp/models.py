from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Instructions(models.Model):
    recipe = models.ForeignKey('recipesapp.Recipes', on_delete=models.CASCADE)
    text = models.TextField()
    image_1 = models.ImageField(upload_to='instructions/')
    image_2 = models.ImageField(upload_to='instructions/')
    image_3 = models.ImageField(upload_to='instructions/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)


class Ingredients(models.Model):
    recipe = models.ForeignKey('recipesapp.Recipes', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)


class Recipes(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/recipe/')
    cook_time = models.IntegerField()
    serves = models.IntegerField()
    location = models.CharField(max_length=100)
    likes = models.ManyToManyField(User, related_name='blogpost_like')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, verbose_name='Categories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    recipe = models.ForeignKey('recipesapp.Recipes', on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.ManyToManyField(User)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
