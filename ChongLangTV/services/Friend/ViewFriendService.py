from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ChongLangTV.models import UserUserFriendRelationship
from ChongLangTV.services.util.CheckUserNameAvailability import isUsernameExist


@csrf_exempt
def viewFriends(request: HttpRequest):
    if request.method != "GET":
        return HttpResponseBadRequest()
    userName = "abcd"
    if userName is not None and isUsernameExist(userName=userName):
        list1 = UserUserFriendRelationship.objects.filter(userName1=userName)
        list2 = UserUserFriendRelationship.objects.filter(userName2=userName)
        friends = []
        for i in list1:
            friends.append(i.userName2.username)
        for i in list2:
            friends.append(i.userName1.username)
        return JsonResponse({"success": True, "friends": friends}, status=200)
    else:
        return JsonResponse({"success": False}, status=200)
