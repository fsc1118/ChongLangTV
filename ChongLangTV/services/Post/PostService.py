import json

from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ChongLangTV.models import User, Post
from ChongLangTV.services.util.CheckUserNameAvailability import isUsernameExist


@csrf_exempt
def postService(request: HttpRequest):
    body = json.loads(request.body)
    if request.method == "POST":
        creator = request.session.get("userName", None)
        creator = "abc"
        postName = body["postName"]
        postContent = body["content"]
        if postName is not None and postContent is not None and isUsernameExist(creator):
            user = User.objects.get(username=creator)
            newPost = Post()
            newPost.postName = postName
            newPost.content = postContent
            newPost.creator = user
            newPost.save()
            return JsonResponse({"success": True}, status=200)
        return HttpResponseBadRequest()

    if request.method == "GET":
        postId = request.GET.get("id", None)
        name = request.GET.get("name", None)
        postName = request.GET.get("postName", None)
        result = Post.objects.all()
        if postId is not None:
            result = result.filter(id=postId)
        if name is not None and isUsernameExist(userName=name):
            result = result.filter(creator=User.objects.get(username=name))
        if postName is not None:
            result = result.filter(postName=postName)
        posts = []
        for i in result:
            posts.append({
                "id": i.id,
                "postName": i.postName,
                "user": i.creator.username
            })
        return JsonResponse({"success": True, "result": posts}, status=200)

    if request.method == "DELETE":
        user = request.session.get("userName", None)
        user = "abc"
        if user is not None and isUsernameExist(userName=user):
            user = User.objects.get(username=user)
            postId = body["postId"]
            post = Post.objects.filter(creator=user, id=postId)
            for i in post:
                i.delete()
            return JsonResponse({"success": True}, status=200)
    return HttpResponseBadRequest()
