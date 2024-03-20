from django import forms
from phonenumber_field.formfields import PhoneNumberField

from .models import Booking


class BookingForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your First Name",
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your Last Name",
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "your_email@google.com",
            }
        )
    )

    phone_number = PhoneNumberField(
        region="UA",
        widget=forms.TextInput(
            attrs={
                "placeholder": "+380-XX-XXX-XXXX",
                "pattern": "\+380-[0-9]{2}-[0-9]{3}-[0-9]{4}",
                "maxlength": "100",
                "required": True,
            }
        ),
    )

    reservation_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
            }
        )
    )
    reservation_time = forms.ChoiceField(
        choices=[(i, i) for i in range(10, 21)], widget=forms.Select()
    )

    class Meta:
        model = Booking
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "reservation_date",
            "reservation_time",
        ]
