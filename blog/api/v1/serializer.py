from rest_framework import serializers
from blog.models import *

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [ 'title','status']

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['name','email','message']


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = [ 'title' , 'content','description', 'status'] 

class BlogDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = [ 'title', 'content','description' , 'status']

class BlogTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogTag
        fields = [ 'title' , 'status']