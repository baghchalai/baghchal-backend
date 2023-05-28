from rest_framework import routers
from .views import PlayerViewSet,GameWithBotViewSet, MapperViewSet,LeaderboardView, RoomViewSet, MultiplayerViewSet
from django.urls import path

router = routers.DefaultRouter()
router.register(r'', GameWithBotViewSet)
router.register(r'player', PlayerViewSet)
router.register(r'mapper', MapperViewSet)
router.register(r'room', RoomViewSet)
router.register(r'multiplayer', MultiplayerViewSet)
urlpatterns = router.urls
urlpatterns.append(
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
)