from models import Seat
from django.http import JsonResponse
def populate_seats(request):
    Seat.objects.all().delete()  # Clear existing seats

    rows = "ABCDEFGHIJKL"  # 12 rows labeled A-L
    seat_count = 1

    for row in rows:
        seats_in_row = 7  # Each row has 7 seats
        for seat in range(1, seats_in_row + 1):
            Seat.objects.create(seat_number=f"{row}{seat}", is_booked=False)
            seat_count += 1

    return JsonResponse({"message": "Seats populated successfully!"})
