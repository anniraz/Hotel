from rest_framework.routers import DefaultRouter

from apps.news.api.views import *

router = DefaultRouter()
router.register(
    prefix='news',
    viewset=NewsApiViewset
)
router.register(
    prefix='comment',
    viewset=CommentsApiViewset
)

urlpatterns = router.urls