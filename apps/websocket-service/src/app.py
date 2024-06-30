import sys

import socketio
from socketio import AsyncAioPikaManager

from settings import settings
from websocket.adapters.namespaces.weighing import WeighingNamespace, WEIGHING_NAMESPACE

APP_FROZEN = getattr(sys, "frozen", False)

RABBIT_URL = (
        f"amqp://{settings.RABBITMQ_IN_WEBSOCKET_USERNAME}:{settings.RABBITMQ_IN_WEBSOCKET_PASSWORD}"
        + f"@{settings.RABBITMQ_IN_WEBSOCKET_HOST_NAME}:{settings.RABBITMQ_IN_WEBSOCKET_PORT}//"
)

sio = socketio.AsyncServer(
    async_mode="asgi",
    client_manager=AsyncAioPikaManager(url=RABBIT_URL),
    cors_allowed_origins=settings.CORS_ORIGINS
)

sio.register_namespace(WeighingNamespace(WEIGHING_NAMESPACE))

app = socketio.ASGIApp(sio)
