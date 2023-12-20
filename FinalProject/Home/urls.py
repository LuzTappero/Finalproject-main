
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.Home, name='Home'),
    path('registro/', views.registro_view, name='registro'), #type:ignore
    path('login/', views.login_view, name='login')
    # path('logout', LogoutView.as_view(template_name='Home/logout.html'), name='logout')
]
