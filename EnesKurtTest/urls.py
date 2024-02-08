from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ( UserViewSet, PostsViewSet, AlbumViewSet, PhotosViewSet, CommentsViewSet, TodosViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostsViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'photos', PhotosViewSet)
router.register(r'comments', CommentsViewSet)
router.register(r'todos', TodosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('users/<int:pk>/update/', UserViewSet.as_view({'put': 'update'})),
    path('users/<int:pk>/delete/', UserViewSet.as_view({'delete': 'delete'})),


]

urlpatterns += router.urls