from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from customuser.models import User, Genders


class SignUpUserForm(UserCreationForm):
    display_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Nickname',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    profile_image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your First Name',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Last Name',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    gender = forms.ModelChoiceField(queryset=Genders.objects.all(), empty_label='Homosexual', widget=forms.Select(attrs={
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    bio = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Bio',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    class Meta:
        model = User
        fields = ('display_name', 'profile_image', 'email', 'first_name', 'last_name', 'gender', 'bio')


class SignInUserForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))


class UpdateUserForm(forms.ModelForm):
    paypal_email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'placeholder': 'Your paypal_email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    class Meta:
        model = User
        fields = ('paypal_email', )

