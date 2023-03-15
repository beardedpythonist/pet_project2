from django.contrib.auth.forms import *
from django.core.exceptions import ValidationError
from django.forms import  Textarea
from django.utils.translation import gettext as _

from .models import *

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                'class': 'input100',
                'name': 'password1',
                'placeholder': 'Enter Password'
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                'class': 'input100',
                'name': 'password1',
                'placeholder': 'Re-Enter Password'
            }
        ),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'input100',
                'name': 'password1',
                'placeholder': 'Enter Username'
            }
        )
    )

class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'input100',
                'name': 'password1',
                'placeholder': 'Enter Username'
            }
        )
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                'class': 'input100',
                'name': 'password1',
                'placeholder': 'Re-Enter Password'
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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget = Textarea(attrs={'rows':2})
