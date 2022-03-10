from django import forms
from datetimepicker.widgets import DateTimePicker
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from .widgets import CustomClearableFileInput
from .models import Product
from datetimewidget.widgets import DateTimeWidget
from datetime import datetime


dateTimeOptions = {
    'minuteStep': 30,
    'startDate': datetime.now(),
}


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

    dt = forms.DateTimeField(widget=DateTimeWidget(options=dateTimeOptions))

        


# dts = [dt.strftime('%Y-%m-%d T%H:%M Z') for dt in 
#        datetime_range(datetime(2016, 9, 1, 7), datetime(2016, 9, 1, 9+12), 
#        timedelta(minutes=15))]

# print(dts)
