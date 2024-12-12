from django.urls import path
from .views import book_seats, populate_seats,get_booked_seats

urlpatterns = [
    path("book-seats/", book_seats, name="book_seats"),
        path('populate_seats/', populate_seats, name='populate_seats'),
        path('booked-seats/', get_booked_seats, name='booked_seats'),

]
