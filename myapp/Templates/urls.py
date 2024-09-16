# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_email, name='send_email'),
    path('success/', views.success, name='success'),
]
# myproject/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
