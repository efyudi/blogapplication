from django import forms
from django.forms import fields, models, widgets
from .models import Comments

class CommentsForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(attrs={
        "rows": "3",
    }))

    class Meta:
        model = Comments
        fields = ["body"]