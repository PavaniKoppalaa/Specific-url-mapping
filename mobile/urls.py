from django.urls import path
from mobile.views import *
app_name='mobile'
urlpatterns=[
    path('realme/',realme,name='realme.html'),
]