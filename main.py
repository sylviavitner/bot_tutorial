# make sure discord.py and dotenv are installed!

# import libraries
import discord
from dotenv import load_dotenv
import os
import random

# enable message intents
intents = discord.Intents.default()
intents.message_content = True

load_dotenv() # load .env file

# create a client class
# this is where you define your bot's behavior
class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}.')

    async def on_message(self, message):
        # ignore message from itself
        if message.author == self.user:
            return
        
        # get message content
        content = message.content.lower()

        # respond based on a specific keyword in the message
        if "hello" in content:
            await message.channel.send(f'Hello {message.author.name}!')
        
        elif "roll dice" in content:
            dice_roll = random.randint(1, 6)
            await message.channel.send(f'You rolled {dice_roll}.')

# create a client instance and run your bot with your token!
client = Client(intents=intents)
client.run(os.getenv('TOKEN'))