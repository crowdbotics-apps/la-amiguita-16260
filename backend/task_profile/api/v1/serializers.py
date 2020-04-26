from rest_framework import serializers
from task_profile.models import CustomerProfile, TaskerProfile, Notification


class TaskerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskerProfile
        fields = "__all__"


class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"
