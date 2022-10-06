from django.urls import path

from apps.news.views import news,post,categoryPost,reply



urlpatterns=[
    path('news/',news,name='news'),
    path('post/<int:id>/',post, name='detail_post'),
    path('post/category/<int:id>/',categoryPost,name='post_category'),
    path('post/comment/<int:id>/<int:id1>',reply , name='reply')

]
