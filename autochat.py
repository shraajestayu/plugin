import asyncio
from pyrogram import filters
from strings import get_command, get_string
import config
from config import OWNER_ID
from AnonX import app
from AnonX.utils.database import (add_served_chat,
                                       add_served_user,
                                       get_served_chats,
                                       get_served_users,
                                       )

#Imported_Modules 
#Please Note That: Auto Chat Recovery tool is just for private bots or allowing from ayush

AUTOCHAT_COMMAND = get_command("AUTOCHAT_COMMAND")
AUTOUSER_COMMAND = get_command("AUTOUSER_COMMAND")

IS_AUTOCHAT = False
IS_AUTOUSER = False




@app.on_message(filters.command(AUTOCHAT_COMMAND) & filters.user(OWNER_ID))
async def trigger(client, message: Message):
    get_option = message.text.split(None, 1)[1]
    global IS_AUTOCHAT
    if "on" in get_option:
        IS_AUTOCHAT = True
        await message.reply(f"Auto Chat Recovery Activated Now!\nThis Bot Will Recover All chats within 24hrs\n\nplugin by - Ayush")
    elif "off" in get_option:
        if IS_AUTOCHAT==False:
            await message.reply(f"HUH!\nThis option is not ON\nTRY - /autochat on\n\nplugin by - Ayush")
        else:
            IS_AUTOCHAT = False
            await message.reply(f"Auto Chat Recovery Deactivated!")
    else:
        pass



@app.on_message(filters.command(AUTOUSER_COMMAND) & filters.user(OWNER_ID))
async def trigger_user(client, message: Message):
    get_option = message.text.split(None, 1)[1]
    if "on" in get_option:
        global IS_AUTOUSER
        IS_AUTOUSER = True
        await message.reply(f"Auto User Recovery Activated Now!\nThis Bot Will Recover All Users within 24hrs\n\nplugin by - Ayush")
    elif "off" in get_option:
        if IS_AUTOUSER==False:
            await message.reply(f"HUH!\nThis option is not ON\nTRY - /autouser on\n\nplugin by - Ayush")
        else:
            global IS_AUTOUSER
            IS_AUTOUSER = False
            await message.reply(f"Auto User Recovery Deactivated!")
    else:
        pass


@app.on_message(filters.text)
async def autouser_collect(client, message: Message):
    if IS_AUTOUSER==True:
        user_id = message.from_user.id
        if user_id in await get_served_users():
            pass
        else:
            await add_served_user(user_id)
    else:
        pass






@app.on_message(filters.text & filters.group)
async def autochat_ayu(client, message: Message):
    if IS_AUTOCHAT==True:
        chat_id = message.chat.id
        if chat_id in await get_served_chats():
            pass
        else:
            await add_served_chat(chat_id)
    else:
        pass
