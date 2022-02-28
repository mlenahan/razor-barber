from django import forms
from .widgets import CustomClearableFileInput
from .models import Product
from products.widgets import TimePickerInput, DateTimePickerInput

CHOICES = (
    (10.00, '10.00'),
    (10.30, '10.30'),
    (11.00, '11.00'),
    (11.30, '11.30'),
    (12.00, '12.00'),
    (12.30, '12.30'),
    (13.00, '13.00'),
    (13.30, '13.30'),
    (14.00, '14.00'),
    (14.30, '14.30'),
    (15.00, '15.00'),
    (15.30, '15.30'),
    (16.00, '16.00'),
    (16.30, '16.30'),
    (17.00, '17.00'),
    (17.30, '17.30'),
    (18.00, '18.00'),
    (18.30, '18.30'),
)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DateForm(forms.Form):
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    time_choice = forms.ChoiceField(choices=CHOICES)
