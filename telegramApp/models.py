from django.db import models


# Create your models here.
class Thread(models.Model):
    name = models.CharField(max_length=255)


class Message(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    isMe = models.BooleanField(default=True)
