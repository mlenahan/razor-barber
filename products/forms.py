from django import forms
from django.contrib.admin import widgets
from .widgets import CustomClearableFileInput
from .models import Product
from products.widgets import TimePickerInput, DateTimePickerInput
from datetime import datetime, timedelta


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
    dt = forms.DateTimeField(widget=widgets.AdminSplitDateTime)


        

    

# dts = [dt.strftime('%Y-%m-%d T%H:%M Z') for dt in 
#        datetime_range(datetime(2016, 9, 1, 7), datetime(2016, 9, 1, 9+12), 
#        timedelta(minutes=15))]

# print(dts)
