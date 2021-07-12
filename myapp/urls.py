from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('evs', views.evs, name='evs'),
    path('java', views.java, name='java'),
    path('cm', views.cm, name='cm'),
    path('maths2', views.maths2, name='maths2'),
    path('physics', views.physics, name='physics'),
    path('tn', views.tn, name='tn'),
    path('ws', views.ws, name='ws'),
    path('ref', views.ref, name='ref'),
    
]