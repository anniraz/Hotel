from rest_framework.routers import DefaultRouter

from apps.rooms.api.views import RoomsApiViewset

router=DefaultRouter()

router.register('rooms',RoomsApiViewset)

urlpatterns=router.urls