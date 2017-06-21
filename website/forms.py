from django import forms
from .models import Content


class InputForm(forms.ModelForm):
	class Meta:
		model = Content
		fields = ("text", "n_gram", "maatriks")
		labels = {"text": "Tekst" ,"n_gram": 'N-gram pikkus '}
