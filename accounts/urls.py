from django.urls import path,include
from .import views

app_name = 'accounts'

urlpatterns =[
   path('sign_up/', views.sign_up_view, name='sign_up'),
   path('log_in/', views.log_in_view, name='log_in'),
   path('log_out/', views.log_out_view, name='log_out'),

]