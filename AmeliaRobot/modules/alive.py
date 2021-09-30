from telethon import events, Button, custom
from AmeliaRobot import dispatcher

from telegram import ParseMode, Update
from telegram.ext import CommandHandler, CallbackContext
from telegram.ext.dispatcher import  run_async

GIT_PIC = "https://telegra.ph/file/c5868d73616b42698e8bd.jpg"

GIT_TEXT = """
Iron Man Is Advanced Group Manager Bot By A [Legend](https://t.me/Pavakkka)

*Contributors/Credits*

> [彡1̸2̸3̸ ᑕᖇEᗩTIOᑎ₴彡](https://t.me/Pavakkka)
> [☬Ň𝔲𝐛☮𝐤ι𝔫ﻮ☫](https://t.me/AASFCYBERKING)
> [War-Legend/AmeliaRobot](https://github.com/War-Legend/AmeliaRobot)

[Legend](https://t.me/Pavakkka)
[Support](https://t.me/PigasusSupport)
[Updates](https://t.me/PigasusUpdates)

"""

BUTTON = [[Button.url("𝙎𝙐𝙋𝙋𝙊𝙍𝙏", "https://t.me/PigasusSupport"), Button.url("𝙐𝙋𝘿𝘼𝙏𝙀", "https://t.me/PigasusUpdates")]]
"""

@run_async
def alive(update: Update, context: CallbackContext):
    update.effective_message.reply_photo(
        GIT_PIC,
        caption = GIT_TEXT,
        buttons=BUTTON,
        parse_mode=ParseMode.MARKDOWN
        )

ALIVE_HANDLER = CommandHandler("alive", alive)

dispatcher.add_handler(ALIVE_HANDLER)

