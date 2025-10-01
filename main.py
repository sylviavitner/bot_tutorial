# make sure discord.py and dotenv are installed!

import discord
from dotenv import load_dotenv
import os

# enable message intents
intents = discord.Intents.default()
intents.message_content = True

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}.') # prints to terminal

load_dotenv() # load .env file

client = Client(intents=intents)
client.run(os.getenv('TOKEN'))
