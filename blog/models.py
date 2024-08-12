from django.db import models
from root.models import Team
from django.contrib.auth import get_user_model
User = get_user_model



class Category(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    image = models.ImageField(upload_to='blog' , default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    website = models.CharField(max_length=100)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.name



class Blog(models.Model):
    category = models.ManyToManyField(Category)
    comments = models.ManyToManyField(Comment)
    title = models.CharField(max_length=200)
    publisher = models.ForeignKey(Team, on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog' , default='default.jpg')
    content = models.TextField()
    description = models.TextField()
    image_publisher = models.ImageField(upload_to='blog' , default='default.jpg')
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.title
    


    
class BlogTag(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title





# Create your models here.
