from django.db import models

class Seat(models.Model):
    row = models.CharField(max_length=1,default=None,null=True)  # A, B, C
    seat_number = models.CharField(max_length=3,null=True)  # 1, 2, 3
    is_booked = models.BooleanField(default=False)
    booking = models.ForeignKey(
        'Booking', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        related_name='seats'
    )

    def __str__(self):
        return f"{self.row}{self.seat_number}"


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    seat_numbers = models.ManyToManyField(
        Seat,
        related_name='bookings' 
    )

    def __str__(self):
        return f"Booking {self.booking_id}"
