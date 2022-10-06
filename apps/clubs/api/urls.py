from rest_framework.routers import DefaultRouter

from apps.clubs.api.views import *

router = DefaultRouter()
router.register(
    prefix='clubs',
    viewset=ClubsApiViewset
)
router.register(
    prefix='etiquette',
    viewset=ClubsEtiquetteApiViewset
)
router.register(
    prefix='info',
    viewset=ClubsInfoApiViewset
)
urlpatterns = router.urls