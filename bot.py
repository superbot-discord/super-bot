from discord_slash.utils.manage_commands import create_option, create_choice
from discord_slash import SlashCommand, SlashContext
from discord import Webhook, RequestsWebhookAdapter
from unicode_charnames import search_charnames
from datetime import datetime, date, timedelta
from discord_webhook import DiscordWebhook
from captcha.image import ImageCaptcha
import selenium.common.exceptions
from discord.ext import commands
import matplotlib.pyplot as plt
from selenium import webdriver
import emojis as ems
from cmath import *
import ascii as asc
import random as ra
import pytesseract
import numpy as np
from math import *
import time as tm
import subprocess
import datetime
import requests
import aiohttp
import asyncio
import qr_img
import pytube
import typing
import PIL
import re
import os

from botwebscrape import *
from botwebinfo import *
from botengrave import *
from botanimals import *
from botpycalc import *
from botbasic import *
from botembed import *
from botplot import *
from botinfo import *

banned_ids = []
banned_text = []
bot_admins = [687474789342117900]
bot = commands.Bot(command_prefix=commands.when_mentioned_or("="), intents=discord.Intents.all())
bot.remove_command('help')
slash = SlashCommand(bot, sync_commands=False)
allid=[]
id_pattern = re.compile(r'([A-Z]{5})', re.IGNORECASE)
verify_pattern = re.compile(r'[^ ⠀][\s\S]{0,30}?[^ ⠀]#?[\d]{4}(,|, | )?[\d+\-*/×÷%xyz()\[\]\{\}]{1,50}=[\d+\-*/×÷%xyz()\[\]\{\}]{1,50}(,|, | )?[\S ]{3,20}(,|, | )?(Red|Orange|Yellow|Green|Light( |_)?Green|Dark( |_)?Green|Cyan|Blue|Light( |_)?Blue|Dark( |_)?Blue|Purple|Pink|Brown)', re.IGNORECASE)
poll_pattern = re.compile(r'([\w]+?)(:\w{2,32}:|[\uD800-\uDBFF])')
UNITS = {'s':'seconds', 'm':'minutes', 'h':'hours', 'd':'days', 'w':'weeks'}
image = ImageCaptcha()
typer=0
cmaphsv = plt.cm.hsv
def func(pct, allvals):
  absolute = int(pct/100*np.sum(allvals))
  return "{:d} ({:.1f}%)".format(absolute, int(pct))
sniper1={} # Most recent
sniper2={}
sniper3={}
sniper4={}
sniper5={} # Oldest
sniperdate1={}
sniperdate2={}
sniperdate3={}
sniperdate4={}
sniperdate5={}
sniperdict={}
sniping={}
snipereactions=[]
overwrite = discord.PermissionOverwrite()
overwrite.view_channel = True

def botadmin(context):
  return context.author.id == 687474789342117900

@bot.event
async def on_member_join(member):
  if member.guild.id == 824524455924727839:
    if member.bot:
      await member.add_roles(member.guild.get_role(824524665842040852))
      await member.guild.get_channel(824524893152477206).create_text_channel(member.name.lower().replace(" ","-"),slowmode_delay=1, topic = f"Use and talk about the bot {member.name}.", overwrites={member.guild.default_role: discord.PermissionOverwrite(read_messages=False), member.guild.get_role(824526276835803176): discord.PermissionOverwrite(read_messages=True), member: discord.PermissionOverwrite(read_messages=True)})
    else:
      embed = discord.Embed(title = "Welcome", desc="Hello and welcome to Bot Laboratoratory! You can add any bot to this server by [proposing](https://discord.gg/etb53Cvheh). Simply send the bot's invite and we will discuss about it. Have fun!")
      await member.send(embed=embed)
  if member.guild.id == 823405852131328001:
    ch=await member.guild.create_text_channel('verify', overwrites = {member.guild.default_role: discord.PermissionOverwrite(view_channel=False), member: discord.PermissionOverwrite(view_channel=True)})
    await ch.send(f"{member.mention}, please verify by calculating {str(ra.randint(1,20))}"+ra.choice(["+","-","×"])+str(ra.randint(1,10))+".")

@bot.event
async def on_voice_state_update(member, before, after):
  try:
    if before.channel.id == 822750915466493982 and after.channel == None:
      supchat = member.guild.get_channel(822753048510070784)
      await supchat.purge(limit=1000)
      await supchat.set_permissions(member, overwrite=None)
  except:
    1
  try:
    if before.channel == None and after.channel.id == 822750915466493982:
      supchat = member.guild.get_channel(822753048510070784)
      await supchat.purge(limit=1000)
      await supchat.set_permissions(member, overwrite=overwrite)
  except:
    1

@bot.event
async def on_message_delete(message):
  keyname = str(message.guild.id)+str(message.channel.id)
  val = message.content
  if val.replace(" ","") == "":
    return
  adt = "By "+message.author.name+"#"+str(message.author.discriminator)+" at "+message.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  if sniper1.get(keyname, 1) == 1:
    sniper1[keyname] = val
    sniperdate1[keyname] = adt
  elif sniper2.get(keyname, 1) == 1:
    sniper2[keyname] = sniper1[keyname]
    sniper1[keyname] = val
    sniperdate2[keyname] = sniperdate1[keyname]
    sniperdate1[keyname] = adt
  elif sniper3.get(keyname, 1) == 1:
    sniper3[keyname] = sniper2[keyname]
    sniper2[keyname] = sniper1[keyname]
    sniper1[keyname] = val
    sniperdate3[keyname] = sniperdate2[keyname]
    sniperdate2[keyname] = sniperdate1[keyname]
    sniperdate1[keyname] = adt
  elif sniper4.get(keyname, 1) == 1:
    sniper4[keyname] = sniper3[keyname]
    sniper3[keyname] = sniper2[keyname]
    sniper2[keyname] = sniper1[keyname]
    sniper1[keyname] = val
    sniperdate4[keyname] = sniperdate3[keyname]
    sniperdate3[keyname] = sniperdate2[keyname]
    sniperdate2[keyname] = sniperdate1[keyname]
    sniperdate1[keyname] = adt
  else:
    sniper5[keyname] = sniper4[keyname]
    sniper4[keyname] = sniper3[keyname]
    sniper3[keyname] = sniper2[keyname]
    sniper2[keyname] = sniper1[keyname]
    sniper1[keyname] = val
    sniperdate5[keyname] = sniperdate4[keyname]
    sniperdate4[keyname] = sniperdate3[keyname]
    sniperdate3[keyname] = sniperdate2[keyname]
    sniperdate2[keyname] = sniperdate1[keyname]
    sniperdate1[keyname] = adt

@bot.event
async def on_reaction_add(reaction, user):
  if snipereactions.count(reaction.message) != 0 and user.id != 796686363604680755:
    keyname = str(reaction.message.guild.id)+str(reaction.message.channel.id)
    if reaction.emoji == '⏪':# and sniper1.get(keyname, 1) != 1:
      sniperdict[reaction.message] = 1
    elif reaction.emoji == '⬅️' and sniperdict[reaction.message] > 1:
      sniperdict[reaction.message] = sniperdict[reaction.message] - 1
    elif reaction.emoji == '📌' and reaction.message.pinned == False and reaction.message.guild.get_member(796686363604680755).permissions_in(reaction.message.channel).manage_messages:
      await reaction.message.pin()
      pinmsg = await reaction.message.channel.fetch_message(reaction.message.channel.last_message_id)
      await pinmsg.delete()
    elif reaction.emoji == '📌' and reaction.message.pinned and reaction.message.guild.get_member(796686363604680755).permissions_in(reaction.message.channel).manage_messages:
      await reaction.message.unpin()
    elif reaction.emoji == '📌':
      await reaction.message.channel.send("Unable to Pin/Unpin messages without `Manage Server` permission.")
      return
    elif reaction.emoji == '➡️' and sniperdict[reaction.message] <5 and eval('sniper'+str(sniperdict[reaction.message]+1)+'.get(keyname, 1)') != 1:
      sniperdict[reaction.message] = sniperdict[reaction.message] + 1
    elif reaction.emoji == '⏩' and sniper5.get(keyname, 1) != 1:
      sniperdict[reaction.message] = 5
    elif reaction.emoji == '⏩' and sniper4.get(keyname, 1) != 1:
      sniperdict[reaction.message] = 4
    elif reaction.emoji == '⏩' and sniper3.get(keyname, 1) != 1:
      sniperdict[reaction.message] = 3
    elif reaction.emoji == '⏩' and sniper2.get(keyname, 1) != 1:
      sniperdict[reaction.message] = 2
    elif reaction.emoji == '⏩' and sniper1.get(keyname, 1) != 1:
      sniperdict[reaction.message] = 1
    elif reaction.emoji == '⬅️' or reaction.emoji == '➡️':
      await reaction.remove(user)
      return
    else:
      return
    await reaction.remove(user)
    if sniper2.get(keyname, 1) == 1:
      maxc = 1
    elif sniper3.get(keyname, 1) == 1:
      maxc = 2
    elif sniper4.get(keyname, 1) == 1:
      maxc = 3
    elif sniper5.get(keyname, 1) == 1:
      maxc = 4
    else:
      maxc = 5
    #if eval('sniper'+str(sniperdict[reaction.message])+'.get(keyname, 1)') == 1:
    #  sniperdict[reaction.message] = sniperdict[reaction.message] - 1
    ti = "Snipped message ("+str(sniperdict[reaction.message])+r"/"+str(maxc)+")"
    desc = eval('sniper'+str(sniperdict[reaction.message])+'[keyname]')
    foot = eval('sniperdate'+str(sniperdict[reaction.message])+'[keyname]')
    embed = discord.Embed(title=ti, description=desc)
    embed.set_footer(text=foot)
    await reaction.message.edit(embed=embed)

@bot.event
async def on_member_update(before, after):
  if after.guild.id == 809368482344075265 and after.id == 757431801487556748:
    if after.roles.count(before.guild.get_role(813569850123223060)) == 0:
      await after.add_roles(before.guild.get_role(), reason = "He is a raider")
    if after.roles.count(before.guild.get_role(814038966793797642)) == 0:
      await after.add_roles(before.guild.get_role(), reason = "He is an ex-raider")

@bot.event
async def on_message(message):
  """match = verify_pattern.fullmatch(message.content)
  if message.channel.id == 811562994151850024 and match == None and message.author.roles.count(message.guild.get_role(810729029790597190)) == 0:
    await message.channel.send(f"Invalid verification format! Please double check the format and try again.\n**Format: **Username#Discriminator, Math equation with equal sign(Max. 100 characters), Favourite Food, Colour\n**Original Content: **"+message.content, delete_after=10)
    try:
      await message.delete()
    except:
      1"""
  if message.guild.id == 852899227004305458 and message.author.id != 796686363604680755 and message.channel.id in [856053769149874196, 864757953121878026, 864754633910255646]:
    await message.add_reaction("<:UpArrowSquare:864762633194569728>")
    await message.add_reaction("<:DownArrowSquare:864762633625534485>")
  if not (message.author.bot or message.author.id == 802834139728445501):
    try:
      for count in message.author.mutual_guilds:
        for count2 in count.emojis:
          if message.content.count(f":{count2.name}:") and count2.animated:
            desc = message.content
            gid = message.guild.id
            desc = re.sub(r'(:[a-zA-Z_-]{2,32}:)', r"\<\1"+str(gid)+"\>", desc)
            desc = desc.replace("{nothing}", "")
            whl = await message.channel.webhooks()
            ourweb = False
            for count3 in whl:
              if count3.name == "AnimatedEmoji":
                ourweb = True
                token = count3.token
                identify = count3.id
                break
            if len(whl) == 0 or ourweb == False:
              wh = await message.channel.create_webhook(name = "AnimatedEmoji")
              token = wh.token
              identify = wh.id
            try:
              await message.delete()
            except:
              1
            async with aiohttp.ClientSession() as session:
              webhook = Webhook.partial(identify, token, adapter=RequestsWebhookAdapter())
              await webhook.send(desc, username=message.author.name, avatar_url=message.author.avatar_url)
            break
    except:
      1
    if banned_ids.count(message.author.id)==0 and message.content.startswith("=") and message.content.startswith("==")==False:
      await bot.process_commands(message)
    elif message.content.startswith("="):
      await message.channel.send("You are banned from the bot. Reason: "+banned_text[banned_ids.index(message.author.id)])
  elif message.author.id == 802834139728445501 and message.guild.id == 836809816662999060:
    await message.delete()#delay=3)

@bot.command()
async def unicode(ctx, *, query):
  allchars = search_charnames(query)
  embed = discord.Embed(title = "Search results for: "+query)
  for count, count2 in zip(allchars, range(0,25)):
    embed.add_field(name = count[1].title(), value = "U+" + count[0] + eval("u\" \\u"+count[0]+"\""))
  
  await ctx.send(embed=embed)

@bot.command()
async def redirect(ctx, *, url):
  await ctx.send(botredirect(url))

@bot.command()
async def qr(ctx, *, text=None):
  for count in ctx.message.attachments:
    await count.save('qrcode.png')
    await ctx.send(qr_img.qr_decode('qrcode.png'))
    os.remove('qrcode.png')

@bot.command()
async def qrmake(ctx, *, text):
  output = botqrencode(text)
  try:
    await ctx.send(file=discord.File("QRCode.png"))
    os.remove("QRCode.png")
  except:
    await ctx.send(output)

@bot.command()
async def dog(ctx, number=1):
  if number<9:
    await ctx.send(botdog(number))

@bot.command()
async def cat(ctx, number=1):
  if number<9:
    await ctx.send(botcat(number))

@bot.command()
async def verify(ctx):
  if ctx.message.guild.id == 823405852131328001:
    if ctx.author.roles.count(ctx.guild.get_role(823407479303569419))==1:
      overdict = ctx.message.guild.get_channel(823410283723620362).overwrites
      verifiedmem = list(overdict)[0]
      theinvite = await bot.get_guild(806083349688877077).get_channel(806085319521992705).create_invite(max_age=300, max_uses=1)
      desc = "You are verified! Please use [this invite]("+theinvite.url+") to join the Historical Community server. It would expire in 5 minutes. Please kindly ask Henry or Johann if the link expired and you need a new one."
      embed = discord.Embed(title="Verified", description=desc)
      await discord.utils.find(lambda userarg: userarg.roles[0].id != 823407479303569419, ctx.channel.members).send(embed=embed)
      await ctx.channel.send(embed=embed)

@bot.command()
async def makeinvite(ctx, timetocount, uses : int = 0):
  seconds = int(timedelta(**{
    UNITS.get(m.group('unit').lower(), 'seconds'): int(m.group('val'))
    for m in re.finditer(r'(?P<val>\d+)(?P<unit>[smhdw]?)', timetocount, flags=re.I)
  }).total_seconds())
  theinvite = await ctx.channel.create_invite(max_age = seconds, max_uses = uses)
  await ctx.send("An invite was generated with "+str(seconds)+" seconds of valid duration: "+theinvite.url)

@bot.command()
async def reactions(ctx, *, msg : discord.Message):
  reactions = msg.reactions
  numlist = []
  labelslist = []
  for counter in reactions:
    numlist.append(counter.count)
    labelslist.append(em.demojize(counter.emoji))
  y = np.array(numlist)
  labels = tuple(labelslist)
  mycolors = []
  for count in range(0, len(numlist)):
    mycolors.append(cmaphsv(count/len(numlist)))
  plt.pie(y, labels=labels, colors=mycolors, autopct=lambda pct: func(pct, y), textprops = {'color':"w"})
  plt.legend(loc="lower right")
  plt.title("Reaction Status")
  plt.savefig("reactions.png", transparent=True)
  await ctx.send(file = discord.File('reactions.png'))
  plt.clf()

@bot.command(aliases=['sniper'])
async def snipe(ctx, *, text = None):
  keyname = str(ctx.guild.id)+str(ctx.channel.id)
  if text == None:
    if sniping.get(keyname, 1) == 1 or sniping[keyname] == True:
      chnl = ctx.channel
      if sniper1.get(keyname, 1) == 1:
        ti = "Error"
        desc = "Nothing to snipe from this channel."
        embed = discord.Embed(title=ti, description=desc)
        await ctx.send(embed=embed)
        return
      else:#if sniper2.get(keyname, 1) == 1:
        if sniper2.get(keyname, 1) == 1:
          maxc = 1
        elif sniper3.get(keyname, 1) == 1:
          maxc = 2
        elif sniper4.get(keyname, 1) == 1:
          maxc = 3
        elif sniper5.get(keyname, 1) == 1:
          maxc = 4
        else:
          maxc = 5
        ti = "Snipped message (1/"+str(maxc)+")"
        desc = sniper1[keyname]
        foot = sniperdate1[keyname]
      embed = discord.Embed(title=ti, description=desc)
      embed.set_footer(text=foot)
      cmsg = await ctx.send(embed=embed)
      sniperdict[cmsg] = 1
      await cmsg.add_reaction('⏪')
      await cmsg.add_reaction('⬅️')
      await cmsg.add_reaction('📌')
      await cmsg.add_reaction('➡️')
      await cmsg.add_reaction('⏩')
      snipereactions.append(cmsg)
    else:
      await ctx.send("Snipping is disabled. Please ask someone with manage messages permission to re-enable it.")
  elif ctx.author.permissions_in(ctx.channel).manage_messages:
    if text.startswith("y") or text.startswith("t") or text.startswith("e") or text.replace(" ","")=="1":
      sniping[keyname] = True
      await ctx.send("Sniping is now enabled.")
    else:
      sniping[keyname] = False
      await ctx.send("Sniping is now disabled.")

@bot.command()
async def poll(ctx, *, text):
  options = []
  reactions = []
  textlist = text.split(" ")
  ti = ""
  desc = ""
  for count in textlist:
    match = poll_pattern.fullmatch(em.demojize(count))
    if match:
      optn = re.sub(poll_pattern, r'\1', ems.demojize(count))
      rect = re.sub(poll_pattern, r'\2', ems.demojize(count))
      desc = desc + f"{rect} {optn} (0)\n"
      options.append(optn)
      reactions.append(ems.emojize(rect))
    else:
      ti = ti + count + " "
  embed = discord.Embed(title = ti, description = em.emojize(desc))
  poll = await ctx.send(embed=embed)
  for count in reactions:
    await poll.add_reaction(count) 

@bot.command()
async def unscramble(ctx, text, length="0"):
  output = botunscramble(text, length)
  await ctx.send(embed=output, file=discord.File("output.txt"))
  os.remove('output.txt')

@bot.command()
async def youtube(ctx, *, link):
  try:
    playlist = pytube.Playlist(link)
    text = ""
    for count in playlist:
      text=text+str(count)+"  "+pytube.YouTube(text).streams.filter(mime_type="video/mp4").filter(progressive="True").filter(type="video").order_by("resolution").first().url+f"\n"
    file = open("output.txt", "w")
    file.write(text)
    file.close()
    await ctx.send(file=discord.File("output.txt"))
    os.remove("output.txt")
  except:
    try:
      youtube = pytube.YouTube(link)
    except:
      youtube = pytube.Search(link).results[0]
    yt = youtube.streams.filter(mime_type="video/mp4").filter(progressive="True").filter(type="video").order_by("resolution").first()
    embed = discord.Embed(title="Download (Click here)", url=yt.url, description="This video has a size of around "+str(round(yt.filesize/1048.576)/1000)+f"MB. Make sure you use a WiFi network for large videos.\n[Channel]("+youtube.channel_url+")")
    embed.add_field(name="Title", value=str(youtube.title), inline=False)
    embed.add_field(name="Description", value=str(youtube.description), inline=False)
    embed.add_field(name="Tags", value=", ".join(youtube.keywords), inline=False)
    embed.add_field(name="Views", value=str(youtube.views), inline=True)
    embed.add_field(name="Date uploaded", value=youtube.publish_date.strftime("%d %b, %Y (%a) %H:%M:%S"), inline=True)
    ytlen = youtube.views.length
    if ytlen >= 21600:
      ytlenformat = str(ytlen//21600)+"  days plus "+str(ytlen%21600//3600).zfill(2)+":"+str(ytlen%3600//60).zfill(2)+":"+str(ytlen%60).zfill(2)
    elif ytlen >= 3600:
      ytlenformat = str(ytlen//3600).zfill(2)+":"+str(ytlen%3600//60).zfill(2)+":"+str(ytlen%60).zfill(2)
    else:
      ytlenformat = str(ytlen//60).zfill(2)+":"+str(ytlen%60).zfill(2)
    embed.add_field(name="Length", value=ytlenformat, inline=True)
    channel = Channel(youtube.channel_url)
    embed.add_field(name="Channel", value="["+channel.channel_name+"]("+youtube.channel_url+")", inline=False)
    embed.add_field(name="Channel Views", value=channel.views, inline=True)
    embed.add_field(name="Channel Videos", value=str(len(channel.videos)), inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def clearsnipe(ctx, *, chnl : discord.TextChannel = None):
  if chnl == None:
    chnl = ctx.channel
  if ctx.author.permissions_in(chnl).manage_channels or bot_admins.count(ctx.author.id)!=0:
    sniper1.pop(str(ctx.guild.id)+str(chnl.id))
    sniper2.pop(str(ctx.guild.id)+str(chnl.id))
    sniper3.pop(str(ctx.guild.id)+str(chnl.id))
    sniper4.pop(str(ctx.guild.id)+str(chnl.id))
    sniper5.pop(str(ctx.guild.id)+str(chnl.id))
    await ctx.send('Cleared snipe database for '+chnl.mention+'.')
  else:
    await ctx.send("You don't have the required permissions.")

@bot.command()
async def nick(ctx, *, newnick):
  if ctx.author.permissions_in(ctx.channel).manage_nicknames:
    await ctx.guild.get_member(796686363604680755).edit(nick = newnick)
    await ctx.send("Nickname changed.")

@bot.command()
async def tts(ctx, *, desc):
  await ctx.send(desc, tts = True)

@bot.command()
async def raw(ctx, msg : discord.Message):
  embed = discord.Embed(title = "Raw message", url = msg.jump_url, description = "```"+discord.utils.escape_markdown(msg.content, as_needed=True)+"```")
  await ctx.send(embed=embed)

@bot.command()
async def help(ctx, *, cat=None):
  embed = bothelp(cat)
  await ctx.send(embed=embed)

@bot.command()
async def invite(ctx, *, text=None):
  embed = botinvite()
  await ctx.send(embed=embed)

@bot.command()
@commands.is_owner()
async def purgeserver(ctx, text, condition="1==1", *, nothing):
  text = text.lower()
  if text.startswith("role"):
    allroles = ctx.guild.roles()
    for _role in allroles:
      if condition:
        await _role.delete()
    await ctx.send("Role purging completed.")

@bot.command()
@commands.is_owner()
async def botban(ctx, user : discord.User, *, text="No reason was provided"):
  banned_ids.append(user.id)
  banned_text.append(text)
  await ctx.send("Banned user from using the bot.")

@bot.command()
@commands.is_owner()
async def botunban(ctx, user : discord.User):
  if banned_ids.count(user.id) == 1:
    banned_text.remove(banned_text[banned_ids.index(user.id)])
    banned_ids.remove(user.id)
    await ctx.send("Unbanned user from using the bot.")

@bot.command()
@commands.is_owner()
async def botadmin(ctx, user : discord.User):
  bot_admins.append(user.id)
  await ctx.send("Added user as bot admin.")

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
    await ctx.send("You don't have the required permissions.")

@bot.command()
async def engrave(ctx, product = "list", *, text = "Your text goes here."):
  embed = botengrave(product, text)
  await ctx.send(embed=embed)

@bot.command()
async def python(ctx, *, script):
  output = botpython(script)
  await ctx.send(output)

@bot.command()
async def regex(ctx, regularexp, *, text):
  embed = botregex(regularexp, text)
  await ctx.send(embed=embed)

@bot.command()
async def regsub(ctx, regular1, regular2, *, text):
  embed = botregsub(regular1, regular2, text)
  await ctx.send(embed=embed)

@bot.command()
async def define(ctx, function = None, definition = None, *, argumentsraw = ""):
  if botdefine(function, definition, argumentsraw) == "Not enough args":
    await ctx.send("Invalid usage! Please use the format `=define [name] [definition] {arguments separated by spaces}`.")
  else:
    await ctx.message.add_reaction("👍")

@bot.command()
async def calc(ctx, *, arg = None):
  output = botcalc(arg)
  if output == "Add_Reaction":
    await ctx.message.add_reaction("👍")
  else:
    await ctx.send(output)

@bot.command()
async def covid(ctx, *, country="world"):
  output = botcovid(country)
  if output == "Invalid country. Please try again.":
    await ctx.send(output)
  else:
    await ctx.send(files=output[0], embed=output[1])

@bot.command()
async def minecraft(ctx, *, item="tnt"):
  output = botminecraft(item)
  if output == "No Wiki page with that name found.":
    await ctx.send(output)
  else:
    await ctx.send(embed=output)

@bot.command()
async def population(ctx, country="current"):
  output = botpopulation(country)
  if output == "Invalid country. Please try again.":
    await ctx.send(output)
  else:
    await ctx.send(embed=output)

@bot.command(aliases=["simpcolour", "simplecolor", "simplecolour"])
async def simpcolor(ctx, *, name):
  botsimpcolor(name)
  try:
    file = discord.File("color.png")
    await ctx.send(file=file)
  except:
    await ctx.send("Invalid colour name, please try again.")

@bot.command(alias=["snowgraph", "snowflake"])
async def snow(ctx, recursion = 10):  
  try:
    if float(recursion) > 10:
      await ctx.send("We are sorry, the maximum recursion we can process is 10.")
    else:
      botsnow(int(recursion))
      file = discord.File("snow.png")
      await ctx.send(file=file)
      os.remove('snow.png')
  except:
    await ctx.send("Invalid input. Please try again.")

@bot.command(aliases=["piechart", "circlechart"])
async def pie(ctx, numbers, label, *, title="No_title_required"):
  try:
    botpie(title, numbers, label)
    file = discord.File("piechart.png")
    await ctx.send(file=file)
    os.remove('piechart.png')
  except:
    await ctx.send("Invalid input. Please try again.")

@bot.command()
async def captcha(ctx, *, text=None):
  if text == None:
    text = ra.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") + ra.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") + ra.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") + ra.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
  data = image.generate(text)
  image.write(text, 'captcha.png')
  await ctx.send(f"Captcha for {text}", file = discord.File('captcha.png'))
  os.remove('captcha.png')

@bot.command()
async def hello(ctx, *, text=None):
  embed = discord.Embed(title="Leaderboard", description="We upload the leaderboard to YouTube every week. You can find the leaderboard [here](https://youtu.be/4spCNEPawyQ).")
  await ctx.send(embed=embed)

@bot.command()
async def draw(ctx, *, text):
  output = botdraw(text)
  if len(output) > 1994:
    await ctx.send(file=discord.File('drawing.txt'))
  else:
    await ctx.send(f"```{output}```", file=discord.File('drawing.txt'))
  os.remove('drawing.txt')

@bot.command()
async def ascii(ctx, *, text):
  output = botascii(text)
  if len(output) > 1994 or len(text) > 11:
    await ctx.send(file=discord.File('ascii.txt'))
  else:
    await ctx.send(f"```{output}```", file=discord.File('ascii.txt'))
  os.remove('ascii.txt')

@bot.command()
async def table(ctx, *, text):
  output = bottable(text)
  if output == "Invalid syntax, please try again.":
    await ctx.send(output)
  else:
    file = open("table.txt", "w")
    file.write(output)
    file.close()
    await ctx.send(f"```{output}```", file=discord.File('table.txt'))
    os.remove('table.txt')

@bot.command()
async def barh(ctx, numbers, label, *, title="No_title_required"):
  try:
    botbarh(title, numbers, label)
    file = discord.File("horizontalbarchart.png")
    await ctx.send(file=file)
    os.remove('horizontalbarchart.png')
  except:
    await ctx.send("Invalid input. Please try again.")

@bot.command()
async def barv(ctx, numbers, label, *, title="No_title_required"):
  try:
    botbarv(title, numbers, label)
    file = discord.File("verticalbarchart.png")
    await ctx.send(file=file)
    os.remove('verticalbarchart.png')
  except:
    await ctx.send("Invalid input. Please try again.")

@bot.command(aliases=["histogram", "histograms"])
async def hist(ctx, numbers, *, title="No title"):
  try:
    bothist(title, numbers)
    file = discord.File("histogram.png")
    await ctx.send(file=file)
    os.remove('histogram.png')
  except:
    await ctx.send("Invalid input. Please try again.")

@bot.command()
async def translate(ctx, langinput = "list", *, text = "Sample text"):
  output = bottranslate(langinput, text)
  if output[0] == "*" or output[0] == "L":
    await ctx.send(output)
  else:
    e1 = output[0]
    e2 = output[1]
    await ctx.send(embed=e1)
    await ctx.send(embed=e2)

@bot.command()
async def render(ctx):
  for count in range(40, 4, -1):
    try:
      output = asc.loadFromUrl(ctx.message.attachments[0].url, columns=ctx.message.attachments[0].width*count/10, color=False)
      break
    except:
      pass
  file = open('Output.txt', 'w')
  file.write(output)
  file.close()
  await ctx.send(file = discord.File('Output.txt'))
  os.remove('Output.txt')

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
        try:
          field=":"+count.emoji.name+": "+count.name
        except:
          try:
            field=count.name
          except:
            field=":"+count.emoji.name+":"
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
async def ping(ctx, *, text = None):
  now1 = datetime.datetime.now()
  message = await ctx.send("Pong!")
  mcs = str(int((datetime.datetime.now() - now1).microseconds)+int(((datetime.datetime.now() - now1).total_seconds())%60))
  await message.edit(content="Pong! "+mcs+" microseconds")

@bot.command()
async def screenshot(ctx, url = None, form = "all"):
  a = botscreenshot(url, form)
  if a == "Invalid format! Please use the format `=screenshot [url]`.":
    await ctx.send(a)
  else:
    try:
      await ctx.send(file=discord.File('web_screenshot1.png'))
      os.remove('web_screenshot1.png')
    except:
      pass
    try:
      await ctx.send(file=discord.File('web_screenshot2.png'))
      os.remove('web_screenshot2.png')
    except:
      pass

@bot.command()
async def ocr(ctx, lang="eng", *, text = None):
  images = ctx.message.attachments
  for count in range(0,len(images)):
    r = requests.get(images[count].url, stream=True)
    r.raise_for_status()
    r.raw.decode_content = True
    with PIL.Image.open(r.raw) as img:
      desc=pytesseract.image_to_string(img, lang=lang)
    r.close()
    if desc.replace(" ","")=="":
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
  bothtml(code)
  await ctx.send(file=discord.File('html_screenshot.png'))
  os.remove('html_screenshot.png')

@bot.command(aliases=['md'])
async def markdown(ctx, *, mdcode = None):
  botmd(mdcode)
  await ctx.send(file=discord.File('md_screenshot.png'))
  os.remove('md_screenshot.png')

@bot.command()
async def definition(ctx, *, word):
  output = botdefinition(word)
  if output == "Invalid word. Please try again.":
    await ctx.send(output)
  else:
    await ctx.send(embed=output)

@bot.command()
async def wiki(ctx, *, query):
  embed = botwiki(query)
  await ctx.send(embed=embed)
  
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
  await asyncio.sleep(3)
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
    if textlist[2].startswith("y") or textlist[2].startswith("t") or textlist[2].startswith("e") or textlist[2].lower()=="1":
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
async def ett(ctx, msg : discord.Message):
  text = botett(msg)
  await ctx.send("```"+text+"```")

@bot.command(aliases=["fastembed", "qe"])
async def quickembed(ctx, *, text):
  embed = botquickembed(text)
  await ctx.send(embed=embed)

@bot.command(aliases=["simpleembed", "simplembed"])
async def simpembed(ctx, *, text):
  embed = botsimpembed(text)
  await ctx.send(embed=embed)

@bot.command()
async def embed(ctx,*,text):
  embed = botembed(text)
  await ctx.send(embed=embed)

@bot.command()
async def editembed(ctx, message : discord.Message, *,text):
  embed = botembed(text)
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
  if ctx.author.permissions_in(ctx.channel).manage_messages or bot_admins.count(ctx.author.id)!=0 or pyscript.replace(" ","") == "msg.author.id==814292078984167425":
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

@bot.command(aliases=["colour"])
async def color(ctx, arg1, arg2=None, arg3=None):
    output = botcolor(arg1, arg2, arg3)
    if output == "Please specify a correct colour value.":
      await ctx.send(output)
    else:
      await ctx.send(embed=output)

@bot.command()
async def time(ctx, *, timezoneinput="0"):
  output = bottime(timezoneinput)
  if type(output) == str:
    await ctx.send(output)
  else:
    await ctx.send(embed=output)

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
async def emojiinfo(ctx,emojiarg : typing.Union[discord.Emoji, str]):
  try:
    try:
      creator = await ctx.guild.fetch_emoji(emojiarg.id)
      desc = str(emojiarg)+emojiarg.name+"\nCreated by "+str(creator.user.mention)+" at "+str(emojiarg.created_at.strftime("%d %b, %Y (%a) %H:%M:%S"))
      embed = discord.Embed(title="Emoji Info", description=desc)
      embed.add_field(name="ID", value=emojiarg.id, inline=True)
    except:
      desc = str(emojiarg)+emojiarg.name+"\n`Created by` field can only be retrieved with the manage-emojis permission.\nCreated at "+str(emojiarg.created_at.strftime("%d %b, %Y (%a) %H:%M:%S"))
      embed = discord.Embed(title="Emoji Info", description=desc)
      embed.add_field(name="ID", value=emojiarg.id, inline=True)
  except:
    cemoji = ems.db.get_emoji_by_alias(emojiarg)
    if cemoji == None:
      cemoji = ems.db.get_emoji_by_code(emojiarg)
    embed = discord.Embed(title="Emoji Info", description = (cemoji[1] + " :" + ":, :".join(cemoji[0]) + ":"))
    embed.add_field(name="Category", value=cemoji[3], inline=True)
    embed.add_field(name="Unicode Version", value=cemoji[4], inline=True)
    if len(cemoji[2]) > 0:
      embed.add_field(name="Tags", value=", ".join(cemoji[2]), inline=True)
  await ctx.send(embed=embed)

@bot.command()
async def reverse(ctx, *, text):
  await ctx.send(text[::-1])

@bot.command()
async def emoji(ctx, *, text):
  await ctx.send(botemoji(text))

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
    end = datetime.datetime.now() + timedelta(seconds = sec)
    seconds = int((end - datetime.datetime.now()).total_seconds())
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
      seconds = int((end - datetime.datetime.now()).total_seconds())
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
async def ttimer(ctx, timetocount,*,Text=None):
    sec = int(timedelta(**{
      UNITS.get(m.group('unit').lower(), 'seconds'): int(m.group('val'))
      for m in re.finditer(r'(?P<val>\d+)(?P<unit>[smhdw]?)', timetocount, flags=re.I)
    }).total_seconds())
    end = datetime.datetime.now() + timedelta(seconds = sec)
    seconds = int((end - datetime.datetime.now()).total_seconds())
    newidcode = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]
    exec("terminate"+newidcode.lower()+str(ctx.guild.id)+"=0",globals())
    allid.append(newidcode+str(ctx.guild.id))
    desc = "Initializing countdown…"
    message = await ctx.send(desc)
    while seconds>=1 and eval("terminate"+newidcode.lower()+str(ctx.guild.id))==0:
      seconds = int((end - datetime.datetime.now()).total_seconds())
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
      prevdesc = desc
      if seconds<0:
        break
      desc="Timer (Terminate with `=terminate "+newidcode+f"`)\n**"+newday+"** d   **"+newhrs+"** h   **"+newmin+"** m   **"+newsec+"**s"
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
async def getrole(ctx, role : discord.Role, member : discord.Member = None):
  if member == None:
    member = ctx.author
  #if ctx.author.permissions_in(ctx.channel).manage_roles or bot_admins.count(ctx.author.id)!=0:
  if ctx.author.permissions_in(ctx.channel).manage_roles or ctx.author.id == 687474789342117900 or role.id == 805462470604095539 or role.id == 805462557472194581 or role.id == 822743463883702302:
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
  embed=discord.Embed(title=ti, description=desc)
  await ctx.send(embed=embed)

@bot.command()
async def avatar(ctx,user: discord.Member=None):
  ti="Avatar"
  if user==None:
    user=ctx.author
  desc=f"Avatar of {user.mention}"
  embed=discord.Embed(title=ti, description=desc)
  embed.set_image(url=user.avatar_url)
  await ctx.send(embed=embed)

@bot.command()
async def role(ctx,role: discord.Role=None):
  ti="Role Information: "+role.name
  if role==None:
    role=ctx.authortop_role
  desc=role.mention + " created at " + role.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  embed=discord.Embed(title=ti,color=role.color, description=desc)
  memberlist=role.members
  if len(memberlist) == 0:
    f0v = "No members assigned with this role."
  else:
    f0v = ""
    for count in memberlist:
      f0v = f0v + count.mention + " "
    f0v = f0v[:-1]
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
  f4v=role.id
  f5v=role.position
  f6v=role.color
  embed.add_field(name="Mentions", value=f1v, inline=True)
  embed.add_field(name="Displayed separately?", value=f2v, inline=True)
  embed.add_field(name="Role ID", value=f4v, inline=True)
  embed.add_field(name="Position in hierarchy", value=f5v, inline=True)
  embed.add_field(name="Color", value=f6v, inline=True)
  if role.is_integration():
    f7v="This role is managed by an integration, such as a bot."
    embed.add_field(name="Integration", value=f7v, inline=False)
  embed.add_field(name="Members ("+str(len(memberlist))+")", value=f0v, inline=False)
  #embed.add_field(name="Channel Permissions", value=f3vb, inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def server(ctx, text = "regular"):
  guild=ctx.guild
  ti=guild.name
  desc="Created at "+guild.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")+" by "+str(guild.owner.mention)+f"\nRegion: "+str(guild.region)+f"\n[Server Icon]("+str(guild.icon_url)+")"
  embed=discord.Embed(title=ti, description=desc)
  embed.set_author(name="Server Information",icon_url=guild.icon_url)
  if text == "mod":
    if ctx.guild.id != 814407577042944040:
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
      await ctx.send("Since a barbarian forced me to disable this command, I had to disable it.")
  else:
    f0v=""
    for count in guild.text_channels:
      if len(f0v+str(count.mention)+" ") > 1024:
        f0v = ""
        for count2 in guild.text_channels:
          if len(f0v+count2.name+" ") > 1024:
            f0v = f0v + "… "
            break
          f0v = f0v + count2.name + " "
        break
      f0v=f0v+str(count.mention)+" "
    f1v=""
    f0v=f0v[:-1]
    if len(guild.voice_channels)==0:
      f1v="No Voice Channels"
    else:
      f1v = ""
      for count in guild.voice_channels:
        f1v = f1v + count.name + ", "
      f1v = f1v[:-2]
      if len(f1v) > 500:
        f1v = ""
        for count in guild.voice_channels:
          if len(f1v + count.name) > 500:
            break
          f1v = f1v+count.name+", "
        f1v = f1v [:-2] + "…"
    f1vb=""
    if len(guild.categories)==0:
      f1vb="No Categories"
    else:
      for count in guild.categories:
        f1vb=f1vb+str(count.name)+", "
      f1vb = f1vb[:-2]
    f1va = ""
    f1valist = guild.roles
    f1valist.reverse()
    for count in f1valist:
      f1va = f1va + count.mention+" "
    f1va = f1va[:-1]
    f2v = str(guild.bitrate_limit//1000)+" kbps"
    f3v = str(guild.filesize_limit//1048576)+" MB"
    f4v = str(guild.emoji_limit)
    f5v = guild.mfa_level
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
    if len(f8v) > 500:
      f8v = ""
      for count in guild.members:
        if len(f8v + count.name) > 500:
          break
        f8v = f8v+count.name+", "
      f8v = f8v [:-2] + "…"
    f10va = str(guild.id)
    f13v = guild.description
    if f13v == None:
      f13v = "No description"
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
    #if guild.default_notifications.all_messages:
    #  embed.add_field(name="Default Notifications", value="Members receive notifications for every message by default.", inline=True)
    #else:
    #  embed.add_field(name="Default Notifications", value="Members only receive notifications for messages they are mentioned in by default.", inline=True)
    if guild.features.count("COMMUNITY")==1:
      embed.add_field(name="Community", value="This is a community server.", inline=True)
    if guild.features.count("WELCOME_SCREEN_ENABLED")==1:
      embed.add_field(name="Welcome Screen", value="The server has enabled the welcome screen.", inline=True)
    if guild.features.count("PUBLIC")==1:
      embed.add_field(name="Public", value="This is a public server.", inline=True)
    embed.add_field(name="Description", value=f13v, inline=False)
    try:
      f11v=" ".join(guild.emojis)
      if len(f11v)!=0:
        embed.add_field(name="Emojis", value=f11v, inline=True)
    except:
      1
  try:
    await ctx.send(embed=embed)
  except:
    f1va = ""
    for count in f1valist:
      if len(f1va + count.name) > 500:
        break
      f1va = f1va + count.name+", "
    f1va = f1va [:-2] + "…"
    embed.set_field_at(3, name="Roles ("+str(len(guild.roles))+")", value=f1va, inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def template(ctx,temp: discord.Template):
  ti="Template Information: "+temp.name+" ("+temp.code+")"
  desc="Created at "+temp.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")+" by "+str(temp.creator)
  f0v=temp.description
  f1v=temp.uses
  f2v=temp.updated_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  f3v=temp.source_guild
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
  embed=discord.Embed(title=ti, description=desc)
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
  if f5v == "Never Expires":
    f7v = "Never"
  else:
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
async def autochannel(ctx, channel : typing.Union[discord.TextChannel, discord.VoiceChannel, discord.StageChannel]):
  if channel.type == discord.ChannelType.voice:
    ti="Voice Channel Information"
    desc=channel.name
    embed=discord.Embed(title=ti, description=desc)
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
  elif channel.type == discord.ChannelType.text:
    ti="Channel Information: "+channel.name
    desc=channel.mention
    embed=discord.Embed(title=ti, description=desc)
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
  elif channel.type == discord.ChannelType.stage:
    ti="Stage Channel Information"
    try:
      desc=channel.name + "  " + channel.topic
    except:
      desc=channel.name
    embed=discord.Embed(title=ti, description=desc)
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
    f6vlist=channel.requesting_to_speak
    f6v=""
    for count in f6vlist:
      f6v=f6v+count.mention+"  "
    f6v=f6v[:-2]
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
    if len(f6vlist)!=0:
      embed.add_field(name="Members requesting to speak", value=f6v, inline=True)
  else:
    embed = discord.Embed(desc = "Invalid input!")
  await ctx.send(embed=embed)

@bot.command()
async def channel(ctx, channel: discord.TextChannel=None):
  if channel==None:
    channel=ctx.channel
  ti="Channel Information: "+channel.name
  desc=channel.mention
  embed=discord.Embed(title=ti, description=desc)
  f0v=channel.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  f3v=str(channel.topic)
  f4v=str(channel.category)
  f5vlist=await channel.invites()
  f5v=""
  for count in f5vlist:
    f5v=f5v+count.url+"  "
  f5v=f5v[:-2]
  for count in channel.members:
    f8v=f8v+count.mention+" "
  f8v=f8v[:-1]
  if len(f8v) > 500:
    f8v = ""
    for count in channel.members:
      if len(f8v + count.name) > 500:
        break
      f8v = f8v+count.name+", "
    f8v = f8v [:-2] + "…"
  embed.add_field(name="Created", value=f0v, inline=True)
  if channel.is_nsfw()==True:
    embed.add_field(name="NSFW", value="This is an NSFW channel.", inline=True)
  if channel.is_news()==True:
    embed.add_field(name="News", value="This is a news channel.", inline=True)
  embed.add_field(name="Topic", value=f3v, inline=True)
  embed.add_field(name="Category", value=f4v, inline=True)
  embed.add_field(name="Members", value=f8v, inline=False)
  if len(f5vlist)!=0:
    embed.add_field(name="Invites", value=f5v, inline=True)
  embed.add_field(name="ID", value=channel.id, inline=True)
  await ctx.send(embed=embed)

@bot.command()
async def message(ctx, message: discord.Message=None):
  if message==None:
    message=ctx.message
  ti="Message Information"
  
  desc=f"Sent by {message.author.mention} at {message.created_at.strftime('%d %b, %Y (%a) %H:%M:%S')}"
  if message.edited_at != None:
    desc += f"Edited at {message.edited_at.strftime('%d %b, %Y (%a) %H:%M:%S')}"
  f0vraw = message.reactions
  f0v = ""
  for count in f0vraw:
    if count.custom_emoji:
      f0v += f":{count.emoji}:   ("+str(count.count)+")"
    else:
      f0v += f"{count.emoji}   ("+str(count.count)+")"
  f1vraw = message.attachments
  f1v = ""
  for count in f1vraw:
    if count.spoiler:
      f1v += f"[{count.filename}]({count.url}) (" + str(count.size/1024) + "MB, marked as spoiler)"
    else:
      f1v += f"[{count.filename}]({count.url}) (" + str(count.size/1024) + "MB)"
  f2vraw = message.channel_mentions
  f2v = ""
  for count in f2vraw:
    f2v += count.mention + " "
  f3vraw = message.role_mentions
  f3v = ""
  for count in f3vraw:
    f3v += count.mention + " "
  f4vraw = message.mentions
  f4v = ""
  for count in f4vraw:
    f4v += count.mention + " "
  embed=discord.Embed(title=ti, description=desc, url=message.jump_url)
  embed.add_field(name="Content", value=message.content[:500], inline=False)
  embed.add_field(name="From channel", value=message.channel.mention, inline=True)
  if message.webhook_id != None:
    embed.add_field(name="Webhook message", value="This message is sent by a webhook.", inline=True)
  if message.pinned:
    embed.add_field(name="Pinned", value="This message is pinned.", inline=True)
  if message.mention_everyone:
    embed.add_field(name="@everyone", value="This message mentioned everyone.", inline=True)
  embed.add_field(name="ID", value=str(message.id), inline=True)
  if message.type == discord.MessageType.recipient_add:
    embed.add_field(name="System message", value="This is a system message indicating that a recipient has been added to the group.", inline=False)
  elif message.type == discord.MessageType.recipient_remove:
    embed.add_field(name="System message", value="This is a system message indicating that a recipient has been removed from the group.", inline=False)
  elif message.type == discord.MessageType.call:
    embed.add_field(name="System message", value="This is a system message indicating that someone missed or started a call.", inline=False)
  elif message.type == discord.MessageType.channel_name_change:
    embed.add_field(name="System message", value="This is a system message indicating that someone changed the group's name.", inline=False)
  elif message.type == discord.MessageType.channel_icon_change:
    embed.add_field(name="System message", value="This is a system message indicating that someone changed the group's icon.", inline=False)
  elif message.type == discord.MessageType.pins_add:
    embed.add_field(name="System message", value="This is a system message indicating that someone pinned a message.", inline=False)
  elif message.type == discord.MessageType.new_member:
    embed.add_field(name="System message", value="This is a system message indicating that someone joined the server.", inline=False)
  elif message.type == discord.MessageType.premium_guild_subscription:
    embed.add_field(name="System message", value="This is a system message indicating that someone nitro-boosted the server.", inline=False)
  elif message.type == discord.MessageType.premium_guild_tier_1:
    embed.add_field(name="System message", value="This is a system message indicating that someone nitro-boosted the server. It is now level 1.", inline=False)
  elif message.type == discord.MessageType.premium_guild_tier_2:
    embed.add_field(name="System message", value="This is a system message indicating that someone nitro-boosted the server. It is now level 2.", inline=False)
  elif message.type == discord.MessageType.premium_guild_tier_3:
    embed.add_field(name="System message", value="This is a system message indicating that someone nitro-boosted the server. It is now level 3.", inline=False)
  elif message.type == discord.MessageType.channel_follow_add:
    embed.add_field(name="System message", value="This is a system message indicating that someone followed another server's announcement.", inline=False)
  if message.application != None:
    embed.add_field(name=message.application[name], value=f"This message is created by {message.application[name]}.\n{message.application[description]}", inline=False)
  if len(f0vraw) != 0:
    embed.add_field(name="Reactions ("+str(len(f0vraw))+")", value=f0v, inline=False)
  if len(f1vraw) != 0:
    embed.add_field(name="Attachments ("+str(len(f1vraw))+")", value=f1v, inline=False)
  if len(f2vraw) != 0:
    embed.add_field(name="Channel mentions ("+str(len(f2vraw))+")", value=f2v, inline=False)
  if len(f3vraw) != 0:
    embed.add_field(name="Role mentions ("+str(len(f3vraw))+")", value=f3v, inline=False)
  if len(f4vraw) != 0:
    embed.add_field(name="User mentions ("+str(len(f4vraw))+")", value=f4v, inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def voicechannel(ctx, channel: discord.VoiceChannel):
  ti="Voice Channel Information"
  desc=channel.name
  embed=discord.Embed(title=ti, description=desc)
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
async def leftuser(ctx, *, userinput):
  global bot
  lfuser = await bot.fetch_user(int(userinput))
  ti="Left User Information"
  if lfuser == None:
    lfuser = ctx.author
  bottrue = lfuser.bot
  if bottrue == True:
    desc = f"{lfuser.mention} (bot)"
  else:
    desc = f"{lfuser.mention} (human)"
  embed=discord.Embed(title=ti,color=lfuser.color, description=desc)
  embed.set_thumbnail(url=lfuser.avatar_url)
  f0v=f"{lfuser.name}#{lfuser.discriminator}"
  f1v=lfuser.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  f1ts = str(datetime.datetime.now() - lfuser.created_at)
  if f1ts.count(" days, ") == 0:
    f1va = re.sub(r'(\d{1,2}):(\d{2}):(\d{2})', r'\1 hours \2 minutes \3 seconds', f1ts) + f"\n≈ "+f1ts.split(":")[0]+" hours"
  else:
    days = int(re.sub(r'([\d]+) days, [\s\S]*', r'\1', f1ts))
    f1va = re.sub(r'([\d]+) days, (\d{1,2}):(\d{2}):(\d{2})', r'\1 days \2 hrs \3 mins \4 secs', f1ts)[:-7] + f"\n≈ "+str((int(f1ts.split(" days, ")[0]))//365) + " years " + str(int(f1ts.split(" days, ")[0]) % 365) + " days"
  embed.add_field(name="Name", value=f0v, inline=False)
  embed.add_field(name="Time since user registered", value=f1va, inline=True)
  embed.add_field(name="Registered", value=f1v, inline=True)
  await ctx.send(embed=embed)

@bot.command()
async def user(ctx, user: discord.Member = None, channel: discord.TextChannel = None):
  ti="User Information"
  if user==None:
    user=ctx.author
  if channel==None:
    channel=ctx.channel
  bottrue = user.bot
  if bottrue == True:
    desc=f"{user.mention} (bot)"
  else:
    desc=f"{user.mention} (human)"
  embed=discord.Embed(title=ti,color=user.color, description=desc)
  embed.set_thumbnail(url=user.avatar_url)
  if user.name==user.display_name:
    f0v=f"{user.name}#{user.discriminator}"
  else:
    f0v=f"{user.name}#{user.discriminator} (__Nickname:__  `{user.display_name}`)"
  f1v=user.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  f1ts = str(datetime.datetime.now() - user.created_at)
  if f1ts.count(" days, ") == 0:
    f1va = re.sub(r'(\d{1,2}):(\d{2}):(\d{2})', r'\1 hours \2 minutes \3 seconds', f1ts) + f"\n≈ "+f1ts.split(":")[0]+" hours"
  else:
    days = int(re.sub(r'([\d]+) days, [\s\S]*', r'\1', f1ts))
    f1va = re.sub(r'([\d]+) days, (\d{1,2}):(\d{2}):(\d{2})', r'\1 days \2 hrs \3 mins \4 secs', f1ts)[:-7] + f"\n≈ "+str((int(f1ts.split(" days, ")[0]))//365) + " years " + str(int(f1ts.split(" days, ")[0]) % 365) + " days"
  f2v=user.joined_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  f2ts = str(datetime.datetime.now() - user.joined_at)
  if f2ts.count(" days, ") == 0:
    f2va = re.sub(r'(\d{1,2}):(\d{2}):(\d{2})', r'\1 hours \2 minutes \3 seconds', f2ts) + f"\n≈ "+f2ts.split(":")[0]+"hours"
  else:
    f2va = re.sub(r'([\d]+) days, (\d{1,2}):(\d{2}):(\d{2})', r'\1 days \2 hrs \3 mins \4 secs', f2ts)[:-7] + f"\n≈ "+str((int(f2ts.split(" days, ")[0]))//365) + " years " + str(int(f2ts.split(" days, ")[0]) % 365) + " days"
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
  
  f3ve=""
  if user.guild_permissions.connect:
    f3ve=f3ve+"Connect, "
  if user.guild_permissions.speak:
    f3ve=f3ve+"Speak (Audio), "
  if user.guild_permissions.stream:
    f3ve=f3ve+"Stream (Video), "
  if user.guild_permissions.use_voice_activation:
    f3ve=f3ve+"Use Voice Activity, "
  if user.guild_permissions.priority_speaker:
    f3ve=f3ve+"Priority Speaker, "
  if user.guild_permissions.mute_members:
    f3ve=f3ve+"Mute Memvers, "
  if user.guild_permissions.deafen_members:
    f3ve=f3ve+"Deafen Members, "
  if user.guild_permissions.move_members:
    f3ve=f3ve+"Move Members, "
  if user.guild_permissions.request_to_speak:
    f3ve=f3ve+"Request to Speak, "
  f3ve=f3ve[:-2]
  if f3ve=="":
    f3ve="No permissions"
  
  if user.status == discord.Status.online:
    f3vd = "Online"
  elif user.status == discord.Status.idle:
    f3vd = "Idle"
  elif user.status == discord.Status.dnd:
    f3vd = "Do Not Disturb"
  elif user.status == discord.Status.offline:
    f3vd = "Offline"
  else:
    f3vd = "Unknown"
  f3vcraw = user.activity
  try:
    if f3vcraw.type.playing:
      try:
        f3vc = f"Playing {f3vcraw.name} since "+f3vcraw.start.strftime("%d %b, %Y (%a) %H:%M:%S")+f"\n{f3vcraw.details}"
      except:
        f3vc = f"Playing {f3vcraw.name}"
    elif f3vcraw.type.streaming:
      f3vc = f"Streaming [{f3vcraw.name}({f3vcraw.game})]({f3vcraw.url}) via {f3vcraw.platform}\n{f3vcraw.details}"
    elif f3vcraw.type.listening:
      f3vc = f"Listening to {f3vcraw.artist} - {f3vcraw.album}: {f3vcraw.title}\nStarted: "+f3vcraw.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")+f"\n{f3vcraw.details}"
    elif f3vcraw.type.watching:
      try:
        f3vc = f"Watching [{f3vcraw.name}]({f3vcraw.url}) since "+f3vcraw.start.strftime("%d %b, %Y (%a) %H:%M:%S")+f"\n{f3vcraw.details}"
      except:
        f3vc = f"Watching {f3vcraw.name}since "+f3vcraw.start.strftime("%d %b, %Y (%a) %H:%M:%S")
    elif f3vcraw.type.custom:
      try:
        f3vc = f":{f3vcraw.emoji.name}: {f3vcraw.details}"
      except:
        f3vc = f":{f3vcraw.emoji.name}:"
  except:
    1
  f4v=""
  if len(allroles)>1:
    allroles.reverse()
    for count in allroles:
      f4v = f4v + count.mention+" "
    f4v = f4v[:-1]
  else:
    f4v="No roles"
  f5v = ""
  if user.public_flags.staff:
    f5v = f5v + f"**Staff:** The user is a Discord Employee.\n"
  if user.public_flags.partner:
    f5v = f5v + f"**Partner:** The user is a Discord Partner.\n"
  if user.public_flags.hypesquad:
    f5v = f5v + f"**Hypesquad:** The user is a HypeSquad Events member.\n"
  if user.public_flags.early_supporter:
    f5v = f5v + f"**Early Support:** The user is an Early Supporter.\n"
  if user.public_flags.team_user:
    f5v = f5v + f"**Team User:** The user is a Team User.\n"
  if user.public_flags.bug_hunter:
    f5v = f5v + f"**Bug Hunter:** The user is a Bug Hunter.\n"
  if user.public_flags.bug_hunter_level_2:
    f5v = f5v + f"**Bug Hunter 2:** The user is a Bug Hunter (Level 2).\n"
  if user.public_flags.system:
    f5v = f5v + f"**System:** The user is a system user (represents Discord officially).\n"
  if user.public_flags.verified_bot_developer:
    f5v = f5v + f"**Developer:** The user is a Verified Bot Developer.\n"
  if user.public_flags.verified_bot:
    f5v = f5v + f"**✔︎Bot:** The user is a Verified Bot.\n"
  if user.public_flags.hypesquad_bravery:
    f5v = f5v + f"**Hypesquad:** The user is in the Hypesquad Bravery House.\n"
  if user.public_flags.hypesquad_brilliance:
    f5v = f5v + f"**Hypesquad:** The user is in the Hypesquad Brilliance House.\n"
  if user.public_flags.hypesquad_balance:
    f5v = f5v + f"**Hypesquad:** The user is in the Hypesquad Balance House.\n"
  if len(f5v) == 0:
    f5v = "No badges"
  else:
    f5v = f5v[:-1]
  embed.add_field(name="Time since user registered", value=f1va, inline=True)
  embed.add_field(name="Time since user joined", value=f2va, inline=True)
  embed.add_field(name="Name", value=f0v, inline=False)
  embed.add_field(name="Registered", value=f1v, inline=True)
  embed.add_field(name="Joined", value=f2v, inline=True)
  embed.add_field(name="Roles", value=f4v, inline=False)
  embed.add_field(name="Server Permissions", value=f3v, inline=False)
  embed.add_field(name="Channel Permissions", value=f3vb, inline=False)
  embed.add_field(name="Channel Permissions", value=f3ve, inline=False)
  embed.add_field(name="Status", value=f3vd, inline=True)
  try:
    embed.add_field(name="Activity", value=f3vc, inline=True)
  except:
    1
  embed.add_field(name="Badges", value=f5v, inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def ban(ctx, user: discord.User, *, delete : int =0, reason="No reason provided"):
  if ctx.author.permissions_in(ctx.channel).ban_members or bot_admins.count(ctx.author.id)!=0:
    await ctx.guild.ban(user, delete_message_days = delete, reason=reason)
    embed1 = discord.Embed(title=f"You were banned from the server.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    try:
      await user.send(embed=embed1)
    except:
      1
    embed2 = discord.Embed(title=f"{user.name} was banned.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await ctx.send(embed=embed2)
  else:
    await ctx.send("You don't have the required permissions.")

@bot.command()
async def unban(ctx, user: discord.User, *, reason="No reason provided"):
  if ctx.author.permissions_in(ctx.channel).ban_members or bot_admins.count(ctx.author.id)!=0:
    await ctx.guild.unban(user)
    embed1 = discord.Embed(title=f"You were unbanned from the server.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    try:
      await user.send(embed=embed1)
    except:
      1
    embed2 = discord.Embed(title=f"{user.name} was unbanned.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await ctx.send(embed=embed2)
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
  activity = discord.Activity(type=discord.ActivityType.playing, name="with =help", details="=ping to check whether the bot is responsive; =help for a list of commands; =invite to invite the bot to your own server")
  await bot.change_presence(status=discord.Status.idle, activity=activity)
  print("Bot is ready!")

@slash.slash(name="purge", description="Purge a number of messages in the current channel.", options=[create_option(name="Number",description="Amount of messages to purge in the current channel.",option_type=4,required=True)])
async def _purge(ctx, num:int):
  if ctx.author.permissions_in(ctx.channel).manage_messages or bot_admins.count(ctx.author.id)!=0:
    await ctx.channel.purge(limit=num+1)
    await ctx.send("Purging completed.", delete_after = 5)
  else:
    await ctx.send("You don't have the required permissions.")

@slash.slash(name="ban", description="Bans a member.", options=[create_option(name="Member",description="The member to ban.",option_type=6,required=True), create_option(name="Purge-Days",description="The number of days of messages to purge from the user.",option_type=4,required=False), create_option(name="Reason",description="The reason to ban the member, which shows in the audit logs.",option_type=3,required=False)])
async def _ban(ctx, user: discord.User, delete : int =0, reason="No reason provided"):
  if ctx.author.permissions_in(ctx.channel).ban_members or bot_admins.count(ctx.author.id)!=0:
    await ctx.guild.ban(user, delete_message_days = delete, reason=reason)
    embed1 = discord.Embed(title=f"You were banned from the server.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    try:
      await user.send(embed=embed1)
    except:
      1
    embed2 = discord.Embed(title=f"{user.name} was banned.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await ctx.send(embed=embed2)
  else:
    await ctx.send("You don't have the required permissions.")

@slash.slash(name="kick", description="Kicks a member.", options=[create_option(name="Member",description="The member to kick.",option_type=6,required=True), create_option(name="Reason",description="The reason to kick the member, which shows in the audit logs.",option_type=3,required=False)])
async def _kick(ctx, user: discord.Member, reason="No reason provided"):
  if ctx.author.permissions_in(ctx.channel).kick_members or bot_admins.count(ctx.author.id)!=0:
    embed = discord.Embed(title=f"{user.name} was kicked.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await ctx.send(embed=embed)
    embed = discord.Embed(title=f"You were kicked from the server.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    try:
      await user.send(embed=embed)
    except:
      1
    await user.kick(reason=reason)
  else:
    await ctx.send("You don't have the required permissions.")

@slash.slash(name="slowmode", description="Set the slowmode delay for the current channel.", options=[create_option(name="Delay",description="Adjust the slowmode threshold for the current channel.",option_type=4,required=True)])
async def _slowmode(ctx, time:int):
  if ctx.author.permissions_in(ctx.channel).manage_channels or bot_admins.count(ctx.author.id)!=0:
    if 21600>=time>=0:
      await ctx.channel.edit(slowmode_delay = time)
      await ctx.send("Set slowmode to "+str(time)+" second(s) for this channel.")
    else:
      await ctx.send("Please enter an integer between 0 and 21600 (inclusive).")
  else:
    await ctx.send("You do not have the required permissions.")

@slash.slash(name="calc", description="Evaluate a mathematical equation..", options=[create_option(name="Equation",description="A math equation to calculate.",option_type=3,required=True)])
async def _calc(ctx, equation:str):
  output = botcalc(equation)
  if output == "Add_Reaction":
    await ctx.message.add_reaction("👍")
  else:
    await ctx.send(output)

@slash.slash(name="random", description="Draws a random integer between two numbers.", options=[create_option(name="Lower",description="The lower bound.",option_type=4,required=True), create_option(name="Upper",description="The upper bound.",option_type=4,required=True)])
async def _random(ctx, lower:int, upper:int):
  ti="Random number between "+str(lower)+" and "+str(upper)
  rand=ra.randint(lower,upper)
  desc="Your random number is "+str(rand)
  embed=discord.Embed(title=ti, description=desc)
  await ctx.send(embed=embed)

@slash.slash(name="server", description="Shows information about the current server.")
async def _server(ctx):
  1

@slash.subcommand(base = "server", name = "regular", description = "Shows regular information about the current server.")
async def _server_regular(ctx):
  guild=ctx.guild
  ti=guild.name
  desc="Created at "+guild.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")+" by "+str(guild.owner.mention)+f"\nRegion: "+str(guild.region)+f"\n[Server Icon]("+str(guild.icon_url)+")"
  embed=discord.Embed(title=ti, description=desc)
  embed.set_author(name="Server Information",icon_url=guild.icon_url)
  f0v=""
  for count in guild.text_channels:
    if len(f0v+str(count.mention)+" ") > 1024:
      f0v = ""
      for count2 in guild.text_channels:
        if len(f0v+count2.name+" ") > 1024:
          f0v = f0v + "… "
          break
        f0v = f0v + count2.name + " "
      break
    f0v=f0v+str(count.mention)+" "
  f1v=""
  f0v=f0v[:-1]
  if len(guild.voice_channels)==0:
    f1v="No Voice Channels"
  else:
    f1v = ""
    for count in guild.voice_channels:
      f1v = f1v + count.name + ", "
    f1v = f1v[:-2]
    if len(f1v) > 500:
      f1v = ""
      for count in guild.voice_channels:
        if len(f1v + count.name) > 500:
          break
        f1v = f1v+count.name+", "
      f1v = f1v [:-2] + "…"
  f1vb=""
  if len(guild.categories)==0:
    f1vb="No Categories"
  else:
    for count in guild.categories:
      f1vb=f1vb+str(count.name)+", "
    f1vb = f1vb[:-2]
  f1va = ""
  f1valist = guild.roles
  f1valist.reverse()
  for count in f1valist:
    f1va = f1va + count.mention+" "
  f1va = f1va[:-1]
  f2v = str(guild.bitrate_limit//1000)+" kbps"
  f3v = str(guild.filesize_limit//1048576)+" MB"
  f4v = str(guild.emoji_limit)
  f5v = guild.mfa_level
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
  if len(f8v) > 500:
    f8v = ""
    for count in guild.members:
      if len(f8v + count.name) > 500:
        break
      f8v = f8v+count.name+", "
    f8v = f8v [:-2] + "…"
  f10va = str(guild.id)
  f13v = guild.description
  if f13v == None:
    f13v = "No description"
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
  #if guild.default_notifications.all_messages:
  #  embed.add_field(name="Default Notifications", value="Members receive notifications for every message by default.", inline=True)
  #else:
  #  embed.add_field(name="Default Notifications", value="Members only receive notifications for messages they are mentioned in by default.", inline=True)
  if guild.features.count("COMMUNITY")==1:
    embed.add_field(name="Community", value="This is a community server.", inline=True)
  if guild.features.count("WELCOME_SCREEN_ENABLED")==1:
    embed.add_field(name="Welcome Screen", value="The server has enabled the welcome screen.", inline=True)
  if guild.features.count("PUBLIC")==1:
    embed.add_field(name="Public", value="This is a public server.", inline=True)
  embed.add_field(name="Description", value=f13v, inline=False)
  try:
    f11v=" ".join(guild.emojis)
    if len(f11v)!=0:
      embed.add_field(name="Emojis", value=f11v, inline=True)
  except:
    1
  try:
    await ctx.send(embed=embed)
  except:
    f1va = ""
    for count in f1valist:
      if len(f1va + count.name) > 500:
        break
      f1va = f1va + count.name+", "
    f1va = f1va [:-2] + "…"
    embed.set_field_at(3, name="Roles ("+str(len(guild.roles))+")", value=f1va, inline=False)
    await ctx.send(embed=embed)

@slash.subcommand(base = "server", name = "mod", description = "Shows banned members and valid invites for the current server.")
async def _server_mod(ctx):
  guild=ctx.guild
  ti=guild.name
  desc="Created at "+guild.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")+" by "+str(guild.owner.mention)+f"\nRegion: "+str(guild.region)+f"\n[Server Icon]("+str(guild.icon_url)+")"
  embed=discord.Embed(title=ti, description=desc)
  embed.set_author(name="Server Information",icon_url=guild.icon_url)
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
  await ctx.send(embed=embed)

@slash.slash(name="role", description="Shows information about a role.", options=[create_option(name="Role",description="The role to show information for.",option_type=8,required=True)])
async def _role(ctx, role:discord.Role):
  ti="Role Information: "+role.name
  if role==None:
    role=ctx.authortop_role
  desc=role.mention
  embed=discord.Embed(title=ti,color=role.color, description=desc)
  memberlist=role.members
  if len(memberlist) == 0:
    f0v = "No members assigned with this role."
  else:
    f0v = ""
    for count in memberlist:
      f0v = f0v + count.mention + " "
    f0v = f0v[:-1]
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
  embed.add_field(name="Members ("+str(len(memberlist))+")", value=f0v, inline=True)
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

@slash.slash(name="channel", description="Shows information about a channel.", options=[create_option(name="Channel",description="The channel to show information for.",option_type=7,required=True)])
async def _channel(ctx, channel:discord.abc.GuildChannel):
  if channel.type == discord.ChannelType.text:
    ti="Channel Information: "+channel.name
    desc=channel.mention
    embed=discord.Embed(title=ti, description=desc)
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
  elif channel.type == discord.ChannelType.voice:
    ti="Voice Channel Information"
    desc=channel.name
    embed=discord.Embed(title=ti, description=desc)
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

@slash.slash(name="simplecolor", description="Gets information about a named color.", options=[create_option(name="Colour",description="The name of the colour.",option_type=3,required=True)])
async def _simplecolor(ctx):
  botsimpcolor(name)
  try:
    file = discord.File("color.png")
    await ctx.send(file=file)
  except:
    await ctx.send("Invalid colour name, please try again.")

@slash.slash(name="status", description="Shows the status of a member.", options=[create_option(name="Member",description="The name of the colour.",option_type=6,required=True)])
async def _status(ctx, member : discord.Member = None):
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
        try:
          field=":"+count.emoji.name+": "+count.name
        except:
          try:
            field=count.name
          except:
            field=":"+count.emoji.name+":"
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

bot.run('Nzk2Njg2MzYzNjA0NjgwNzU1.X_bh_g.6uKl_EPp5r5XZpSxCxPTIuA69aE')
