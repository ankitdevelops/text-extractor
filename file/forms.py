from django import forms
from .models import *


class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ("file",)
