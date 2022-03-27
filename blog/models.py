from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
   name = models.CharField(max_length=100)
   def __str__(self):
      return self.name

class Post(models.Model):
   category = models.ForeignKey(
      Category,
      on_delete=models.PROTECT,
      default= 1
   )
   title = models.CharField(max_length=250)
   excerpt = models.TextField(null=True, blank=True)
   content = models.TextField()
   published = models.DateTimeField(default=timezone.now)
   slug = models.SlugField(max_length=250, unique_for_date='published')
   author = models.ForeignKey(
      User, on_delete=models.CASCADE, related_name='blog_posts'
   )
   StatusOptions = (
      ('published', 'Published'),
      ('draft', 'Draft')
   )
   status = models.CharField(max_length=10, choices=StatusOptions, default='published')
   #! lets create custom manager for this mdoel
   class PostObjects(models.Manager):
      def get_queryset(self):
         return super().get_queryset().filter(status='published')
   objects = models.Manager()
   publishedObjects = PostObjects() 

   class Meta:
      ordering = ('-published',)
   
   def __str__(self):
      return self.title