from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# DATABASE
from Database.User.UserDatabase import User
from Database.Dick.DickDatabase import Dick

start_router = Router()

userDb = User()
dickDb = Dick()


@start_router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    if not userDb.user_exists(message.from_user.id):
        userDb.add_user(message.from_user.id, message.from_user.username, message.from_user.first_name,
                        message.from_user.last_name)

        dickDb.create_dick(message.from_user.id)

    await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>")
