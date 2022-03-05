from django.urls import path

from .services.Account import ChangePasswordService, LoginService, SigninService
from .services.Friend import SendFriendRequestServiceService, \
    GetFriendRequestReceivedService, AcceptFriendRequestService, ViewFriendService

urlpatterns = [
    path('signin', SigninService.signin),
    path('login', LoginService.login),
    path('changePassword', ChangePasswordService.changePassword),
    path('f', SendFriendRequestServiceService.sendFriendRequest),
    path('getRequests', GetFriendRequestReceivedService.getFriendRequestReceived),
    path('a', AcceptFriendRequestService.acceptFriendRequestReceived),
    path('v', ViewFriendService.viewFriends)
]
