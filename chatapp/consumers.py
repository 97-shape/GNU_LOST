import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from chatapp.models import ChatMessage, ChatRoom

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs'].get('room_name')  # room_name으로 유지
        if self.room_id:
            try:
                chat_room = await sync_to_async(ChatRoom.objects.get)(room_id=self.room_id)
                self.room_id = chat_room.room_id  # room_id를 ChatRoom의 id로 업데이트
                await self.channel_layer.group_add(
                    str(self.room_id),  # 그룹 이름을 문자열로 변경
                    self.channel_name
                )
                await self.accept()
            except ChatRoom.DoesNotExist:
                # 처리할 로직 추가
                await self.close()
        else:
            # room_id가 없는 경우 처리 로직 추가
            await self.close()

    async def disconnect(self, close_code):
        if self.room_id:
            await self.channel_layer.group_discard(
                str(self.room_id),  # 그룹 이름을 문자열로 변경
                self.channel_name
            )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = self.scope['user']

        # Save the chat message to the database
        try:
            chat_room = await sync_to_async(ChatRoom.objects.get)(room_id=self.room_id)# room_id로 조회
        except ChatRoom.DoesNotExist:
            # 처리할 로직 추가
            return

        await sync_to_async(ChatMessage.objects.create)(
            room_id=chat_room,
            content=message,
            sender=sender
        )

        # Send message to room group
        await self.channel_layer.group_send(
            str(self.room_id),  # 그룹 이름을 문자열로 변경
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender.username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))
