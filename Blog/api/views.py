from django.shortcuts import render
from rest_framework import generics
from .serializers import BlogSerializer
from Blog.models import Blog
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsCreator

#class based apis for interacting with blogs

class BlogCreateApiView(generics.CreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogUpdateApiView(generics.UpdateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = (IsAuthenticated,IsCreator)

class BlogListsApi(generics.ListAPIView):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer

class BlogDeleteAPI(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, IsCreator)
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()