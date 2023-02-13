from django.urls import path, include
from .views import PostListAPIView, PostRetrieveAPIView

urlpatterns = [
    path('posts/', PostListAPIView.as_view()),
    path('posts/<int:pk>/', PostRetrieveAPIView.as_view())
]
