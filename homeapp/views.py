from django.shortcuts import render, redirect

# Create your views here.
from postapp.models import Post, Photo


def homeView(request):
    # 가장 최신인 습득 마지막
    get_post = Post.objects.prefetch_related('photos').filter(
        category = '습득'
    ).latest('writedate')

    lost_post = Post.objects.prefetch_related('photos').filter(
        category='분실'
    ).latest('writedate')

    return render(request, "home.html", {"get_post": get_post, "lost_post": lost_post})