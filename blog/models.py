from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):

    title = models.CharField(max_length=254)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title


class Reply(models.Model):

    class Meta:
        verbose_name_plural = 'Replies'
        ordering = ["-created"]

    creator = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name="user_replies")
    body = models.TextField()
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE,
                             related_name="blog_replies")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reply {self.body} by {self.creator}"