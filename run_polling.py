import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dtb.settings')
django.setup()

from tgbot.custom.bot import CustomBot as Bot
from telegram.ext import Updater

from dtb.settings import TELEGRAM_TOKEN
from tgbot.dispatcher import setup_dispatcher


def run_polling(tg_token: str = TELEGRAM_TOKEN):
    """ Run bot in polling mode """
    bot = Bot(tg_token)

    updater = Updater(bot=bot)
    
    dp = updater.dispatcher
    dp = setup_dispatcher(dp)

    bot_info = bot.get_me()
    bot_link = f"https://t.me/{bot_info['username']}"

    print(f"Polling of '{bot_link}' has started")
    # it is really useful to send '👋' emoji to developer
    # when you run local test
    # bot.send_message(text='👋', chat_id=<YOUR TELEGRAM ID>)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    run_polling()
