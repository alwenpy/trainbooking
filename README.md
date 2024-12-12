# Train Booking API

This is a simple API for managing seat bookings in a train. The API allows users to book seats, retrieve all seat information, get details of booked seats, and populate seats initially.

## Endpoints

1. **`POST /book-seats/`**  
   - **Description**: Books a specified number of available seats. The request body should contain the number of seats to book.
   - **Request Body**:
     ```json
     {
       "num_seats": 3
     }
     ```
   - **Response**:
     - **Success**: 
       ```json
       {
         "booked_seats": ["A1", "A2", "A3"]
       }
       ```
     - **Error** (if not enough seats available): 
       ```json
       {
         "error": "Not enough seats available"
       }
       ```

2. **`POST /populate-seats/`**  
   - **Description**: Populates seats in the system. This endpoint creates seats with row labels from `A` to `L` and seat numbers from `1` to `7`.
   - **Response**:
     ```json
     {
       "message": "Seats populated successfully!"
     }
     ```

3. **`GET /seat-info/`**  
   - **Description**: Returns all seat information, including whether each seat is booked or not.
   - **Response**:
     ```json
     {
       "booked_seats": [
         {"row": "A", "seat_number": "1", "is_booked": true},
         {"row": "B", "seat_number": "2", "is_booked": false}
       ]
     }
     ```

4. **`GET /get-booked-seats/`**  
   - **Description**: Returns a list of all booked seats.
   - **Response**:
     ```json
     {
       "booked_seats": [
         {"row": "A", "seat_number": "1"},
         {"row": "B", "seat_number": "2"}
       ]
     }
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