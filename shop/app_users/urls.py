from rest_framework import routers
from .api import UserViewSet


router = routers.DefaultRouter()
router.register('profile', UserViewSet)
urlpatterns = router.urls
