from django.db import models
from items.models import Item
from django.contrib.auth.models import User

class Message(models.Model):
    item = models.ForeignKey(Item, related_name="messages", on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.sender} to {self.recipient} at {self.timestamp}"
    

class MessageContent(models.Model):
    message = models.ForeignKey(Message, related_name="message_contents", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="message_contents", on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message at {self.created_at}"