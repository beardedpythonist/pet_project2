from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, Select

from .models import *


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=250)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10}))
    is_published = forms.BooleanField()
    cat = forms.ModelChoiceField(queryset=Category.objects.all())
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='ЛОгин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    Password1 = forms.CharField(label='пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    Password2= forms.CharField(label='пароль повтор', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')
        widgets = {'username':  forms.TextInput(attrs={'class': 'form-input'}),
            'password':  forms.PasswordInput(attrs={'class': 'form-input'}),
          'password2': forms.PasswordInput(attrs={'class': 'form-input'})
        }