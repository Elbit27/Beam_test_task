# chat/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()  # Подключение принимается

        self.send(text_data=json.dumps({"message": "WebSocket подключен"}))

    def disconnect(self, close_code):
        # Логика при отключении (если нужна)
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Отправка сообщения обратно
        self.send(text_data=json.dumps({"message": message}))
