from django import forms

from .models import Url


class UrlCreateForm(forms.ModelForm):
    origin = forms.URLField(label='Create Short Url')

    class Meta:
        model = Url
        fields = ('origin',)
