from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

# Create your views here.
from postapp.models import Post

def login(request):
    return render(request, "login.html")

def need_login(request):
    return render(request, "login.html")

def myaccount(request):

    posts = Post.objects.prefetch_related('photos').filter(
        user = request.user.id
    )

    return render(request, "account.html", {'posts': posts})