import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Bot

status = ['/help', 'за KASQ']


Bot = commands.Bot(command_prefix= '/')

@Bot.event
async def on_ready():
    print("Bot are ready")





Bot.run('NjEyNTIyMDU2MDU5MzIyMzg5.XgzvGQ.gAUXEHESd2YRPCTP9-oMtEdFYG8')
