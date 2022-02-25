from django import forms
from .widgets import CustomClearableFileInput
from .models import Product
from products.widgets import TimePickerInput, DateTimePickerInput


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DateForm(forms.Form):
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    my_time_field = forms.TimeField(widget=TimePickerInput)
    my_date_time_field = forms.DateTimeField(widget=DateTimePickerInput)
