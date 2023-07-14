from aiogram import Bot, Dispatcher, types
import aiogram
from aiogram.utils import executor
from aiogram.types import \
    ReplyKeyboardMarkup, KeyboardButton, \
    ContentType

API_TOKEN = '6329940263:AAGqVNwUKxfAbVN3iv-_a-LrEFhGf-lArWw'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
  KeyboardButton("Telefon raqamni jo'natish ☎️", request_contact=True)
)

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
  await bot.send_message(message.chat.id, "Botga xush kelibsiz! Iltimos telefon raqamingizni jo'nating.", reply_markup=markup_request)

@dp.message_handler(content_types=ContentType.CONTACT)
async def process_phone_number(message: types.Message):
  phone_number = message.contact.phone_number
  if '+' in phone_number:
    phone_number = int(phone_number[slice(1,len(phone_number))])
  await bot.send_message(
      message.chat.id,
      f"Telefon raqamingiz: +{phone_number}",
      reply_markup=aiogram.types.ReplyKeyboardRemove()
    )

if __name__ == '__main__':
  executor.start_polling(dp)