from rest_framework import serializers
from .models import Player, GameWithBot

class PlayerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Player
        fields = ['id', 'user_id', 'rating']


class GameWithBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameWithBot
        fields = ['id', 'user','pgn','played_as']