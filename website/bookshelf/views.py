from .forms import BookForm
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book
from django.urls import reverse_lazy
from .filters import BookFilter
from django import forms
from django_filters import MultipleChoiceFilter

class CreateBook(CreateView) :
    model = Book
    template_name = 'bookshelf/contact.html'
    form_class = BookForm
    # fields = ['name', 'author', 'genre', 'language']
    success_url = reverse_lazy('list-book')

class BookList(ListView) :
    model = Book
    template_name = 'bookshelf/index.html'
    context_object_name = 'books'
    field_class = forms.ModelMultipleChoiceField

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['filter'] = BookFilter(self.request.GET, queryset = self.get_queryset())
        return context

class BookDetailview(DetailView) :
    model = Book
    template_name = 'bookshelf/about.html'
    context_object_name = 'book'