from django.db import models
from django.db import models
from django.conf import settings
from django.db.models import UniqueConstraint
from userapp.models import Users


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)


class Recipes(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='image/recipe/')
    cook_time = models.IntegerField()
    serves = models.IntegerField()
    views_number = models.IntegerField(default=0)
    location = models.CharField(max_length=100)
    author = models.ForeignKey(Users, related_name='recipe_owner', on_delete=models.CASCADE, verbose_name='Owner')
    category = models.ManyToManyField('Category', verbose_name='Categories')

    def __str__(self):
        return self.title


class Instructions(BaseModel):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    text = models.TextField()
    image_1 = models.ImageField(upload_to='media/instructions/')
    image_2 = models.ImageField(upload_to='media/instructions/')
    image_3 = models.ImageField(upload_to='media/instructions/')

    def __str__(self):
        return self.text[:20]


class Ingredients(BaseModel):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:20]


class Category(BaseModel):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class FoodComment(BaseModel):
    author = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='author')
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='recipe')
    comment = models.TextField()
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='child',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.comment[:20]} by {self.author}"


class FoodLike(BaseModel):
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    recipe = models.ForeignKey('Recipes', on_delete=models.CASCADE, related_name='recipe_likes')

    # home.likes buyrugi berilsa shu homga tegishli barcha likelar keladi

    class Meta:  # 1 ta modelga 1 user ko'p like bosmasligi uchun
        constraints = [
            UniqueConstraint(
                fields=['author', 'recipe'],
                # ko'rsatilgan author ko'rsatilgan postga 1 marta like bosadi (2 - sini qbulqilmaydi)
                name='foodLikeUnique'
            )
        ]

    def __str__(self):
        return f"{self.author} -- {self.recipe}"


class CommentLike(BaseModel):
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    comment = models.ForeignKey(FoodComment, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['author', 'comment'],
                name='CommentLikeUnique'
            )
        ]

    def __str__(self):
        return f"{self.author} -- {self.comment}"


class SaveModel(BaseModel):
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='save')

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['author', 'recipe'],
                name='SaveUnique'
            )
        ]

    def __str__(self):
        return f"{self.author} -- {self.recipe}"
