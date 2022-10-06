from django.contrib import admin

from apps.news.models import News,NewsCategory,Comments
admin.site.register(NewsCategory)
admin.site.register(News)
admin.site.register(Comments)