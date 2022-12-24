from .models import Article
from django import forms

class ArticleForm(forms.ModelForm):
    required_css_class = "form-group"
    class Meta:
        model = Article
        css_class = "form-post"
        fields = ('title', 'content')