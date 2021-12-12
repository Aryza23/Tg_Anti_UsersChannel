import os
import shutil
import sys
import traceback
from functools import wraps
from os import environ, execle

import psutil
from config import (
    BOT_USERNAME,
    OWNER_ID,
)
from pyrogram import Client, filters
from pyrogram.types import Message
from stats_db import db


@Client.on_message(
    filters.private
    & filters.command("stats")
    & filters.user(OWNER_ID)
    & filters.reply
)
async def botstats(_, message: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    total_users = await db.total_users_count()
    await message.reply_text(
        text=f"**📊 stats of @{BOT_USERNAME}** \n\n**🤖 bot version:** `IDZ V.0.1Xr` \n\n**🙎🏼 total users:** \n » **on bot pm:** `{total_users}` \n\n**💾 disk usage:** \n » **disk space:** `{total}` \n » **used:** `{used}({disk_usage}%)` \n » **free:** `{free}` \n\n**🎛 hardware usage:** \n » **CPU usage:** `{cpu_usage}%` \n » **RAM usage:** `{ram_usage}%`",
        parse_mode="Markdown",
        quote=True,
    )
