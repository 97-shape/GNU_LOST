from django.contrib.auth.decorators import login_required
from django.db.models import Subquery, OuterRef, Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from chatapp.forms import SendMessageForm
from chatapp.models import User, ChatRoom, ChatMessage


# Create your views here.

def index(request):
    return render(request, "index.html")

@login_required(login_url='/account/need_login')
def room_list(request):
    # or문
    rooms = ChatRoom.objects.filter(user1_id=request.user.id) | ChatRoom.objects.filter(user2_id=request.user.id)

    rooms = rooms.annotate(
        last_message=Subquery(
            ChatMessage.objects.filter(room_id=OuterRef('room_id')).order_by('-timestamp').values('content')[:1]
        )
    )
    return render(request, "room_list.html", {"rooms": rooms})

@login_required(login_url='/account/need_login')
def create_chatroom(request, writer_id):
    user1 = request.user
    user2 = User.objects.get(id=writer_id)  # post를 통해서 상대방 정보 받아오기
    chat_room = ChatRoom.objects.create(user1=user1, user2=user2)
    # response = {'redirect_url': reverse('', args=[chat_room.id])}
    return redirect(reverse('room', kwargs={'room_id': chat_room.pk}))

@login_required(login_url='/account/need_login')
def send_message(request, room_id):
    chat_room = ChatRoom.objects.get(id=room_id)
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            sender = request.user
            ChatMessage.objects.create(room=chat_room, content=content, sender=sender)
            return redirect('room', room_id=room_id)
    else:
        form = SendMessageForm()
    messages = get_chat_messages(room_id)
    return render(request, 'room.html', {'form': form, 'messages': messages})

def get_chat_messages(room_id):
    messages = ChatMessage.objects.filter(room_id=room_id).order_by('timestamp')
    return messages

@login_required(login_url='/account/need_login')
def chatroom_create_or_join(request, writer_id):
    # 채팅방이 이미 존재하는지 확인
    chatrooms = ChatRoom.objects.filter(
        Q(user1_id=request.user.id, user2_id=writer_id) | Q(user1_id=writer_id, user2_id=request.user.id) #Q를 이용해서 표현 가능
    )

    # 채팅방이 존재하는 경우 해당 채팅방으로 이동
    if chatrooms:
        return redirect(reverse('room', kwargs={'room_id': chatrooms.first().room_id}))
    else:
        # 채팅방이 존재하지 않는 경우, 채팅방 생성 후 해당 채팅방으로 이동
        return create_chatroom(request, writer_id)

@login_required(login_url='/account/need_login')
def chatroom_detail(request, room_id):
    chat_room = ChatRoom.objects.get(room_id=room_id)
    messages = ChatMessage.objects.filter(chat_id=room_id)

    return render(request, 'room.html', {
        'room_id': room_id,
        'messages': messages,
        'chat_room': chat_room
    })