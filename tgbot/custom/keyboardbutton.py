from telegram import KeyboardButton
from telegram.utils.types import JSONDict
from tgbot.custom.keyboardbuttonrequest import KeyboardButtonRequestChat, KeyboardButtonRequestUser

class CustomKeyboardButton(KeyboardButton):
    __slots__ = KeyboardButton.__slots__ + ('request_user', 'request_chat',)

    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop('request_user', None)
        self.request_chat = kwargs.pop('request_chat', None)
        super().__init__(*args, **kwargs)

    @classmethod
    def de_json(cls, data: JSONDict, bot) -> 'CustomKeyboardButton':
        data = cls._parse_data(data)
        
        if not data:
            return None

        data['request_user'] = KeyboardButtonRequestUser.de_json(
            data.get('request_user'), bot)
        data['request_chat'] = KeyboardButtonRequestChat.de_json(
            data.get('request_chat'), bot)

        return super().de_json(data, bot)