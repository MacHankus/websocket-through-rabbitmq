from urllib.parse import parse_qs

from socketio import AsyncNamespace
from socketio.exceptions import ConnectionRefusedError

from loguru import logger

CHAT_NAMESPACE = "/chat"


class ChatNamespace(AsyncNamespace):
    def on_connect(self, sid, environ):
        logger.info(f"{sid} Connecting... ")
        logger.info(
            f"Connected [sid: {sid}, environ: {environ}] to namespace: {CHAT_NAMESPACE}"
        )

        self.emit("someone_joined", {"username": environ["login"]})
        # raise ConnectionRefusedError()

    def on_disconnect(self, sid):
        logger.info(f"{sid}: Disconnecting...")
        rooms = self.rooms(sid, namespace=CHAT_NAMESPACE)
        logger.info(f"Rooms to disconnect: {len(rooms)}")
        for room in rooms:
            self.leave_room(sid, room=room, namespace=CHAT_NAMESPACE)
            logger.info(f"sid={sid} left room {room}")

    def on_invite(self, sid, data):
        logger.info(f"{sid} has invited user... ")

    def on_message(self, sid, data):
        logger.info(f"{sid} has sent message... ")
