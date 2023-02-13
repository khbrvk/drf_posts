from rest_framework import serializers
from .models import Post, Comment


class PostsCommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'text')


class PostListSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    views = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    last_comment = PostsCommentsSerializer()

    class Meta:
        model = Post
        fields = ('title', 'content', 'views', 'created_at', 'last_comment')


class PostsRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'content', 'views', 'created_at')