from django.contrib import admin
from .models import Player

# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name', 'rating', 'game_played']
    list_select_related = ['user']