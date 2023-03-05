





from dataclasses import field, fields
from pyexpat import model
from django.forms import ModelForm
from .models import Books, Music


class BooksForm(ModelForm):
    class Meta:
        model=Books
        fields='__all__'
        