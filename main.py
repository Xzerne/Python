import discord
import pycord
import json
import requests
from discord.ext import commands
from discord import app_commands
intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready():
  print("URAHARA KISUKE IS HERE BABY")
  print("-----------------")

@tree.command(
  name="fluxus",
  description="Bypass Key")

@app_commands.describe(hwid='Enter Your Hwid')

async def key(i: discord.Integration, hwid: str):
  if not hwid:
    return
  try:
   response = requests.get(f"https://stickx.top/api-fluxus/?hwid={hwid.split('HWID=')[-1]}&api_key=E99l9NOctud3vmu6bPne")
                           
   await i.response.send_message(response.json()['key'])
   await i.response.send_message(hwid)
  except:
    await i.response.send_message(f"Error")

bot.run("MTI1MjU0NjAyNzA3Njk4MDc0Ng.GMDui-.WUp8sNDxdf_hTTm_1VisAtWpCnI4D-vlkAGyyc")
