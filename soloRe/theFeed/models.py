from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

class Album(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    posted_on = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return f'/album/{self.pk}'

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='profile')
    about_me = models.TextField(null=True)
    profile_pic = models.ImageField(null=True, blank=False, upload_to='images/', default='static\img\missing_avatar.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    album = models.ForeignKey(Album, null=True, on_delete=models.SET_NULL, related_name='posts')
    description = models.TextField()
    file = models.ImageField(null=True, blank=False, upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    likes = models.ManyToManyField(User, related_name='post_likes')
    posted_on = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def likes_count(self):
        return self.likes.count()

    def get_absolute_url(self):
        return f'/post/{self.pk}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    body = models.TextField()
    likes = models. ManyToManyField(User, related_name='comment_likes')
    posted_on = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title + ' | ' + str(self.author)

    def likes_count(self):
        return self.likes.count()

    def get_absolute_url(self):
        return f'/post/{self.post.pk}'