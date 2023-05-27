from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Player, GameWithBot, Mapper
from .serializers import PlayerSerializer, GameWithBotSerializer, MapperSerializer

# Create your views here.
class PlayerViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,viewsets.GenericViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = 'user_id'
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=False, methods=['GET','POST']) # players/me
    def me(self, request):
        (player,created) = Player.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = PlayerSerializer(player)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = PlayerSerializer(player, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = PlayerSerializer(player, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

class LeaderboardView(generics.ListAPIView):
    queryset = Player.objects.select_related('user').order_by('-rating')
    serializer_class = PlayerSerializer

class GameWithBotViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    queryset = GameWithBot.objects.all()
    serializer_class = GameWithBotSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        player = Player.objects.get(user_id=self.request.user.id)
        print(player)
        player.rating = player.rating + 10 # TODO
        player.save()
        return super().perform_create(serializer)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

class MapperViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Mapper.objects.all()
    serializer_class = MapperSerializer
    lookup_field = 'room'
    permission_classes = [IsAuthenticated]
