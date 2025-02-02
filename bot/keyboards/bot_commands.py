from aiogram import Bot
from aiogram.types import BotCommand


async def set_bot_commands(bot: Bot):
    commands = {"start": "Start bot", "help": "Help"}
    commands = [
        BotCommand(command=command, description=description)
        for command, description in commands.items()
    ]
    await bot.set_my_commands(commands)