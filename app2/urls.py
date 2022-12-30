from django.urls import path
from app2.views import *
app_name='friends'
urlpatterns=[
    path('dhanu2/',dhanu2,name='dhanu2'),
]