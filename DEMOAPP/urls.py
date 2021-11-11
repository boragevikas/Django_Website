from .import views
from django.urls import path
from DEMOAPP import views
urlpatterns = [
    path("", views.index, name='home_page'),
    path("about", views.about, name='about_page'),
    path("contact", views.contact, name='contact_page'),
    path("projects", views.projects, name='services_page'),
    path("home", views.index, name='index_page'),



]