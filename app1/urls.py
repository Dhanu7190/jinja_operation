from django.urls import path
from app1.views import *
app_name='dhanu'
urlpatterns=[
    path('dhanu1/',dhanu1,name='dhanu1'),
]