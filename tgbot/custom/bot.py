from telegram import Bot
from tgbot.custom.update import CustomUpdate as Update
from telegram.utils.types import JSONDict
from typing import cast, List


class CustomBot(Bot):
    def get_updates(self, offset=None, limit=100, timeout=0, read_latency=2, allowed_updates=None, api_kwargs=None):
        data = {'timeout': timeout}

        if offset:
            data['offset'] = offset
        if limit:
            data['limit'] = limit
        if allowed_updates is not None:
            data['allowed_updates'] = allowed_updates

        result = cast(
            List[JSONDict],
            self._post(
                'getUpdates',
                data,
                timeout=float(read_latency) + float(timeout),
                api_kwargs=api_kwargs,
            ),
        )

        if result:
            self.logger.debug('Getting updates: %s', [
                              u['update_id'] for u in result])
        else:
            self.logger.debug('No new updates found.')
            
        return Update.de_list(result, self)
