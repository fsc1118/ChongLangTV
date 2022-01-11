from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
# Create your views here.
from django.template import loader

from . import form


def homePage(request: HttpRequest):
    if request.COOKIES.__contains__("username"):
        tempfile = loader.get_template("BrightSpace/Homepage.html")
        return HttpResponse(tempfile.render(request=request))
    else:
        tempfile = loader.get_template("BrightSpace/login.html")
        context = {"form": form.LoginForm}
        return HttpResponse(tempfile.render(request=request, context=context))


def createUser(request: HttpRequest):
    if request.method != "POST":
        return HttpResponseBadRequest()
    # data = form.LoginForm(request.POST)
    # queryResult = User.objects.get(username=userName)


# def signinPage(requst: HttpRequest):


def loginPage(request: HttpRequest):
    tempfile = loader.get_template("BrightSpace/login.html")
    return HttpResponse(tempfile.render(request=request))
