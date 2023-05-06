from django.contrib import admin
from .models import Player, GameWithBot

# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name', 'rating', 'game_played']
    list_select_related = ['user']

@admin.register(GameWithBot)
class GameWithBotAdmin(admin.ModelAdmin):
    list_display = ['user','pgn','played_as', 'won','draw']