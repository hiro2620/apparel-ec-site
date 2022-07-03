from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SigninForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class SignUpForm(UserCreationForm):
    gender = forms.ChoiceField(choices=(
        ("0", "男性"),
        ("1", "女性"),
        ("2", "その他/回答しない"),
    ))
    birth_date = forms.DateField(
        help_text='YYYY-MM-DD 形式で入力して下さい。',
        label='誕生日',
    )
    location =forms.CharField(required=False)
    favorite_words = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

