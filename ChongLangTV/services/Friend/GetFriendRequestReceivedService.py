from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ChongLangTV.models import FriendRequest, User
from ChongLangTV.services.util.CheckUserNameAvailability import isUsernameExist


@csrf_exempt
def getFriendRequestReceived(request: HttpRequest):
    if request.method != "GET":
        return HttpResponseBadRequest()
    receiverName = request.session.get("username", None)
    if receiverName is not None and isUsernameExist(userName=receiverName):
        receiver = User.objects.get(username=receiverName)
        returnList = FriendRequest.objects.filter(receiver=receiver)
        receivedRequests = []
        for i in returnList:
            receivedRequests.append([i.sender.username, i.receiver.username])
        return JsonResponse({"success": True, "friendRequest": receivedRequests}, status=200)
    else:
        return JsonResponse({"success": False})
