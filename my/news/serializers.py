from rest_framework import serializers
from .models import Artiles

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiles
        fields = '__all__'