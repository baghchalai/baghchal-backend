from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name' ]

class UserSerializer(BaseUserSerializer):
    profile_present = serializers.SerializerMethodField()
    class Meta(BaseUserSerializer.Meta):
        fields=['id','username','email','first_name','last_name','profile_present']
    
    def get_profile_present(self, obj):
        try:
            if obj.player:
                return True
            else:
                return False
        except:
            return False
