from django.urls import path
from .views import book_seats, populate_seats,get_booked_seats, get_all_seat_info

urlpatterns = [
    path("book-seats/", book_seats, name="book_seats"),
        path('populate-seats/', populate_seats, name='populate_seats'),
        path('seat-info/', get_all_seat_info, name='get_all_seat_info'),
        path('get-booked-seats/', get_booked_seats, name='get_booked_seats'),   
]
