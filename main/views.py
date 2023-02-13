from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Post, Comment
from .serializers import PostListSerializer, PostsCommentsSerializer, PostsRetrieveSerializer


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.last()
    serializer_class = PostsCommentsSerializer


class PostListAPIView(APIView):

    def get(self, request):
        queryset = Post.objects.all()
        for obj in queryset:
            instance = Comment.objects.filter(post=obj.id).last()
            obj.last_comment = instance
        serializer = PostListSerializer(instance=queryset, many=True)
        return Response(serializer.data)


class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsRetrieveSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)