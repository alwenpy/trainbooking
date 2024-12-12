from django.urls import path
from .views import book_seats, populate_seats

urlpatterns = [
    path("book-seats/", book_seats, name="book_seats"),
        path('populate_seats/', populate_seats, name='populate_seats'),

]
