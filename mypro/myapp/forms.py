from django import forms
from django.contrib.auth.models import User
from myapp.models import ModelOne


class FormOne(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username','email','password')

class FormTwo(forms.ModelForm):

    class Meta():
        model = ModelOne
        fields = ('profile_pic','portfolio')