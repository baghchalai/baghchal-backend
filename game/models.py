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

GAME_CHOICES = (
    ('bagh','BAGH'),
    ('goat', 'GOAT'),
)

class GameWithBot(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pgn = models.CharField(default='',max_length=500)
    played_as = models.CharField(max_length=6, choices=GAME_CHOICES)

    def won(self):
        [goat,bagh] = self.pgn.split('#')[1].split('-')
        if goat != '1/2' and bagh != '1/2':
            if self.played_as == 'bagh' and int(bagh) == 1:
                return True
            if self.played_as == 'goat' and int(goat) == 1:
                return True
        return False

    def draw(self):
        [goat,bagh] = self.pgn.split('#')[1].strip().split('-')
        if goat == '1/2' and bagh == '1/2':
            return True
        return False