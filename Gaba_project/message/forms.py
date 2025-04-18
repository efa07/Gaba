from django import forms

from .models import  MessageContent

class MessageContentForm(forms.ModelForm):
    class Meta:
        model = MessageContent
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full h-32 p-2 border border-gray-300 rounded-lg',
                'placeholder': 'Type your message here...'
            }),
        }