from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = Student
        fields = [
            'username', 'first_name', 'last_name', 'email', 'password',  # These fields are required for user creation
            'date_of_birth', 'gender', 'phone_number', 'address',  # Student-specific fields
        ]