import asyncio
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN=os.getenv("TOKEN")

intents=discord.Intents.default()
intents.members=True
intents.message_content=True

bot=commands.Bot(command_prefix="!", intents=intents)

EXTENSIONS=[
"cogs.profile",
"cogs.welcome",
"cogs.invites",
"cogs.ranking",
"cogs.giveaway",
]

async def main():
    async with bot:
        for ext in EXTENSIONS:
            try:
                await bot.load_extension(ext)
                print(f"Loaded {ext}")
            except Exception as e:
                print(e)
        await bot.start(TOKEN)

if __name__=="__main__":
    asyncio.run(main())
