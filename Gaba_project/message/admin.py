from django.contrib import admin

from .models import Message, MessageContent

admin.site.register(Message)
admin.site.register(MessageContent)