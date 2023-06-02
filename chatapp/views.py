from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from chatapp.forms import SendMessageForm
from chatapp.models import User, ChatRoom, ChatMessage


# Create your views here.

def index(request):
    return render(request, "index.html")

def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})

@login_required
def create_chatroom(request):
    if request.method == 'POST':
        user1 = request.user
        print(request.POST.get('writer_id'))
        user2 = User.objects.get(id=request.POST.get('writer_id'))  # post를 통해서 상대방 정보 받아오기
        chat_room = ChatRoom.objects.create(user1=user1, user2=user2)
        # response = {'redirect_url': reverse('', args=[chat_room.id])}
        return render(request, 'room.html', {'room_id': chat_room.pk})

@login_required
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

@login_required
def chatroom_create_or_join(request):
    if request.method == 'POST':
        # 클릭 이벤트 핸들러에서 전달한 채팅방 ID를 가져옴
        chat_room_id = request.POST.get('chat_room_id')

        # 채팅방이 이미 존재하는지 확인
        chat_room = get_object_or_404(ChatRoom, id=chat_room_id)

        # 채팅방이 존재하는 경우 해당 채팅방으로 이동
        if chat_room:
            return redirect('chat_room_detail', chat_room_id=chat_room_id)
        else:
            # 채팅방이 존재하지 않는 경우, 채팅방 생성 후 해당 채팅방으로 이동
            return create_chatroom(request)

def chatroom_detail(request, room_id):
    chat_room = ChatRoom.objects.get(room_id=room_id)
    messages = ChatMessage.objects.filter(chat_id=room_id)

    return render(request, 'room.html', {
        'room_id': room_id,
        'messages': messages,
        'chat_room': chat_room
    })