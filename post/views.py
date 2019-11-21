from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request,'post/index.html',{ 'posts':posts })

def likepost(request):
    print("\n\n Request===",request)
    if request.method == 'GET':
        print("==========GET METHOD==========")
        post_id = request.GET.get('post_id',False)
        print("POST ID=====",post_id)
        likepost = Post.objects.get(pk=post_id)
        m = Like(post=likepost)
        m.save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Request method is not a GET")