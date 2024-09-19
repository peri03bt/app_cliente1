
from django import forms
from .models import Contact, PostProjects 


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your name...',
        'id': 'name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'name@example.com',
        'id': 'email'
    }))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '(123) 456-7890',
        'id': 'phone'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your message here...',
        'id': 'message',
        'style': 'height: 10rem'
    }))

class PostProjectsForm(forms.ModelForm):
    class Meta:
        model = PostProjects
        fields = ['title', 'image', 'description']