from django import forms


class FormClass(forms.Form):
    name = forms.CharField()
    message = forms.CharField(
    )


