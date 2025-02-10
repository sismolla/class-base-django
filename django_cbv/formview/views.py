from django.shortcuts import render
from .forms import FormClass,LoginForm,SignupForm
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView,UpdateView
from django.shortcuts import get_object_or_404

from .models import Trial
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect


class LoginViewPage(FormView):
    template_name = 'login.html'
    model = User
    form_class = LoginForm
    success_url = reverse_lazy('form_views:listView')

    def form_valid(self, form):
        user =  form.get_user()
        login(self.request,user)
        return redirect(self.success_url)
    

class SignupViewPage(FormView):
    model = User
    form_class = SignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('form_views:listView')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)
    

class FormClass(LoginRequiredMixin, FormView):
    form_class = FormClass
    model = Trial
    login_url = reverse_lazy('form_views:login')
    template_name = 'form.html'
    success_url = reverse_lazy('form_views:listView')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user

        return kwargs   

class ListViewPage(ListView):
    template_name = 'list.html'
    model = Trial
    # login_url = reverse_lazy('form_views:login')
    context_object_name = 'list'
    queryset = Trial.objects.all() #the default one to get all the model objects

    

class DetailViewPage(LoginRequiredMixin,DetailView):
    model = Trial
    login_url = reverse_lazy('form_views:login')
    template_name = 'Detail.html'
    context_object_name = 'detail'

class DeleteViewPage(LoginRequiredMixin,DeleteView):
    template_name  = 'delete.html'
    model = Trial
    login_url = reverse_lazy('form_views:login')
    success_url = reverse_lazy('form_views:listView')


class UpdateViewPage(LoginRequiredMixin,UpdateView):
    model = Trial
    login_url = reverse_lazy('form_views:login')
    fields = ['name','title', 'message']
    template_name = 'update.html'
    success_url = reverse_lazy('form_views:listView')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)