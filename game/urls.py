from rest_framework import routers
from .views import PlayerViewSet,GameWithBotViewSet, MapperViewSet

router = routers.DefaultRouter()
router.register(r'', GameWithBotViewSet)
router.register(r'player', PlayerViewSet)
router.register(r'mapper', MapperViewSet)
urlpatterns = router.urls