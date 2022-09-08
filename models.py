from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    blog_image = models.ImageField(upload_to="blog-images/", max_length=250,null=True, blank=True)
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1200)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_blog')

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    date_commented = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=500)

    def __str__(self):

        return self.comment
