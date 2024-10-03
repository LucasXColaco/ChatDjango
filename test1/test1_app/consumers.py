import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        usuario = text_data_json['usuario']
        mensagem = text_data_json['mensagem']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_mensagem',
                'usuario': usuario,
                'mensagem': mensagem,
            }
        )
    
    def chat_mensagem(self, event):
        usuario = event['usuario']
        mensagem = event['mensagem']

        self.send(text_data=json.dumps({
            'type': 'chat',
            'usuario': usuario,
            'mensagem': mensagem,
        }))