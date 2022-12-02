from rest_framework import serializers
from .models import User


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.about = validated_data.get('about', instance.about)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
