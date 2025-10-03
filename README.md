# Discord Bot Setup Guide

This repository provides a simple guide for creating and running your own Discord bot in Python.

## Prerequisites

- Python installed (3.8 or higher)  
- `pip` package manager installed  

## Installation

In your terminal, install the required dependencies:

```bash
pip install discord.py
pip install python-dotenv
```

## Project setup
1. Create a new project folder or clone this repository
2. Inside the folder, create a Python script (main.py) for your bot's code
3. Create a Discord sever to test your bot (or use one you already have) 

## Bot setup
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click on **New Application** and give your application a name.
3. On the left sidebar, click on **bot**.
   - You can change the username and image if you want to.
4. Scroll down to **Privileged Gateway Intents**
5. Enable all three intents, allowing the bot to interact with your server.
6. Give your bot administrator privileges (or the specific permissions you want).

## Getting your bot on a server
1. On the left sidebar, click **OAuth2**.
2. In the URL generator, select **bot**.
3. In bot permissions, select administrator (or previously chosen permissions).
4. Copy the generated URL at the bottom of the page.
5. Paste the URL in a new tab, and sign in to Discord if prompted.
6. Select the server you want to add your bot to.
7. Click **Authorize**.
8. Check Discord to see if your bot joined the server.

## Running your bot
1. Go back to the **Bot** tab and click the **reset token** button.
2. Copy your unique token.
3. Create another file in the project named .env
4. Set one variable:
```python
TOKEN='your_unique_token_here'
```
5. Clone this repository or use your own code to add behaviors for your bot.
6. Test your bot on the Discord server you selected earlier.

## Useful links
- [Discord.py Documentation]('https://discordpy.readthedocs.io/en/stable/')
- [Discord.py Learning Guide]('https://www.pythondiscord.com/pages/guides/python-guides/discordpy/')
- [Discord.py GitHub Repository]('https://github.com/Rapptz/discord.py')

