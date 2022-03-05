from django.urls import path

from .services import LoginService, SigninService, ChangePasswordService

urlpatterns = [
    path('signin', SigninService.signin),
    path('login', LoginService.login),
    path('changePassword', ChangePasswordService.changePassword)
]
