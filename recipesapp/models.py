from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)


class Recipes(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/recipe/')
    cook_time = models.IntegerField()
    serves = models.IntegerField()
    views_number = models.ManyToManyField(User, verbose_name="ViewsNumber", related_name="recipes_views")
    location = models.CharField(max_length=100)
    likes = models.ManyToManyField(User, related_name='blogpost_like')
    recipe_owner = models.ForeignKey(User, related_name='recipe_owner', on_delete=models.CASCADE, verbose_name='Owner')
    category = models.ManyToManyField("Category", verbose_name='Categories', related_name='recipes_category')


class Comments(BaseModel):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.ManyToManyField(User)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')\


class Category(BaseModel):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Ingredients(BaseModel):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:20]


class Instructions(BaseModel):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    text = models.TextField()
    image_1 = models.ImageField(upload_to='media/instructions/')
    image_2 = models.ImageField(upload_to='media/instructions/')
    image_3 = models.ImageField(upload_to='media/instructions/')

    def __str__(self):
        return self.text[:20]
