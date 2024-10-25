from django.urls import path
from .views import BlogListCreateAPIView, BlogDetailAPIView, CommentListCreateAPIView

urlpatterns = [
    path('', BlogListCreateAPIView.as_view(), name='blog-list-create'),
    path('<int:pk>/', BlogDetailAPIView.as_view(), name='blog-detail'),
    path('<int:blog_pk>/comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
]
