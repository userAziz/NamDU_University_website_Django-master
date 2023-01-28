from django.contrib import admin
from django.urls import path,include
from .import views

app_name= 'contact'
urlpatterns = [
    path('contact/', views.contact, name='contact'),
#     path('^(?P<slug_path>[\w-]+)/', views.item_details, name='details_of_items'),

]