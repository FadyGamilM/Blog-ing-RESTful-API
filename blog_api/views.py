from django.shortcuts import render

#! utilize CBV from DRF 
from rest_framework import generics
#! utlize the Post model and Post serializer
from . import serializers
from blog.models import Post

#! => create CBVs
class PostList(generics.ListCreateAPIView):
   # utlize the custom object manager to filter all published posts only
   queryset = Post.publishedObjects.all()
   serializer_class = serializers.PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
   # here we have to return all the objects to be able to filter them, 
   # because maybe the post that matches this id isn't published yet .. 
   queryset = Post.objects.all()
   serializer_class = serializers.PostSerializer