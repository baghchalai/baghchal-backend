from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    class Meta:
        model = Player
        fields = ['id', 'user_id', 'rating']