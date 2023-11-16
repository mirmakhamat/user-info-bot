from telegram.utils.types import JSONDict
from telegram import Update

from tgbot.custom.message import CustomMessage as Message

from telegram import (
    CallbackQuery,
    ChosenInlineResult,
    InlineQuery,
    Poll,
    PreCheckoutQuery,
    ShippingQuery,
    ChatMemberUpdated,
    ChatJoinRequest,
)
from telegram.poll import PollAnswer


class CustomUpdate(Update):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def de_json(cls, data: JSONDict, bot):
        data = cls._parse_data(data)

        if not data:
            return None

        data['message'] = Message.de_json(data.get('message'), bot)
        data['edited_message'] = Message.de_json(
            data.get('edited_message'), bot)
        data['inline_query'] = InlineQuery.de_json(
            data.get('inline_query'), bot)
        data['chosen_inline_result'] = ChosenInlineResult.de_json(
            data.get('chosen_inline_result'), bot
        )
        data['callback_query'] = CallbackQuery.de_json(
            data.get('callback_query'), bot)
        data['shipping_query'] = ShippingQuery.de_json(
            data.get('shipping_query'), bot)
        data['pre_checkout_query'] = PreCheckoutQuery.de_json(
            data.get('pre_checkout_query'), bot)
        data['channel_post'] = Message.de_json(data.get('channel_post'), bot)
        data['edited_channel_post'] = Message.de_json(
            data.get('edited_channel_post'), bot)
        data['poll'] = Poll.de_json(data.get('poll'), bot)
        data['poll_answer'] = PollAnswer.de_json(data.get('poll_answer'), bot)
        data['my_chat_member'] = ChatMemberUpdated.de_json(
            data.get('my_chat_member'), bot)
        data['chat_member'] = ChatMemberUpdated.de_json(
            data.get('chat_member'), bot)
        data['chat_join_request'] = ChatJoinRequest.de_json(
            data.get('chat_join_request'), bot)

        return cls(**data)
