from rest_framework import serializers

from apps.news.models import *

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields='__all__'

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields='__all__'