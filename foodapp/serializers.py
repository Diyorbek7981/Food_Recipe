from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'photo')
        ref_name = 'hi'
        # shunga o'xshash serializer yana boshqa joyda bo'lsa ref_name qo'yiladi


class FoodLikeSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = FoodLike
        fields = ("id", "author", "recipe")


class SaveSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = FoodLike
        fields = ("id", "author", "recipe")


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    replies = serializers.SerializerMethodField('get_replies')
    me_liked = serializers.SerializerMethodField('get_me_liked')
    likes_count = serializers.SerializerMethodField('get_likes_count')
    replies_count = serializers.SerializerMethodField('get_replies_count')

    class Meta:
        model = FoodComment
        fields = [
            "id",
            "author",
            "comment",
            "recipe",
            "parent",
            "created_at",
            "me_liked",
            "likes_count",
            "replies_count",
            "replies",
        ]

    def get_replies(self, obj):
        if obj.child.exists():
            serializers = self.__class__(obj.child.all(), many=True, context=self.context)
            return serializers.data
        else:
            return None

    def get_me_liked(self, obj):  # ---------- user bosgan like lar userga true korinishida boradi
        user = self.context.get('request').user
        if user.is_authenticated:
            return obj.likes.filter(author=user).exists()
        else:
            return False

    @staticmethod
    def get_likes_count(obj):
        return obj.likes.count()

    @staticmethod
    def get_replies_count(obj):
        return obj.child.count()


class CommentLikeSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = CommentLike
        fields = ("id", "author", "comment")


class RecipesSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    recipe_likes_count = serializers.SerializerMethodField('get_recipe_likes_count')
    recipe_comments_count = serializers.SerializerMethodField('get_recipe_comments_count')
    me_liked = serializers.SerializerMethodField('get_me_liked')
    me_saved = serializers.SerializerMethodField('get_me_saved')

    class Meta:
        model = Recipes
        fields = (
            "id",
            "title",
            "description",
            'image',
            "cook_time",
            "serves",
            "views_number",
            "location",
            "author",
            "category",
            'created_at',
            "recipe_likes_count",
            "recipe_comments_count",
            "me_liked",
            "me_saved",
        )
        extra_kwargs = {"image": {"required": False}}

    def get_recipe_likes_count(self, obj):
        return obj.recipe_likes.count()

    def get_recipe_comments_count(self, obj):
        return obj.recipe.count()

    def get_me_liked(self, obj):
        request = self.context.get('request', None)
        if request and request.user.is_authenticated:
            try:
                like = FoodLike.objects.get(recipe=obj, author=request.user)
                return True
            except FoodLike.DoesNotExist:
                return False

        return False

    def get_me_saved(self, obj):
        request = self.context.get('request', None)
        if request and request.user.is_authenticated:
            try:
                like = SaveModel.objects.get(recipe=obj, author=request.user)
                return True
            except SaveModel.DoesNotExist:
                return False

        return False
