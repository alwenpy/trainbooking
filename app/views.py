import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Seat, Booking
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q


@csrf_exempt
def book_seats(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            num_seats = int(data.get("num_seats", 0))  

            # Validate if the number of seats is positive
            if num_seats <= 0:
                return JsonResponse({"error": "Invalid number of seats"}, status=400)

            available_seats = list(Seat.objects.filter(is_booked=False).order_by('row', 'seat_number'))
            
            # If there aren't enough available seats, return an error
            if len(available_seats) < num_seats:
                return JsonResponse({"error": "Not enough seats available"}, status=400)

            # Group available seats by row
            grouped_seats = {}
            for seat in available_seats:
                grouped_seats.setdefault(seat.row, []).append(seat)

            booked_seats = [] 

            # Iterate through rows to find contiguous available seats in the same row
            for row in sorted(grouped_seats.keys()):
                seats_in_row = grouped_seats[row]

                # If there are not enough seats in this row, skip to the next row
                if len(seats_in_row) < num_seats:
                    continue

                # Book the required number of seats in this row
                booked_seats.extend(seats_in_row[:num_seats])
                grouped_seats[row] = seats_in_row[num_seats:]  # Update remaining seats in the row

                if len(booked_seats) >= num_seats:
                    break  # Stop once enough seats are booked

            # If enough seats weren't booked in the same row, try to book them in adjacent rows
            if len(booked_seats) < num_seats:
                for row in sorted(grouped_seats.keys()):
                    if len(booked_seats) >= num_seats:
                        break  # Stop if enough seats have been booked
                    for seat in grouped_seats[row]:
                        if len(booked_seats) < num_seats:
                            booked_seats.append(seat)
                        else:
                            break 
            if len(booked_seats) < num_seats:
                return JsonResponse({"error": "Not enough seats available after checking adjacent rows"}, status=400)

            # Mark the booked seats as taken in the database
            for seat in booked_seats:
                seat.is_booked = True
                seat.save()

            # Return the booked seats as a response
            return JsonResponse({"booked_seats": [f"{seat.row}{seat.seat_number}" for seat in booked_seats]})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


def populate_seats(request):
    rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    seat_numbers = range(1, 8) 

    # Iterate through each row and seat number to create and save a Seat object
    for row in rows:
        for seat_number in seat_numbers:
            seat = Seat(row=row, seat_number=str(seat_number)) 
            if not len(seat.seat_number) == 80:  # Check if seat_number is not of length 80 (validation step)
                seat.save() 
    return JsonResponse({"message": "Seats populated successfully!"})
