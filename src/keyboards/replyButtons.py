from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

from config.config import URL

webApp = WebAppInfo(url=URL)


async def menuButton():
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.insert(
        KeyboardButton(text="🍽 Menyu", web_app=webApp)
    )
    return markup