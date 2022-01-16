import asyncio
import json
import math
import os
import random as ra
import re
import sys
import traceback
import typing
from datetime import datetime, timedelta, timezone
from difflib import SequenceMatcher

import emojis as ems
import folium
import matplotlib as mpl
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import selenium
from bs4 import BeautifulSoup
from markdown2 import Markdown
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import sys
import os
sys.path.append(os.path.abspath('./modules'))
import requests
import nextcord as discord
from nextcord import Embed, Permissions
from nextcord.enums import VoiceRegion
from nextcord.ext import commands
import discord_ui as ui

bot_ = commands.Bot(command_prefix=commands.when_mentioned_or("="),intents=discord.Intents.all(),
                    allowed_mentions=discord.AllowedMentions(everyone=False, users=True,
                    roles=False, replied_user=False), case_insensitive=True, strip_after_prefix=True)
bu = ui.UI(bot_)

f = open('./assets/database.json', 'r')
db = json.loads(f.read())
f.close()

plt.style.use('mpl.mplstyle')

youtube_headers={'cookie':"""SID=CghejA2ZNiG3ffH-ea-xuLc9tIaHBbwGapD38onoVwAzAbkHnjoZtpUhHdUAmcNRJO
HTDw.; __Secure-1PSID=CghejA2ZNiG3ffH-ea-xuLc9tIaHBbwGapD38onoVwAzAbkHEoE3S8JEj0cM-biiWZLVyA.;__Sec
ure-3PSID=CghejA2ZNiG3ffH-ea-xuLc9tIaHBbwGapD38onoVwAzAbkH4sXzfbXVlttnq4TjWVCEfg.; HSID=A-m2IhioZ3o
eerjgh; SSID=AbaPAqttHYjZqyPhz; APISID=tPPnfzostQvEsOd-/ALcV81KVGrbqB4Igh; SAPISID=ClVhEot1sUk0cUo-
/AEEQ1aXT00mYUmE7f; __Secure-1PAPISID=ClVhEot1sUk0cUo-/AEEQ1aXT00mYUmE7f; __Secure-3PAPISID=ClVhEot
1sUk0cUo-/AEEQ1aXT00mYUmE7f; YSC=33OC1x1sBQc; …:QUQ3MjNmenRqWWtfNkdJSGRkbkhLQkJVVHN0a1lkVE41ajhsTzR
TTk9RLURmN2FCN1hkZ1JOTGMzYXAxdi1HS3p1NUxFMFRFeXcyVE84Rlg5LWZVRTNNOThHM0RLTDZBQzZucDQ4a0R0VURzYUtOZE
dtOGJDSUoxRktjckg0QTAxd3JwTGNybzJQYTBUN1c5bUo5NVAxVXNtV2JRNjlmdjZJajg3ZC1MQy1rMGZrcWtkQTFXTmlUcUdYe
kpEbHRwYmU1YkpILXl6Tmx5RDI5RnJueDN4czRkdXliUzNFd2FUZw==; SIDCC=AJi4QfF-hT3IbtAsSfRNu4EviRtD9WBBt481
66pXbGGDIX2wN5n4luQgHUDSmwX-WSozfHfc; __Secure-3PSIDCC=AJi4QfFRxCGcdkA1zU8EIyJ7kPmscvGPk9vdyN5QWKwe
Sv4jI-xcXxr8GtSt2loCC7scCGMS; PREF=f4=4000000&tz=Asia.Hong_Kong""".replace(f"\n", "")}

func            =lambda pct,allvals: "{:d} ({:.1f}%)".format(int(pct/100*np.sum(allvals)), round(pct, 1))
botadmin        =lambda context    : context.author.id in db['botadmins']
number_to_emoji =lambda a          : a.replace("1",":one: ").replace("2",":two: ").replace("3",":three: ").replace("4",":four: ").replace("5",":five: ").replace("6",":six: ").replace("7",":seven: ").replace("8",":eight: ").replace("9",":nine: ").replace("0",":zero: ")
sizer           =lambda bytes      : f"{round(bytes,4):,} Bytes" if bytes<1024 else (f"{round(bytes/1024,4):,}KB" if bytes<1048576 else (f"{round(bytes/1048576,4):,}MB" if bytes<1073741824 else f"{round(bytes/1073741824,4):,}GB"))
sizer2          =lambda bytes      : f"{str(round(bytes,4)).zfill(9)} Bytes" if bytes<1024 else (f"{str(round(bytes/1024,4)).zfill(9)}KB" if bytes<1048576 else (f"{str(round(bytes/1048576,4)).zfill(9)}MB" if bytes<1073741824 else f"{round(bytes/1073741824,4):,}GB"))
format_abr      =lambda stream     : f"{stream.__getattribute__('abr')}\t" if stream.__getattribute__("abr") else 'No audio'
format_length   =lambda secs       : f"{secs//86400} days plus {str(secs%21600//3600).zfill(2)}:{str(secs%3600//60).zfill(2)}:{str(secs%60).zfill(2)}" if secs >= 86400 else (f"{str(secs//3600).zfill(2)}:{str(secs%3600//60).zfill(2)}:{str(secs%60).zfill(2)}" if secs >= 3600 else f"{str(secs//60).zfill(2)}:{str(secs%60).zfill(2)}")
format_video    =lambda stream     : f"{format_abr(stream)}\t{stream.resolution}\t{format_fps(stream)}\t{sizer2(stream.filesize)}\t{stream.url}"
specialbool     =lambda input      : input.lower() in ["1", "ok", "yes", "ye", "y", "yeah", "enable", "on", "enabled", "tic", "true", "up", "positive", "+"]
has_perms       =lambda ch,mem,prm : (ch.permissions_for(mem).value  & 1 << prm) or (ch.permissions_for(mem).value  & 1 << 8) or mem.id in db["botadmins"]
naiveness       =lambda dt         : "Naive" if (dt.tzinfo is None or dt.tzinfo.utcoffset(dt) is None) else "Not Naive"
chance          =lambda ratio      : ra.randint(1, ratio) == ratio
unix_timestamp  =lambda dt,flag="F": f"<t:{round(datetime.timestamp(dt))}:{flag}>"
time_display    =lambda dt         : dt.strftime("%A, %d %b %Y, %H:%M:%S")
st_nd_th_format =lambda n          : "st" if str(n).endswith("1") and not str(n).endswith("11") else ("th" if str(n).endswith("2") and not str(n).endswith("12") else "nd")
perm_display    =lambda integer, x : "<:pt:932171999936135168><:tr:932189462648209468> " if integer & (1 << x) else "<:px:912206780015190038><:tr:932189462648209468> "
permission_messages={}

forecast_formatter = """
"""

def format_fps(stream):
  try:
    return stream.fps
  except:
    return 'No vid.'

def try_delete(*filenames):
  for x in filenames:
    try:
      os.remove(x)
    except:
      pass

def try_delete_message(msg):
  try:
    msg.delete()
  except:
    pass

def voice_region_format(region):
  if not region: return "Auto"
  if region == VoiceRegion.amsterdam  : return "Amsterdam"
  if region == VoiceRegion.brazil     : return "Brazil"
  if region == VoiceRegion.dubai      : return "Dubai"
  if region == VoiceRegion.eu_central : return "Europe (Central)"
  if region == VoiceRegion.eu_west    : return "Europe (West)"
  if region == VoiceRegion.europe     : return "Europe"
  if region == VoiceRegion.frankfurt  : return "Frankfurt"
  if region == VoiceRegion.hongkong   : return "Hong Kong"
  if region == VoiceRegion.india      : return "India"
  if region == VoiceRegion.japan      : return "Japan"
  if region == VoiceRegion.london     : return "London"
  if region == VoiceRegion.russia     : return "Russia"
  if region == VoiceRegion.singapore  : return "Singapore"
  if region == VoiceRegion.southafrica: return "South Africa"
  if region == VoiceRegion.south_korea: return "South Korea"
  if region == VoiceRegion.sydney     : return "Sydney"
  if region == VoiceRegion.us_central : return "USA (Central)"
  if region == VoiceRegion.us_east    : return "USA (East)"
  if region == VoiceRegion.us_south   : return "USA (South)"
  if region == VoiceRegion.us_west    : return "USA (West)"
  if region == VoiceRegion.vip_amsterdam: return "Amsterdam (VIP)"
  if region == VoiceRegion.vip_us_east  : return "USA (East) (VIP)"
  if region == VoiceRegion.vip_us_west  : return "USA (West) (VIP)"
  return "An error occured."

verify_pattern = re.compile(r'[^ ⠀][\s\S]{0,30}?[^ ⠀]#?[\d]{4}(,|, | )?[\d+\-*/×÷%xyz()\[\]\{\}]{1,50}=[\d+\-*/×÷%xyz()\[\]\{\}]{1,50}(,|, | )?[\S ]{3,20}(,|, | )?(Red|Orange|Yellow|Green|Light( |_)?Green|Dark( |_)?Green|Cyan|Blue|Light( |_)?Blue|Dark( |_)?Blue|Purple|Pink|Brown)', re.IGNORECASE)
id_pattern = re.compile(r'([A-Z]{5})', re.IGNORECASE)
poll_pattern = re.compile(r'([\w]+?)(:\w{1,32}:|[\uD800-\uDBFF])')
UNITS = {'s':'seconds', 'm':'minutes', 'h':'hours', 'd':'days', 'w':'weeks'}
view_overwrite = discord.PermissionOverwrite()
view_overwrite.view_channel = True
clickers = {}
vclients={}
timestamp_pattern = re.compile(r'<t:-?[\d]{1,13}(:[FfDdTtR])?>')

#clicker_button = ui.Button(style=discord.ButtonStyle.primary, row=0, custom_id="clicker", label="Click me!")

custom_permissions = {
  # Tens of digits            4         3         2         1         0
  "admin"     : Permissions(0b00000000000000000000000000000000000001000),
  "semiadmin" : Permissions(0b11111111111111111111111111111111111110111),
  "mod"       : Permissions(0b11111110011101111111111111111111011100011),
  "manager"   : Permissions(466255085123),
  "speaker"   : Permissions(414598024897),
  "member"    : Permissions(414568664129),
  "semimember": Permissions(277129449025),
  "restrict"  : Permissions(274914675777),
  "mute"      : Permissions(67175425),
  "freeze"    : Permissions(66560),
  "none"      : Permissions(0),
}

server_real = {
  3 : "Administrator",
  33: "Manage Events",
  10: "View Channels",
  4 : "Manage Channels",
  28: "Manage Roles",
  30: "Manage Emojis and Stickers",
  7 : "View Audit Logs",
  19: "View Server Insights",
  29: "Manage Webhooks",
  5 : "Manage Server"
}

membership_real = {
  0 : "Create Invites",
  26: "Change Nickname",
  27: "Manage Nicknames",
  1 : "Kick Members",
  2 : "Ban Members",
  40: "Timeout Members"
}

text_channel_real = {
  11: "Send Messages",
  38: "Send Messages in Threads",
  35: "Create Public Threads",
  36: "Create Private Threads",
  14: "Embed Links",
  15: "Attach Files",
  6 : "Add Reactions",
  18: "Use External Emojis",
  37: "Use External Stickers",
  17: "Mention Everyone",
  13: "Manage Messages",
  34: "Manage Threads",
  16: "Read Message History",
  12: "Send TTS Messages",
  31: "Use Application Commands"
}

voice_channel_real = {
  20: "Connect to Voice",
  21: "Speak (Audio)",
  9 : "Stream (Video)",
  39: "Start Activities",
  25: "Use Voice Activity",
  8 : "Priority Speaker",
  22: "Mute Members",
  23: "Deafen Members",
  24: "Move Members",
  32: "Request to Speak"
}

badges_real = {
  0 : "Staff (Discord Employee)",
  1 : "Partnered Server Owner",
  2 : "HypeSquad Events member",
  9 : "Early Supporter",
  10: "Team User",
  3 : "Bug Hunter (Level 1)",
  14: "Bug Hunter (Level 2)",
  12: "System User",
  17: "Early Verified Bot Developer",
  16: "Verified Bot",
  6 : "HypeSquad Bravery House",
  7 : "HypeSquad Brilliance House",
  8 : "HypeSquad Balance House"
}

# Integer TO Permission Utilities
# Comma-separated permission items - e.g. "Administrator, Manage Channels, Manage Roles"
def badges_itop(integer: int):
  x = (", ".join([y for x,y in badges_real.items() if integer & (1 << x)]))
  return x if x else "No badges"
def server_itop(integer: int):
  x = (", ".join([y for x,y in server_real.items() if integer & (1 << x)]))
  return x if x else "No server permissions"
def ms_itop(integer: int):
  x = (", ".join([y for x,y in membership_real.items() if integer & (1 << x)]))
  return x if x else "No membership permissions"
def tc_itop(integer: int):
  x = (", ".join([y for x,y in text_channel_real.items() if integer & (1 << x)]))
  return x if x else "No text channel permissions"
def vc_itop(integer: int):
  x = (", ".join([y for x,y in voice_channel_real.items() if integer & (1 << x)]))
  return x if x else "No voice channel permissions"

# Integer TO Discord Display Utilities
# All permissions with :pt: or :pf: emoji from SuperBot Support
server_itod = lambda integer: f"\n".join([perm_display(integer, x) + y for x,y in server_real.items()])
ms_itod = lambda integer: f"\n".join([perm_display(integer, x) + y for x,y in membership_real.items()])
tc_itod = lambda integer: f"\n".join([perm_display(integer, x) + y for x,y in text_channel_real.items()])
vc_itod = lambda integer: f"\n".join([perm_display(integer, x) + y for x,y in voice_channel_real.items()])
