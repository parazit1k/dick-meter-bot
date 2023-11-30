from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# DATABASE
from Database.User.UserDatabase import User
from Database.Dick.DickDatabase import Dick

dick_router = Router()

dickDb = Dick()


@dick_router.message(Command("dick"))
async def dick_command_handler(message: Message):
    size = dickDb.update_dick(message.from_user.id)
    if size is not None:
        await message.reply(f"Твоя пиписька {size}!")
    else:
        await message.reply("У тебя кд, дядя")
