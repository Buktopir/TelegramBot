from aiogram import types

async def set_default_comands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('help','helps'),
        types.BotCommand('profile', 'Получить данные мз BD'),
        types.BotCommand('register', 'Регистрация')
    ])