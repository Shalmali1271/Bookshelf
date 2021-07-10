from django.db import models
from django import forms

class Genre_Choices(models.Model):
    genre_choices = models.CharField(max_length=300)

    def __str__(self) : 
            return self.genre_choices

class Book(models.Model) :
    
    LANGUAGE_CHOICE = (
        ('English', 'English'),
        ('Hindi', 'Hindi'),
        ('Marathi', 'Marathi'),
    )

    name = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    genre = models.ManyToManyField(Genre_Choices)
    language = models.CharField(max_length = 200, choices = LANGUAGE_CHOICE)

    def __str__(self) : 
        return self.name



