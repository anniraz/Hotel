from rest_framework.routers import DefaultRouter

from apps.restaurant.api.views import *

router=DefaultRouter()
router.register('restaurant',RestuarantApiViewset)
router.register('menu',MenuApiViewset)
urlpatterns = router.urls