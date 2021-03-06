from django.db import models
from ckeditor .fields import RichTextField

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    intro = models.TextField(max_length=280) #twitter character limit to keep the intro short.
    body = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    #isbn test
    #isbn = models.CharField(max_length=255)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
