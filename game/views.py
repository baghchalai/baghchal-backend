from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Player
from .serializers import PlayerSerializer

# Create your views here.
class PlayerViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,viewsets.GenericViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=False, methods=['GET','PUT']) # players/me
    def me(self, request):
        (player,created) = Player.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = PlayerSerializer(player)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = PlayerSerializer(player, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
