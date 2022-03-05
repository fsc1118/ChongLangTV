from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ChongLangTV.models import FriendRequest, User
from ChongLangTV.services.util.CheckUserNameAvailability import isUsernameExist


@csrf_exempt
def sendFriendRequest(request: HttpRequest):
    if request.method != "GET":
        return HttpResponseBadRequest()
    sender = request.GET.get("sender", None)
    receiver = request.GET.get("receiver", None)
    if sender is not None and receiver is not None and isUsernameExist(userName=sender) and isUsernameExist(
            userName=receiver):
        senderEntry = User.objects.get(username=sender)
        receiverEntry = User.objects.get(username=receiver)
        newFriendRequest = FriendRequest(sender=senderEntry, receiver=receiverEntry)
        newFriendRequest.save()
        return JsonResponse({"success": True}, status=200)
    else:
        return JsonResponse({"success": False}, status=200)
