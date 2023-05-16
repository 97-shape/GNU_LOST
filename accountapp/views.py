from django.shortcuts import render, redirect

# Create your views here.


def login(request):
    return render(request, "login.html")

def myaccount(request):
    return render(request, "account.html")