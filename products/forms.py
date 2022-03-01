from django import forms
from .widgets import CustomClearableFileInput
from .models import Product
from products.widgets import TimePickerInput, DateTimePickerInput
from datetime import datetime, timedelta

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


def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta


class DateForm(forms.Form):
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    time_choice = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        time_field = self.fields['time_choice']
        today = datetime.today()
        
        opening = today.replace(hour=9, minute=0, second=0, microsecond=0)
        closing = today.replace(hour=17, minute=0, second=0, microsecond=0)
        delta = timedelta(minutes=30)
        time_range = datetime_range(opening, closing, delta)
        choices = []
        for dt in time_range:
            value = dt.time
            display = dt.strftime('%H:%M')
            choice = [value, display]
            choices.append(choice)
        time_field.choices = choices


    

# dts = [dt.strftime('%Y-%m-%d T%H:%M Z') for dt in 
#        datetime_range(datetime(2016, 9, 1, 7), datetime(2016, 9, 1, 9+12), 
#        timedelta(minutes=15))]

# print(dts)
