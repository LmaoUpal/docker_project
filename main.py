import whisper
from aiogram import Bot, Dispatcher, types
import asyncio
import sys
import logging
from aiogram import F

dp = Dispatcher()

TOKEN = "6792409083:AAGQ9d5MHZFQQC53Qve4j3fNwEEb4EMPkEc"

def recongize(object):
    model = whisper.load_model("small", download_root="./models")
    result = model.transcribe(object)
    return result["text"]


@dp.message((F.content_type.in_({"voice"})))
async def echo_handler(message: types.Message, bot: Bot) -> None:
    await bot.download(message.voice.file_id, destination="voice_message.ogg")
    text = recongize("voice_message.ogg")
    await message.reply(text)



async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
