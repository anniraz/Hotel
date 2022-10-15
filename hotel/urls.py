from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

api_urlpatterns = [

    path('', include('apps.booking.api.urls')),
    path('', include('apps.clubs.api.urls')),
    path('', include('apps.home.api.urls')),
    path('', include('apps.news.api.urls')),
    path('', include('apps.restaurant.api.urls')),
    path('', include('apps.rooms.api.urls')),
    path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]


urlpatterns = [

    path('admin/', admin.site.urls),
    path('rooms/',include('apps.rooms.urls')),
    path('home/',include('apps.home.urls')),
    path('restuarant/',include('apps.restaurant.urls')),
    path('clubs/',include('apps.clubs.urls')),
    path('news/',include('apps.news.urls')),
    path('booking/',include('apps.booking.urls')),
    path('api/', include(api_urlpatterns)),

    # ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('i18n/',include('django.conf.urls.i18n')),

]


# celery -A hotel  worker -l info
# celery -A hotel beat -l info

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
