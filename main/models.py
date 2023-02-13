from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=64, unique=True)
    content = models.TextField()
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    text = models.TextField(max_length=256)
    crated_at = models.DateTimeField(auto_now_add=True)