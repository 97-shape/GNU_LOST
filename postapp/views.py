from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

# Create your views here.
from postapp.forms import PostForm, PhotoFormSet
from postapp.models import Post


def displayDetail(request):
    return render(request, "detail.html")

def test(request):
    posts = Post.objects.all()
    return render(request, "detail.html", {"posts":posts})

User = get_user_model()  #  request.user을 User 모델 형식으로

def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, prefix='post')
        photo_formset = PhotoFormSet(request.POST, request.FILES, prefix='photo')
        if post_form.is_valid() and photo_formset.is_valid():
            post = post_form.save(commit=False)
            post.id = request.user
            post.save()
            photo_formset.instance = post
            photo_formset.save()
            return redirect('detail')
    else:
        post_form = PostForm(prefix='post')
        photo_formset = PhotoFormSet(prefix='photo')

    context = {
        'post_form': post_form,
        'photo_formset': photo_formset
    }

    return render(request, 'create_post.html', context)