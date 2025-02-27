from django.forms import ModelForm,widgets
from django.forms.widgets import TextInput, EmailInput
from .models import *
from django import forms


class PostForm(forms.ModelForm):
    content = forms.CharField() # widget=CKEditorWidget()
    class Meta:
        model = Post
        fields = '__all__'
    
    