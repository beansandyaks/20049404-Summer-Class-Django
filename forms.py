from django import  forms
from django.contrib.auth.forms import UserCreationForm

from .models import *
from django.contrib.auth.models import User


class BlogForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Title...'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter blog content...'}))
    class Meta:
        model = Blog
        fields = ['blog_image', 'title', 'body']


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email','first_name','last_name','username','password1','password2']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add a comment...'}))
    class Meta:
        model = Comment
        fields = ['comment']
