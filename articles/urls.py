from django.contrib import admin
from django.urls import path,include
from .import views

app_name= 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.article_create, name='article.create'),
    path('article/', views.article_list, name='list_of_articles'),
    path('^(?P<slug>[\w-]+)/', views.article_details, name='details_of_articles'),
    path('our_team/', views.our_team, name='our_team'),
    path('majors/', views.majors, name='majors'),
    path('admissions/', views.admissions, name='admissions'),
    path('campus/', views.campus, name='campus'),
]