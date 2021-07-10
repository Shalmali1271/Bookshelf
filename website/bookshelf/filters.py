from django.db.models.query import QuerySet
import django_filters
from .models import Book, Genre_Choices
from django import forms

class BookFilter(django_filters.FilterSet):

    genre = django_filters.ModelMultipleChoiceFilter(label='Genre',  widget=forms.CheckboxSelectMultiple, queryset=Genre_Choices.objects.all(),)
    language = django_filters.MultipleChoiceFilter(label = 'Language', choices = Book.LANGUAGE_CHOICE, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Book
        fields = []
