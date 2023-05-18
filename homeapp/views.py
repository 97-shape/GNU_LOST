from django.shortcuts import render

# Create your views here.
from postapp.models import Post, Photo


def homeView(request):
    from django.db.models import Max
    posts = Post.objects.filter(
        category = '습득'
    ).latest('writedate')
    photo = Photo.objects.filter(
        post_id = posts.post_id
    ).first()
    return render(request, "home.html", {'posts': posts, 'photo': photo})