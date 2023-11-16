from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from users.models import User
from tgbot.handlers.onboarding.keyboards import make_keyboard_for_start_command


def command_start(update: Update, context: CallbackContext) -> None:
    User.get_user_and_created(update, context)
    user = update.effective_user

    text = ""

    if user.username:
        text += f"@{user.username}\n"
    text += f"ID: <code>{user.id}</code>\n"
    text += f"First: {user.first_name}\n"
    if user.last_name:
        text += f"Last: {user.last_name}\n"
    text += f"Lang: {user.language_code}"

    update.message.reply_text(text=text,
                              parse_mode=ParseMode.HTML,
                              reply_markup=make_keyboard_for_start_command())


def shared(update: Update, context: CallbackContext) -> None:
    if update.message.user_shared:
        text = f"User id: <code>{update.message.user_shared.user_id}</code>"
    else:
        text = f"Chat id: <code>{update.message.chat_shared.chat_id}</code>"

    update.message.reply_text(text=text,
                              parse_mode=ParseMode.HTML)
