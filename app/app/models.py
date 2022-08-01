from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'content')
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "author": forms.Select(attrs={
                "class": "form-control"
            }),
            "content": forms.Textarea(attrs={
                "class": "form-control"
            })
 
        }
