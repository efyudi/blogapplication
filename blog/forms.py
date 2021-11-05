from django import forms
from .models import Comments, PostModel


class BlogForm(forms.ModelForm):
    title = forms.CharField(max_length=200, label="Blog Title", widget=forms.TextInput(attrs={
        "size": "50px"
    }))
    content = forms.CharField(label="Blog Content", widget=forms.Textarea(attrs={
        "rows": "3",
        "cols": "50",
    }))

    class Meta:
        model = PostModel
        fields = ["title", "content"]


class CommentsForm(forms.Form):
    body = forms.CharField(label="",widget=forms.Textarea(attrs={
        "rows": "3",
        "placeholder": "Write your comment here..."
    }))

    class Meta:
        model = Comments
        fields = ["body"]