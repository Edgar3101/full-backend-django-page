from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    preview = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    photos= models.ImageField()
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Profile(models.Model):
    name= models.CharField(max_length=200, unique=True)
    email= models.EmailField(max_length=224)
    profile_photo= models.ImageField(upload_to="static/img/profiles/")
    update_on = models.DateTimeField(auto_now= True)
    class Meta:
        ordering = ['-update_on']
    def __str__(self):
        return self.name

# Create your models here.
