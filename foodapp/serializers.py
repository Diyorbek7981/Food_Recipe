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
