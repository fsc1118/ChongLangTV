import json

from django.contrib.auth.hashers import make_password
from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ChongLangTV.models import User
from .util.CheckUserNameAvailability import isUsernameExist


@csrf_exempt
def changePassword(request: HttpRequest):
    if request.method != "POST":
        return HttpResponseBadRequest()
    requestBody = json.loads(request.body)
    userName = requestBody["userName"]
    password = requestBody["password"]
    if isUsernameExist(userName=userName):
        user = User.objects.get(username=userName)
        user.password = make_password(password=password)
        user.save()
        return JsonResponse({"success": True}, status=200)
    else:
        return JsonResponse({"success": False}, status=200)
