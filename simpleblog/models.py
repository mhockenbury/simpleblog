from django.db import models
from django.forms import ModelForm

class Comment(models.Model):
    author = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField()
    article_uuid = models.CharField(max_length=36)

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [ 'author', 'text' ]
