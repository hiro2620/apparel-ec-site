from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SigninForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

GENDER_CHOICE = (
    (0, "男性"),
    (1, "女性"),
    (2, "その他/回答しない"),
)

class SignUpForm(UserCreationForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICE, initial=2)
    zipcode =forms.CharField(required=True, max_length=7, initial="")
    location =forms.CharField(required=True, max_length=30, initial="")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

