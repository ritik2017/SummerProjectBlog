from django.shortcuts import render
from rest_framework import generics
from .serializers import BlogSerializer
from Blog.models import Blog
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsCreator
from rest_framework.decorators import api_view
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



#function based view
@api_view(['GET', 'POST'])
def blog_create(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)