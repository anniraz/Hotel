from rest_framework import viewsets,permissions,filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.news.models import *
from apps.news.serializers import *

class NewsApiViewset(viewsets.ModelViewSet):
    queryset=News.objects.all()
    serializer_class=NewsSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['title', 'category']
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

class CommentsApiViewset(viewsets.ModelViewSet):
    queryset=Comments.objects.all()
    serializer_class=CommentSerializers
