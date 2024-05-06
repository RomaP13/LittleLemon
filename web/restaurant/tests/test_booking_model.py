from django.core.exceptions import ValidationError
from django.test import TestCase
from restaurant.utils import create_booking


class BookingModelTest(TestCase):

    # Test a valid booking object
    def test_booking_creation(self):
        booking = create_booking()
        self.assertEqual(booking.first_name, "John")
        self.assertEqual(booking.last_name, "Doe")
        self.assertEqual(booking.email, "john.doe@example.com")
        self.assertEqual(booking.phone_number, "+380991234567")
        # Format the date object to a string for comparison
        self.assertEqual(booking.reservation_date.strftime("%Y-%m-%d"),
                         "2024-05-10")
        self.assertEqual(booking.reservation_time, 10)

    # Test the booking with blank first_name
    def test_invalid_first_name(self):
        with self.assertRaises(ValidationError):
            create_booking(first_name="")

    # Test the booking with blank last_name
    def test_invalid_last_name(self):
        with self.assertRaises(ValidationError):
            create_booking(last_name="")

    # Test the booking with invalid email
    def test_invalid_email(self):
        with self.assertRaises(ValidationError):
            create_booking(email="invalid_email")

    # Test the booking with invalid phone number
    def test_invalid_phone_number(self):
        with self.assertRaises(ValidationError):
            create_booking(phone_number="1234567890")

    # Test the booking with blank reservation_date
    def test_invalid_reservation_date(self):
        with self.assertRaises(ValidationError):
            create_booking(reservation_date="")

    # Test the booking with blank reservation_time
    def test_invalid_reservation_time(self):
        with self.assertRaises(ValidationError):
            create_booking(reservation_time="")

    # Test the booking above max limit
    def test_reservation_time_above_max(self):
        with self.assertRaises(ValidationError):
            create_booking(reservation_time="100")

    # Test the booking below min limit
    def test_reservation_time_below_min(self):
        with self.assertRaises(ValidationError):
            create_booking(reservation_time="0")
