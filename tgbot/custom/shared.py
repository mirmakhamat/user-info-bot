from telegram.base import TelegramObject


class UserShared(TelegramObject):

    __slots__ = ("request_id", "user_id", "bot", "_id_attrs")

    def __init__(
        self,
        request_id: int,
        user_id: int,
        bot=None
    ):
        self.request_id: int = request_id
        self.user_id: int = user_id

        self._id_attrs = (self.request_id, self.user_id)


class ChatShared(TelegramObject):

    __slots__ = ("request_id", "chat_id", "bot", "_id_attrs")

    def __init__(
        self,
        request_id: int,
        chat_id: int,
        bot=None
    ):
        self.request_id: int = request_id
        self.chat_id: int = chat_id

        self._id_attrs = (self.request_id, self.chat_id)
