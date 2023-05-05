from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from .models import Player
from .serializers import PlayerSerializer

# Create your views here.
class PlayerViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,viewsets.GenericViewSet):
 queryset = Player.objects.all()
 serializer_class = PlayerSerializer