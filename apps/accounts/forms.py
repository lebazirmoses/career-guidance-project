from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    # Defining these manually to add Tailwind-friendly placeholders
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Minimum 8 characters'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}),
        label='Confirm Password'
    )

    class Meta:
        model = CustomUser
        # password MUST be in this list to be processed by the form
        fields = [
            'full_name', 'email', 'password', 'phone', 
            'date_of_birth', 'gender', 'state', 'city', 'education_level'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password")
        p2 = cleaned_data.get("password2")

        if p1 and p2 and p1 != p2:
            self.add_error('password2', "Passwords do not match.")
        
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        # set_password handles the PBKDF2 hashing automatically
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'your@email.com', 'autofocus': True})
    )