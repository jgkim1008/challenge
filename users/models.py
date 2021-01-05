from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

  """user model"""
  PREFERENCE_MOVIES = "movies"
  PREFERENCE_BOOKS = "books"

  PREFERENCE_CHOICES = (PREFERENCE_MOVIES,"movies"),(PREFERENCE_BOOKS,"books")

  

  bio = models.TextField(
        default="", blank=True
        )

  LANGUEAGE_ENGLISH = "english"
  LANGUEAGE_KOREAN = "korean"

  LANGUEAGE_CHOICES = (LANGUEAGE_ENGLISH,"english"),(LANGUEAGE_KOREAN, "korean")

  language = models.CharField(
        choices=LANGUEAGE_CHOICES,max_length=10, blank=True
        )
  preference = models.TextField(
        choices=PREFERENCE_CHOICES,max_length=10, blank=True
        )

  favourite_book_genre = models.TextField(
    default="", blank = True)
  favourite_movie_genre = models.TextField(
    default="", blank = True)