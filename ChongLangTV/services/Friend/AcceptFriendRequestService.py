import json

from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ChongLangTV.models import FriendRequest, User, UserUserFriendRelationship
from ChongLangTV.services.util.CheckUserNameAvailability import isUsernameExist


@csrf_exempt
def acceptFriendRequestReceived(request: HttpRequest):
    if request.method != "POST":
        return HttpResponseBadRequest()
    receiverName = request.session.get("username", None)
    receiverName = "abc"
    senderName = json.loads(request.body)["sender"]
    if receiverName is not None and isUsernameExist(userName=receiverName) and isUsernameExist(userName=senderName):
        receiver = User.objects.get(username=receiverName)
        sender = User.objects.get(username=senderName)
        try:
            friendRequest = FriendRequest.objects.get(receiver=receiver, sender=sender)
            friendRequest.delete()
            UserUserFriendRelationship(userName1=receiver, userName2=sender).save()
            return JsonResponse({"success": True}, status=200)
        except User.DoesNotExist:
            return JsonResponse({"success": False}, status=200)
    else:
        return JsonResponse({"success": False})
