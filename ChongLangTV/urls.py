from django.urls import path

from .services.Account import ChangePasswordService, LoginService, SignupService
from .services.Friend import ViewFriendService, FriendRequestService
from .services.Post import PostService

urlpatterns = [
    path('signup', SignupService.signup),
    path('login', LoginService.login),
    path('password', ChangePasswordService.changePassword),
    path('request', FriendRequestService.friendRequestService),
    path('friend', ViewFriendService.viewFriends),
    path('post', PostService.postService)
]
