banned_ids = [757431801487556748, 598477713543659523]

from selenium.webdriver.chrome.options import Options
from discord import Webhook, RequestsWebhookAdapter
from datetime import datetime, date, timedelta
from discord_webhook import DiscordWebhook
from pygoogletranslation import Translator
from pdf2image import convert_from_path
from PIL import ImageDraw, ImageFilter
from PyDictionary import PyDictionary
from discord.ext.commands import *
from discord.ext import commands
from selenium import webdriver
from cmath import *
import random as ra
import emoji as em
import numpy as np
from math import *
import pytesseract
import time as tm
import subprocess
import wikipedia
import requests
import aiohttp
import asyncio
import discord
import pdfkit
import pytube
import pytz
import PIL
import re
import os

file = open("program.py", "x")
set(pytz.all_timezones_set)
dictionary=PyDictionary()
allid=[]
hexstring_pattern = re.compile(r'#?([0-9A-F]{2})([0-9A-F]{2})([0-9A-F]{2})', re.IGNORECASE)
id_pattern = re.compile(r'([A-Z]{5})', re.IGNORECASE)
alphaend_pattern = re.compile(r'.*[a-z]', re.IGNORECASE)
python_pattern = re.compile(r'^\`\`\`(py)?\n[\s\S]*\`\`\`$')
html_pattern = re.compile(r'^\`\`\`(html)?\n[\s\S]*\`\`\`$')
UNITS = {'s':'seconds', 'm':'minutes', 'h':'hours', 'd':'days', 'w':'weeks'}
intents = discord.Intents.all()
pre = "="
bot = commands.Bot(command_prefix=commands.when_mentioned_or(pre), intents=intents)
client = discord.Client()
bot.remove_command('help')
typer=0
autodel=None
translatorvar = Translator()
unsortedlangdict = translatorvar.glanguage().get("tl")
unsortedsrclangdict = translatorvar.glanguage().get("sl")
langkeys = list(unsortedlangdict.keys())
langkeys.sort()
langdict = {}
for count in langkeys:
  langdict[count] = unsortedlangdict[count]
srclangkeys = list(unsortedsrclangdict.keys())
srclangkeys.sort()
srclangdict = {}
for count in srclangkeys:
  srclangdict[count] = unsortedsrclangdict[count]
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)
def is_me(msg):
  return msg.author == client.user

async def on_ready(self):
  print('Connected!')

@bot.event
async def on_message(message):
  if message.author.id == 746227806278647928 and message.content.startswith("="):
    await message.channel.send("You are banned from the bot. Expires: 10 Feb. Reason: abuse of =engrave command.")
  elif banned_ids.count(message.author.id)==0:
    await bot.process_commands(message)

"""@bot.event
async def on_reaction_add(reaction, user):
  print(1)
  flagname = reaction.emoji
  print(2)
  print(flagname)
  if "🇦🇫🇦🇽🇦🇱🇩🇿🇦🇸🇦🇩🇦🇴🇦🇮🇦🇶🇦🇬🇦🇷🇦🇲🇦🇼🇦🇨🇦🇺🇦🇹🇦🇿🇧🇸🇧🇭🇧🇩🇧🇧🇧🇾🇧🇪🇧🇿🇧🇯🇧🇲🇧🇹🇧🇴🇧🇦🇧🇼🇧🇻🇧🇷🇮🇴🇻🇬🇧🇳🇧🇬🇧🇫🇧🇮🇰🇭🇨🇲🇨🇦🇮🇨🇨🇻🇧🇶🇰🇾🇨🇫🇪🇦🇹🇩🇨🇱🇨🇳🇨🇽🇨🇵🇨🇨🇨🇴🇰🇲🇨🇬🇨🇩🇨🇰🇨🇷🇨🇮🇭🇷🇨🇺🇨🇼🇨🇾🇨🇿🇩🇰🇩🇬🇩🇯🇩🇲🇩🇴🇪🇨🇪🇬🇸🇻🇬🇶🇪🇷🇪🇪🇪🇹🇪🇺🇫🇰🇫🇴🇫🇯🇫🇮🇫🇷🇬🇫🇵🇫🇹🇫🇬🇦🇬🇲🇬🇪🇩🇪🇬🇭🇬🇮🇬🇷🇬🇱🇬🇩🇬🇵🇬🇺🇬🇹🇬🇬🇬🇳🇬🇼🇬🇾🇭🇹🇭🇲🇭🇳🇭🇰🇭🇺🇮🇸🇮🇳🇮🇩🇮🇷🇮🇶🇮🇪🇮🇲🇮🇱🇮🇹🇯🇲🇯🇵🇯🇪🇯🇴🇰🇿🇰🇪🇰🇮🇽🇰🇰🇼🇰🇬🇱🇦🇱🇻🇱🇧🇱🇸🇱🇷🇱🇾🇱🇮🇱🇹🇱🇺🇲🇴🇲🇰🇲🇬🇲🇼🇲🇾🇲🇻🇲🇱🇲🇹🇲🇭🇲🇶🇲🇷🇲🇺🇾🇹🇲🇽🇫🇲🇲🇩🇲🇨🇲🇳🇲🇪🇲🇸🇲🇦🇲🇿🇲🇲🇳🇦🇳🇷🇳🇵🇳🇱🇳🇨🇳🇿🇳🇮🇳🇪🇳🇬🇳🇺🇳🇫🇲🇵🇰🇵🇳🇴🇴🇲🇵🇰🇵🇼🇵🇸🇵🇦🇵🇬🇵🇾🇵🇪🇵🇭🇵🇳🇵🇱🇵🇹🇵🇷🇶🇦🇷🇪🇷🇴🇷🇺🇷🇼🇼🇸🇸🇲🇸🇹🇸🇦🇸🇳🇷🇸🇸🇨🇸🇱🇸🇬🇸🇽🇸🇰🇸🇮🇸🇧🇸🇴🇿🇦🇬🇸🇰🇷🇸🇸🇪🇸🇱🇰🇧🇱🇸🇭🇰🇳🇱🇨🇲🇫🇵🇲🇻🇨🇸🇩🇸🇷🇸🇯🇸🇿🇸🇪🇨🇭🇸🇾🇹🇼🇹🇯🇹🇿🇹🇭🇹🇱🇹🇬🇹🇰🇹🇴🇹🇹🇹🇦🇹🇳🇹🇷🇹🇲🇹🇨🇹🇻🇺🇬🇺🇦🇦🇪🇬🇧".count(flagname) == 1:
    print(21)
    flagname = flagname.replace("flag_gb", "en")
    flagname = flagname.replace("flag_us", "en")
    flagname = flagname.replace("flag_ca", "en")
    flagname = flagname.replace("flag_eu", "en")
    flagname = flagname.replace("flag_jp", "ja")
    flagname = flagname.replace("flag_cz", "cs")
    flagname = flagname.replace("flag_gr", "el")
    flagname = flagname.replace("flag_cn", "zh-CN")
    flagname = flagname.replace("flag_hk", "zh-TW")
    flagname = flagname.replace("flag_tw", "zh-TW")
    print(3)
    flagname = flagname.lstrip("_galf:")
    lang = flagname.replace(":","")
    print(4)
    try:
      msg = await ctx.send("Translating **"+reaction.message.content+"** to "+langdict[lang])
      translation = translatorvar.translate(reaction.message.content, dest=lang)
      await msg.edit(content = "**Translation from "+langdict[translatorvar.detect(reaction.message.content).lang]+" to "+langdict[lang]+f":**\n"+translation.text.replace("u003c", "<").replace("u003e", ">").replace("u0026", "&"))
    except:
      await reaction.message.channel.send("Sorry, but this language is not supported.")"""

@bot.command()
async def botpurge(ctx, *, num):
  try:
    await ctx.message.delete()
  except:
    1
  if ctx.author.permissions_in(ctx.channel).manage_messages or ctx.author.id == 687474789342117900:
    num = int(num)
    purged = 0
    async for count in ctx.channel.history(limit=1000):
      if count.author.id == 796686363604680755:
        await count.delete()
        purged = purged + 1
        if purged >= num:
          break
        
    await ctx.send("Bot purging completed.", delete_after = 5)
  else:
    print(6)
    await ctx.send("You don't have the required permissions.")

@bot.command()
async def nick(ctx, *, newnick):
  await ctx.guild.get_member(796686363604680755).edit(nick = newnick)
  await ctx.send("Nickname changed.")

@bot.command()
async def help(ctx, *, cat=None):
  if cat!=None:
    cat=cat.lower()
    cat=cat.replace(" ","")
    cat=cat.replace("-","")
    cat=cat.replace("_","")
  if cat=="basic" or cat=="simple" or cat=="normal" or cat=="regular" or cat=="core":
    ti="Basic Commands"
    desc="""
**help {Command or Category}**
Show the help for a specific command/category. The command/category is optional.

**invite**
Invites the bot to your server.

**prefix {New prefix}**
View or change the prefix of the bot.

**ping**
Checks the speed of the bot.

**speedtest**
Does the `ping` command 5 times, thus more accurate.
  """
  elif cat=="discordinfo" or cat=="discordinformation" or cat=="discordi":
    ti="Discord Information Commands"
    desc="""
**server**
Shows information about the current server.

**role [Role ID or Mention]**
Shows information about the desired role.

**channel {Channel Name or ID}**
Shows information about the desired channel.

**voicechannel [Channel Name or ID]**
Shows information about the desired Voice Channel.

**user [User Name, Nickname, ID or Mention] [Channel Name, ID or Mention]**
Shows information about the desired User in a specific channel.
The arguments are optional.

**uservoice [User Name, Nickname, ID or Mention] [Channel Name or ID]**
Shows information about the desired User in a specific voice channel.

**avatar {User Name, Nickname, ID or Mention}**
Shows the avatar of the desired user.

**voicechannel [Invite link or ID]**
Shows information about the desired invite link.

**template [Template ID]**
Shows information about the desired server template.
This command is still in BETA.
  """
  elif cat=="discord":
    ti="Discord Commands"
    desc="""
**spam [Number of times to spam] [Text to spam]**
Spams the text.
It must be less than 30 times and without any mentions.

**embed [Title] [Description] [Color] [Author] [Author URL] [Author Image URL] [Footer] [Thumbnail Image URL] [Image URL]…**
Generates an embed.
**One line for each argument.**
Please check the [documentation](https://github.com/johann-lau/Bot#embed-message-help) for more information.

**pretend [User Name, Nickname, ID or Mention] [Text]**
Pretends as a user and send something, using the magic of webhooks.

**pretendembed [User Name, Nickname, ID or Mention] [Title] [Description] [Color] [Author] [Author URL] [Author Image URL] [Footer] [Thumbnail Image URL] [Image URL]…**
Pretends as a user and generates an embed.
**One line for each argument.**
Please check the [documentation](https://github.com/johann-lau/Bot#embed-message-help) for more information.

**pretendspam [User Name, Nickname, ID or Mention] [Text]**
Pretends as a user and spams the text.
It must be less than 30 times and without any mentions.
  """
  elif cat=="text" or cat=="textmanipulation" or cat=="manipulation":
    ti="Text Manipulation Commands"
    desc="""
**insert [Emoji] [Text]**
Replaces the spaces in the text with emojis.
Protip: also works with multiple emojis by wrapping all emojis in quotation marks. E.g. `=insert ":thumbsup: :heart:" I love this bot!`

**spoiler [Text]**
Generates an annoying spoiler.

**rawspoiler [Text]**
Generates an annoying spoiler for you to copy and paste.

**reverse [Text]**
sesrever the provided text.

**emoji [Text]**
Generates emoji text.
Supported characters: A-Z a-z 0-9 ! ? $ # * + - × ÷
  """
  elif cat=="moderation" or cat=="moderate" or cat=="moderator" or cat=="administer" or cat=="administration" or cat=="administrator" or cat=="manage" or cat=="management" or cat=="manager":
    ti="Moderation Commands"
    desc="""
**kick [User Name, Nickname, ID or Mention] {Reason}**
Kicks a desired user. The Reason is optional.

**ban [User Name, Nickname, ID or Mention] {Reason}**
Bans a desired user. The Reason is optional.
  """
  elif cat=="information" or cat=="info" or cat=="informative":
    ti="Information Commands"
    desc="""
**calc [Formula]**
Does boring math for you. Logical comparisons, scientific math, variables and user-defined functions are available. Please check the [documentation](https://github.com/johann-lau/Bot/blob/main/README.md#math-help) for more information.

**define [name] [definition] [arguments separated by spaces]**
Defines a custom function. Please check the [documentation](https://github.com/johann-lau/Bot/blob/main/README.md#math-help) for more information.

**time {Timezone}**
Checks the time in your timezone. If Timezone is not specified, you will see the UTC time.

**rtimer [Time to count] {Text}**
Starts a timer. Please see the help command for more information.

**terminate [Timer ID]**
Properly terminates a running timer generated by `rtime`.
The Timer ID is a random 5-alphabet code and can be found at the beginning of a timer.

**translate [To language]{,From language} [Text]**
Translates text to another language. If From language is not provided, it will detect the language. e.g. `=translate en Ahoj` `=translate en,cs Ahoj`

**timer [Seconds] {Text}**
Starts a timer. The Text is optional.
**Alert: This command is outdated. Consider using** `rtimer` **instead.**
  """
  elif cat=="web" or cat=="link" or cat=="url" or cat=="website" or cat=="developer" or cat=="tools" or cat=="misc":
    ti="Web Command and Developer Tools"
    desc="""
**screenshot [URL]**
Screenshots the desired webpage. A regular-sized screenshot and a whole-webpage-sized screenshot will be shown.

**youtube [URL]**
Downloads a youtube video and the captions. If the video size is larger than 8MB, only the captions will be uploaded.

**wiki [Query]**
Finds a related Wikipedia article.

**engrave [Product] [Text]**
Engraves the text on an Apple Product. Airpods, iPad, iPod and Apple Pencil are available. Please check the [documentation](https://github.com/johann-lau/Bot/blob/main/README.md#apple-engrave-help) for more information.

**python [Script]**
Executes a Python (3.9.1) script.

**ocr [Image]**
Does an OCR scan for the image.

**text [PDF]**
Turns the PDF to plain text.
  """
  elif cat=="help":
    ti="help {Command or Category}"
    desc="Show the help for a specific command/category. The command/category is optional."
  elif cat=="invite":
    ti="invite"
    desc="Invites the bot to your server."
  elif cat=="prefix":
    ti="prefix"
    desc="View the prefix of the bot."
  elif cat=="ping":
    ti="ping"
    desc="Checks the speed of the bot."
  elif cat=="speedtest":
    ti="speedtest"
    desc="Does the `ping` command 5 times, thus more accurate."
  elif cat=="server":
    ti="server"
    desc="Shows information about the current server."
  elif cat=="role":
    ti="role [Role ID or Mention]"
    desc="Shows information about the desired role."
  elif cat=="channel":
    ti="channel {Channel Name, ID or Mention}"
    desc="Shows information about the desired channel."
  elif cat=="voicechannel":
    ti="voicechannel [Channel Name or ID]"
    desc="Shows information about the desired Voice Channel."
  elif cat=="user":
    ti="user [User Name, Nickname, ID or Mention] [Channel Name, ID or Mention]"
    desc=f"Shows information about the desired User in a specific channel.\nThe arguments are optional."
  elif cat=="uservoice":
    ti="uservoice [User Name, Nickname, ID or Mention] [Channel Name or ID]"
    desc="Shows information about the desired User in a specific voice channel."
  elif cat=="avatar":
    ti="avatar [User Name, Nickname, ID or Mention]"
    desc="Shows the avatar of the desired user."
  elif cat=="invite":
    ti="voicechannel [Invite link or ID]"
    desc="Shows information about the desired invite link."
  elif cat=="template":
    ti="template [Template ID]"
    desc=f"Shows information about the desired server template.\nThis command is still in BETA."
  elif cat=="spam":
    ti="spam [Number of times to spam] [Text to spam]"
    desc=f"Spams the text.\nIt must be less than 30 times and without any mentions."
  elif cat=="embed":
    ti="embed [Title] [Description] [Color]…"
    desc=f"Generates an embed.\n**One line for each argument.**\nPlease check the [documentation](https://github.com/johann-lau/Bot#embed-message-help) for more information."
  elif cat=="pretend":
    ti="pretend [User Name, Nickname, ID or Mention] [Text]"
    desc="Pretends as a user and send something, using the magic of webhooks."
  elif cat=="pretendembed":
    ti="pretendembed [User Name, Nickname, ID or Mention] [Title] [Description] [Color]…"
    desc=f"Pretends as a user and generates an embed.\n**One line for each argument.**\nPlease check the [documentation](https://github.com/johann-lau/Bot#embed-message-help) for more information."
  elif cat=="pretendspam":
    ti="pretendspam [User Name, Nickname, ID or Mention] [Text]"
    desc=f"Pretends as a user and spams the text.\nIt must be less than 30 times and without any mentions."
  elif cat=="insert":
    ti="insert [Emoji] [Text]"
    desc=f"Replaces the spaces in the text with emojis.\nProtip: also works with multiple emojis by wrapping all emojis in quotation marks. E.g. `=insert \":thumbsup: :heart:\" I love this bot!`"
  elif cat=="spoiler":
    ti="spoiler [Text]"
    desc="Generates an annoying spoiler."
  elif cat=="rawspoiler":
    ti="rawspoiler [Text]"
    desc="Generates an annoying spoiler for you to copy and paste."
  elif cat=="reverse":
    ti="reverse [Text]"
    desc="sesrever the provided text."
  elif cat=="emoji":
    ti="emoji [Text]"
    desc=f"Generates emoji text.\nSupported characters: A-Z a-z 0-9 ! ? $ # * + - × ÷"
  elif cat=="kick":
    ti="kick [User Name, Nickname, ID or Mention] {Reason}"
    desc="Kicks a desired user. The Reason is optional."
  elif cat=="ban":
    ti="ban [User Name, Nickname, ID or Mention] {Reason}"
    desc="Bans a desired user. The Reason is optional."
  elif cat=="slowmode":
    ti="slowmode [Seconds] {Channel(s)}"
    desc=f"Sets the slowmode for the channel. Any non-numeric value, or zero, disables it.\nChannels is optional. If Channel(s) is not provided, the current channel will be set.\nYou are allowed to use multiple channels, or use all to set for all channels in the server."
  elif cat=="math":
    ti="math [Formula]"
    desc="Does boring math for you. Logical comparisons, scientific math, variables and user-defined functions are available. Please check the [documentation](https://github.com/johann-lau/Bot/blob/main/README.md#math-help) for more information."
  elif cat=="define":
    ti="define [name] [definition] [arguments separated by spaces]"
    desc="Defines a custom function. Please check the [documentation](https://github.com/johann-lau/Bot/blob/main/README.md#math-help) for more information."
  elif cat=="time":
    ti="time {Timezone}"
    desc="Checks the time in your timezone. If Timezone is not specified, you will see the UTC time."
  elif cat=="rtimer":
    ti="rtimer [Time to count] {Text}"
    desc=f"Starts a timer. Use `s` (seconds), `m` (minutes), `h` (hours), `d` (days) and `w` (weeks).\nIf you specify a unit twice (e.g. `10s5s`), the first one will be omitted.\nDefault to seconds if no unit is specified.\nThe Text is optional."
  elif cat=="terminate":
    ti="terminate [Timer ID]"
    desc=f"Properly terminates a running timer generated by `rtime`.\nThe Timer ID is a random 5-alphabet code and can be found at the beginning of a timer."
  elif cat=="translate":
    ti="translate [To lang]{,From lang} [Text]"
    desc="Translates text to another language. If From language is not provided, it will detect the language. e.g. `=translate en Ahoj` `=translate en,cs Ahoj`"
  elif cat=="timer":
    ti="timer [Seconds] {Text}"
    desc=f"Starts a timer. The Text is optional.\n**Alert: This command is outdated. Consider using** `rtimer` **instead.**"
  elif cat=="screenshot":
    ti="screenshot [URL]"
    desc="Screenshots the desired webpage. A regular-sized screenshot and a whole-webpage-sized screenshot will be shown."
  elif cat=="youtube":
    ti="youtube [URL]"
    desc="Downloads a youtube video and the captions. If the video size is larger than 8MB, only the captions will be uploaded."
  elif cat=="wiki":
    ti="wiki [Query]"
    desc="Finds a related Wikipedia article."
  elif cat=="engrave":
    ti="engrave [Product] [Text]"
    desc="Engraves the text on an Apple Product. Airpods, iPad, iPod and Apple Pencil are available. Please check the [documentation](https://github.com/johann-lau/Bot/blob/main/README.md#apple-engrave-help) for more information."
  elif cat=="python":
    ti="python [Python script]"
    desc="Executes a Python (3.9.1) script."
  elif cat=="ocr":
    ti="ocr [Image]"
    desc=f"Does an OCR scan for the image."
  elif cat=="text":
    ti="text [PDF]"
    desc=f"Turns the PDF to plain text."
  else:
    ti="Tunnelers' Bot Help"
    desc="""
**Prefix: **`=`

**Basic Commands**
`help` `invite` `prefix` `ping` `speedtest`

**Discord Information Commands**
`server` `role` `channel` `voicechannel` `user` `uservoice` `avatar` `invite` `template` (BETA)

**Discord Commands**
`spam` `embed` `pretend` `pretendembed` `pretendspam` (BETA)

**Text Manipulation Commands**
`insert` `spoiler` `rawspoiler` `reverse` `emoji`

**Moderation & Information Commands**
`kick` `ban` `slowmode` `math` `define` `time` `rtimer` `terminate` `timer` (Outdated)

**Web Commands & Developer Tools**
`screenshot` `youtube` `wiki` `engrave` `python` `ocr` `text` `html` (BETA)

Need help? check the [documentation](https://github.com/johann-lau/Bot#bot-documentation)!
  """
  embed=discord.Embed(title=ti, description=desc, color=0x0061ff)
  await ctx.send(embed=embed)

@bot.command()
async def invite(ctx, *, text):
  embed = discord.Embed(title="Invite", description = "Our bot could be invited [here](https://discord.com/oauth2/authorize?client_id=796686363604680755&permissions=805399670&scope=bot).")
  await ctx.send(embed=embed)

@bot.command()
async def translate(ctx, langinput = "list", *, text = "Sample text"):
  if langinput == "list" or langinput == "all":
    embed1 = discord.Embed(description = f"**List of Language Input (Abbreviations)**\n`"+"` `".join(list(langdict.keys()))+f"`\n\n**List of Language Input (Full Names)**\n`"+"` `".join(list(langdict.values())))
    embed2 = discord.Embed(description = f"**List of Language Output (Abbreviations)**\n`"+"` `".join(list(srclangdict.keys()))+f"`\n\n**List of Language Output (Full Names)**\n`"+"` `".join(list(srclangdict.values()))+"`")
    await ctx.send(embed=embed1)
    await ctx.send(embed=embed2)
  else:
    if langinput.count(",")==1:
      lang = langinput.split(",")[0]
      fromlang = langinput.split(",")[1]
      if list(srclangdict.values()).count(fromlang) == 1:
        fromlang = list(srclangdict.keys())[list(srclangdict.values()).index(fromlang)]
    else:
      fromlang = "auto"
      lang = langinput
    if list(langdict.values()).count(lang) == 1:
      lang = list(langdict.keys())[list(langdict.values()).index(lang)]
    msg = await ctx.send("Translating **"+text+"** to "+langdict[lang])
    translation = translatorvar.translate(text, src=fromlang, dest=lang)
    try:
      await msg.edit(content = "**Translation from "+srclangdict[fromlang]+" to "+langdict[lang]+f":**\n"+translation.text.replace("u003c", "<").replace("u003e", ">").replace("u0026", "&"))
    except:
      await ctx.send("Language not found! Please use `=translate list` to get a list of languages.")

@bot.command()
async def engrave(ctx, product = "list", *, text = "Your text goes here."):
  product = product.lower()
  product = product.replace(" ","")
  product = product.replace("-","")
  product = product.replace("_","")
  product = product.replace(".","")
  product = product.replace(",","")
  text = text.replace("%","%25")
  text = text.replace(" ","%20")
  text = text.replace("+","%2B")
  text = text.replace("/","%2F")
  text = text.replace(":","%3A")
  text = text.replace(";","%3B")
  text = text.replace("[","%5B")
  text = text.replace("]","%5D")
  text = text.replace("{","%7B")
  text = text.replace("}","%7D")
  text = text.replace("=","%3D")
  text = text.replace("|","%7C")
  text = text.replace("#","%23")
  text = text.replace("$","%24")
  text = text.replace("&","%26")
  text = text.replace("?","%3F")
  text = text.replace("@","%40")
  text = text.replace("^","%5E")
  text = text.replace("`","%60")
  if product == "airpodspro" or product == "airpodpro":
    embed = discord.Embed(title="Engrave on AirPods Pro")
    embed.set_image(url="https://www.apple.com/shop/preview/engrave/PWP22AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "airpodson" or product == "airpodon":
    embed = discord.Embed(title="Engrave on AirPods (On)")
    embed.set_image(url="https://www.apple.com/shop/preview/engrave/PRXJ2AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "airpods" or product == "airpod" or product == "airpodsoff" or product == "airpodoff":
    embed = discord.Embed(title="Engrave on AirPods")
    embed.set_image(url="https://www.apple.com/shop/preview/engrave/PV7N2AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "airpodsmaxgray" or product == "airpodmaxgray" or product == "airpodsmaxgrey" or product == "airpodmaxgrey" or product == "airpodsmaxspacegray" or product == "airpodmaxspacegray" or product == "airpodsmaxspacegrey" or product == "airpodmaxspacegrey" or product == "airpodsmax" or product == "airpodmax":
    embed = discord.Embed(title="Engrave on AirPods Max (Space Gray)")
    embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PGYH3AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "airpodsmaxsilver" or product == "airpodmaxsilver":
    embed = discord.Embed(title="Engrave on AirPods Max (Silver)")
    embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PGYJ3AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "airpodsmaxgreen" or product == "airpodmaxgreen":
    embed = discord.Embed(title="Engrave on AirPods Max (Green)")
    embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PGYN3AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "airpodsmaxblue" or product == "airpodmaxblue" or product == "airpodsmaxskyblue" or product == "airpodmaxskyblue":
    embed = discord.Embed(title="Engrave on AirPods Max (Sky blue)")
    embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PGYL3AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "airpodsmaxpink" or product == "airpodmaxpink":
    embed = discord.Embed(title="Engrave on AirPods Max (Pink)")
    embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PGYM3AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "ipadprogray" or product == "ipadprogrey" or product == "ipadpro" or product == "padpro":
    embed = discord.Embed(title="Engrave on iPad Pro (Space Gray)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PXAV2LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PXAV2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadprosilver":
    embed = discord.Embed(title="Engrave on iPad Pro (Silver)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PXAW2LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PXAW2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadgray" or product == "ipadgrey" or product == "padgray" or product == "padgrey" or product == "ipadspacegray" or product == "ipadspacegrey" or product == "padspacegray" or product == "padspacegrey" or product == "ipad" or product == "pad":
    embed = discord.Embed(title="Engrave on iPad (Space Gray)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYN72LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYN72LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadsilver" or product == "padsilver":
    embed = discord.Embed(title="Engrave on iPad (Silver)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYN82LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYN82LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadgold" or product == "ipadgolden" or product == "padgold" or product == "ipadgolden":
    embed = discord.Embed(title="Engrave on iPad (Gold)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYN92LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYN92LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadairgray" or product == "ipadairgrey" or product == "padairgray" or product == "padairgrey" or product == "ipadairspacegray" or product == "ipadairspacegrey" or product == "padairspacegray" or product == "padairspacegrey" or product == "ipadair" or product == "padair":
    embed = discord.Embed(title="Engrave on iPad Air (Space Gray)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYHX2LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYHX2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadairsilver" or product == "padairsilver":
    embed = discord.Embed(title="Engrave on iPad Air (Silver)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYHY2LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYHY2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadairrose" or product == "ipadairrosegold" or product == "padairrose" or product == "padairrosegold":
    embed = discord.Embed(title="Engrave on iPad Air (Rose Gold)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYJ02LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYJ02LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadairgreen" or product == "padairgreen":
    embed = discord.Embed(title="Engrave on iPad Air (Green)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYJ22LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYJ22LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadairblue" or product == "ipadairskyblue" or product == "padairblue" or product == "padairskyblue":
    embed = discord.Embed(title="Engrave on iPad Air (Sky Blue)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYJ12LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYJ12LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadminigray" or product == "ipadminigrey" or product == "padminigray" or product == "padminigrey" or product == "ipadminispacegray" or product == "ipadminispacegrey" or product == "padminispacegray" or product == "padminispacegrey" or product == "ipadmini" or product == "padmini":
    embed = discord.Embed(title="Engrave on iPad Mini (Space Gray)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PUXM2LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PUXM2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadminisilver" or product == "padminisilver":
    embed = discord.Embed(title="Engrave on iPad Mini (Silver)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PUXN2LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PUXN2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadminigold" or product == "ipadminigolden" or product == "padminigold" or product == "padminigolden":
    embed = discord.Embed(title="Engrave on iPad Mini (Gold)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PUXP2LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PUXP2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipodgray" or product == "ipodgrey" or product == "podgray" or product == "podgrey" or product == "ipodspacegray" or product == "ipodspacegrey" or product == "podspacegray" or product == "podspacegrey" or product == "ipodtouchgray" or product == "ipodtouchgrey" or product == "podtouchgray" or product == "podtouchgrey" or product == "ipodtouchspacegray" or product == "ipodtouchspacegrey" or product == "podtouchspacegray" or product == "podtouchspacegrey" or product == "ipod" or product == "pod" or product == "ipodtouch" or product == "podtouch" :
    embed = discord.Embed(title="Engrave on iPod Touch (Space Gray)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVJE2LL/A?th="+split[0]+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVJE2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipodsilver" or product == "podsilver" or product == "ipodtouchsilver" or product == "podtouchsilver":
    embed = discord.Embed(title="Engrave on iPod Touch (Silver)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVJD2LL/A?th="+split[0]+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVJD2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipodgold" or product == "ipodgolden" or product == "podgold" or product == "podgolden" or product == "ipodtouchgold" or product == "ipodtouchgolden" or product == "podtouchgold" or product == "podtouchgolden":
    embed = discord.Embed(title="Engrave on iPod Touch (Gold)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVJ92LL/A?th="+split[0]+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVJ92LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipodblue" or product == "podblue" or product == "ipodtouchblue" or product == "podtouchblue":
    embed = discord.Embed(title="Engrave on iPod Touch (Blue)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVJC2LL/A?th="+split[0]+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVJC2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipodpink" or product == "podpink" or product == "ipodtouchpink" or product == "podtouchpink":
    embed = discord.Embed(title="Engrave on iPod Touch (Pink)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVJ82LL/A?th="+split[0]+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVJ82LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipodred" or product == "podred" or product == "ipodtouchred" or product == "podtouchred":
    embed = discord.Embed(title="Engrave on iPod Touch (Red)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVJF2LL/A?th="+split[0]+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVJF2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "pencil" or product == "pencil2":
    embed = discord.Embed(title="Engrave on Apple Pencil (2nd generation)")
    embed.set_image(url="https://www.apple.com/shop/preview/engrave/PU8F2AM/A?th="+text+"&s=2&tl=")
  elif product == "list" or product == "product" or product == "help" or product == "products":
    embed = discord.Embed(title="List of products")
    embed.add_field(name="AirPods/Pencil", value="`airpods` `airpodson` `airpodspro` `pencil`", inline=False)
    embed.add_field(name="AirPods Max", value="`airpodsmax` `airpodsmaxgray` `airpodsmaxsilver` `airpodsmaxpink` `airpodsmaxgreen` `airpodsmaxblue`", inline=False)
    embed.add_field(name="iPad/iPad Mini", value="`ipadmini` `ipadminigray` `ipadminisilver` `ipadminigold`", inline=False)
    embed.add_field(name="iPad Pro", value="`ipadpro` `ipadprogray` `ipadprosilver`", inline=False)
    embed.add_field(name="iPad Air", value="`ipadair` `ipadairgray` `ipadairsilver` `ipadairrose` `ipadairgreen` `ipadairblue`", inline=False)
    embed.add_field(name="iPod Touch", value="`ipod` `ipodgray` `ipodsilver` `ipodgold` `ipodred` `ipodpink` `ipodblue`", inline=False)
    
  else:
    embed = discord.Embed(title="Invalid product", description="")
  await ctx.send(embed=embed)

@bot.command()
async def transparent(ctx, alpha = 128):
  await ctx.message.attachments[0].save("Not_Transparent.png")
  img = PIL.Image.open("Not_Transparent.png")
  img2 = img.copy()
  img2.putalpha(int(alpha))
  img.paste(img2, img)
  img.save('Transparent.png')
  await ctx.send(file = discord.File('Transparent.png'))
  os.remove('Transparent.png')

@bot.command()
async def mandelbrot(ctx, size = 1024):
  img = PIL.Image.effect_mandelbrot((int(size), int(size)), (-1.5, -2.5, 3.5, 2.5), 95)
  img.save('Mandelbrot.png')
  await ctx.send(file = discord.File('Mandelbrot.png'))
  os.remove('Mandelbrot.png')

@bot.command()
async def status(ctx, member : discord.Member = None):
  if member==None:
    member=ctx.author
  if member.is_on_mobile==True:
    desc = str(member.status)+" on mobile"
  else:
    desc = str(member.status)+" on desktop"
  embed = discord.Embed(title="Status: "+member.name, description=desc)
  for count in member.activities:
    if str(count.type)=="ActivityType.custom":
      if count.emoji==None:
        field=count.name
      else:
        field=count.emoji+count.name
      embed.add_field(name="Status", value=field, inline=False)
    if str(count.type)=="ActivityType.playing":
      field=count.name+f"\nStarted: "+str(count.start.strftime("%d %b, %Y (%a) %H:%M:%S"))
      embed.add_field(name="Game", value=field, inline=False)
    if str(count.type)=="ActivityType.streaming":
      field="["+count.platform+":"+count.name+"]("+count.url+f")\nStarted: "+count.start.strftime("%d %b, %Y (%a) %H:%M:%S")
      embed.add_field(name="Game", value=field, inline=False)
      embed.set_thumbnail(url=count.large_image_url)
    if str(count.type)=="ActivityType.listening":
      field=count.artist+" : "+count.title+f"\nStarted: "+count.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")
      embed.add_field(name="Spotify : "+count.album, value=field, inline=False)
      embed.set_thumbnail(url=count.album_cover_url)
  await ctx.send(embed=embed)

@bot.command()
async def define(ctx, function = None, definition = None, *, argumentsraw = ""):
  if function == None or definition == None:
    await ctx.send("Invalid usage! Please use the format `=define [name] [definition] {arguments separated by spaces}`.")
  else:
    definition=definition.replace("^","**")
    definition=definition.replace("÷","/")
    definition=definition.replace("×","*")
    definition=definition.replace("mod","%")
    definition=definition.replace("√(","sqrt(")
    definition=definition.replace("pi",str(pi))
    definition=definition.replace("e",str(e))
    program="def "+function+"("
    if argumentsraw != "":
      arguments = argumentsraw.split(" ")
      for count in arguments:
        program = program + count + ","
    program = program[:-1]
    program = program + f"):\n  return "+definition
    exec(program, globals())
    await ctx.message.add_reaction("👍")

@bot.command()
async def python(ctx, *, script):
  match = python_pattern.fullmatch(script)
  if match:
    script = script.replace("```py","", 1)
    script = script.replace("```","")
  file = open("program.py", "w")
  file.write(script)
  file.close()
  proc = subprocess.Popen(['python', 'program.py',  ''], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  try:
    output = str(proc.communicate(timeout = 1)[0])
    output = output.lstrip("'b(").rstrip("\\n'").replace("\n", f"\n")
  except subprocess.TimeoutExpired:
    proc.kill()
    output = str(proc.communicate())
  output = output.lstrip("'b(").rstrip("\\n'").replace("\n", f"\n")
  outputlist = output.split("\\n")
  if len(outputlist)<=11:
    formatoutput = ""
    for count in range(0, len(outputlist)):
      if count+1<=9:
        formatoutput = formatoutput + "0" + str(count+1) + " | " + outputlist[count] + f"\n"
      else:
        formatoutput = formatoutput + str(count+1) + " | " + outputlist[count] + f"\n"
    
    if formatoutput == f"01 | \n":
      await ctx.send("There was no result to be shown.")
    else:
      await ctx.send(f"```\n"+formatoutput+f"\n```")
  else:
    truncatedoutput = ""
    for count in range(0,11):
      if count+1<=9:
        truncatedoutput = truncatedoutput + "0" + str(count+1) + " | " + outputlist[count] + f"\n"
      else:
        truncatedoutput = truncatedoutput + str(count+1) + " | " + outputlist[count] + f"\n"
    await ctx.send(f"The result was truncated due to the length of the result. It had probably timed out.\n```\n"+truncatedoutput+f"\n```")

@bot.command()
async def calc(ctx, *, arg = None):
  if arg == None:
    await ctx.send("Invalid format! Please use the format `=calc [formula]`.")
  else:
    arg=arg.replace("^","**")
    arg=arg.replace("÷","/")
    arg=arg.replace("×","*")
    arg=arg.replace("mod","%")
    arg=arg.replace("√(","sqrt(")
    arg=arg.replace("pi",str(pi))
    arg=arg.replace("e",str(e))
    if arg.count("=")==0 or arg.count("==")!=0 or arg.count("!=")!=0 or arg.count(">=")!=0 or arg.count("<=")!=0 or arg.count(">")!=0 or arg.count("<")!=0 or arg.count("and")!=0 or arg.count("or")!=0 or arg.count("not")!=0:
      lcls = locals()
      exec("result = "+arg, globals(), lcls)
      result = lcls["result"]
      if result.real==result:
        result=result.real
      if len(str(result))>400:
        number=result
        result=str(number)[0]+"."
        for count in range(1,60):
          result=result+str(number)[count]
        result=result+"e+"+str(len(str(number))-1)
      elif len(str(result))>100:
        result="{0:.3E}".format(float(result))
      disp = "Result: "+str(result)
      await ctx.send(disp)
    elif arg.count("=")!=0 and arg.count("==")==0 and arg.count("!=")==0 and arg.count(">=")==0 and arg.count("<=")==0 and arg.count(">")==0 and arg.count("<")==0 and arg.count("and")==0 and arg.count("or")==0 and arg.count("not")==0:
      lcls = locals()
      exec(arg, globals(), lcls)
      await ctx.message.add_reaction("👍")
    else:
      await ctx.send("Invalid input, please try again.")

@bot.command()
async def ping(ctx, *, text = None):
  now1 = datetime.now()
  message = await ctx.send("Pong!")
  mcs = str((datetime.now() - now1).microseconds+(datetime.now() - now1).seconds*1000000)
  await message.edit(content="Pong! "+mcs+" microseconds")

@bot.command()
async def speedtest(ctx, *, text = None):
  total=0
  now1 = datetime.now()
  message = await ctx.send("Pong!")
  mcs = (datetime.now() - now1).microseconds
  total = total + mcs
  for count in range(1,6):
    now1 = datetime.now()
    await message.edit(content="Pong! "+str(mcs)+" microseconds  (Test "+str(count)+")")
    mcs = (datetime.now() - now1).microseconds
    total = total + mcs
  avg = int(total/6)
  await message.edit(content=f"Pong!\nTotal time: "+str(total)+f" mcs\nAverage time: "+str(avg)+" mcs")

@bot.command()
async def screenshot(ctx, url = None, form = "all"):
  if url == None:
    await ctx.send("Invalid format! Please use the format `=screenshot [url]`.")
  else:
    driver.get(url)
    if form == "short" or form == "first" or form == "normal" or form == "regular" or form == "basic" or form == "general" or form == "all":
      driver.set_window_size(1440,900)
      driver.get_screenshot_as_file('web_screenshot1.png')
      await ctx.send(file=discord.File('web_screenshot1.png'))
      os.remove('web_screenshot1.png')
    if form == "everything" or form == "full" or form == "entire" or form == "whole" or form == "all":
      S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
      driver.set_window_size(S('Width'),S('Height'))
      for count in range(900, 5400, 900):
        driver.execute_script("window.scrollTo(0, "+str(count)+")")
      driver.get_screenshot_as_file('web_screenshot2.png')
      driver.quit()
      await ctx.send(file=discord.File('web_screenshot2.png'))
      os.remove('web_screenshot2.png')

@bot.command()
async def ocr(ctx, *, text = None):
  images = ctx.message.attachments
  for count in range(0,len(images)):
    r = requests.get(images[count].url, stream=True)
    r.raise_for_status()
    r.raw.decode_content = True
    with PIL.Image.open(r.raw) as img:
      desc=pytesseract.image_to_string(img)
    r.close()
    if desc=="":
      desc="There was no text."
    await ctx.send(desc)

@bot.command()
async def text(ctx, *, text = None):
  files = ctx.message.attachments
  for count in range(0,len(files)):
    r = requests.get(files[count].url, stream=True)
    r.raise_for_status()
    r.raw.decode_content = True
    if files[count].filename.endswith(".pdf"):
      open('pdf.pdf', 'wb').write(r.content)
      images = convert_from_path('pdf.pdf')
      for count in images:
        desc=pytesseract.image_to_string(count)
      os.remove('pdf.pdf')
    elif files[count].endswith(".txt"):
      open('txt.txt', 'wb').write(r.content)
      with open('data.txt', 'r') as file:
        desc = file.read().replace('\n', '')
      os.remove('txt.txt')
    else:
      desc = "Unsupported format. Please use .pdf or .txt."
    if desc=="":
      desc="There was no text."
    await ctx.send(desc)

@bot.command()
async def html(ctx, *, code = None):
  match = html_pattern.fullmatch(code)
  if match:
    code = code.replace("```html","", 1)
    code = code.replace("```","")
  if code == None:
    r = requests.get(ctx.message.attachments[0].url, stream=True)
    r.raise_for_status()
    r.raw.decode_content = True
    code = r.content
  driver.get(f"data:text/html;charset=utf-8,{code}")
  S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
  driver.set_window_size(S('Width'),S('Height'))
  driver.save_screenshot('html_screenshot.png')
  driver.quit()
  await ctx.send(file=discord.File('html_screenshot.png'))
  os.remove('html_screenshot.png')

@bot.command()
async def youtube(ctx, *, url):
  youtube = pytube.YouTube(url)
  video = youtube.streams.filter(file_extension='mp4').get_highest_resolution()
  if video.filesize<=8388119:
    video.download(filename='YTVideo')
  else:
    for count in youtube.streams.filter(file_extension='mp4', progressive=True).order_by('resolution').desc():
      if count.filesize<=8388119:
        count.download(filename='YTVideo')
        break
  try:
    msg = await ctx.send(file=discord.File('YTVideo.mp4'))
  except:
    await ctx.send("The video is too large to upload.")
  audio = youtube.streams.filter(only_audio=True, file_extension='mp3')[0]
  audio.download(filename='YTAudio')
  await ctx.send(file=discord.File('YTAudio.mp3'))
  try:
    captions = youtube.captions.get_by_language_code('en').generate_srt_captions()
    actualcaptions = ""
    for count in captions.splitlines():
      if count.isnumeric()==False and (count.count(" --> ")!=1 or count.count(":")!=4 or count.count(",")!=2):
        actualcaptions = actualcaptions + count + f"\n"
    file = open("captions.txt", "w")
    file.write(actualcaptions)
    file.close()
    await ctx.send(file=discord.File('captions.txt'))
    os.remove('captions.txt')
  except:
    await edit(msg, "No captions available for the video.")
  os.remove('YTVideo.mp4')

@bot.command()
async def definition(ctx, *, word):
  ti = "Definition of "+word
  desc = ""
  definitions = dictionary.meaning(word)
  for count in list(definitions.keys()):
    desc = desc + "**"+count+f"**\n"+definitions[count]+f"\n"
  desc = desc + f"**Synonyms**\n"
  for count in dictionary.synonym(word):
    desc = desc + count + ", "
  desc = desc [:-2]
  desc = desc + f"\n**Antonyms**\n"
  for count in dictionary.antonym(word):
    desc = desc + count + ", "
  desc = desc [:-2]
  embed = discord.Embed(title=ti, description=desc)

@bot.command()
async def wiki(ctx, *, query):
  wikipedia.set_lang("en")
  try:
    desc = wikipedia.summary(query)
    if len(desc)>2048:
      desc = desc[0:2046]+"…"
    page = wikipedia.page(title=query, auto_suggest=True, redirect=True, preload=False)
    embed = discord.Embed(title=query, description=desc)
    #for count in page.sections:
    #  embed.add_field(name=count, value=wikipeida.section(count)[:500], inline=False)
    if len(page.images)!=0:
      embed.set_thumbnail(url = page.images[0])
    if len(page.images)>=2:
      embed.set_image(url = page.images[1])
    await ctx.send(embed = embed)
    file = open("wiki.html", "w")
    file.write(page.html())
    file.close()
    await ctx.send(file=discord.File('wiki.html'))
    os.remove('wiki.html')
    desc = ""
    for count in page.images:
      desc = desc + str(count) + " "
    await ctx.send(desc)
  except:
    results = wikipedia.search(query, results=20, suggestion=False)
    desc = "**Please make one of these searches:**"
    for count in results:
      desc = desc + "`"+str(count)+"` "
    embed = discord.Embed(title=query, description=desc)
    await ctx.send(embed = embed)
  
@bot.command()
async def purgereactions(ctx, messages, emoji: discord.Emoji = None):
  if emoji == None:
    async for message in ctx.channel.history(limit=int(messages)+1):
      await message.clear_reactions()
  else:
    async for message in ctx.channel.history(limit=int(messages)+1):
      await message.clear_reaction(emoji)

@bot.command(pass_context=True)
async def react(ctx, message : discord.Message, emoji : discord.Emoji):
  await ctx.message.delete()
  await message.add_reaction(emoji)
  asyncio.sleep(3)
  member=ctx.guild.get_member(796686363604680755)
  await message.remove_reaction(emoji, member)

@bot.command(pass_context=True)
async def pretend(ctx, member : discord.Member, *, message):
  try:
    await ctx.message.delete()
  except:
    1
  whl = await ctx.channel.webhooks()
  ourweb = False
  for count in whl:
    if count.name == "Pretender":
      ourweb = True
      token = count.token
      identify = count.id
  if len(whl) == 0 or ourweb == False:
    wh = await ctx.channel.create_webhook(name = "Pretender")
    token = wh.token
    identify = wh.id
  async with aiohttp.ClientSession() as session:
    webhook = Webhook.partial(identify, token, adapter=RequestsWebhookAdapter())
  await webhook.send(message, username=member.name, avatar_url=member.avatar_url)

@bot.command(pass_context=True)
async def pretendembed(ctx, member : discord.Member, *, text):
  try:
    await ctx.message.delete()
  except:
    1
  whl = await ctx.channel.webhooks()
  ourweb = False
  for count in whl:
    if count.name == "Pretender":
      ourweb = True
      token = count.token
      identify = count.id
  if len(whl) == 0 or ourweb == False:
    wh = await ctx.channel.create_webhook(name = "Pretender")
    token = wh.token
    identify = wh.id
  async with aiohttp.ClientSession() as session:
    webhook = Webhook.partial(identify, token, adapter=RequestsWebhookAdapter())
  textlist=text.splitlines()
  if textlist[3]=="":
    embed=discord.Embed(title=textlist[0], url=textlist[1], description=textlist[2].replace("{{{newline}}}","\n"))
  else:
    embed=discord.Embed(title=textlist[0], url=textlist[1], description=textlist[2].replace("{{{newline}}}","\n"), color=int(textlist[3]))
  textlist.remove(textlist[0])
  textlist.remove(textlist[0])
  textlist.remove(textlist[0])
  textlist.remove(textlist[0])
  embed.set_author(name=textlist[0], url=textlist[1], icon_url=textlist[2])
  textlist.remove(textlist[0])
  textlist.remove(textlist[0])
  textlist.remove(textlist[0])
  embed.set_footer(text=textlist[0])
  textlist.remove(textlist[0])
  embed.set_thumbnail(url=textlist[0])
  textlist.remove(textlist[0])
  embed.set_image(url=textlist[0])
  textlist.remove(textlist[0])
  for count in range(0,len(textlist)//3):
    if textlist[2].lower()=="y" or textlist[2].lower()=="yes" or textlist[2].lower()=="true" or textlist[2].lower()=="1":
      inl=True
    else:
      inl=False
    embed.add_field(name=textlist[0], value=textlist[1].replace("{{{newline}}}","\n"), inline=inl)
    textlist.remove(textlist[0])
    textlist.remove(textlist[0])
    textlist.remove(textlist[0])
  await webhook.send(embed=embed, username=member.name, avatar_url=member.avatar_url)

@bot.command()
async def type(ctx):
  global typer
  if typer==0:
    channel=ctx.channel
    await ctx.send("Started typing")
    async with channel.typing():
      typer=1
      var=0
  else:
    typer=0
    await ctx.send("Stopped typing")

@bot.command()
async def embed(ctx,*,text):
  if ctx.author.id == 746227806278647928 and ctx.guild.id == 801994114467233862:
    embed = discord.Embed(title="Rules", description="There are no rules! Have fun!")
  elif ctx.author.id != 746227806278647928:
      textlist=text.splitlines()
      if textlist[3] == "":
        embed=discord.Embed(title=textlist[0], url=textlist[1], description=textlist[2].replace("{{{newline}}}","\n"))
      else:
        embed=discord.Embed(title=textlist[0], url=textlist[1], description=textlist[2].replace("{{{newline}}}","\n"), color=int(textlist[3]))
      textlist.remove(textlist[0])
      textlist.remove(textlist[0])
      textlist.remove(textlist[0])
      textlist.remove(textlist[0])
      embed.set_author(name=textlist[0], url=textlist[1], icon_url=textlist[2])
      textlist.remove(textlist[0])
      textlist.remove(textlist[0])
      textlist.remove(textlist[0])
      embed.set_footer(text=textlist[0])
      textlist.remove(textlist[0])
      embed.set_thumbnail(url=textlist[0])
      textlist.remove(textlist[0])
      embed.set_image(url=textlist[0])
      textlist.remove(textlist[0])
      for count in range(0,len(textlist)//3):
        if textlist[2].lower()=="y" or textlist[2].lower()=="yes" or textlist[2].lower()=="true" or textlist[2].lower()=="1":
          inl=True
        else:
          inl=False
        embed.add_field(name=textlist[0], value=textlist[1].replace("{{{newline}}}","\n"), inline=inl)
        textlist.remove(textlist[0])
        textlist.remove(textlist[0])
        textlist.remove(textlist[0])
  await ctx.send(embed=embed)

@bot.command()
async def editembed(ctx, message : discord.Message, *,text):
  textlist=text.splitlines()
  embed=discord.Embed(title=textlist[0], url=textlist[1], description=textlist[2].replace("{{{newline}}}","\n"), color=int(textlist[3]))
  textlist.remove(textlist[0])
  textlist.remove(textlist[0])
  textlist.remove(textlist[0])
  textlist.remove(textlist[0])
  embed.set_author(name=textlist[0], url=textlist[1], icon_url=textlist[2])
  textlist.remove(textlist[0])
  textlist.remove(textlist[0])
  textlist.remove(textlist[0])
  embed.set_footer(text=textlist[0])
  textlist.remove(textlist[0])
  embed.set_thumbnail(url=textlist[0])
  textlist.remove(textlist[0])
  embed.set_image(url=textlist[0])
  textlist.remove(textlist[0])
  for count in range(0,len(textlist)//3):
    if textlist[2].lower()=="y" or textlist[2].lower()=="yes" or textlist[2].lower()=="true" or textlist[2].lower()=="1":
      inl=True
    else:
      inl=False
    embed.add_field(name=textlist[0], value=textlist[1].replace("{{{newline}}}","\n"), inline=inl)
    textlist.remove(textlist[0])
    textlist.remove(textlist[0])
    textlist.remove(textlist[0])
  await message.edit(embed=embed)

@bot.command()
async def insert(ctx,emoji,*,text):
  text=text.replace(" "," "+emoji+" ")
  await ctx.send(text)

@bot.command()
async def purge(ctx, num):
  try:
    await ctx.message.delete()
  except:
    1
  if ctx.author.permissions_in(ctx.channel).manage_messages or ctx.author.id == 687474789342117900:
    num=int(num)
    await ctx.channel.purge(limit=num+1)
    await ctx.send("Purging completed.", delete_after = 5)
  else:
    await ctx.send("You don't have the required permissions.")

@bot.command()
async def purgeregex(ctx, num, *, regex):
  try:
    await ctx.message.delete()
  except:
    1
  if ctx.author.permissions_in(ctx.channel).manage_messages or ctx.author.id == 687474789342117900:
    exec("purge_pattern = re.compile(r'"+regex+"')", globals())
    num = int(num)
    purged = 0
    async for count in ctx.channel.history(limit=1000):
      match = match = purge_pattern.fullmatch(count.content)
      try:
        if match:
          await count.delete()
          purged = purged + 1
          if purged >= num:
            break
      except:
        await ctx.send("I don't have the required permissions, or the regex was malformed.")
        break
    await ctx.send("Regex purging completed.", delete_after = 5)
  else:
    await ctx.send("You don't have the required permissions.")

@bot.command()
async def purgepygex(ctx, num, regex, *, pyscript):
  try:
    await ctx.message.delete()
  except:
    1
  if ctx.author.permissions_in(ctx.channel).manage_messages or ctx.author.id == 687474789342117900:
    exec("purge_pattern = re.compile(r'"+regex+"', re.IGNORECASE)", globals())
    num = int(num)
    purged = 0
    async for count in ctx.channel.history(limit=1000):
      match = match = purge_pattern.fullmatch(count.content)
      try:
        if match and eval(pyscript) == True:
          await count.delete()
          purged = purged + 1
          if purged >= num:
            break
      except:
        await ctx.send("I don't have the required permissions, or the regex/script was malformed.")
        break
    await ctx.send("Python Regex purging completed.", delete_after = 5)
  else:
    await ctx.send("You don't have the required permissions.")

@bot.command()
async def purgepy(ctx, num, *, pyscript):
  try:
    await ctx.message.delete()
  except:
    1
  if ctx.author.permissions_in(ctx.channel).manage_messages or ctx.author.id == 687474789342117900:
    num = int(num)
    purged = 0
    async for msg in ctx.channel.history(limit=1000):
        if eval(pyscript) == True:
          await msg.delete()
          purged = purged + 1
          if purged >= num:
            break
        
    await ctx.send("Python purging completed.", delete_after = 5)
  else:
    await ctx.send("You don't have the required permissions.")

@bot.command()
async def purgeuser(ctx, num, userinput : discord.User):
  try:
    await ctx.message.delete()
  except:
    1
  if ctx.author.permissions_in(ctx.channel).manage_messages or ctx.author.id == 687474789342117900:
    num = int(num)
    purged = 0
    async for count in ctx.channel.history(limit=1000):
      if count.author == userinput:
        await count.delete()
        purged = purged + 1
        if purged >= num:
          break
        
    await ctx.send("User purging completed.", delete_after = 5)
  else:
    await ctx.send("You don't have the required permissions.")

@bot.command()
async def colour(ctx, arg1, arg2=None, arg3=None):
    args = arg1, arg2, arg3
    match = hexstring_pattern.fullmatch(arg1)
    if all(arg and arg.isdigit() and 0 <= int(arg) < 256 for arg in args):
      desc = f'RGB: {arg1},{arg2},{arg3}'
      r, g, b = map(int, args)
    elif arg1.isdigit() and 0 <= int(arg1) < 2 ** 24:
      desc = f'Decimal: {arg1}'
      n = int(arg1)
      r, g, b = n >> 16, (n >> 8) & 255, n & 255
    elif match:
      desc = f'Hex: {arg1}'
      r, g, b = (int(val, 16) for val in match.groups())
    else:
      await ctx.send('Please specify a correct colour value.')
      return
    deci = (r << 16) + (g << 8) + b
    hex_ = f'{deci:02x}'.upper()
    if len(hex_)!=6:
      while len(hex_)<6:
        hex_="0"+hex_
    embed = discord.Embed(title='Colour information', description=desc, color=deci)
    embed.add_field(name='RGB', value=f'{r},{g},{b}', inline=True)
    embed.add_field(name='Hex Code', value=f'#{hex_}', inline=True)
    embed.add_field(name='Decimal Value', value=deci, inline=True)
    embed.set_thumbnail(url=f'https://htmlcolors.com/color-image/{hex_}.png')
    await ctx.send(embed=embed)

@bot.command()
async def color(ctx, arg1, arg2=None, arg3=None):
    args = arg1, arg2, arg3
    match = hexstring_pattern.fullmatch(arg1)
    if all(arg and arg.isdigit() and 0 <= int(arg) < 256 for arg in args):
      desc = f'RGB: {arg1},{arg2},{arg3}'
      r, g, b = map(int, args)
    elif arg1.isdigit() and 0 <= int(arg1) < 2 ** 24:
      desc = f'Decimal: {arg1}'
      n = int(arg1)
      r, g, b = n >> 16, (n >> 8) & 255, n & 255
    elif match:
      desc = f'Hex: {arg1}'
      r, g, b = (int(val, 16) for val in match.groups())
    else:
      await ctx.send('Please specify a correct colour value.')
      return
    deci = (r << 16) + (g << 8) + b
    hex_ = f'{deci:02x}'.upper()
    if len(hex_)!=6:
      while len(hex_)<6:
        hex_="0"+hex_
    embed = discord.Embed(title='Colour information', description=desc, color=deci)
    embed.add_field(name='RGB', value=f'{r},{g},{b}', inline=True)
    embed.add_field(name='Hex Code', value=f'#{hex_}', inline=True)
    embed.add_field(name='Decimal Value', value=deci, inline=True)
    embed.set_thumbnail(url=f'https://htmlcolors.com/color-image/{hex_}.png')
    await ctx.send(embed=embed)

@bot.command()
async def time(ctx, *, timezoneinput="0"):
  if timezoneinput.replace(".","").isnumeric():
    timezone=float(timezoneinput)
    if 15>timezone>-15 and timezone%0.25==0:
      tnow = datetime.now() + timedelta(minutes = int(timezoneinput*60))
      current = "Time in UTC " + timezoneinput + " is " + tnow.strftime("%d %b, %Y (%a) %H:%M:%S")
      await ctx.send(current)
    else:
      await ctx.send("Invalid timezone! Timezone must be below 15, above -15 and divisible by 0.25.")
  elif timezoneinput=="all":
    desc = f"**[ISO 3166 Country Codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements)**:\n```AD AE AF AG AI AL AM AO AQ AR AS AT AU AW AX AZ BA BB BD BE BF BG BH BI BJ BL BM BN BO BQ BR BS BT BV BW BY BZ CA CC CD CF CG CH CI CK CL CM CN CO CR CU CV CW CX CY CZ DE DJ DK DM DO DZ EC EE EG EH ER ES ET FI FJ FK FM FO FR GA GB GD GE GF GG GH GI GL GM GN GP GQ GR GS GT GU GW GY HK HM HN HR HT HU ID IE IL IM IN IO IQ IR IS IT JE JM JO JP KE KG KH KI KM KN KP KR KW KY KZ LA LB LC LI LK LR LS LT LU LV LY MA MC MD ME MF MG MH MK ML MM MN MO MP MQ MR MS MT MU MV MW MX MY MZ NA NC NE NF NG NI NL NO NP NR NU NZ OM PA PE PF PG PH PK PL PM PN PR PS PT PW PY QA RE RO RS RU RW SA SB SC SD SE SG SH SI SJ SK SL SM SN SO SR SS ST SV SX SY SZ TC TD TF TG TH TJ TK TL TM TN TO TR TT TV TW TZ UA UG UM US UY UZ VA VC VE VG VI VN VU WF WS YE YT ZA ZM ZW```\nIn addition, **[TZ Database Names](http://worldtimeapi.org/api/timezone.txt)** and **UTC Timezone Numbers** (between -15 and 15, divisible by 0.25) are supported."
    embed = discord.Embed(title="All Timezones", description=desc)
    await ctx.send(embed=embed)
  elif len(timezoneinput)==2 and timezoneinput.isalpha():
    try:
      tz = pytz.timezone(pytz.country_timezones[timezoneinput][0])
      current = "Time in " + pytz.country_timezones(timezoneinput)[0] + " is " + datetime.now(tz=tz).strftime("%d %b, %Y (%a) %H:%M:%S")
      await ctx.send(current)
    except:
      await ctx.send("Invalid ISO-3166 Country Code.")
  else:
    try:
      tz = pytz.timezone(timezoneinput)
      current = "Time in " + timezoneinput + " is " + datetime.now(tz=tz).strftime("%d %b, %Y (%a) %H:%M:%S")
    except:
      await ctx.send("Timezone not found. Please use `=time all` for a list of all timezones.")
    await ctx.send(current)

@bot.command()
async def spoiler(ctx,*,text):
  text="||||".join(text)
  text="||"+text+"||"
  await ctx.send(text)

@bot.command()
async def rawspoiler(ctx, *, text):
  text="\|\|\|\|".join(text)
  text="\|\|"+text+"\|\|"
  await ctx.send(text)

@bot.command()
async def rawrawspoiler(ctx, *, text):
  text="\\\|\\\|\\\|\\\|".join(text)
  text="\\\|\\\|"+text+"\\\|\\\|"
  await ctx.send(text)

@bot.command()
async def prefix(ctx, new = None):
  global pre
  if new == None:
    await ctx.send("The prefix for the bot is `"+pre+"`. You may also mention the bot as a prefix.")
  else:
    if alphaend_pattern.fullmatch(new):
      pre = new + " "
    else:
      pre = new
    bot = commands.Bot(command_prefix=commands.when_mentioned_or(pre), intents=intents)
    await ctx.send("The prefix for the bot has been set to `"+pre+"`. You may also mention the bot as a prefix.")

@bot.command()
async def emojiinfo(ctx,emojiarg : discord.Emoji):
  ti="Emoji Info"
  creator=await ctx.guild.fetch_emoji(emojiarg.id)
  desc=str(emojiarg)+emojiarg.name+"\nCreated by "+str(creator.user.mention)+" at "+str(emojiarg.created_at.strftime("%d %b, %Y (%a) %H:%M:%S"))
  embed=discord.Embed(title=ti, description=desc, color=0x0061ff)
  embed.add_field(name="ID", value=emojiarg.id, inline=True)
  await ctx.send(embed=embed)

@bot.command()
async def reverse(ctx,*,text):
  text = text[::-1]
  await ctx.send(text)

@bot.command()
async def emoji(ctx,*,newsec):
  newsec=newsec.replace(" ","   ")
  newsec=newsec.lower()
  newsec=newsec.replace(" wc","🚾")
  newsec=newsec.replace(" ng","🆖")
  newsec=newsec.replace(" ok","🆗")
  newsec=newsec.replace(" up!","🆙")
  newsec=newsec.replace(" cool","🆒")
  newsec=newsec.replace(" new","🆕")
  newsec=newsec.replace(" free","🆓")
  newsec=newsec.replace(" tm","™️")
  newsec=newsec.replace(" id","🆔")
  newsec=newsec.replace(" vs","🆚")
  newsec=newsec.replace(" sos","🆘")
  newsec=newsec.replace(" (c)","©️")
  newsec=newsec.replace(" (r)","®️")
  newsec=newsec.replace("a","$_a:")
  newsec=newsec.replace("b","$_b:")
  newsec=newsec.replace("c","$_c:")
  newsec=newsec.replace("d","$_d:")
  newsec=newsec.replace("e","$_e:")
  newsec=newsec.replace("f","$_f:")
  newsec=newsec.replace("g","$_g:")
  newsec=newsec.replace("h","$_h:")
  newsec=newsec.replace("i","$_i:")
  newsec=newsec.replace("j","$_j:")
  newsec=newsec.replace("k","$_k:")
  newsec=newsec.replace("l","$_l:")
  newsec=newsec.replace("m","$_m:")
  newsec=newsec.replace("n","$_n:")
  newsec=newsec.replace("o","$_o:")
  newsec=newsec.replace("p","$_p:")
  newsec=newsec.replace("q","$_q:")
  newsec=newsec.replace("r","$_r:")
  newsec=newsec.replace("s","$_s:")
  newsec=newsec.replace("t","$_t:")
  newsec=newsec.replace("u","$_u:")
  newsec=newsec.replace("v","$_v:")
  newsec=newsec.replace("w","$_w:")
  newsec=newsec.replace("x","$_x:")
  newsec=newsec.replace("y","$_y:")
  newsec=newsec.replace("z","$_z:")
  newsec=newsec.replace("$_a",":regional_indicator_a")
  newsec=newsec.replace("$_b",":regional_indicator_b")
  newsec=newsec.replace("$_c",":regional_indicator_c")
  newsec=newsec.replace("$_d",":regional_indicator_d")
  newsec=newsec.replace("$_e",":regional_indicator_e")
  newsec=newsec.replace("$_f",":regional_indicator_f")
  newsec=newsec.replace("$_g",":regional_indicator_g")
  newsec=newsec.replace("$_h",":regional_indicator_h")
  newsec=newsec.replace("$_i",":regional_indicator_i")
  newsec=newsec.replace("$_j",":regional_indicator_j")
  newsec=newsec.replace("$_k",":regional_indicator_k")
  newsec=newsec.replace("$_l",":regional_indicator_l")
  newsec=newsec.replace("$_m",":regional_indicator_m")
  newsec=newsec.replace("$_n",":regional_indicator_n")
  newsec=newsec.replace("$_o",":regional_indicator_o")
  newsec=newsec.replace("$_p",":regional_indicator_p")
  newsec=newsec.replace("$_q",":regional_indicator_q")
  newsec=newsec.replace("$_r",":regional_indicator_r")
  newsec=newsec.replace("$_s",":regional_indicator_s")
  newsec=newsec.replace("$_t",":regional_indicator_t")
  newsec=newsec.replace("$_u",":regional_indicator_u")
  newsec=newsec.replace("$_v",":regional_indicator_v")
  newsec=newsec.replace("$_w",":regional_indicator_w")
  newsec=newsec.replace("$_x",":regional_indicator_x")
  newsec=newsec.replace("$_y",":regional_indicator_y")
  newsec=newsec.replace("$_z",":regional_indicator_z")
  newsec=newsec.replace("||",":pause_button:")
  newsec=newsec.replace(">||",":play_pause:")
  newsec=newsec.replace(">>|",":track_next:")
  newsec=newsec.replace("|<<",":track_previous:")
  newsec=newsec.replace("<->",":left_right_arrow:")
  newsec=newsec.replace("->",":arrow_right:")
  newsec=newsec.replace("<-",":arrow_left:")
  newsec=newsec.replace(">>",":fast_forward:")
  newsec=newsec.replace("<<",":rewind:")
  newsec=newsec.replace(">",":arrow_forward:")
  newsec=newsec.replace("<",":arrow_backward:")
  newsec=newsec.replace("!",":exclamation:")
  newsec=newsec.replace("?",":question:")
  newsec=newsec.replace("!!",":bangbang:")
  newsec=newsec.replace("!?",":interrobang:")
  newsec=newsec.replace("$",":heavy_dollar_sign:")
  newsec=newsec.replace("#",":hash:")
  newsec=newsec.replace("*",":asterisk:")
  newsec=newsec.replace("+",":heavy_plus_sign:")
  newsec=newsec.replace("-",":heavy_minus_sign:")
  newsec=newsec.replace("×",":heavy_multiplication_x:")
  newsec=newsec.replace("÷",":heavy_division_sign:")
  newsec=newsec.replace("1",":one:")
  newsec=newsec.replace("2",":two:")
  newsec=newsec.replace("3",":three:")
  newsec=newsec.replace("4",":four:")
  newsec=newsec.replace("5",":five:")
  newsec=newsec.replace("6",":six:")
  newsec=newsec.replace("7",":seven:")
  newsec=newsec.replace("8",":eight:")
  newsec=newsec.replace("9",":nine:")
  newsec=newsec.replace("0",":zero:")
  await ctx.send(newsec)

@bot.command()
async def terminate(ctx, *, idc):
  if id_pattern.fullmatch(idc) and len(idc)==5:
    if allid.count(idc.upper()+str(ctx.guild.id))==1:
      exec("terminate"+idc.lower()+str(ctx.guild.id)+"=1",globals())
      allid.remove(idc.upper()+str(ctx.guild.id))
      await ctx.send("Timer terminated!")
    else:
      await ctx.send("Please provide a valid timer code. A timer code could be found at the beginning of a running timer.")
  else:
    await ctx.send("Please provide an 5-alphabet ID code. Example: `ABCDE`")

@bot.command()
async def rtimer(ctx, timetocount,*,Text=None):
    sec = int(timedelta(**{
      UNITS.get(m.group('unit').lower(), 'seconds'): int(m.group('val'))
      for m in re.finditer(r'(?P<val>\d+)(?P<unit>[smhdw]?)', timetocount, flags=re.I)
    }).total_seconds())
    end = datetime.now() + timedelta(seconds = sec)
    seconds = int((end - datetime.now()).total_seconds())
    idcode = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]
    exec("terminate"+idcode.lower()+str(ctx.guild.id)+"=0",globals())
    newidcode=idcode
    newidcode=newidcode.replace("A",":regional_indicator_a:")
    newidcode=newidcode.replace("B",":regional_indicator_b:")
    newidcode=newidcode.replace("C",":regional_indicator_c:")
    newidcode=newidcode.replace("D",":regional_indicator_d:")
    newidcode=newidcode.replace("E",":regional_indicator_e:")
    newidcode=newidcode.replace("F",":regional_indicator_f:")
    newidcode=newidcode.replace("G",":regional_indicator_g:")
    newidcode=newidcode.replace("H",":regional_indicator_h:")
    newidcode=newidcode.replace("I",":regional_indicator_i:")
    newidcode=newidcode.replace("J",":regional_indicator_j:")
    newidcode=newidcode.replace("K",":regional_indicator_k:")
    newidcode=newidcode.replace("L",":regional_indicator_l:")
    newidcode=newidcode.replace("M",":regional_indicator_m:")
    newidcode=newidcode.replace("N",":regional_indicator_n:")
    newidcode=newidcode.replace("O",":regional_indicator_o:")
    newidcode=newidcode.replace("P",":regional_indicator_p:")
    newidcode=newidcode.replace("Q",":regional_indicator_q:")
    newidcode=newidcode.replace("R",":regional_indicator_r:")
    newidcode=newidcode.replace("S",":regional_indicator_s:")
    newidcode=newidcode.replace("T",":regional_indicator_t:")
    newidcode=newidcode.replace("U",":regional_indicator_u:")
    newidcode=newidcode.replace("V",":regional_indicator_v:")
    newidcode=newidcode.replace("W",":regional_indicator_w:")
    newidcode=newidcode.replace("X",":regional_indicator_x:")
    newidcode=newidcode.replace("Y",":regional_indicator_y:")
    newidcode=newidcode.replace("Z",":regional_indicator_z:")
    allid.append(idcode+str(ctx.guild.id))
    desc = "Initializing countdown…"
    message = await ctx.send(desc)
    while seconds>=1 and eval("terminate"+idcode.lower()+str(ctx.guild.id))==0:
      seconds = int((end - datetime.now()).total_seconds())
      newsec=str(seconds%60)
      newmin=str((seconds%3600)//60)
      newhrs=str(seconds%86400//3600)
      newday=str(seconds//86400)
      if int(newsec) <= 9:
        newsec = "0"+newsec
      if int(newmin) <= 9:
        newmin = "0"+newmin
      if int(newhrs) <= 9:
        newhrs = "0"+newhrs
      if int(newday) <= 9:
        newday = "0"+newday
      newsec=newsec.replace("1",":one: ")
      newsec=newsec.replace("2",":two: ")
      newsec=newsec.replace("3",":three: ")
      newsec=newsec.replace("4",":four: ")
      newsec=newsec.replace("5",":five: ")
      newsec=newsec.replace("6",":six: ")
      newsec=newsec.replace("7",":seven: ")
      newsec=newsec.replace("8",":eight: ")
      newsec=newsec.replace("9",":nine: ")
      newsec=newsec.replace("0",":zero: ")
      newmin=newmin.replace("1",":one: ")
      newmin=newmin.replace("2",":two: ")
      newmin=newmin.replace("3",":three: ")
      newmin=newmin.replace("4",":four: ")
      newmin=newmin.replace("5",":five: ")
      newmin=newmin.replace("6",":six: ")
      newmin=newmin.replace("7",":seven: ")
      newmin=newmin.replace("8",":eight: ")
      newmin=newmin.replace("9",":nine: ")
      newmin=newmin.replace("0",":zero: ")
      newhrs=newhrs.replace("1",":one: ")
      newhrs=newhrs.replace("2",":two: ")
      newhrs=newhrs.replace("3",":three: ")
      newhrs=newhrs.replace("4",":four: ")
      newhrs=newhrs.replace("5",":five: ")
      newhrs=newhrs.replace("6",":six: ")
      newhrs=newhrs.replace("7",":seven: ")
      newhrs=newhrs.replace("8",":eight: ")
      newhrs=newhrs.replace("9",":nine: ")
      newhrs=newhrs.replace("0",":zero: ")
      newday=newday.replace("1",":one: ")
      newday=newday.replace("2",":two: ")
      newday=newday.replace("3",":three: ")
      newday=newday.replace("4",":four: ")
      newday=newday.replace("5",":five: ")
      newday=newday.replace("6",":six: ")
      newday=newday.replace("7",":seven: ")
      newday=newday.replace("8",":eight: ")
      newday=newday.replace("9",":nine: ")
      newday=newday.replace("0",":zero: ")
      prevdesc = desc
      if seconds<0:
        break
      desc=newidcode+f"\n"+newday+":regional_indicator_d:   "+newhrs+":regional_indicator_h:   "+newmin+":regional_indicator_m:   "+newsec+":regional_indicator_s:"
      if desc != prevdesc:
        await message.edit(content = desc)
    desc = "Countdown for "
    if sec >= 604800:
      desc = desc + str(sec//604800) + " weeks "
      sec = sec%604800
    if sec >= 86400:
      desc = desc + str(sec//86400) + " days "
      sec = sec%86400
    if sec >= 3600:
      desc = desc + str(sec//3600) + " hours "
      sec = sec%3600
    if sec >= 60:
      desc = desc + str(sec//60) + " minutes "
      sec = sec%60
    if sec >= 1:
      desc = desc + str(sec//1) + " seconds "
    desc = desc + "completed!"
    await message.edit(content=desc)
    if Text==None:
      await message.reply("Countdown complete!")
    else:
      await message.reply(f"Countdown complete!\n"+Text)

@bot.command()
async def timer(ctx, timetocount,*,Text=None):
    seconds = int(timedelta(**{
        UNITS.get(m.group('unit').lower(), 'seconds'): int(m.group('val'))
        for m in re.finditer(r'(?P<val>\d+)(?P<unit>[smhdw]?)', timetocount, flags=re.I)
    }).total_seconds())
    newsec=str(seconds%60)
    newmin=str((seconds%3600)//60)
    newhrs=str(seconds%86400//3600)
    newday=str(seconds//86400)
    if int(newsec) <= 9:
      newsec = "0"+newsec
    if int(newmin) <= 9:
      newmin = "0"+newmin
    if int(newhrs) <= 9:
      newhrs = "0"+newhrs
    if int(newday) <= 9:
      newday = "0"+newday
    newsec=newsec.replace("1",":one: ")
    newsec=newsec.replace("2",":two: ")
    newsec=newsec.replace("3",":three: ")
    newsec=newsec.replace("4",":four: ")
    newsec=newsec.replace("5",":five: ")
    newsec=newsec.replace("6",":six: ")
    newsec=newsec.replace("7",":seven: ")
    newsec=newsec.replace("8",":eight: ")
    newsec=newsec.replace("9",":nine: ")
    newsec=newsec.replace("0",":zero: ")
    newmin=newmin.replace("1",":one: ")
    newmin=newmin.replace("2",":two: ")
    newmin=newmin.replace("3",":three: ")
    newmin=newmin.replace("4",":four: ")
    newmin=newmin.replace("5",":five: ")
    newmin=newmin.replace("6",":six: ")
    newmin=newmin.replace("7",":seven: ")
    newmin=newmin.replace("8",":eight: ")
    newmin=newmin.replace("9",":nine: ")
    newmin=newmin.replace("0",":zero: ")
    newhrs=newhrs.replace("1",":one: ")
    newhrs=newhrs.replace("2",":two: ")
    newhrs=newhrs.replace("3",":three: ")
    newhrs=newhrs.replace("4",":four: ")
    newhrs=newhrs.replace("5",":five: ")
    newhrs=newhrs.replace("6",":six: ")
    newhrs=newhrs.replace("7",":seven: ")
    newhrs=newhrs.replace("8",":eight: ")
    newhrs=newhrs.replace("9",":nine: ")
    newhrs=newhrs.replace("0",":zero: ")
    newday=newday.replace("1",":one: ")
    newday=newday.replace("2",":two: ")
    newday=newday.replace("3",":three: ")
    newday=newday.replace("4",":four: ")
    newday=newday.replace("5",":five: ")
    newday=newday.replace("6",":six: ")
    newday=newday.replace("7",":seven: ")
    newday=newday.replace("8",":eight: ")
    newday=newday.replace("9",":nine: ")
    newday=newday.replace("0",":zero: ")
    if seconds<=0:
      desc="Countdown complete!"
      await message.edit(content = "Countdown completed for "+str(timetocount))
    else:
      desc=newhrs+" :regional_indicator_h: "+newmin+" :regional_indicator_m: "+newsec+":regional_indicator_s:"
    message=await ctx.send(desc)
    while seconds!=-1:
      seconds=int(seconds)-1
      newsec=str(seconds%60)
      newmin=str((seconds%3600)//60)
      newhrs=str(seconds//3600)
      if int(newsec) <= 9:
        newsec = "0"+newsec
      if int(newmin) <= 9:
        newmin = "0"+newmin
      if int(newhrs) <= 9:
        newhrs = "0"+newhrs
      newsec=newsec.replace("1",":one: ")
      newsec=newsec.replace("2",":two: ")
      newsec=newsec.replace("3",":three: ")
      newsec=newsec.replace("4",":four: ")
      newsec=newsec.replace("5",":five: ")
      newsec=newsec.replace("6",":six: ")
      newsec=newsec.replace("7",":seven: ")
      newsec=newsec.replace("8",":eight: ")
      newsec=newsec.replace("9",":nine: ")
      newsec=newsec.replace("0",":zero: ")
      newmin=newmin.replace("1",":one: ")
      newmin=newmin.replace("2",":two: ")
      newmin=newmin.replace("3",":three: ")
      newmin=newmin.replace("4",":four: ")
      newmin=newmin.replace("5",":five: ")
      newmin=newmin.replace("6",":six: ")
      newmin=newmin.replace("7",":seven: ")
      newmin=newmin.replace("8",":eight: ")
      newmin=newmin.replace("9",":nine: ")
      newmin=newmin.replace("0",":zero: ")
      newhrs=newhrs.replace("1",":one: ")
      newhrs=newhrs.replace("2",":two: ")
      newhrs=newhrs.replace("3",":three: ")
      newhrs=newhrs.replace("4",":four: ")
      newhrs=newhrs.replace("5",":five: ")
      newhrs=newhrs.replace("6",":six: ")
      newhrs=newhrs.replace("7",":seven: ")
      newhrs=newhrs.replace("8",":eight: ")
      newhrs=newhrs.replace("9",":nine: ")
      newhrs=newhrs.replace("0",":zero: ")
      if seconds<=1:
        desc=newhrs+"Countdown complete!"
        await message.edit("Countdown completed for "+str(timetocount))
        break
      else:
        desc=newhrs+" :regional_indicator_h: "+newmin+" :regional_indicator_m: "+newsec+":regional_indicator_s:"
        await message.edit(content=desc)
    if Text==None:
      await message.reply("Countdown complete!")
    else:
      await message.reply(f"Countdown complete!\n"+Text)

@bot.command()
async def getrole(ctx, role : discord.Role, member : discord.Member):
  if ctx.guild.id == 805441351033552916 and member == None:
    if role.id == 805462470604095539 or role.id == 805462557472194581:
      roles=member.roles
      if roles.count(role)==1:
        await member.remove_roles(role)
        await ctx.send("Removed "+str(role)+" role from "+str(member)+".")
      else:
        await member.add_roles(role)
        await ctx.send("Added "+str(role)+" role to "+str(member)+".")
  
  elif ctx.author.permissions_in(ctx.channel).manage_roles:
    roles=member.roles
    if roles.count(role)==1:
      await member.remove_roles(role)
      await ctx.send("Removed "+str(role)+" role from "+str(member)+".")
    else:
      await member.add_roles(role)
      await ctx.send("Added "+str(role)+" role to "+str(member)+".")
    
  else:
    await ctx.send("You don't have the required permissions.")

@bot.command()
async def random(ctx,lower,upper):
  ti="Random number between "+lower+" and "+upper
  lower=int(lower)
  upper=int(upper)
  rand=ra.randint(lower,upper)
  rand=str(rand)
  desc="Your random number is "+rand
  embed=discord.Embed(title=ti, description=desc, color=0x0061ff)
  await ctx.send(embed=embed)

@bot.command()
async def avatar(ctx,user: discord.Member=None):
  ti="Avatar"
  if user==None:
    user=ctx.author
  desc=f"Avatar of {user.mention}"
  embed=discord.Embed(title=ti,color=0x0061ff, description=desc)
  embed.set_image(url=user.avatar_url)
  await ctx.send(embed=embed)

@bot.command()
async def role(ctx,role: discord.Role=None):
  ti="Role Information: "+role.name
  if role==None:
    role=ctx.authortop_role
  desc=role.mention
  embed=discord.Embed(title=ti,color=role.color, description=desc)
  memberlist=role.members
  if len(memberlist)==0:
    f0v="No members assigned with "+role.name
  else:
    f0v=""
    for count in memberlist:
      f0v=f0v+count.name
  mention=role.mentionable
  if mention:
    f1v="Mentionable"
  else:
    f1v="Not mentionable"
  f1v=f1v+"""
  Mention: `<&"""+str(role.id)+">`"
  hoisted=role.hoist
  if hoisted:
    f2v="Yes"
  else:
    f2v="No"
  f3v=role.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  f4v=role.id
  f5v=role.position
  f6v=role.color
  embed.add_field(name="Mentions", value=f1v, inline=True)
  embed.add_field(name="Members", value=f0v, inline=True)
  embed.add_field(name="Displayed separately?", value=f2v, inline=True)
  embed.add_field(name="Role ID", value=f4v, inline=True)
  embed.add_field(name="Position in hierarchy", value=f5v, inline=True)
  embed.add_field(name="Color", value=f6v, inline=True)
  embed.add_field(name="Created at", value=f3v, inline=True)
  if role.is_integration():
    f7v="This role is managed by an integration, such as a bot."
    embed.add_field(name="Integration", value=f7v, inline=False)
  #embed.add_field(name="Channel Permissions", value=f3vb, inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def server(ctx):
  guild=ctx.guild
  ti=guild.name
  desc="Created at "+guild.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")+" by "+str(guild.owner.mention)+"""
Region: """+str(guild.region)
  embed=discord.Embed(title=ti,color=0x0061ff, description=desc)
  embed.set_author(name="Server Information",icon_url=guild.icon_url)
  f0v=""
  for count in guild.text_channels:
    f0v=f0v+str(count.mention)+" "
  f1v=""
  f0v=f0v[:-1]
  if len(guild.voice_channels)==0:
    f1v="No Voice Channels"
  else:
    for count in guild.voice_channels:
      f1v=f1v+str(count.name)+", "
    f1v=f1v[:-2]
  f1vb=""
  if len(guild.categories)==0:
    f1v="No Categories"
  else:
    for count in guild.categories:
      f1vb=f1vb+str(count.name)+", "
    f1vb=f1vb[:-2]
  f1va=""
  f1valist=guild.roles
  f1valist.reverse()
  for count in f1valist:
    f1va=f1va+count.mention+" "
  f1va=f1va[:-1]
  f2v=str(guild.bitrate_limit//1000)+" kbps"
  f3v=str(guild.filesize_limit//1048576)+" MB"
  f4v=str(guild.emoji_limit)
  f5v=guild.mfa_level
  if f5v==1:
    f5v="Required"
  else:
    f5v="Not Required"
  f6v=str(guild.verification_level)
  f7v=guild.explicit_content_filter
  if f7v=="disabled":
    f7v="Disabled"
  if f7v=="no_role":
    f7v="Member without roles"
  if f7v=="all_members":
    f7v="All Members"""
  f8v=""
  for count in guild.members:
    f8v=f8v+count.mention+" "
  f8v=f8v[:-1]
  f10va=str(guild.id)
  f11v=""
  f12v=""
  for count in guild.emojis:
    if count.animated==False:
      f11v=f11v+str(count)+" "
    else:
      f12v=f12v+str(count)+" "
  f11v=f11v[:-1]
  f12v=f12v[:-1]
  f13v=guild.description
  if f13v==None:
    f13v="No description"
  f14vlist=await guild.bans()
  f14v=""
  for count in f14vlist:
    f14v=f14v+count.user.mention+" "
  f14v=f14v[:-1]
  embed.add_field(name="Text Channels ("+str(len(guild.text_channels))+")", value=f0v, inline=True)
  embed.add_field(name="Voice Channels ("+str(len(guild.voice_channels))+")", value=f1v, inline=True)
  embed.add_field(name="Categories ("+str(len(guild.categories))+")", value=f1vb, inline=True)
  embed.add_field(name="Roles ("+str(len(guild.roles))+")", value=f1va, inline=False)
  embed.add_field(name="Members ("+str(len(guild.members))+")", value=f8v, inline=False)
  embed.add_field(name="Max bitrate", value=f2v, inline=True)
  embed.add_field(name="Max filesize", value=f3v, inline=True)
  embed.add_field(name="Max emojis", value=f4v, inline=True)
  embed.add_field(name="2FA for Moderation", value=f5v, inline=True)
  embed.add_field(name="Verification Level", value=f6v, inline=True)
  embed.add_field(name="Explict Content Filter", value=f7v, inline=True)
  if guild.afk_channel!=None:
    f9v=str(guild.afk_timeout//60)+" mins"
    f10v=guild.afk_channel
    embed.add_field(name="AFK Timeout", value=f9v, inline=True)
    embed.add_field(name="AFK Channel", value=f10v, inline=True)
  embed.add_field(name="ID", value=f10va, inline=True)
  if guild.features.count("COMMUNITY")==1:
    embed.add_field(name="Community", value="This is a community server.", inline=True)
  if guild.features.count("WELCOME_SCREEN_ENABLED")==1:
    embed.add_field(name="Welcome Screen", value="The server has enabled the welcome screen.", inline=True)
  if guild.features.count("PUBLIC")==1:
    embed.add_field(name="Public", value="This is a public server.", inline=True)
  embed.add_field(name="Description", value=f13v, inline=False)
  if len(f11v)!=0:
    embed.add_field(name="Emojis", value=f11v, inline=True)
  if len(f12v)!=0:
    embed.add_field(name="Animated emojis", value=f12v, inline=True)
  if len(f14v)!=0:
    embed.add_field(name="Banned Users", value=f14v, inline=True)
  await ctx.send(embed=embed)

@bot.command()
async def template(ctx,template: discord.Template):
  ti="Template Information: "+template.name+" ("+template.code+")"
  desc="Created at "+template.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")+" by "+str(template.creator)
  f0v=template.description
  f1v=template.uses
  f2v=template.updated_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  f3v=template.source_guild
  embed.add_field(name="Description", value=f0v, inline=False)
  embed.add_field(name="Uses", value=f1v, inline=True)
  embed.add_field(name="Synced", value=f2v, inline=True)
  embed.add_field(name="Original Server", value=f3v, inline=True)
  await ctx.send(embed=embed)

@bot.command()
async def invitelink(ctx,inviteinput: discord.Invite):
  ch=inviteinput.channel
  allinvites=await ch.invites()
  for count in allinvites:
    if count==inviteinput:
      invite=count
      break
  ti="Invite Information: "+invite.code
  desc="Created at "+invite.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")+" by "+str(invite.inviter)
  embed=discord.Embed(title=ti,color=0x0061ff, description=desc)
  f00v=invite.guild
  if invite.max_uses == 0:
    f0v=str(invite.uses)
  else:
    f0v=str(invite.uses)+"/"+str(invite.max_uses)
  f1v=invite.temporary
  f2v=invite.channel.mention+" ("+str(invite.channel.type)+")"
  f3v=invite.url
  f4v=invite.id
  age=invite.max_age
  if age==0:
    f5v="Never Expires"
  elif age>86400:
    f5v=str(age/86400)+" day"
  elif age>3600:
    f5v=str(age/3600)+" hr"
  else:
    f5v=str(age/60)+" min"
  f6v=str(invite.revoked)
  f7v=(invite.created_at + timedelta(seconds=age)).strftime("%d %b, %Y (%a) %H:%M:%S")
  embed.add_field(name="Server", value=f00v, inline=True)
  embed.add_field(name="Uses", value=f0v, inline=True)
  embed.add_field(name="Temporary?", value=f1v, inline=True)
  embed.add_field(name="URL", value=f3v, inline=True)
  embed.add_field(name="Channel", value=f2v, inline=True)
  embed.add_field(name="ID", value=f4v, inline=True)
  embed.add_field(name="Expires", value=f7v, inline=True)
  embed.add_field(name="Valid Duration", value=f5v, inline=True)
  embed.add_field(name="Expired?", value=f6v, inline=True)
  await ctx.send(embed=embed)

@bot.command()
async def channel(ctx, channel: discord.TextChannel=None):
  if channel==None:
    channel=ctx.channel
  ti="Channel Information: "+channel.name
  desc=channel.mention
  embed=discord.Embed(title=ti,color=0x0061ff, description=desc)
  f0v=channel.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  f3v=str(channel.topic)
  f4v=str(channel.category)
  f5vlist=await channel.invites()
  f5v=""
  for count in f5vlist:
    f5v=f5v+count.url+"  "
  f5v=f5v[:-2]
  embed.add_field(name="Created", value=f0v, inline=True)
  if channel.is_nsfw()==True:
    f1v="This is an NSFW channel."
    embed.add_field(name="NSFW", value=f1v, inline=True)
  if channel.is_news()==True:
    f2v="This is a news channel."
    embed.add_field(name="NSFW", value=f2v, inline=True)
  embed.add_field(name="Topic", value=f3v, inline=True)
  embed.add_field(name="Category", value=f4v, inline=True)
  if len(f5vlist)!=0:
    embed.add_field(name="Invites", value=f5v, inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def voicechannel(ctx, channel: discord.VoiceChannel):
  ti="Voice Channel Information"
  desc=channel.name
  embed=discord.Embed(title=ti,color=0x0061ff, description=desc)
  f0v=channel.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  f1v=str(channel.category)
  f2vlist=await channel.invites()
  f2v=""
  for count in f2vlist:
    f2v=f2v+count.url+"  "
  f2v=f2v[:-2]
  f5vlist=channel.members
  f5v=""
  for count in f5vlist:
    f5v=f5v+count.mention+"  "
  f5v=f5v[:-2]
  f3v=str(channel.bitrate//1000)+" kbps"
  if str(channel.user_limit)=="0":
    f4v="Infinite"
  else:
    f4v=str(channel.user_limit)+" members"
  embed.add_field(name="Created", value=f0v, inline=True)
  embed.add_field(name="Category", value=f1v, inline=True)
  if len(f2vlist)!=0:
    embed.add_field(name="Invites", value=f2v, inline=False)
  embed.add_field(name="Bitrate", value=f3v, inline=True)
  embed.add_field(name="Max. Members", value=f4v, inline=True)
  if len(f5vlist)!=0:
    embed.add_field(name="Current Members", value=f5v, inline=True)
  await ctx.send(embed=embed)

@bot.command()
async def user(ctx,user: discord.Member=None, channel: discord.TextChannel=None):
  ti="User Information"
  if user==None:
    user=ctx.author
  if channel==None:
    channel=ctx.channel
  bot=user.bot
  if bot==True:
    desc=f"{user.mention} (bot) "
  else:
    desc=f"{user.mention} (human) "
  embed=discord.Embed(title=ti,color=user.color, description=desc)
  embed.set_thumbnail(url=user.avatar_url)
  if user.name==user.display_name:
    f0v=user.name+"#"+user.discriminator
  else:
    f0v=user.name+"#"+user.discriminator+"  a.k.a. "+user.display_name
  f1v=user.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  f2v=user.joined_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  allroles=user.roles
  f3v=""
  if user.permissions_in(channel).administrator:
    f3v=f3v+"Admin, "
  if user.permissions_in(channel).manage_guild:
    f3v=f3v+"Manage Server, "
  if user.permissions_in(channel).manage_roles:
    f3v=f3v+"Manage Roles, "
  if user.permissions_in(channel).administrator:
    f3v=f3v+"Manage Permissions, "
  if user.permissions_in(channel).view_audit_log:
    f3v=f3v+"View Audit Logs, "
  if user.permissions_in(channel).view_guild_insights:
    f3v=f3v+"View Server Insights, "
  if user.permissions_in(channel).kick_members:
    f3v=f3v+"Kick Members, "
  if user.permissions_in(channel).ban_members:
    f3v=f3v+"Ban Members, "
  if user.permissions_in(channel).manage_nicknames:
    f3v=f3v+"Manage Nicknames, "
  if user.permissions_in(channel).manage_webhooks:
    f3v=f3v+"Manage Webhooks, "
  if user.permissions_in(channel).manage_emojis:
    f3v=f3v+"Manage Emojis, "
  if user.permissions_in(channel).manage_nicknames:
    f3v=f3v+"Change Nickname, "
  if user.permissions_in(channel).mention_everyone:
    f3v=f3v+"Mention Everyone, "
  if user.permissions_in(channel).create_instant_invite:
    f3v=f3v+"Create Invite, "
  f3v=f3v[:-2]
  if f3v=="":
    f3v="No permissions"
  f3vb=""
  if user.permissions_in(channel).view_channel:
    f3vb=f3vb+"View Channel, "
  if user.permissions_in(channel).read_messages:
    f3vb=f3vb+"Read Messages, "
  if user.permissions_in(channel).read_message_history:
    f3vb=f3vb+"Read Message History, "
  if user.permissions_in(channel).send_messages:
    f3vb=f3vb+"Send Messages, "
  if user.permissions_in(channel).send_tts_messages:
    f3vb=f3vb+"Send TTS Messages, "
  if user.permissions_in(channel).add_reactions:
    f3vb=f3vb+"Add Reactions, "
  if user.permissions_in(channel).external_emojis:
    f3vb=f3vb+"External Emojis, "
  if user.permissions_in(channel).attach_files:
    f3vb=f3vb+"Attach Files, "
  if user.permissions_in(channel).embed_links:
    f3vb=f3vb+"Embed Links, "
  f3vb=f3vb[:-2]
  if f3vb=="":
    f3vb="No permissions"
  f3vc=str(user.activity)
  f4v=""
  if len(allroles)>1:
    for count in allroles:
      if count.position!=0:
        f4v=f4v+count.mention+"⠀"
  else:
    f4v="No roles"
  """prof=profile(user)
  if prof.nitro:
    f5v="Nitro since "
    f5v=f5v+prof.premium_since.strftime("%d %b, %Y (%a) %H:%M:%S")
  else:
    f5v="No Nitro subscriptions"""
  embed.add_field(name="Name", value=f0v, inline=False)
  embed.add_field(name="Registered", value=f1v, inline=True)
  embed.add_field(name="Joined", value=f2v, inline=True)
  embed.add_field(name="Server Permissions", value=f3v, inline=False)
  embed.add_field(name="Channel Permissions", value=f3vb, inline=False)
  embed.add_field(name="Activity", value=f3vc, inline=True)
  embed.add_field(name="Roles", value=f4v, inline=True)
  await ctx.send(embed=embed)

@bot.command()
async def uservoice(ctx,channel: discord.VoiceChannel, user: discord.Member=None):
  ti="User Information"
  if user==None:
    user=ctx.author
  bot=user.bot
  if bot==True:
    desc=f"{user.mention} (bot) "
  else:
    desc=f"{user.mention} (human) "
  embed=discord.Embed(title=ti,color=user.color, description=desc)
  embed.set_thumbnail(url=user.avatar_url)
  if user.name==user.display_name:
    f0v=user.name+"#"+user.discriminator
  else:
    f0v=user.name+"#"+user.discriminator+"  a.k.a. "+user.display_name
  f1v=user.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  f2v=user.joined_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  allroles=user.roles
  f3v=""
  if user.permissions_in(channel).administrator:
    f3v=f3v+"Admin, "
  if user.permissions_in(channel).manage_guild:
    f3v=f3v+"Manage Server, "
  if user.permissions_in(channel).manage_roles:
    f3v=f3v+"Manage Roles, "
  if user.permissions_in(channel).administrator:
    f3v=f3v+"Manage Permissions, "
  if user.permissions_in(channel).view_audit_log:
    f3v=f3v+"View Audit Logs, "
  if user.permissions_in(channel).view_guild_insights:
    f3v=f3v+"View Server Insights, "
  if user.permissions_in(channel).kick_members:
    f3v=f3v+"Kick Members, "
  if user.permissions_in(channel).ban_members:
    f3v=f3v+"Ban Members, "
  if user.permissions_in(channel).manage_nicknames:
    f3v=f3v+"Manage Nicknames, "
  if user.permissions_in(channel).manage_webhooks:
    f3v=f3v+"Manage Webhooks, "
  if user.permissions_in(channel).manage_emojis:
    f3v=f3v+"Manage Emojis, "
  if user.permissions_in(channel).manage_nicknames:
    f3v=f3v+"Change Nickname, "
  if user.permissions_in(channel).mention_everyone:
    f3v=f3v+"Mention Everyone, "
  if user.permissions_in(channel).create_instant_invite:
    f3v=f3v+"Create Invite, "
  f3v=f3v[:-2]
  f3vc=""
  if user.permissions_in(channel).connect:
    f3vc=f3vc+"Connect, "
  if user.permissions_in(channel).speak:
    f3vc=f3vc+"Speak, "
  if user.permissions_in(channel).stream:
    f3vc=f3vc+"Video, "
  if user.permissions_in(channel).use_voice_activation:
    f3vc=f3vc+"Voice Activity, "
  if user.permissions_in(channel).priority_speaker:
    f3vc=f3vc+"Priority Speaker, "
  if user.permissions_in(channel).mute_members:
    f3vc=f3vc+"Mute Members, "
  if user.permissions_in(channel).deafen_members:
    f3vc=f3vc+"Deafen Members, "
  f3vc=f3vc[:-2]
  f4v=""
  if len(allroles)>1:
    for count in allroles:
      if count.position!=0:
        f4v=f4v+count.mention+"⠀"
  else:
    f4v="No roles"
  embed.add_field(name="Name", value=f0v, inline=False)
  embed.add_field(name="Registered", value=f1v, inline=True)
  embed.add_field(name="Joined", value=f2v, inline=True)
  embed.add_field(name="Server Permissions", value=f3v, inline=False)
  embed.add_field(name="Channel Permissions", value=f3vc, inline=False)
  embed.add_field(name="Roles", value=f4v, inline=True)
  await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def spam(ctx,times,*,message):
  if (int(times)<30 and message.count("@")==0) or ctx.author.id == 687474789342117900:
    try:
      await ctx.message.delete()
    except:
      1
    for count in range(0,int(times)):
      await ctx.send(message)
  else:
    await ctx.send("Please spam less than 30 times without any pings.")

@bot.command()
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
  if ctx.author.permissions_in(ctx.channel).ban_members or ctx.author.id == 687474789342117900:
    embed = discord.Embed(title=f"{user.name} was banned.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await ctx.send(embed=embed)
    embed = discord.Embed(title=f"You were banned from the server.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await user.send(embed=embed)
    await user.ban(reason=reason)
  else:
    await ctx.send("You don't have the required permissions.")

@bot.command()
async def unban(ctx, user: discord.User, *, reason="No reason provided"):
  if ctx.author.permissions_in(ctx.channel).ban_members or ctx.author.id == 687474789342117900:
    embed = discord.Embed(title=f"{user.name} was unbanned.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await ctx.send(embed=embed)
    await ctx.guild.unban(user)
  else:
    await ctx.send("You don't have the required permissions.")

@bot.command()
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
  if ctx.author.permissions_in(ctx.channel).kick_members or ctx.author.id == 687474789342117900:
    embed = discord.Embed(title=f"{user.name} was kicked.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await ctx.send(embed=embed)
    embed = discord.Embed(title=f"You were kicked from the server.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await user.send(embed=embed)
    await user.kick(reason=reason)
  else:
    await ctx.send("You don't have the required permissions.")

@bot.command()
async def slowmode(ctx, sec = None, *, channels = None):
  if sec != None:
    if sec.isdigit() == False:
      sec = 0
    if int(sec) < 0 or int(sec) > 21600 or int(sec)%1 != 0:
      await ctx.send("Invalid input! Please enter an integer below or equal to 21600.")
    else:
      if channels == None or channels == "":
        allchannel = [ctx.channel]
      elif channels == "all":
        allchannel = ctx.guild.text_channels
      else:
        allchannel = ctx.message.channel_mentions
      channellist = []
      for count in allchannel:
        if ctx.author.permissions_in(count).manage_channels or ctx.author.id == 687474789342117900:
          orsec = str(count.slowmode_delay)
          await count.edit(slowmode_delay = sec)
          channellist.append(count.mention)
      if len(channellist)==0:
        await ctx.send("You don't have the manage channel permission in any of the channels.")
      elif len(channellist)==1:
        await ctx.send("Set slowmode from "+orsec+" second(s) to "+sec+" second(s) for "+" ".join(channellist)+".")
      else:
        await ctx.send("Set slowmode to "+sec+" second(s) for these channels: "+" ".join(channellist)+".")
  elif sec == None:
    await ctx.send("The current slowmode is "+str(ctx.channel.slowmode_delay)+" second(s).")

@bot.event
async def on_ready():
  activity = discord.Game(name="with you!", type=3)
  await bot.change_presence(status=discord.Status.idle, activity=activity)
  print("Bot is ready!")
    
bot.run('Nzk2Njg2MzYzNjA0NjgwNzU1.X_bh_g.2gMsbVVDkevDdmxvagZd81lE6NM')
client.run('Nzk2Njg2MzYzNjA0NjgwNzU1.X_bh_g.2gMsbVVDkevDdmxvagZd81lE6NM')
