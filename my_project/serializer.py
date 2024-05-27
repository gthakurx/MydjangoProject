from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
#convert user model and convert all the feilds
    class Meta:
        model = User
        fields = '__all__'