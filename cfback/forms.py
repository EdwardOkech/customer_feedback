from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from cfback.models import *

SEX = (
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
        )
USER_TYPE = (
    ('customer','Customer'),
    ('employee','Employee')
    )
class UserRegistrationForm(forms.Form):
    username = forms.CharField( max_length=30)
    first_name = forms.CharField( max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(
        widget = forms.PasswordInput()
        )
    password2 = forms.CharField(
        widget = forms.PasswordInput()
        )

    def clean_password(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Passwords do not match')


    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ['date_posted','status']


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        exclude = ['answer']

##class DeveloperRegistrationForm(ModelForm):
##
##    class Meta:
##        model=Developer
##        exclude=['user']
##
##class ClientRegistrationForm(ModelForm):
##
##    class Meta:
##        model=Client
##        exclude=['user']
