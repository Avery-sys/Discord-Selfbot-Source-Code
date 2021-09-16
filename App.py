import discord
import time
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

token = input("Your Token: ")

print('logging in...')
time.sleep(5)

print('almost there...')
time.sleep(2)

@client.event
async def on_ready():
    print('Logged In!')


client.run(token)
