from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import LoginViewPage,SignupViewPage, FormClass,ListViewPage,DetailViewPage,DeleteViewPage,UpdateViewPage


app_name = 'form_views'

urlpatterns = [
    path('login/',LoginViewPage.as_view(), name='login'),
    path('signup/',SignupViewPage.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('form/',FormClass.as_view(), name = 'forms'),
    path('',ListViewPage.as_view(), name = 'listView'),
    path("detail/<slug:slug>/", DetailViewPage.as_view(), name="detail"),
    path('delete/<slug:slug>/',DeleteViewPage.as_view(), name='delete'),
    path('edit/<slug:slug>/',UpdateViewPage.as_view(), name='edit'),

]