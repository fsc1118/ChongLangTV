from django.urls import path

from . import views

urlpatterns = [
    path('signin', views.signin),
    path('createUser', views.createUser),
    path('checkLogin', views.checkLogin),
    path('checkAvailability', views.checkAvailability)
]
