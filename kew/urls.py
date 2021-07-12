
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('myapp.urls')),
    path('keshav_e_world', include('myapp.urls')),
    path('admin/', admin.site.urls),
]
