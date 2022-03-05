from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=16, default="Unspecified", primary_key=True)
    password = models.CharField(max_length=16, default="Unspecified")


class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    sendDate = models.DateTimeField(auto_now_add=True)


class UserUserFriendRelationship(models.Model):
    userName1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user1")
    userName2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2")
    relationshipFormationDate = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    postName = models.CharField(max_length=100, default=" ")
    createDate = models.DateTimeField(auto_now_add=True)
    lastRepliedDate = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1024, default=" ")


class ReplyOfPosts(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=1024, default="")
    repliedDate = models.DateTimeField(auto_now_add=True)
    repliedDaterUsername = models.ForeignKey(User, on_delete=models.CASCADE)


class ReplyOfReply(models.Model):
    repliedPost = models.ForeignKey(ReplyOfPosts, on_delete=models.CASCADE)
    content = models.CharField(max_length=1024, default="")
    repliedDate = models.DateTimeField(auto_now_add=True)
    repliedDaterUsername = models.ForeignKey(User, on_delete=models.CASCADE)
