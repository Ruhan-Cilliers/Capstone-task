from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
"""
Form for user registration.

Extends the built-in UserCreationForm provided by Django to include additional fields:
- first_name: First name of the user.
- last_name: Last name of the user.
- email: Email address of the user.

Inherits from:
    UserCreationForm: A form for creating a new user account.

Attributes:
    first_name (CharField): Field for entering the first name.
    last_name (CharField): Field for entering the last name.
    email (EmailField): Field for entering the email address.

Meta:
    model (User): The User model to use for registration.
    fields (list): List of fields to include in the form, including built-in and custom fields.
"""