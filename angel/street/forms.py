from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    bio = forms.CharField(help_text='A bit about yourself')
    email = forms.EmailField(help_text="A valid email id")
    pic  = forms.FileField(help_text="A picture of you!")


    class Meta:
        model = User
        fields = ('username', 'bio', 'email' , 'pic' ,'password1', 'password2', )
