import discord
from discord.ext import commands
import random as ra
import time as tm
from datetime import datetime, date, timedelta
from discord_webhook import DiscordWebhook
from discord.ext.commands import *
from discord import Webhook, RequestsWebhookAdapter
import aiohttp
from math import *
from cmath import *
import numpy as np
import re
import pytesseract
import requests
import PIL
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from pdf2image import convert_from_path
import imgkit
import pytube
from pygoogletranslation import Translator
import wikipedia

hexstring_pattern = re.compile(r'#?([0-9A-F]{2})([0-9A-F]{2})([0-9A-F]{2})', re.IGNORECASE)
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or("="), intents=intents)
client = discord.Client()
bot.remove_command('help')
typer=0
autodel=None

class MyClient(discord.Client):
  async def on_ready(self):
    print('Connected!')

@bot.event
async def on_reaction_add(reaction, user):
  lang = reaction.emoji.replace("flag_","")
  await reaction.message.channel.send(lang)
  if len(lang)==2:
    translator = Translator(to_lang=lang)
    translation = translator.translate(reaction.message.content)
    await reaction.message.channel.send(translation)

@bot.event
async def on_member_update(before, after):
  desc="Profile of "+before.mention+" was updated!"
  embed = discord.Embed(title="Profile update", description=desc, color=after.color)
  if before.status != after.status:
    embed.add_field(name="Status before", value=before.status, inline=False)
    embed.add_field(name="Status after", value=after.status, inline=False)
  """if before.activity != after.activity:
    embed.add_field(name="Activity before", value=before.activity.name, inline=False)
    embed.add_field(name="Activity after", value=after.activity.name, inline=False)"""
    #embed.add_field(name="Activity state", value=after.activity.state, inline=True)
    #embed.set_thumbnail(url=activity.large_image_url)
  if before.nick != after.nick:
    embed.add_field(name="Nickname before", value=before.nick, inline=False)
    embed.add_field(name="Nickname after", value=after.nick, inline=False)
  if before.roles != after.roles:
    br=""
    ar=""
    for count in before.roles:
      br=br+count.mention+" "
    br=br[:-1]
    for count in after.roles:
      ar=ar+count.mention+" "
    ar=ar[:-1]
    embed.add_field(name="Roles before", value=br, inline=False)
    embed.add_field(name="Roles after", value=ar, inline=False)
  embed.set_thumbnail(url=after.avatar_url)
  sendto = bot.get_channel(797989308023832607)
  if after.name!="NQN":
    await sendto.send(embed=embed)

@bot.event
async def on_member_join(member):
  desc="Welcome, "+member.mention+"! Wish you a pleasure time in the server."
  embed = discord.Embed(title="Welcome", description=desc)
  sendto = bot.get_channel(796624935606026241)
  await sendto.send(embed=embed)

@bot.event
async def on_message_delete(message):
  desc="Message deleted in "+message.channel.mention+f"\n"+message.content
  embed = discord.Embed(title="Message Deleted", description=desc)
  sendto = bot.get_channel(797989308023832607)
  await sendto.send(embed=embed)

@bot.event
async def on_message_edit(before, after):
  desc="Message edited in "+before.channel.mention+f"\n [Jump!]("+after.jump_url+")"
  embed = discord.Embed(title="Message Edited", description=desc)
  embed.add_field(name="Before", value=before.content, inline=False)
  embed.add_field(name="After", value=after.content, inline=False)
  sendto = bot.get_channel(797989308023832607)
  if len(before.content)!=0 and len(after.content)!=0:
    await sendto.send(embed=embed)

@bot.event
async def on_guild_role_create(role):
  desc=role.mention+" was created."
  embed = discord.Embed(title="New role created!", description=desc)
  sendto = bot.get_channel(797989308023832607)
  await sendto.send(embed=embed)

@bot.event
async def on_guild_role_delete(role):
  desc=role.mention+" was deleted."
  embed = discord.Embed(title="Role deleted!", description=desc, color=role.color)
  sendto = bot.get_channel(797989308023832607)
  await sendto.send(embed=embed)

"""@bot.event
async def on_typing(channel, user, when):
  desc=user.mention+" started typing in "+channel.mention+" at "+when.strftime("%d %b, %Y (%a) %H:%M:%S")
  embed = discord.Embed(title="Typing!", description=desc, color=user.color)
  sendto = bot.get_channel(797989308023832607)
  await sendto.send(embed=embed)"""

@bot.event
async def on_user_update(before, after):
  desc="Profile of "+before.mention+" was updated!"
  embed = discord.Embed(title="Profile update", description=desc)
  if before.avatar != after.avatar:
    embed.add_field(name="Avatar before", value="[click]("+str(before.avatar_url)+")", inline=False)
    embed.set_thumbnail(url=before.avatar_url)
    embed.add_field(name="Avatar after", value="[click]("+str(after.avatar_url)+")", inline=False)
  """if before.discriminator != after.discriminator:
    embed.add_field(name="Discriminator before", value="#"+before.discriminator, inline=False)
    embed.add_field(name="Discriminator after", value="#"+after.discriminator, inline=False)"""
  if before.name != after.name:
    embed.add_field(name="Username before", value=before.name, inline=False)
    embed.add_field(name="Username after", value=after.name, inline=False)
  embed.set_thumbnail(url=after.avatar_url)
  sendto = bot.get_channel(797989308023832607)
  await sendto.send(embed=embed)

@bot.command()
async def help(ctx,cat=None):
  if cat!=None:
    cat=cat.lower()
  ti="Commands: Tunnelers' Abyss"
  if cat=="ta":
    desc="""
  **admins**
  Show admins of the server.
  **Alias:** `=administrators`
  
  **mods**
  Show mods of the server.
  **Alias:** `=moderators`
  
  **gsmrl**
  Shows information about GSMRL.
  
  **tttl**
  Shows information about TTTL.
  """
  elif cat=="admins":
    ti="Admins"
    desc="""**=admins**
  Show admins of the server.
  **Alias:** `=administrators`"""
  elif cat=="admins":
    ti="Admins"
    desc="""**=admins**
  Show admins of the server.
  **Alias:** `=administrators`"""
  else:
    ti="Tunnelers' Bot Help"
    desc="""
  Prefix: =
  
  Commands available:
  `admins` `emoji` `gsmrl` `kick` `mods` `random` `reverse` `role` `spam` `spoiler` `time` `timer` `tttl`
  """
  embed=discord.Embed(title=ti, description=desc, color=0x0061ff)
  await ctx.send(embed=embed)

@bot.command()
async def translate(ctx, lang, *, text):
  msg = await ctx.send("**Translating** "+text+" **to** "+lang)
  translatorvar = Translator()
  translation = translatorvar.translate(text, dest='en')
  await msg.edit(content = "**Translation to "+lang+f":**\n"+translation)

@bot.command()
async def status(ctx, member : discord.Member = None):
  if member==None:
    member=ctx.author
  if member.is_on_mobile==True:
    desc = str(member.status)+" on mobile"
  else:
    desc = str(member.status)+" on desktop"
  embed = discord.Embed(title="Status: "+member.name, description=desc)
  #await ctx.send(str(member.activities))
  for count in member.activities:
    #await ctx.send(str(count)+"  "+str(count.type))
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
async def define(ctx, function, definition, *, argumentsraw = ""):
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
async def calc(ctx,*,arg):
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
    splitted=arg.split("=")
    for count in splitted:
      if count.isalpha()==True:
        lcls = globals()
        exec(count+'='+splitted[len(splitted)-1], globals(), lcls)
    await ctx.message.add_reaction("👍")
  else:
    await ctx.send("Invalid input, please try again.")

@bot.command()
async def ping(ctx):
  now1 = datetime.now()
  message = await ctx.send("Pong!")
  mcs = str((datetime.now() - now1).microseconds)
  await message.edit(content="Pong! "+mcs+" microseconds")

@bot.command()
async def speedtest(ctx):
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
async def screenshot(ctx, url):
  try:
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.set_window_size(1440,900)
    driver.get_screenshot_as_file('web_screenshot1.png')
    await ctx.send(file=discord.File('web_screenshot1.png'))
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height'))
    driver.find_element_by_tag_name('body').screenshot('web_screenshot2.png')
    driver.quit()
    await ctx.send(file=discord.File('web_screenshot2.png'))
    os.remove('web_screenshot1.png')
    os.remove('web_screenshot2.png')
  except:
    await ctx.send("The URL was invalid, or the webpage is too long.")

@bot.command()
async def ocr(ctx):
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
async def text(ctx):
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
  if code == None:
    r = requests.get(ctx.message.attachments[0].url, stream=True)
    r.raise_for_status()
    r.raw.decode_content = True
    code = r.content
  imgkit.from_string(code, 'output.jpg')
  await ctx.send(file=discord.File('output.jpg'))
  os.remove('output.jpg')

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
async def wiki(ctx, *, query):
  wikipedia.set_lang("en")
  desc = wikipedia.summary(query)
  if len(desc)>2048:
    desc = desc[0:2046]+"…"
  embed = discord.Embed(title=query, description=desc)
  page = wikipedia.page(title=query, auto_suggest=True, redirect=True, preload=False)
  print(str(page.sections))
  for count in page.sections:
    embed.add_field(name=count, value=wikipeida.section(count)[:500], inline=False)
  if len(page.images)!=0:
    embed.set_thumbnail(url = page.images[0])
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
  tm.sleep(3)
  member=ctx.guild.get_member(796686363604680755)
  await message.remove_reaction(emoji, member)

@bot.command(pass_context=True)
async def pretend(ctx, member : discord.Member, *, message):
  await ctx.message.delete()
  async with aiohttp.ClientSession() as session:
    webhook = Webhook.partial(797029335424434186, 'op96Pi7p-F4mGNWPUbMW5iKwUiQ1tPU_1p-9CkcVpzfrXLYhRMK6E--C0s1rG76BtX9m', adapter=RequestsWebhookAdapter())
  await webhook.send(message, username=member.name, avatar_url=member.avatar_url)

@bot.command(pass_context=True)
async def pretendembed(ctx, member : discord.Member, *, text):
  await ctx.message.delete()
  async with aiohttp.ClientSession() as session:
    webhook = Webhook.partial(797029335424434186, 'op96Pi7p-F4mGNWPUbMW5iKwUiQ1tPU_1p-9CkcVpzfrXLYhRMK6E--C0s1rG76BtX9m', adapter=RequestsWebhookAdapter())
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
  await ctx.send(embed=embed)
  

@bot.command()
async def insert(ctx,emoji,*,text):
  text=text.replace(" "," "+emoji+" ")
  await ctx.send(text)

@bot.command()
async def purge(ctx,num):
  num=int(num)
  await ctx.channel.purge(limit=num+1)

"""@bot.command()
async def autodelete(ctx,num=None):
  global autodel
  isnum=num.isnumeric()
  if isnum:
    autodel=int(num)
    await ctx.send("Autodelete has been set to "+str(autodel)+" seconds.")
  else:
    autodel=None
    await ctx.send("Autodelete has been disabled.")"""
  
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
async def time(ctx,timezoneinput="0"):
  timezone=float(timezoneinput)
  if timezone>-15 and timezone<15:
    now = datetime.now()
    h = now.strftime("%H")
    m = now.strftime("%M")
    h = float(h)+timezone//1-8
    m = timezone%1*60
    if h>=24:
      h=h-24
    if h<0:
      h=h+24
    hdis=str(int(h))
    if int(h)<10:
      hdis="0"+hdis
    mdis=str(int(m))
    if int(m)<10:
      mdis="0"+mdis
    current = "Time in UTC " + timezoneinput + " is `" + now.strftime(hdis+" : "+mdis+" : %S") + "`"
    await ctx.send(current)
  else:
    await ctx.send("Invalid timezone. Please try again.")

@bot.command()
async def spoiler(ctx,*,text):
  text="||||".join(text)
  text="||"+text+"||"
  await ctx.send(text)

@bot.command()
async def getprefix(bot, message):
    extras = await prefixes_for(message.guild) # returns a list
    return commands.when_mentioned_or(*extras)(bot, message)

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
  newsec=newsec.replace("a","$_a: ")
  newsec=newsec.replace("b","$_b: ")
  newsec=newsec.replace("c","$_c: ")
  newsec=newsec.replace("d","$_d: ")
  newsec=newsec.replace("e","$_e: ")
  newsec=newsec.replace("f","$_f: ")
  newsec=newsec.replace("g","$_g: ")
  newsec=newsec.replace("h","$_h: ")
  newsec=newsec.replace("i","$_i: ")
  newsec=newsec.replace("j","$_j: ")
  newsec=newsec.replace("k","$_k: ")
  newsec=newsec.replace("l","$_l: ")
  newsec=newsec.replace("m","$_m: ")
  newsec=newsec.replace("n","$_n: ")
  newsec=newsec.replace("o","$_o: ")
  newsec=newsec.replace("p","$_p: ")
  newsec=newsec.replace("q","$_q: ")
  newsec=newsec.replace("r","$_r: ")
  newsec=newsec.replace("s","$_s: ")
  newsec=newsec.replace("t","$_t: ")
  newsec=newsec.replace("u","$_u: ")
  newsec=newsec.replace("v","$_v: ")
  newsec=newsec.replace("w","$_w: ")
  newsec=newsec.replace("x","$_x: ")
  newsec=newsec.replace("y","$_y: ")
  newsec=newsec.replace("z","$_z: ")
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
  newsec=newsec.replace("!",":exclamation:")
  newsec=newsec.replace("$",":heavy_dollar_sign:")
  newsec=newsec.replace("?",":question:")
  newsec=newsec.replace("#",":hash:")
  newsec=newsec.replace("*",":asterisk:")
  newsec=newsec.replace("+",":heavy_plus_sign:")
  newsec=newsec.replace("-",":heavy_minus_sign:")
  newsec=newsec.replace("×",":heavy_multiplication_x:")
  newsec=newsec.replace("÷",":heavy_division_sign:")
  await ctx.send(newsec)

@bot.command()
async def timer(ctx,seconds,*,Text=None):
  newsec=seconds
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

  if seconds=="1":
    desc=newsec+"second left"
  else:
    desc=newsec+"seconds left"
  message=await ctx.send(desc)
  seconds=str(int(seconds)-1)
  while seconds!="0":
    tm.sleep(0.8)
    newsec=seconds
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
    if seconds=="1":
      desc=newsec+"second left"
    else:
      desc=newsec+"seconds left"
    await message.edit(content=desc)
    seconds=str(int(seconds)-1)
  if Text==None:
    await message.reply("Countdown complete!")
  else:
        await message.reply("Countdown complete! "+Text)


@bot.command()
async def getrole(ctx, member : discord.Member, role : discord.Role):
    
    roles=member.roles
    if roles.count(role)==1:
      await member.remove_roles(role)
      await ctx.send("Removed "+str(role)+" from "+str(member)+".")
    else:
      await member.add_roles(role)
      await ctx.send("Added "+str(role)+" to "+str(member)+".")

@bot.command()
async def admins(ctx):
  embed=discord.Embed(title="Administrators", description="Admins on this server: Hume2, CalebJ, Coram.", color=0x0061ff)
  await ctx.send(embed=embed)

@bot.command()
async def administrators(ctx):
  embed=discord.Embed(title="Administrators", description="Admins on this server: Hume2, CalebJ, Coram.", color=0x0061ff)
  await ctx.send(embed=embed)

@bot.command()
async def mods(ctx):
  embed=discord.Embed(title="Moderators", description="Mods on this server: Josselin, sivarajan, Sokomine, onePlayer, Vikthor", color=0x0061ff)
  await ctx.send(embed=embed)

@bot.command()
async def moderators(ctx):
  embed=discord.Embed(title="Moderators", description="Mods on this server: Josselin, sivarajan, Sokomine, onePlayer, Vikthor", color=0x0061ff)
  await ctx.send(embed=embed)

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
async def invite(ctx,inviteinput: discord.Invite):
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
  f0v=str(invite.uses)+"/"+str(invite.max_uses)
  f1v=invite.temporary
  f2v=invite.channel.mention+" ("+str(invite.channel.type)+")"
  f3v=invite.url
  f4v=invite.id
  age=invite.max_age
  if age==0:
    f5v="Never Expires"
  elif age<60:
    f5v=str(age)+" secs"
  elif age>3600:
    f5v=str(age/3600)+" hrs"
  else:
    f5v=str(age/60)+" mins"
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
  if user.permissions_in(ctx.channel).administrator:
    f3v=f3v+"Admin, "
  if user.permissions_in(ctx.channel).manage_guild:
    f3v=f3v+"Manage Server, "
  if user.permissions_in(ctx.channel).manage_roles:
    f3v=f3v+"Manage Roles, "
  if user.permissions_in(ctx.channel).administrator:
    f3v=f3v+"Manage Permissions, "
  if user.permissions_in(ctx.channel).view_audit_log:
    f3v=f3v+"View Audit Logs, "
  if user.permissions_in(ctx.channel).view_guild_insights:
    f3v=f3v+"View Server Insights, "
  if user.permissions_in(ctx.channel).kick_members:
    f3v=f3v+"Kick Members, "
  if user.permissions_in(ctx.channel).ban_members:
    f3v=f3v+"Ban Members, "
  if user.permissions_in(ctx.channel).manage_nicknames:
    f3v=f3v+"Manage Nicknames, "
  if user.permissions_in(ctx.channel).manage_webhooks:
    f3v=f3v+"Manage Webhooks, "
  if user.permissions_in(ctx.channel).manage_emojis:
    f3v=f3v+"Manage Emojis, "
  if user.permissions_in(ctx.channel).manage_nicknames:
    f3v=f3v+"Change Nickname, "
  if user.permissions_in(ctx.channel).mention_everyone:
    f3v=f3v+"Mention Everyone, "
  if user.permissions_in(ctx.channel).create_instant_invite:
    f3v=f3v+"Create Invite, "
  f3v=f3v[:-2]
  if f3v=="":
    f3v="No permissions"
  f3vb=""
  if user.permissions_in(ctx.channel).view_channel:
    f3vb=f3vb+"View Channel, "
  if user.permissions_in(ctx.channel).read_messages:
    f3vb=f3vb+"Read Messages, "
  if user.permissions_in(ctx.channel).read_message_history:
    f3vb=f3vb+"Read Message History, "
  if user.permissions_in(ctx.channel).send_messages:
    f3vb=f3vb+"Send Messages, "
  if user.permissions_in(ctx.channel).send_tts_messages:
    f3vb=f3vb+"Send TTS Messages, "
  if user.permissions_in(ctx.channel).add_reactions:
    f3vb=f3vb+"Add Reactions, "
  if user.permissions_in(ctx.channel).external_emojis:
    f3vb=f3vb+"External Emojis, "
  if user.permissions_in(ctx.channel).attach_files:
    f3vb=f3vb+"Attach Files, "
  if user.permissions_in(ctx.channel).embed_links:
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
  #embed.add_field(name="Nitro", value=f5v, inline=True)
  #embed.add_field(name="User", value=f6v, inline=True)
  #embed.add_field(name="", value=f7v, inline=True)
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
  if int(times)<30 and message.count("@")==0:
    await ctx.message.delete()
    for count in range(0,int(times)):
      await ctx.send(message)
  else:
    await ctx.send("Please spam less than 30 times without any pings.")

@bot.command()
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
  await user.ban(reason=reason)
  embed = discord.Embed(title=f"{user.name} was banned.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
  sendto = bot.get_channel(796721534676762664)
  await sendto.send(embed=embed)
  embed = discord.Embed(title=f"You were banned from the server.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
  await user.send(embed=embed)

@bot.command()
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
  await user.kick(reason=reason)
  embed = discord.Embed(title=f"{user.name} was kicked.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
  sendto = bot.get_channel(796721534676762664)
  await sendto.send(embed=embed)
  embed = discord.Embed(title=f"You were kicked from the server.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
  await user.send(embed=embed)

@bot.command()
async def gsmrl(ctx):
  ti="Grapeyard Superb Metro Rail Line (GSMRL)"
  desc="Basically Trains in Tunneler's Abyss(TA) is managed by TTTL (Tunneler's Train Transist Limited) project but, in Grapeyard Superb trains are managed by Grapeyard Superb Metro Train Limited(GSMRL) project. These projects are under taken by sivarajan and Hume2. Railway is essential part when it comes to traveling around TA."
  f1v="""Samson and Delilah. Laurel and Hardy. Holmes and Watson. Cheese and cucumber. These names could hardly fit together more naturally than Hume2 and Sivarajan, the latter the owner of the GSMRL company, the former his mentor and inspiration. GSMRL is by far the largest metro network in the Tunnelers' Abyss.
The first line, opened on October 12th 2019 by Hume2, connected the iconic Castle of Glass with Grapeyard Harbor. The indomitable duo opened a second line on November 22nd, and a third (the Narsh Express) on December 3rd.
On December 29th, and with generous assistance from InitialD and ModiJi, the fourth and fifth lines were revealed. Sivarajan constructed a sixth line (with ModiJi) on January 26th, 2020, a seventh line (with balancedAct) on April 10th, and an eighth assisted by tomracer and ShivTiwari on June 10th.
Sivarajan proclaims that this Herculean effort is far from complete. None less than the famous Sokomine, is currently occupied in constructing a Mountain Line."""
  embed=discord.Embed(title=ti,color=0x0061ff, url="https://h2mm.gitlab.io/web/rail.html", description=desc)
  embed.add_field(name="Story", value=f1v, inline=False)
  embed.set_image(url="https://h2mm.gitlab.io/web/screenshots/cog.jpg")
  await ctx.send(embed=embed)

@bot.command()
async def tttl(ctx):
  ti="Tunneler's Train Transist Limited (TTTL)"
  desc="Basically Trains in Tunneler's Abyss(TA) is managed by TTTL (Tunneler's Train Transist Limited) project but, in Grapeyard Superb trains are managed by Grapeyard Superb Metro Train Limited(GSMRL) project. These projects are under taken by sivarajan and Hume2. Railway is essential part when it comes to traveling around TA."
  f1v="""It was a bright spring morning when three weary travellers, refugees fleeing persecution in a faraway land, arrived at the dazzling natural spectacle we now know as Spawn, and decided to call it home.
These intrepid explorers - let us drink a toast to their names! Hume2, hip hip hurrah! CalebJ, hip hip hurrah! Coram, hip hip hurrah! - these intrepid explorers cared little for the basic comforts of life. Whereas lesser men would have occupied themselves in a search for food or shelter, it is said that our heroes spent the famous morning constructing the first railway platform.
Hume2 was quickly distracted by some bushes which produced berries exclusively in prime numbers, but CalebJ and Coram pressed on, hewing a tunnel through the mountains with their bare hands."""

  f2v="""Dreaming of a mighty train line stretching all the way to the far north, they discovered (to their dismay) that Spawn was surrounded by ocean in most directions. After tossing a coin, the track was extended to the west, where they found that Hume2, having decided that the prime number bushes were just a miraculous coincidence, had built a little wooden house. Thus, the town of Fractal Plains was born.
History does not record the names of the passengers on the first train journey to Fractal Plains, but it appears that on departure from Spawn, they all received a complimentary box of bananas."""

  f3v="""We are so used to modern technology, and trains that effortlessly pilot themselves from destination to destination, that it is difficult to imagine how primitive the early train network was. Stories abound of how CalebJ would trot in front of the moving train, waving a big red flag and yelling raucously, while Coram would wander up and down the line, sweeping away fallen apples and leaves with a big broom. This ad-hoc system was known as "Apple Tree Curtailment", or ATC (Automatic Train Control)for short. (In yet another coincidence, the modern system is also called ATC.)
It wasn't long before the competition was heating up. The existing line was extended as far as Red Erosion, while Hume2 began building a new line to the south(dragon Forest)
Hume2 was even more fiercely dedicated to Pure Logic than the original, and soon interlocking technology had been discovered, allowing trains to use the full length of the existing line, and effectively merging the two double tracks into one (the current S2 line)."""

  f4v="""Work soon began on new lines: a second line to Red Erosion, passing through Lava Oasis (S4), and another to the slightly mysterious Thorviss Farm, stopping at several even more mysterious locations (S5).
Around this date, the first train map appeared. Josselin has frequently claimed that a crack team of cartographers work long into the night to keep it updated, but occasional reports suggest the whole thing has been put together in MS Paint.
As news arrived of an idyllic settlement in the east, Grapeyard Superb, work on the celebrated Abyssal Express (S1) line commenced almost immediately. The area attracted an eclectic mix of builders, and soon the town (later re-classified as a city) was expanding rapidly. Meanwhile, the S2 line was extended all the way to Cody Island, this work apparently motivated by a desire for easier access to coconuts."""

  f5v="""With passenger numbers rising ever higher, a third line from Red Erosion was built, this time extending to the far north and stopping at Desert Trap (S3). In the opposite direction, the S1 line was re-routed to the far south, terminating at the world-famous invisible cliffs at Southern Cliff.
October 12th, 2019 was the date of the founding of the Grapeyard Superb metro (GSMRL). Its visionary chief engineer, Sivarajan, dreamed of uniting the disparate settlements along the Sakura Plains into one grand metropolis. Today his vision stands enacted as a metro system encompassing nearly thirty stations. Not content with that feat, Sivarajan and Hume2 established a settlement even further to the east. Narsh, or Legendria, can today be reached via the Narsh Express (R1) line."""

  f6v="""The existing line to Southern Cliff hugged the eastern side of the Poisson Mountains. An additional line (S6) was established along the western side. To help coordinate the construction efforts, Hume2 and Sivarajan built the TA Train transit office in Grapeyard. Around March 2020, the Abyssal Express was extended to Exfactor. Soon afterwards, the brand new S15 line connected little-explored territories between Coram Beach and Green Shore.
By April, and besieged by a mountain of passenger complaints, the decision was taken to re-name and re-number several lines. The trains themselves were modernised to more clearly show their line numbers and destinations. Alas, thrill-seeking passengers were still not entirely satisfied, so in July the average train speed across the network was greatly increased. R1 had been extended to Crystal Farm by Hume2, and the new R2 line was built to connect the charming seaside town of Will Beach with the rest of civilisation, later terminating at End of File station near Narsh."""

  f7v="""The newest line in the Tunnelers' Abyss is the S8, whose grand opening was the 28th September, 2020.Basically Trains in Tunneler's Abyss(TA) is managed by TTTL (Tunneler's Train Transist Limited) project but, in Grapeyard Superb trains are managed by Grapeyard Superb Metro Train Limited(GSMRL) project. These projects are under taken by sivarajan and Hume2. Railway is essential part when it comes to traveling around TA."""
  embed=discord.Embed(title=ti,color=0x0061ff, url="https://h2mm.gitlab.io/web/rail.html", description=desc)
  embed.add_field(name="Story", value=f1v, inline=False)
  embed.add_field(name="⠀", value=f2v, inline=False)
  embed.add_field(name="⠀", value=f3v, inline=False)
  embed.add_field(name="⠀", value=f4v, inline=False)
  embed.add_field(name="⠀", value=f5v, inline=False)
  embed.add_field(name="⠀", value=f6v, inline=False)
  embed.add_field(name="⠀", value=f7v, inline=False)
  embed.set_image(url="https://h2mm.gitlab.io/web/screenshots/trainoffice.png")
  await ctx.send(embed=embed)


@bot.event
async def on_ready():
  activity = discord.Game(name="with TA members", type=3)
  await bot.change_presence(status=discord.Status.idle, activity=activity)
  print("Bot is ready!")
    
bot.run('Nzk2Njg2MzYzNjA0NjgwNzU1.X_bh_g.6zgjj1lIyYLkdyZkF1oc673_0HM')
client.run('Nzk2Njg2MzYzNjA0NjgwNzU1.X_bh_g.6zgjj1lIyYLkdyZkF1oc673_0HM')
