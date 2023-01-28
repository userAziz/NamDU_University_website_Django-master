from django.contrib import admin
from django.urls import path,include
from .import views

app_name= 'items'
urlpatterns = [
    path('lost_found/', views.item_list, name='list_of_items'),
#     path('^(?P<slug_path>[\w-]+)/', views.item_details, name='details_of_items'),

]