from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from discord import Webhook, RequestsWebhookAdapter
from datetime import datetime, date, timedelta
from selenium.webdriver.common.by import By
from pygoogletranslation import Translator
from discord_webhook import DiscordWebhook
import matplotlib.pyplot as plt
from pdf2image import convert_from_path
from PIL import ImageDraw, ImageFilter
from PyDictionary import PyDictionary
from discord.ext.commands import *
import selenium.common.exceptions
from discord.ext import commands
from selenium import webdriver
from markdown2 import Markdown
from pnglatex import pnglatex
from bs4 import BeautifulSoup
from cmath import *
import random as ra
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
import pytube
import pytz
import PIL
import re
import os
banned_ids = []
banned_text = []
bot_admins = [687474789342117900]
file = open("program.py", "x")
set(pytz.all_timezones_set)
dictionary=PyDictionary()
allid=[]
hexstring_pattern = re.compile(r'#?([0-9A-F]{2})([0-9A-F]{2})([0-9A-F]{2})', re.IGNORECASE)
id_pattern = re.compile(r'([A-Z]{5})', re.IGNORECASE)
alphaend_pattern = re.compile(r'.*[a-z]', re.IGNORECASE)
python_pattern = re.compile(r'^\`\`\`(py|python)?\n[\s\S]*\`\`\`$')
html_pattern = re.compile(r'^\`\`\`(html)?\n[\s\S]*\`\`\`$')
md_pattern = re.compile(r'^\`\`\`(md|markdown)?\n[\s\S]*\`\`\`$')
UNITS = {'s':'seconds', 'm':'minutes', 'h':'hours', 'd':'days', 'w':'weeks'}
typer=0
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
markdowner = Markdown(extras=["strike", "footnotes"])
cmaphsv = plt.cm.hsv
wikipedia.set_lang("en")
def is_me(msg):
  return msg.author == client.user
def func(pct, allvals):
  absolute = int(pct/100*np.sum(allvals))
  return "{:d} ({:.1f}%)".format(absolute, pct)

from botcontrol import *
from botbasic import *
from botwebscrape import *
from botengrave import *

@bot.command()
async def botpurge(ctx, *, num):
  try:
    await ctx.message.delete()
  except:
    1
  if ctx.author.permissions_in(ctx.channel).manage_messages or bot_admins.count(ctx.author.id)!=0:
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
async def pie(ctx, title, numbers, labels):
  numlist = []
  for count in numbers.split(","):
    numlist.append(int(count))
  y = np.array(numlist)
  mycolors = []
  if len(labels) > len(numlist):
    labels = labels[:len(numlist)-1]
  elif len(numlist) > len(labels):
    numlist = numlist[:len(labels)-1]
  for count in range(0, len(numlist)):
    mycolors.append(cmaphsv(count/len(numlist)))
  plt.pie(y, labels = labels.split(","), colors=mycolors, autopct=lambda pct: func(pct, y), textprops = {'color':"w"})
  plt.legend(loc="lower right")
  plt.title(title)
  plt.savefig("piechart.png", transparent=True)
  plt.clf()
  file = discord.File("piechart.png")
  await ctx.send(file=file)
  os.remove('piechart.png')

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

from botpycalc import *

@bot.command()
async def ping(ctx, *, text = None):
  now1 = datetime.now()
  message = await ctx.send("Pong!")
  mcs = str(int((datetime.now() - now1).microseconds)+int(((datetime.now() - now1).total_seconds())%60))
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
  driver = webdriver.Chrome(options=options)
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
  driver = webdriver.Chrome(options=options)
  driver.get(f"data:text/html;charset=utf-8,{code}")
  S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
  driver.set_window_size(S('Width'),S('Height'))
  driver.save_screenshot('html_screenshot.png')
  driver.quit()
  await ctx.send(file=discord.File('html_screenshot.png'))
  os.remove('html_screenshot.png')

@bot.command()
async def md(ctx, *, mdcode = None):
  match = md_pattern.fullmatch(mdcode)
  if match:
    mdcode = mdcode.replace("```md","", 1)
    code = mdcode.replace("```","")
  if mdcode == None:
    r = requests.get(ctx.message.attachments[0].url, stream=True)
    r.raise_for_status()
    r.raw.decode_content = True
    mdcode = r.content
  code = str(markdowner.convert(mdcode)).lstrip("'u").rstrip("'")
  driver = webdriver.Chrome(options=options)
  driver.get(f"data:text/html;charset=utf-8,{code}")
  S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
  driver.set_window_size(S('Width'),S('Height'))
  driver.save_screenshot('md_screenshot.png')
  driver.quit()
  await ctx.send(file=discord.File('md_screenshot.png'))
  os.remove('md_screenshot.png')

@bot.command()
async def markdown(ctx, *, mdcode = None):
  match = md_pattern.fullmatch(mdcode)
  if match:
    mdcode = mdcode.replace("```md","", 1)
    code = mdcode.replace("```","")
  if code == None:
    r = requests.get(ctx.message.attachments[0].url, stream=True)
    r.raise_for_status()
    r.raw.decode_content = True
    mdcode = r.content
  code = str(markdowner.convert(mdcode)).lstrip("'u").rstrip("'")
  driver = webdriver.Chrome(options=options)
  driver.get(f"data:text/html;charset=utf-8,{code}")
  S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
  driver.set_window_size(S('Width'),S('Height'))
  driver.save_screenshot('md_screenshot.png')
  driver.quit()
  await ctx.send(file=discord.File('md_screenshot.png'))
  os.remove('md_screenshot.png')

@bot.command()
async def latex(ctx, *, latexcode = None):
  output = pnglatex(latexcode, 'latex.png')
  await ctx.send(file=discord.File('latex.png'))
  os.remove('latex.png')

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
  counter = 0
  for count in list(definitions.keys()):
    desc = desc + "**"+count+f"**\n"+definitions[count][counter]+f"\n"
    counter = counter + 1
  desc = desc + f"**Synonyms**\n"
  for count in dictionary.synonym(word):
    desc = desc + count + ", "
  desc = desc[:-2]
  desc = desc + f"\n**Antonyms**\n"
  for count in dictionary.antonym(word):
    desc = desc + count + ", "
  desc = desc[:-2]
  embed = discord.Embed(title=ti, description=desc)
  await ctx.send(embed=embed)

@bot.command()
async def wiki(ctx, *, query):
  totallen = 0
  try:
    desc = wikipedia.summary(query)[:2047]
    totallen = totallen + len(wikipedia.summary(query)) + len(desc) + len(query)
    wpage = wikipedia.page(title=query, auto_suggest=True, redirect=True, preload=False)
    embed = discord.Embed(title=query, url="https://en.wikipedia.org/wiki/"+wpage.title.replace(" ","_"), description=desc)
    print(wpage.sections)
    counter = 0
    for count in wpage.sections:
      if counter >=4 or totallen + len(wpage.section(count)) >= 6000:
        break
      if len(wpage.section(count))!=0:
        embed.add_field(name=count, value=wpage.section(count)[:499], inline=False)
        totallen = totallen + len(wpage.section(count))
        counter = counter + 1
    if len(wpage.images)>=1:
      embed.set_thumbnail(url = wpage.images[0])
    if len(wpage.images)>=2:
      embed.set_image(url = wpage.images[1])
    await ctx.send(embed = embed)
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
  if ctx.author.id != 746227806278647928:
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
  if ctx.author.permissions_in(ctx.channel).manage_messages or bot_admins.count(ctx.author.id)!=0:
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
  if ctx.author.permissions_in(ctx.channel).manage_messages or bot_admins.count(ctx.author.id)!=0:
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
  if ctx.author.permissions_in(ctx.channel).manage_messages or bot_admins.count(ctx.author.id)!=0:
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
  if ctx.author.permissions_in(ctx.channel).manage_messages or bot_admins.count(ctx.author.id)!=0:
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
  if ctx.author.permissions_in(ctx.channel).manage_messages or bot_admins.count(ctx.author.id)!=0:
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
  newsec=newsec.replace("a","🇦 ")
  newsec=newsec.replace("b","🇧 ")
  newsec=newsec.replace("c","🇨 ")
  newsec=newsec.replace("d","🇩 ")
  newsec=newsec.replace("e","🇪 ")
  newsec=newsec.replace("f","🇫 ")
  newsec=newsec.replace("g","🇬 ")
  newsec=newsec.replace("h","🇭 ")
  newsec=newsec.replace("i","🇮 ")
  newsec=newsec.replace("j","🇯 ")
  newsec=newsec.replace("k","🇰 ")
  newsec=newsec.replace("l","🇱 ")
  newsec=newsec.replace("m","🇲 ")
  newsec=newsec.replace("n","🇳 ")
  newsec=newsec.replace("o","🇴 ")
  newsec=newsec.replace("p","🇵 ")
  newsec=newsec.replace("q","🇶 ")
  newsec=newsec.replace("r","🇷 ")
  newsec=newsec.replace("s","🇸 ")
  newsec=newsec.replace("t","🇹 ")
  newsec=newsec.replace("u","🇺 ")
  newsec=newsec.replace("v","🇻 ")
  newsec=newsec.replace("w","🇼 ")
  newsec=newsec.replace("x","🇽 ")
  newsec=newsec.replace("y","🇾 ")
  newsec=newsec.replace("z","🇿 ")
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
async def server(ctx, text = "regular"):
  guild=ctx.guild
  ti=guild.name
  desc="Created at "+guild.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")+" by "+str(guild.owner.mention)+"""
Region: """+str(guild.region)
  embed=discord.Embed(title=ti, description=desc)
  embed.set_author(name="Server Information",icon_url=guild.icon_url)
  if text == "mod":
    try:
      f1vlist=await guild.bans()
      f1v=""
      for count in f1vlist:
        f1v=f1v+count.user.mention+" "
      f1v=f1v[:-1]
    except:
      f1v="Unable to get banned members without Ban-members permission."
    if len(f1v)!=0:
      embed.add_field(name="Banned Users", value=f1v, inline=True)
    try:
      f2vlist=await guild.invites()
      f2v=""
      for count in f2vlist:
        f2v=f2v+count.url+" "
      f2v=f2v[:-1]
    except:
      f2v="Unable to get invites without Manage-server permission."
    if len(f2v)!=0:
      embed.add_field(name="Invites", value=f2v, inline=True)
  else:
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
    ecf=guild.explicit_content_filter
    if str(ecf)=="disabled":
      f7v="Disabled"
    elif str(ecf)=="no_role":
      f7v="Members without roles"
    elif str(ecf)=="all_members":
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
    embed.add_field(name="Text Channels ("+str(len(guild.text_channels))+")", value=f0v, inline=False)
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
  if (int(times)<30 and message.count("@")==0) or bot_admins.count(ctx.author.id)!=0:
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
  if ctx.author.permissions_in(ctx.channel).ban_members or bot_admins.count(ctx.author.id)!=0:
    embed = discord.Embed(title=f"{user.name} was banned.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await ctx.send(embed=embed)
    embed = discord.Embed(title=f"You were banned from the server.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await user.send(embed=embed)
    await user.ban(reason=reason)
  else:
    await ctx.send("You don't have the required permissions.")

@bot.command()
async def unban(ctx, user: discord.User, *, reason="No reason provided"):
  if ctx.author.permissions_in(ctx.channel).ban_members or bot_admins.count(ctx.author.id)!=0:
    embed = discord.Embed(title=f"{user.name} was unbanned.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await ctx.send(embed=embed)
    await ctx.guild.unban(user)
  else:
    await ctx.send("You don't have the required permissions.")

@bot.command()
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
  if ctx.author.permissions_in(ctx.channel).kick_members or bot_admins.count(ctx.author.id)!=0:
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
        if ctx.author.permissions_in(count).manage_channels or bot_admins.count(ctx.author.id)!=0:
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
