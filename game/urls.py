from rest_framework import routers
from .views import PlayerViewSet

router = routers.DefaultRouter()
router.register(r'player', PlayerViewSet)
urlpatterns = router.urls