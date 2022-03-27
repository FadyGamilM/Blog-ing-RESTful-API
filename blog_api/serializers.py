
#! utilize the serializers from DRF
from rest_framework import serializers
#! utilize the model 
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
   class Meta:
      #! which model
      model = Post
      #! the fields we wanna to return
      fields = ('id', 'title', 'author', 'status', 'content', 'excerpt')