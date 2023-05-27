from rest_framework import serializers
from .models import Player, GameWithBot, Mapper
from core.serializers import UserSerializer

class PlayerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    user = UserSerializer()
    def get_fields(self):
        fields = super().get_fields()
        # Make the read_only_field read-only
        fields['rating'].read_only = True
        fields['game_played'].read_only = True
        fields['game_won'].read_only = True
        fields['game_drawn'].read_only = True
        fields['user'].read_only = True
        return fields
    
    class Meta:
        model = Player
        fields = ['id', 'user_id','user', 'rating', 'game_played', 'game_won','game_drawn','image']


class GameWithBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameWithBot
        fields = ['id', 'user','pgn','played_as']

class MapperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapper
        fields = ['id', 'player1', 'player2', 'room']