from rest_framework import serializers
from .models import ChefyRecipeModel


class MyProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChefyRecipeModel
        fields = '__all__'

class MyProfileImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChefyRecipeModel
        fields = ('chat_gpt_response', 'user')
