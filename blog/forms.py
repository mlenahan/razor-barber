from django import forms
from .models import Reply


class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'body': 'Enter your reply here',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ('border-black '
                                                        'rounded-0 '
                                                        'profile-form-input')
            self.fields[field].label = False
