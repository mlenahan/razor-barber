from django import forms
from .widgets import (
    CustomClearableFileInput,
    DatePickerInput,
    TimePickerInput,
)
from .models import Product
from datetime import datetime


dateTimeOptions = {
    "minuteStep": 30,
    "startDate": datetime.now(),
}


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )


def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta


class DateForm(forms.Form):
    date = forms.DateField(widget=DatePickerInput)
    time_choice = forms.TimeField(widget=TimePickerInput)
