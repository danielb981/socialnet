from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
class PublicationSerializer(ModelSerializer):
    class Meta:
        model = Publication
        fields = ['title', 'content', 'published_date']

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['title', 'content']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['post', 'user', 'created_at', 'updated_at']

class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = ['post', 'user', 'created_at', 'updated_at']