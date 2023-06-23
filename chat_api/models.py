from django.db import models

from django.db import models
from user_api.models import CustomUser

class Chat(models.Model):
    participants = models.ManyToManyField(CustomUser, related_name='chats')

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)