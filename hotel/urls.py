from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static



api_urlpatterns = [
    path('', include('apps.booking.api.urls')),
    path('', include('apps.clubs.api.urls')),
    path('', include('apps.home.api.urls')),
    path('', include('apps.news.api.urls')),
    path('', include('apps.restaurant.api.urls')),
    path('', include('apps.rooms.api.urls')),

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

