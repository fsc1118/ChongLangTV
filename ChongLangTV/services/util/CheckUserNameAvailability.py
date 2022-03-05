from ChongLangTV.models import User


def isUsernameExist(userName: str):
    return User.objects.filter(username=userName).count() != 0
