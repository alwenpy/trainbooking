# Train Booking API

This is a simple API for managing seat bookings in a train. The API allows users to book seats, retrieve booked seats, and populate available seats.

## Endpoints

1. **`POST /book-seats/`**  
   - **Description**: Books selected seats for a user. The request body should include the seat numbers to be booked.
   - **Request Body**:
     ```json
     {
       "seat_numbers": ["A1", "B2", "C3"]
     }
     ```

2. **`POST /populate_seats/`**  
   - **Description**: Populates seats in the system. This endpoint could be used to populate the initial available seat data.
   - **Request Body**: No specific data required. This endpoint would populate seats based on pre-defined logic.

3. **`GET /booked-seats/`**  
   - **Description**: Returns a list of all the seats that have been booked.
   - **Response**:
     ```json
     [
       {"row": "A", "seat_number": "1", "is_booked": true},
       {"row": "B", "seat_number": "2", "is_booked": true}
     ]
     ```

## Models

### `Seat` Model
Represents a seat in the train with information such as the row (e.g., A, B, C), seat number (e.g., 1, 2, 3), and whether the seat is booked.

- **Fields**:
  - `row`: The row identifier (e.g., A, B, C).
  - `seat_number`: The seat number (e.g., 1, 2, 3).
  - `is_booked`: Boolean field indicating whether the seat is booked.
  - `booking`: Foreign key linking the seat to a booking (if booked).

- **Methods**:
  - `__str__`: Returns a string representation of the seat in the format "RowSeatNumber" (e.g., "A1").

### `Booking` Model
Represents a booking with a unique `booking_id` and associated seat numbers.

- **Fields**:
  - `booking_id`: Auto-incremented primary key for the booking.
  - `seat_numbers`: Many-to-many relationship with `Seat`, indicating the seats that are booked in this booking.

- **Methods**:
  - `__str__`: Returns a string representation of the booking in the format "Booking {booking_id}" (e.g., "Booking 1").