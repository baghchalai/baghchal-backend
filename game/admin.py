from django.contrib import admin
from .models import Player, GameWithBot, Multiplayer, Room, Mapper

# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name', 'rating', 'game_played']
    list_select_related = ['user']

@admin.register(GameWithBot)
class GameWithBotAdmin(admin.ModelAdmin):
    list_display = ['user','pgn','played_as', 'won','draw']

@admin.register(Multiplayer)
class MultiplayerAdmin(admin.ModelAdmin):
    list_display = ['player1','player2','pgn','player1_played_as','player2_played_as','won']

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'creator', 'active','game']

@admin.register(Mapper)
class MapperAdmin(admin.ModelAdmin):
    list_display = ['player1','player2','room']