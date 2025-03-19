from django import forms
from .models import Post, Massage


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','user','content','photo']

class MassageForm(forms.ModelForm):
    class Meta:
        model = Massage
        fields = ['text']