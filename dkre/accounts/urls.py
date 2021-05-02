from django.urls import path

from . import views

# pertains to /listings
# for a single listing: /listings/23
# needs a parameter in URL
urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard')

]