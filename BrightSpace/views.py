import json

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse, HttpResponse
# Create your views here.
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from .models import User


def signin(request: HttpRequest):
    tempfile = loader.get_template("BrightSpace/signin.html")
    return HttpResponse(tempfile.render(request=request))


def login(request: HttpRequest):
    tempfile = loader.get_template("BrightSpace/login.html")
    return HttpResponse(tempfile.render(request=request))


@csrf_exempt
def checkAvailability(request: HttpRequest):
    if request.method != "POST":
        return HttpResponseBadRequest()
    data = request.body.decode("utf-8")
    json_data = json.loads(data)
    if "name" not in json_data:
        return HttpResponseBadRequest()
    name = json_data["name"]
    canBeUsed = False
    try:
        User.objects.get(username=name)
    except User.DoesNotExist:
        canBeUsed = True
    resultantJson = {"status": 200, "statusText": "OK", "canBeUsed": canBeUsed}
    return JsonResponse(resultantJson)


@csrf_exempt
def checkLogin(request: HttpRequest):
    if request.method != "POST":
        return HttpResponseBadRequest()
    body_unicode = request.body.decode('utf-8')
    json_data = json.loads(body_unicode)
    if "username" not in json_data or "password" not in json_data:
        return HttpResponseBadRequest()
    username = json_data["username"]
    password = json_data["password"]
    resultant_json = {"status": 200, "statusText": "OK", "isPasswordMatch": True, "isUsernameExist": True}
    try:
        res = User.objects.get(username=username)
        realPassword = res.password
        if check_password(password, realPassword):
            return JsonResponse(resultant_json, safe=False)
        else:
            resultant_json["isPasswordMatch"] = False
            return JsonResponse(resultant_json, safe=False)
    except User.DoesNotExist:
        resultant_json["isUsernameExist"] = False
        return JsonResponse(resultant_json)


@csrf_exempt
def createUser(request: HttpRequest):
    if request.method != "POST":
        return HttpResponseBadRequest()
    data = request.body.decode("utf-8")
    json_data = json.loads(data)
    if "username" not in json_data or "password" not in json_data:
        return HttpResponseBadRequest()
    name = json_data["username"]
    password = json_data["password"]
    newUser = User(username=name, password=make_password(password))
    newUser.save()
    return JsonResponse({"status": 200, "statusText": "OK"})
