from django.conf import settings
from django.db import models

# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(default=500)
    game_played = models.IntegerField(default=0)
    game_won = models.IntegerField(default=0)
    game_drawn = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
    
    def first_name(self):
        return self.user.first_name
    
    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']