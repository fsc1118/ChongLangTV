import json

from django.contrib.auth.hashers import make_password
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
# Create your views here.
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from . import form
from .models import User


def homePage(request: HttpRequest):
    print("asad")
    if request.COOKIES.__contains__("username"):
        tempfile = loader.get_template("BrightSpace/Homepage.html")
        return HttpResponse(tempfile.render(request=request))
    else:
        tempfile = loader.get_template("BrightSpace/login.html")
        context = {"form": form.LoginForm}
        return HttpResponse(tempfile.render(request=request, context=context))


@csrf_exempt
def checkAvailability(request: HttpRequest, name: str):
    isExist = False
    try:
        res = User.objects.get(username=name)
    except User.DoesNotExist:
        isExist = True
    print(isExist)
    jsonBody = {"isAvailable": isExist}
    return JsonResponse(json.dumps(jsonBody), safe=False)


def signin(request: HttpRequest):
    tempfile = loader.get_template("BrightSpace/signin.html")
    context = {"form": form.SigninForm}
    return HttpResponse(tempfile.render(request=request, context=context))


def createUser(request: HttpRequest):
    print("creat user")
    if request.method != "POST":
        return HttpResponseBadRequest()
    data = form.SigninForm(request.POST)
    if data.is_valid():
        userName = data.cleaned_data["userName"]
        password = data.cleaned_data["password"]
        print(userName + " " + password)
        newUser = User()
        newUser.username = userName
        newUser.password = make_password(password)
        newUser.save()
        res = HttpResponseRedirect("/")
        res.set_cookie("username", userName)
        return res
    else:
        return HttpResponseBadRequest()


# def signinPage(requst: HttpRequest):


def loginPage(request: HttpRequest):
    tempfile = loader.get_template("BrightSpace/login.html")
    return HttpResponse(tempfile.render(request=request))
