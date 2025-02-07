from django.shortcuts import render
from .forms import FormClass
from django.views.generic.edit import FormView


class FormClass(FormView):
    form_class = FormClass
    template_name = 'form.html'
