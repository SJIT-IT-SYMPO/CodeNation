from rest_framework import serializers
from accounts.models import UserProfile 

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('name', 'email', 'college', 'phone_no')