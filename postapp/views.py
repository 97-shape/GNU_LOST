from django.contrib.auth import get_user_model
from django.db.models import Min
from django.shortcuts import render, redirect

# Create your views here.
from postapp.forms import PostForm, PhotoFormSet
from postapp.models import Post, Photo


def list(request):
    posts = Post.objects.prefetch_related('photos')
    return render(request, "list.html", {"posts":posts})

def filterdList(request, filter):

    if filter in ['습득', '분실']:
        posts = Post.objects.prefetch_related('photos').filter(
            category=filter
        )
        prev_url = filter + "/"
    else:
        if filter == "카드":
            filter = "카드/신분증"

        posts = Post.objects.prefetch_related('photos').filter(
            type = filter
        )
        prev_url = ""

    return render(request, "list.html", {"posts":posts, "prev_url": prev_url})

def filterdDetailList(request, category, type):
    if type == "카드":
        type = "카드/신분증"

    posts = Post.objects.prefetch_related('photos').filter(
        category = category,
        type = type
    )

    prev_url = category + "/"

    return render(request, "list.html", {"posts":posts, 'prev_url': prev_url})

User = get_user_model()  #  request.user을 User 모델 형식으로

def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, prefix='post')
        photo_formset = PhotoFormSet(request.POST, request.FILES, prefix='photo')
        if post_form.is_valid() and photo_formset.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            for form in photo_formset:
                if form.cleaned_data.get('photo'):  # 이미지가 업로드되었는지 확인
                    photo = form.save(commit=False)
                    photo.post = post  # post와 photo를 연결
                    photo.save()
                    post.photos.add(photo)  # post와 photo를 연결
            return redirect('detail')
    else:
        post_form = PostForm(prefix='post')
        photo_formset = PhotoFormSet(prefix='photo')

    context = {
        'post_form': post_form,
        'photo_formset': photo_formset
    }

    return render(request, 'create_post.html', context)

def detail_post(request, post_id):
    previous_url = request.META.get('HTTP_REFERER', '/')  # 이전 목록으로

    post = Post.objects.filter(
        post_id = post_id
    ).get()
    photos = Photo.objects.filter(
        post_id = post_id
    )
    return render(request, 'detail.html', {'post' : post, 'photos': photos, 'index': range(photos.count()), 'previous_url': previous_url})