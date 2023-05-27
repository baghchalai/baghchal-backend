from rest_framework import routers
from .views import PlayerViewSet,GameWithBotViewSet, MapperViewSet,LeaderboardView
from django.urls import path

router = routers.DefaultRouter()
router.register(r'', GameWithBotViewSet)
router.register(r'player', PlayerViewSet)
router.register(r'mapper', MapperViewSet)
urlpatterns = router.urls
urlpatterns.append(
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
)