from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + ((
        "more info",
        {
            "fields": (
                "language",
                "bio",
                "preference",
                "favourite_book_genre",
                "favourite_movie_genre",
            )
        },
    ), )


    list_filter =('bio','language','preference','favourite_book_genre','favourite_movie_genre')

    list_display=('username','bio','language','preference','favourite_book_genre','favourite_movie_genre')
