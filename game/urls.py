from rest_framework import routers
from .views import PlayerViewSet,GameWithBotViewSet

router = routers.DefaultRouter()
router.register(r'', GameWithBotViewSet)
router.register(r'player', PlayerViewSet)
urlpatterns = router.urls