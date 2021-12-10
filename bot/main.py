from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import config


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    if message.from_user.id not in config.users_security:
        await message.answer(
            'Вас нет в вайт-листе, передайде администратору свой идентификатор: \n' + str(message.from_user.id))
    else:
        await message.answer(
            'Вы уже в вайт-листе, ваш идентификатор: \n' + str(message.from_user.id) + '\nОжидайте уведомлений')
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
