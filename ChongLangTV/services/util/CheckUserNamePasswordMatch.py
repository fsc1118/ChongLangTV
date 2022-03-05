from django.contrib.auth.hashers import check_password

from ChongLangTV.models import User
from .CheckUserNameAvailability import isUsernameExist


def isMatch(userName: str, password: str):
    if isUsernameExist(userName=userName):
        user = User.objects.get(username=userName)
        return check_password(password=password, encoded=user.password)
    return False
