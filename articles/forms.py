from django import forms
from .models import *

class PublishArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'image')