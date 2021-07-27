# (c) @AbirHasan2005

import os
import time
import string
import random
import asyncio
import aiofiles
import datetime
from WebStreamer.utils.broadcast_helper import send_msg
from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from pyrogram import filters, Client
from pyrogram.types import Message
broadcast_ids = {}


@StreamBot.on_message(filters.command("status") & filters.private & filters.user(Var.OWNER_ID) & ~filters.edited)
async def sts(c: Client, m: Message):
    total_users = 10
    await m.reply_text(text=f"**Total Users in DB:** `{total_users}`", parse_mode="Markdown", quote=True)
