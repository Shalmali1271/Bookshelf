from django import forms
from .models import *

class BookForm(forms.ModelForm) :
    class Meta :
        model = Book
        fields = ['name', 'author', 'genre', 'language']
        name = forms.CharField()
        author = forms.CharField()
        genre = forms.ModelMultipleChoiceField(
            queryset=Genre_Choices.objects.all(),
            widget=forms.CheckboxSelectMultiple
        )
        language = forms.CharField()