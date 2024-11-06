from rest_framework import serializers
from ..models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}  # Ensure password is write-only

    def create(self, validated_data):
        password = validated_data.pop('password')
        phone_no = validated_data.pop('phone_no')        
        # Call the custom create_user method
        user = User.objects.create_user(phone_no=phone_no, password=password, **validated_data)
        return user