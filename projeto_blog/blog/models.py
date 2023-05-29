from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = RichTextField()
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)


def __str__(self):
    return self.title
