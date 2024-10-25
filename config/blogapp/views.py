from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class BlogListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.is_staff:
            blogs = Blog.objects.all()
        else:
            blogs = Blog.objects.filter(user=request.user)

        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        blog_instance = get_object_or_404(Blog, pk=pk, user=self.request.user)
        return blog_instance

    def get(self, request, pk):
        blog = self.get_object(pk=pk)
        serializer = BlogSerializer(blog)
        return Response(data=serializer.data)

    def put(self, request, pk):
        blog = self.get_object(pk=pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        blog = self.get_object(pk=pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CommentListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, blog_pk):
        blog = get_object_or_404(Blog, pk=blog_pk)
        comments = blog.comments.all() 
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, blog_pk):
        blog = get_object_or_404(Blog, pk=blog_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(blog=blog, user=request.user) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
