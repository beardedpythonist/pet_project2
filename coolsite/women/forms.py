from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, Textarea, Select

from .models import *



class UserRegisterForm(UserCreationForm):
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                'class': 'field padding-bottom--24',
                'name': 'password1',
                'placeholder': 'Введите пароль '
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'field padding-bottom--24',
                'name': 'password1',
                'placeholder': 'Введите Имя'
            }
        )
    )

class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'field padding-bottom--24',
                'name': 'password1',
                'placeholder': 'Enter Username'
            }
        )
    )
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                'class': 'field padding-bottom--24',
                'name': 'password1',
                'placeholder': 'Введите пароль  '
            }
        ),
    )



class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title




