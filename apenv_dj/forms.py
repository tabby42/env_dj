import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class createGoalForm(forms.Form):
    reminder_date = forms.DateField(help_text="Enter a date", label_suffix='')
    reminder_time = forms.TimeField(label_suffix='')

    def clean_reminder_date():
        data = self.cleaned_data['reminder_date']
          # Check that date is in the future
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - cannot be in the past'))

        return data

