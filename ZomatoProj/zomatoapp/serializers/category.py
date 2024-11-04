from rest_framework import serializers
from ..models import Category

class CategoryPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'