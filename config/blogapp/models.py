from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs') 
    title = models.CharField(max_length=100)  
    post = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  
    status = models.BooleanField(default=True)  

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments') 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments') 
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.user.username
