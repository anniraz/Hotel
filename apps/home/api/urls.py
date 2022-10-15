from rest_framework.routers import DefaultRouter

from apps.home.api.views import *

router = DefaultRouter()
router.register(
    prefix='about',
    viewset=AboutHotelApiViewset
)
router.register(
    prefix='facilities',
    viewset=HotelFacilitiesApiViewset
)
router.register(
    prefix='ourteam',
    viewset=OurTeamApiViewset
)

router.register(
    prefix='extraservicesInfo',
    viewset=ExtraServicesInfoApiViewset
)

router.register(
    prefix='extraservices',
    viewset=ExtraServicesApiViewset
)

router.register(
    prefix='contactus',
    viewset=ContactUsApiViewset
)
router.register(
    prefix='reviews',
    viewset=ReviewsApiViewset
)
router.register(
    prefix='photogallery',
    viewset=PhotoGalleryApiViewset
)
router.register(
    prefix='videogallery',
    viewset=VideoGalleryApiViewset
)

urlpatterns = router.urls