from django.shortcuts import render

# Create your views here.

def displayDetail(request):
    return render(request, "detail.html")