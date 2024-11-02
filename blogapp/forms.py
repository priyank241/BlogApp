# forms.py

from django import forms
from blogs.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'intro', 'body', 'author_name', 'author_email']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter post title'})
        self.fields['slug'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter post slug'})
        self.fields['intro'].widget.attrs.update({'class': 'textarea', 'placeholder': 'Write an introduction'})
        self.fields['body'].widget.attrs.update({'class': 'textarea', 'placeholder': 'Write your post content'})
        self.fields['author_name'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter author name'})
        self.fields['author_email'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter author email'})