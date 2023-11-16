from telegram import ReplyKeyboardMarkup
from tgbot.custom.keyboardbuttonrequest import KeyboardButtonRequestChat, KeyboardButtonRequestUser
from tgbot.custom.keyboardbutton import CustomKeyboardButton as KeyboardButton


def make_keyboard_for_start_command() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton('User 👤', request_user=KeyboardButtonRequestUser(1, False))],
        [
            KeyboardButton('Super Group 👥', request_chat=KeyboardButtonRequestChat(2, False, chat_has_username=True)),
            KeyboardButton('Group 👥', request_chat=KeyboardButtonRequestChat(3, False, chat_has_username=False)),
        ],
        [
            KeyboardButton('Channel 🔊', request_chat=KeyboardButtonRequestChat(4, True, chat_has_username=True)),
            KeyboardButton('Private Channel 🔊', request_chat=KeyboardButtonRequestChat(5, True, chat_has_username=False)),
        ],
        [
            KeyboardButton('Bot 🤖', request_user=KeyboardButtonRequestUser(6, True)),
            KeyboardButton('Premium 🌟', request_user=KeyboardButtonRequestUser(7, user_is_premium=True)),
        ]
    ]

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

