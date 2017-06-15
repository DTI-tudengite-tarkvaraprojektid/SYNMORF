from django import forms
from .models import Content


class InputForm(forms.ModelForm):

	class Meta:
		model = Content
<<<<<<< HEAD
		fields = ("Tekst",)
=======
		fields = ("text", "n_gram", "title", "types")
>>>>>>> 59e624cf8807579d493f5d10cdda9a93964c97c3
