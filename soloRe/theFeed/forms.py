from django import forms
from .models import Album, Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'file', 'author']
        widgets = {
            'title': forms.TextInput(attrs=({'class': 'form-control'})),
            'description': forms.Textarea(attrs=({'class': 'form-control'})),
            'author': forms.TextInput(attrs=({'class': 'form-control','value': '', 'id': 'user', 'type': 'hidden'})),
            'file': forms.FileInput(attrs=({'class': 'form-control'})),
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs=({'class': 'form-control'})),
            'description': forms.Textarea(attrs=({'class': 'form-control'})),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'author', 'post')
        widgets = {
            'body': forms.TextInput(attrs=({'class': 'form-control', 'style': 'opacity: .5; max-width: 66.6%; margin: auto;'})),
            'author': forms.TextInput(attrs=({'class': 'form-control','value': '', 'id': 'user', 'type': 'hidden'})),
            'post': forms.TextInput(attrs=({'class': 'form-control','value': '', 'id': 'postcomment', 'type': 'hidden'})),
        }
        labels = {
            'body': ''
        }

class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('title', 'author')
        widgets = {
            'title': forms.TextInput(attrs=({'class': 'form-control'})),
            'author': forms.TextInput(attrs=({'class': 'form-control','value': '', 'id': 'user', 'type': 'hidden'})),
        }

class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs=({'class': 'form-control text-center'})),
        }