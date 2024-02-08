from rest_framework import viewsets
from .models import User, Posts, Album, Photos, Comments, Todos
from .serializers import (
    UserSerializer, PostsSerializer, AlbumSerializer, PhotosSerializer, CommentsSerializer, TodosSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class PhotosViewSet(viewsets.ModelViewSet):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class TodosViewSet(viewsets.ModelViewSet):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
