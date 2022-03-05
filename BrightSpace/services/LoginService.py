import json

from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from BrightSpace.services.util.CheckUserNamePasswordMatch import isMatch


@csrf_exempt
def login(request: HttpRequest):
    if request.method != "POST":
        return HttpResponseBadRequest()
    requestBody = json.loads(request.body)
    userName = requestBody["userName"]
    password = requestBody["password"]
    if isMatch(userName=userName, password=password):
        return JsonResponse({"success": True}, status=200)
    else:
        return JsonResponse({"success": False}, status=200)
