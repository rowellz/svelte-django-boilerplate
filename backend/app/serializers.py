from rest_framework import serializers
from .models import DjangoAppModel


class MyProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = DjangoAppModel
        fields = '__all__'

class MyProfileImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = DjangoAppModel
        fields = ('entry', 'user')
