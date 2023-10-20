import os
import discord
import dotenv
import importlib
import json
import random

commands = importlib.import_module('commands', __name__)

dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

start_time = None

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

data = json.load(open('frogs.json'))
print(data[0])

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    #activity = discord.Activity(type=discord.ActivityType.watching, name=(PREFIX + 'help'))
    #await client.change_presence(activity=activity)
    
    #global start_time
    #start_time = time.time()

@client.event
async def on_message(message):
    global PREFIX
    global COMMANDS
    #global start_time

    if message.author == client.user:
        return
    
    if message.content == "frog":
        frog = data[random.randint(0, len(data) - 1)]

        if (frog.setdefault('vname') == None):
            frog['vname'] = 'unknown'

        await message.channel.send("Common Name: " + frog['vname'] + "\nScientific Name: " + frog['sname'] + "\nInfo: " + frog['link'] + "\n" + frog['img'])
    
    #if message.content.startswith(PREFIX):
    #    message_content = message.content[1:].lower()
    #    args = message_content.split(' ')[1:]
    #    message_content = message_content.split(' ')[0]

    #    try:
    #        response = commands.command_parser(message_content, args)
    #    except:
    #        response = 'error'

    #    if response != '':
    #        embed = discord.Embed(title=message_content, description=response)
    #        await message.channel.send(response)

client.run(TOKEN)