from rest_framework import serializers

from foodapp.models import *


class InstructionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructions
        fields = '__all__'

