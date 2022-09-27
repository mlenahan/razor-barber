from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Review
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


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['content'].label = False
        self.fields['content'].widget.attrs['placeholder'] = (
            'Please write your review here...'
        )
        self.fields['content'].widget.attrs['rows'] = 5
        self.fields['content'].widget.attrs['class'] = 'review-form-input'
        self.fields['content'].widget.attrs['id'] = 'review-form-content'
        self.fields['content'].widget.attrs['aria-label'] = 'review content'
