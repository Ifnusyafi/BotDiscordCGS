import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

Channel_Trap = 1542052309134221343

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="|", intents=intents)

@bot.event
async def on_ready():
    print(f"Login {bot.user}")

    # WARNING MESSAGE
    channel = bot.get_channel(Channel_Trap)
    if channel:
        
        # TIAP BOT RESTART GK NGIRIM WARNING ULANG
        async for msg in channel.history(limit=1):
            if msg.author == bot.user:
                return 
        await channel.send(
            "⚠️ **BLACKZONE** ⚠️\n"
            "JANGAN NGECHAT DISINI**\n"
            "INI KHUSUS AKUN NGIRIM FOTO TUAN BUAS**.\n"
            "Kena auto ban mampus lu"
        )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == Channel_Trap:
        try:
            # Hapus pesan 
            await message.delete()
            # Abis tu Banned
            await message.guild.ban(
                message.author,
                reason="TUAN BUAS NASI, TUAN BUAS MAKAN NASI",
                delete_message_seconds=86400
            )
            print(f"{message.author} sudah di crucifix")

        except discord.Forbidden:
            print("Bot tidak punya izin. Cek role hierarchy & permission (Ban Members, Manage Messages).")
        except discord.HTTPException as e:
            print(f"Gagal proses: {e}")

    await bot.process_commands(message)

bot.run(TOKEN)