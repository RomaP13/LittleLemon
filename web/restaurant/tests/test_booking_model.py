from django.core.exceptions import ValidationError
from django.test import TestCase
from restaurant.utils import create_booking


class BookingModelTest(TestCase):

    def test_booking_creation(self):
        # Create a valid booking object
        booking = create_booking()

        # Assert the booking was created successfully
        self.assertEqual(booking.first_name, "John")
        self.assertEqual(booking.last_name, "Doe")
        self.assertEqual(booking.email, "john.doe@example.com")
        self.assertEqual(booking.phone_number, "+380991234567")
        self.assertEqual(booking.reservation_date, "2024-05-10")
        self.assertEqual(booking.reservation_time, "10")

    def test_invalid_first_name(self):
        # Test that an exception is raised for booking with empty first_name
        booking_invalid_first_name = create_booking(first_name="")
        self.assertRaises(ValidationError,
                          booking_invalid_first_name.full_clean)

    def test_invalid_last_name(self):
        # Test that an exception is raised for booking with empty last_name
        booking_invalid_last_name = create_booking(last_name="")
        self.assertRaises(ValidationError,
                          booking_invalid_last_name.full_clean)

    def test_invalid_email(self):
        # Test that an exception is raised for booking with invalid email
        booking_invalid_email = create_booking(email="invalid_email")
        self.assertRaises(ValidationError,
                          booking_invalid_email.full_clean)

    def test_invalid_phone_number(self):
        # Test that an exception is raised for booking with invalid phone number
        booking_invalid_phone_number = create_booking(phone_number="1234567890")
        self.assertRaises(ValidationError,
                          booking_invalid_phone_number.full_clean)

    def test_invalid_reservation_date(self):
        # Test that an exception is raised for booking with empty reservation_date
        booking_invalid_reservation_date = create_booking(reservation_date="")
        self.assertRaises(ValidationError,
                          booking_invalid_reservation_date.full_clean)

    def test_invalid_reservation_time(self):
        # Test that an exception is raised for booking with empty reservation_time
        booking_invalid_reservation_time = create_booking(reservation_time="")
        self.assertRaises(ValidationError,
                          booking_invalid_reservation_time.full_clean)

    def test_reservation_time_above_max(self):
        # Test that an exception is raised for booking with reservation_time above max limit
        booking_invalid_reservation_time = create_booking(reservation_time="100")
        self.assertRaises(ValidationError,
                          booking_invalid_reservation_time.full_clean)

    def test_reservation_time_below_min(self):
        # Test that an exception is raised for booking with reservation_time below min limit
        booking_invalid_reservation_time = create_booking(reservation_time="0")
        self.assertRaises(ValidationError,
                          booking_invalid_reservation_time.full_clean)
