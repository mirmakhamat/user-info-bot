from telegram import Bot, Message
from telegram.utils.types import JSONDict

from tgbot.custom.shared import UserShared, ChatShared


class CustomMessage(Message):
    __slots__ = Message.__slots__ + ('user_shared', 'chat_shared',)

    def __init__(self, *args, **kwargs):
        self.user_shared = kwargs.pop('user_shared', None)
        self.chat_shared = kwargs.pop('chat_shared', None)
        super().__init__(*args, **kwargs)

    @classmethod
    def de_json(cls, data: JSONDict, bot: 'Bot') -> 'CustomMessage':
        if not data:
            return None

        data['user_shared'] = UserShared.de_json(
            data.get('user_shared'), bot)
        data['chat_shared'] = ChatShared.de_json(
            data.get('chat_shared'), bot)

        return super().de_json(data, bot)
