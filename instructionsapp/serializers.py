from rest_framework import serializers
from .models import Instructions


class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructions
        fields = ['id', 'recipe', 'text', 'image_1', 'image_2', 'image_3']
