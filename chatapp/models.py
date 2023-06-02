from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class ChatRoom(models.Model):
    room_id = models.AutoField(primary_key=True);
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='room_user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='room_user2')

class ChatMessage(models.Model):
    chat_id = models.AutoField(primary_key=True);
    room_id = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    content = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)