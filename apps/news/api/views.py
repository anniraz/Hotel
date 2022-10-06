from rest_framework import viewsets,permissions
# Create your views here.

from apps.news.models import *
from apps.news.serializers import *

class NewsApiViewset(viewsets.ModelViewSet):
    queryset=News.objects.all()
    serializer_class=NewsSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

class CommentsApiViewset(viewsets.ModelViewSet):
    queryset=Comments.objects.all()
    serializer_class=CommentSerializers
