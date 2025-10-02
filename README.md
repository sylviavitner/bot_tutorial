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

## Project Setup
1. Create a new project folder or clone this repository
2. Inside the folder, create a Python script (main.py) for your bot's code

## Bot Setup
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click on **New Application** and give your application a name.
3. On the left sidebar, click on **bot**.
   - You can change the username and image if you want to.
4. Scroll down to **'Privileged Gateway Intents'**
5. Enable all three intents, allowing the bot to interact with your server.
6. Give your bot administrator privileges (or the specific permissions you want).

## Getting your bot on a server
1. On the left sidebar, click **OAuth2**.
2. In the URL generator, select **bot**.
3. In bot permissions, select administrator (or previously chosen permissions).
4. Copy the generated URL at the bottom of the page.
5. Paste the URL in a new tab, and sign in to Discord if prompted.
  
