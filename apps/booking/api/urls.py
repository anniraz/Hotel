from rest_framework.routers import DefaultRouter

from apps.booking.api.views import BookingApiView

router = DefaultRouter()
router.register(
    prefix='booking',
    viewset=BookingApiView
)

urlpatterns = router.urls