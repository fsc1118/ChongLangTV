import json

from django.contrib.auth.hashers import make_password
from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .util.CheckUserNameAvailability import isUsernameExist
from ..models import User


@csrf_exempt
def signin(request: HttpRequest):
    if request.method != "POST":
        return HttpResponseBadRequest()
    requestBody = json.loads(request.body)
    userName = requestBody["userName"]
    password = requestBody["password"]
    if isUsernameExist(userName=userName):
        return JsonResponse({"success": False}, status=200)
    else:
        newUser = User(username=userName, password=make_password(password))
        newUser.save()
        return JsonResponse({"success": True}, status=200)
