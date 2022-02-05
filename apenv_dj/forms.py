import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True, help_text='Enter a valid e-mail address')
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

""" class createSunshineForm(forms.Form):
    reminder_date = forms.DateField(help_text="Enter a date", label_suffix='')
    reminder_time = forms.TimeField(label_suffix='')

    def clean_reminder_date():
        data = self.cleaned_data['reminder_date']
          # Check that date is in the future
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - cannot be in the past'))

        return data """

