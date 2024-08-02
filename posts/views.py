from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.serializers import *
class PublicationList(APIView):
    def get(self, request, *args, **kwargs):
        publication_list = Publication.objects.all()
        serializer = PublicationSerializer(instance=publication_list, many=True)
        return Response(data=serializer.data)

class PublicationDetail(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        publication_object = Publication.objects.get(pk=pk)
        serializer = PublicationSerializer(publication_object)
        return Response(serializer.data)

class PostCreate(APIView):
    def post(self, request, *args, **kwargs):
        json_data = request.data
        serializer = PostCreateSerializer(data=json_data)
        if serializer.is_valid():
            serializer.save()
            return Response("Created", status=201)
        return Response("Error", status=400)

class PostUpdate(APIView):
    def put(self, request, *args, **kwargs):
        publication = Publication.objects.get(pk=kwargs["pk"])
        serializer = PostCreateSerializer(
            instance=publication,
            data=request.data,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, 400)


class PostDelete(APIView):
    def delete(self, request, *args, **kwargs):
        publication = Publication.objects.get(pk=kwargs["pk"])
        publication.delete()
        return Response("no data", 204)