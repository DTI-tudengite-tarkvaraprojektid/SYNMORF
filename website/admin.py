from django.contrib import admin
from .models import Content
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


# Register your models here.
admin.site.register(Content)