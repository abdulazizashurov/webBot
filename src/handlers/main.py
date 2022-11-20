from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import LabeledPrice

from config.config import CLICK_TOKEN
from loader import dp, bot
from src.db.commands import getProductById
from src.keyboards.replyButtons import menuButton


@dp.message_handler(CommandStart())
async def doStart(message: types.Message):
    markup = await menuButton()
    await message.answer("Assalomu alaykum,Hush kelibsiz!", reply_markup=markup)


@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def buyProduct(message, state: FSMContext):
    prodyuctId = message.web_app_data.data
    product = await getProductById(prodyuctId)
    price = str(product.price).split(".")[0]  # 30000.00 3000000
    price = f"{price}00"
    await state.update_data(prodyuctId=prodyuctId)
    await bot.send_invoice(
        chat_id=message.from_user.id,
        title="Click",
        description="Click orqali xavsiz va tezkor to'lov",
        currency="UZS",
        provider_token=CLICK_TOKEN,
        prices=[
            LabeledPrice(label="Food", amount=int(price))
        ],
        payload="payload:food",
        start_parameter="create_invoice_ds_dur",
        need_name=False,
        need_phone_number=False,
        need_shipping_address=False,
        need_email=False,
    )


@dp.pre_checkout_query_handler(lambda query: True)
async def processPayment(pre:  types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre.id, ok=True)


@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def getPaymentAndCloaseOrderSuccess(message: types.Message, state: FSMContext):
    await message.answer("Buyurtmangiz qabul qilindi.")

    data = await state.get_data()
    productId = data.get("productId")
    #
