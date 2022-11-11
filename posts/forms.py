from django.forms import ModelForm,widgets
from django.forms.widgets import TextInput, EmailInput
from .models import *
from django import forms
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'
    
    