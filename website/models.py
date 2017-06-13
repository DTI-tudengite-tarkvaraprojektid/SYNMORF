from django.db import models

# Create your models here.
from django.utils import timezone

from django.core.validators import MinValueValidator


class Content(models.Model):
	user = models.ForeignKey("auth.User")
	text = models.TextField(default="")
	n_gram = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=1)
	title = models.CharField(max_length=50, default="tekst")
	created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user + "_" + self.created
