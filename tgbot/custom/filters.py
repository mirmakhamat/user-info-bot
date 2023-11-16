from telegram.ext import MessageFilter

class UserSharedFilter(MessageFilter):
    def filter(self, message):
        return bool(message.user_shared)

USER_SHARED = UserSharedFilter()

class ChatSharedFilter(MessageFilter):
    def filter(self, message):
        return bool(message.chat_shared)

CHAT_SHARED = ChatSharedFilter()