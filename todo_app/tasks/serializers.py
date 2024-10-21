from rest_framework import serializers
from .models import Task, UserProfile

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'employer', 'employee', 'created_at', 'updated_at']

class AddTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'employee', 'created_at', 'updated_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'phone_number', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user
