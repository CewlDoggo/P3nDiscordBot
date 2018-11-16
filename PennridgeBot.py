import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import json
import os

Token = 'NTA1MTYxNjUyNDMwMTc2MjU3.DtCipw.orDniRKUGIGLoilqiZlSqu-NUEg'
client = commands.Bot(command_prefix = '~')
os.chdir(r'C:\Users\Howdy\Desktop\Coding\Bots\Pennridge bot')

@client.event
async def on_ready():
    print('bot is ready')

@client.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, member)

    with open('users.json','w') as f:
        json.dump(users, f)

@client.event
async def on_message(message):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, message.author)
    await add_experience(users, message.author, 5)
    await level_up(users, message.author, message.channel)

    with open('users.json','w') as f:
        json.dump(users, f)

async def update_data(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]['experience'] = 0
        users[user.id]['level'] = 1

async def add_experience(users, user, exp):
    users[user.id]['experience'] +=exp

async def level_up(users, user, channel):
    experience = users[user.id]['experience']
    lvl_start = users[user.id]['level']
    lvl_end = int(experience ** (1/4))

    if lvl_start < lvl_end:
        await client.send_message(channel, '{} has leveled up to level {}'.format(user.mention, lvl_end))
        users[user.id]['level'] = lvl_end

@client.event
async def on_message(message):
    if message.content.upper().startswith('~PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('~ECHO'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
    if message.content.upper().startswith('~ANNOUNCE'):
        if "512730303241125890" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            await client.send_message(client.get_channel('505106539019894805'), "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You don't have permission to use that command")  
    if message.content.upper().startswith('~GENERAL'):
        if "512730303241125890" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            await client.send_message(client.get_channel('505101869652246531'), "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You don't have permission to use that command")  

            
client.run (Token)
