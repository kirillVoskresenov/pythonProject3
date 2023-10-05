from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class PostsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'post_type',
            'title',
            'category',
            'text'
        ]


    def clean_name(self):
        name = self.cleaned_data["name"]
        if name[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы."
            )
        return name