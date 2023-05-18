from django.shortcuts import render

# Create your views here.
from postapp.models import Post, Photo


def homeView(request):
    # 가장 최신인 습득 마지막
    new_post = Post.objects.prefetch_related('photos').filter(
        category = '습득'
    ).latest('writedate')

    return render(request, "home.html", {"new_post": new_post})