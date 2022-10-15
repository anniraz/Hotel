from django.urls import path

from apps.news.views import NewsCreateView, news,post,categoryPost,reply,AdminNewsListView,NewsUpdateView,NewsDeleteView



urlpatterns=[
    path('news/',news,name='news'),
    path('post/<int:id>/',post, name='detail_post'),
    path('post/category/<int:id>/',categoryPost,name='post_category'),
    path('post/comment/<int:id>/<int:id1>',reply , name='reply'),
    path('admins/news/',AdminNewsListView.as_view(),name='news_all'),
    path('admins/news/update/<int:pk>/',NewsUpdateView.as_view(),name='news_update'),
    path('admins/news/delate/<int:pk>/',NewsDeleteView.as_view(),name='news_delate'),
    path('admins/news/create/',NewsCreateView.as_view(),name='news_create')


]
