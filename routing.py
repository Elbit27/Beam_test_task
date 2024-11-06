# beam_test_task/routing.py
from django.urls import path
import consumers

websocket_urlpatterns = [
    path("ws/some_path/", consumers.ChatConsumer.as_asgi()),  # Замените some_path и YourConsumer
]
