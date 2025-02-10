from django import forms
from .models import Trial
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class FormClass(forms.ModelForm):

    class Meta:
        model = Trial
        fields = ['name','title', 'message']

        
    def __init__(self,*args,**kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args,**kwargs)

    def clean_name(self):
        name = self.cleaned_data['name'] 
        if len(name)>6:
            raise  forms.ValidationError('please use less than 6 characters!')
        return name


    def save(self,commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.username = self.user
            instance.save()

