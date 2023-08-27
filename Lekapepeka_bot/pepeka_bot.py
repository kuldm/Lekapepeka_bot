# import logging
# import os
# import aiogram
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
# from aiogram.utils import executor



# MEDIA_FOLDER = 'media'

# logging.basicConfig(level=logging.INFO)
load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, добро пожаловать в мемный рай!')


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Я тебя не понимаю.')


if __name__ == '__main__':
    executor.start_polling(dp)




# if not os.path.exists(MEDIA_FOLDER):
#     os.makedirs(MEDIA_FOLDER)
#     os.makedirs(os.path.join(MEDIA_FOLDER, 'photo'))
#     os.makedirs(os.path.join(MEDIA_FOLDER, 'video'))
#
# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     await message.reply("Привет! Я бот. Просто отправь мне фото или видео.")
#
# @dp.message_handler(content_types=[types.ContentTypes.PHOTO, types.ContentTypes.VIDEO])
# async def save_media(message: types.Message):
#     media_type = message.content_type
#     media_id = ""
#
#     if media_type == types.ContentTypes.PHOTO:
#         media = message.photo[-1]
#         media_id = media.file_id
#         subfolder = 'photo'
#     elif media_type == types.ContentTypes.VIDEO:
#         media = message.video
#         media_id = media.file_id
#         subfolder = 'video'
#
#     media_file = await bot.get_file(media_id)
#     media_path = media_file.file_path
#
#     download_path = os.path.join(MEDIA_FOLDER, subfolder, f'{media_id}.mp4' if media_type == types.ContentTypes.VIDEO else f'{media_id}.jpg')
#     await media.download(destination=download_path)
#
#     await message.reply(f"Медиа сохранено: {download_path}")
#
# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
