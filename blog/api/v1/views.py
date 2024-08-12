from blog.models import *
from .serializer import *
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin , CreateModelMixin , RetrieveModelMixin , DestroyModelMixin , UpdateModelMixin



class CategoryApiViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.all()

    



class BlogApiViewSet(GenericAPIView, ListModelMixin, CreateModelMixin):   
    serializer_class = BlogSerializer
    def get_queryset(self):
        return Blog.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




class BlogDetailView(GenericAPIView , RetrieveModelMixin , DestroyModelMixin , UpdateModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BlogDetailSerializer
    def get_queryset(self):
        return Blog.objects.filter(status=True)
    
    def get(self , request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class BlogTagApiViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = BlogTagSerializer
    def get_queryset(self):
        return BlogTag.objects.all()




class CommentApiViewSet(viewsets.ModelViewSet):
    lookup_field='id'
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    def get_queryset(self):
        return Comment.objects.all()
    

