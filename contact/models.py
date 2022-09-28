from django.db import models


class Contact(models.Model):

    class Meta:
        verbose_name_plural = 'Contact Us'

    name = models.CharField(max_length=254)
    email = models.EmailField()
    subject = models.CharField(max_length=254)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.subject} from {self.name}"
