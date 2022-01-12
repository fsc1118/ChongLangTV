from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage),
    path('signin', views.signin),
    path('createUser', views.createUser),
    path('checkAvailability/<str:name>', views.checkAvailability)
]
