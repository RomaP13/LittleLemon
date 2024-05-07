from django.core.exceptions import ValidationError
from django.test import TestCase
from restaurant.utils import create_booking


class BookingModelTest(TestCase):

    def test_booking_creation(self):
        """Test a valid booking object"""
        booking = create_booking()
        self.assertEqual(booking.first_name, "John")
        self.assertEqual(booking.last_name, "Doe")
        self.assertEqual(booking.email, "john.doe@example.com")
        self.assertEqual(booking.phone_number, "+380991234567")
        # Format the date object to a string for comparison
        self.assertEqual(booking.reservation_date.strftime("%Y-%m-%d"),
                         "2024-05-10")
        self.assertEqual(booking.reservation_time, 10)

    def test_invalid_first_name(self):
        """Test the booking with blank first_name"""
        with self.assertRaises(ValidationError):
            create_booking(first_name="")

    def test_invalid_last_name(self):
        """Test the booking with blank last_name"""
        with self.assertRaises(ValidationError):
            create_booking(last_name="")

    def test_invalid_email(self):
        """Test the booking with invalid email"""
        with self.assertRaises(ValidationError):
            create_booking(email="invalid_email")

    def test_invalid_phone_number(self):
        """Test the booking with invalid phone number"""
        with self.assertRaises(ValidationError):
            create_booking(phone_number="1234567890")

    def test_invalid_reservation_date(self):
        """Test the booking with blank reservation_date"""
        with self.assertRaises(ValidationError):
            create_booking(reservation_date="")

    def test_invalid_reservation_time(self):
        """Test the booking with blank reservation time"""
        with self.assertRaises(ValidationError):
            create_booking(reservation_time="")

    def test_reservation_time_above_max(self):
        """Test the booking above max limit"""
        with self.assertRaises(ValidationError):
            create_booking(reservation_time="100")

    def test_reservation_time_below_min(self):
        """Test the booking below min limit"""
        with self.assertRaises(ValidationError):
            create_booking(reservation_time="0")
