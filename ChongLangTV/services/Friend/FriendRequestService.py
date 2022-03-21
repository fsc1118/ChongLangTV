import json

from django.http import HttpRequest, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from ChongLangTV.models import FriendRequest, User, UserUserFriendRelationship
from ChongLangTV.services.util.CheckUserNameAvailability import isUsernameExist


@csrf_exempt
def friendRequestService(request: HttpRequest):
    body = json.loads(request.body)

    # Accept a friend request
    if request.method == "PUT":
        receiver = request.session.get("userName", None)
        receiver = "def"
        sender = body["sender"]
        if receiver is not None \
                and isUsernameExist(userName=sender) \
                and isUsernameExist(userName=receiver):
            receiver = User.objects.get(username=receiver)
            sender = User.objects.get(username=sender)
            try:
                friendRequest = FriendRequest.objects.get(receiver=receiver, sender=sender)
                friendRequest.delete()
                UserUserFriendRelationship(userName1=receiver, userName2=sender).save()
                return JsonResponse({"success": True}, status=200)
            except User.DoesNotExist:
                return JsonResponse({"success": False}, status=200)
        else:
            return JsonResponse({"success": False})

    # view all friend requests
    if request.method == "GET":
        receiver = request.session.get("userName", None)
        receiver = "abc"
        if receiver is not None and isUsernameExist(userName=receiver):
            receiver = User.objects.get(username=receiver)
            returnList = FriendRequest.objects.filter(receiver=receiver)
            receivedRequests = []
            for i in returnList:
                receivedRequests.append([i.sender.username, i.receiver.username])
            return JsonResponse({"success": True, "friendRequest": receivedRequests}, status=200)
        else:
            return HttpResponseBadRequest()

    # send a request
    if request.method == "POST":
        sender = request.session.get("userName", None)
        sender = "abc"
        receiver = json.loads(request.body)["receiver"]

        if sender is not None and receiver is not None and isUsernameExist(userName=sender) and isUsernameExist(
                userName=receiver):
            senderEntry = User.objects.get(username=sender)
            receiverEntry = User.objects.get(username=receiver)
            try:
                FriendRequest.objects.get(sender=senderEntry, receiver=receiverEntry)
                return JsonResponse({"success": True}, status=200)
            except FriendRequest.DoesNotExist:
                newFriendRequest = FriendRequest(sender=senderEntry, receiver=receiverEntry)
                newFriendRequest.save()
                return JsonResponse({"success": True}, status=200)
        else:
            return JsonResponse({"success": False}, status=200)

    # decline a friend request
    if request.method == "DELETE":
        sender = body["sender"]
        receiver = request.session.get("userName", None)
        receiver = "def"
        if sender is not None \
                and receiver is not None \
                and isUsernameExist(userName=sender) \
                and isUsernameExist(userName=receiver):
            try:
                friendRequest = FriendRequest.objects.get(receiver=receiver, sender=sender)
                friendRequest.delete()
                return JsonResponse({"success": True}, status=200)
            except User.DoesNotExist:
                return JsonResponse({"success": False}, status=200)
    return HttpResponseBadRequest()
