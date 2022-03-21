import json

from django.contrib.auth.hashers import make_password
from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ChongLangTV.models import User
from ChongLangTV.services.util.CheckUserNameAvailability import isUsernameExist


@csrf_exempt
def signup(request: HttpRequest):
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
        request.session["userName"] = userName
        return JsonResponse({"success": True}, status=200)
