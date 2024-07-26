from django.db import models
from django.db.models import UniqueConstraint

from recipesapp.models import Recipes
from userapp.models import Users
from categoryapp.models import Category


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)


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
        return f"comment by {self.author}"


class FoodLike(models.Model):
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='recipe_likes')

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
