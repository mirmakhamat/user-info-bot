from typing import Optional

from telegram import ChatAdministratorRights
from telegram import TelegramObject
from telegram.utils.types import JSONDict


class KeyboardButtonRequestUser(TelegramObject):

    __slots__ = (
        "request_id",
        "user_is_bot",
        "user_is_premium",
        "_id_attrs",
    )

    def __init__(
        self,
        request_id: int,
        user_is_bot: Optional[bool] = None,
        user_is_premium: Optional[bool] = None,
    ):
        self.request_id: int = request_id

        self.user_is_bot: Optional[bool] = user_is_bot
        self.user_is_premium: Optional[bool] = user_is_premium

        self._id_attrs = (self.request_id,)


class KeyboardButtonRequestChat(TelegramObject):

    __slots__ = (
        "request_id",
        "chat_is_channel",
        "chat_is_forum",
        "chat_has_username",
        "chat_is_created",
        "user_administrator_rights",
        "bot_administrator_rights",
        "bot_is_member",
        "_id_attrs",
    )

    def __init__(
        self,
        request_id: int,
        chat_is_channel: bool,
        chat_is_forum: Optional[bool] = None,
        chat_has_username: Optional[bool] = None,
        chat_is_created: Optional[bool] = None,
        user_administrator_rights: Optional[ChatAdministratorRights] = None,
        bot_administrator_rights: Optional[ChatAdministratorRights] = None,
        bot_is_member: Optional[bool] = None,
    ):
        self.request_id: int = request_id
        self.chat_is_channel: bool = chat_is_channel

        self.chat_is_forum: Optional[bool] = chat_is_forum
        self.chat_has_username: Optional[bool] = chat_has_username
        self.chat_is_created: Optional[bool] = chat_is_created
        self.user_administrator_rights: Optional[
            ChatAdministratorRights
        ] = user_administrator_rights
        self.bot_administrator_rights: Optional[ChatAdministratorRights] = bot_administrator_rights
        self.bot_is_member: Optional[bool] = bot_is_member

        self._id_attrs = (self.request_id,)

    @classmethod
    def de_json(
        cls, data: Optional[JSONDict], bot
    ) -> Optional["KeyboardButtonRequestChat"]:
        data = cls._parse_data(data)

        if not data:
            return None

        data["user_administrator_rights"] = ChatAdministratorRights.de_json(
            data.get("user_administrator_rights"), bot
        )
        data["bot_administrator_rights"] = ChatAdministratorRights.de_json(
            data.get("bot_administrator_rights"), bot
        )

        return super().de_json(data=data, bot=bot)
