from rest_framework.serializers import ModelSerializer
from .models import Publication
from rest_framework import serializers
class PublicationSerializer(ModelSerializer):
    class Meta:
        model = Publication
        fields = ['title', 'content', 'published_date']

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['title', 'content']

