from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'post_category', 'name', 'text']

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("name")
        if len(description) > 255:
            raise ValidationError({
                "name": "Title must not exceed 255 characters"
            })

        return cleaned_data
