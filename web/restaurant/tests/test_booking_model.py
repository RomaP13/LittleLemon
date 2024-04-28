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
        self.assertEqual(booking.reservation_date, "2024-05-10")
        self.assertEqual(booking.reservation_time, "10")

    # Test the booking with blank first_name
    def test_invalid_first_name(self):
        booking_invalid_first_name = create_booking(first_name="")
        self.assertRaises(ValidationError,
                          booking_invalid_first_name.full_clean)

    # Test the booking with blank last_name
    def test_invalid_last_name(self):
        booking_invalid_last_name = create_booking(last_name="")
        self.assertRaises(ValidationError,
                          booking_invalid_last_name.full_clean)

    # Test the booking with invalid email
    def test_invalid_email(self):
        booking_invalid_email = create_booking(email="invalid_email")
        self.assertRaises(ValidationError,
                          booking_invalid_email.full_clean)

    # Test the booking with invalid phone number
    def test_invalid_phone_number(self):
        booking_invalid_phone_number = create_booking(
            phone_number="1234567890")
        self.assertRaises(ValidationError,
                          booking_invalid_phone_number.full_clean)

    # Test the booking with blank reservation_date
    def test_invalid_reservation_date(self):
        booking_invalid_reservation_date = create_booking(reservation_date="")
        self.assertRaises(ValidationError,
                          booking_invalid_reservation_date.full_clean)

    # Test the booking with blank reservation_time
    def test_invalid_reservation_time(self):
        booking_invalid_reservation_time = create_booking(reservation_time="")
        self.assertRaises(ValidationError,
                          booking_invalid_reservation_time.full_clean)

    # Test the booking above max limit
    def test_reservation_time_above_max(self):
        booking_invalid_reservation_time = create_booking(
            reservation_time="100")
        self.assertRaises(ValidationError,
                          booking_invalid_reservation_time.full_clean)

    # Test the booking below min limit
    def test_reservation_time_below_min(self):
        booking_invalid_reservation_time = create_booking(reservation_time="0")
        self.assertRaises(ValidationError,
                          booking_invalid_reservation_time.full_clean)
