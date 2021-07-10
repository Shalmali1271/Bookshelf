from django.http import request
from django.urls import path
from .views import CreateBook, BookList, BookDetailview
from django.conf.urls import url
from . import views

urlpatterns = [
    path('create-book/', CreateBook.as_view(), name = "create-book"), 
    path('list-book/', BookList.as_view(), name = "list-book"),
    path('detail-book/<int:pk>/', BookDetailview.as_view(), name = "detail-book"),
]