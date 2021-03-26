from discord_slash import SlashCommand, SlashContext
from discord import Webhook, RequestsWebhookAdapter
from discord_slash.utils import manage_commands
from unicode_charnames import search_charnames
from datetime import datetime, date, timedelta
from selenium.webdriver.common.by import By
from discord_webhook import DiscordWebhook
from pdf2image import convert_from_path
import selenium.common.exceptions
from discord.ext import commands
import matplotlib.pyplot as plt
from selenium import webdriver
from markdown2 import Markdown
from cmath import *
import random as ra
import emoji as em
import numpy as np
from math import *
import pytesseract
import time as tm
import subprocess
import datetime
import requests
import aiohttp
import asyncio
import pytube
import PIL
import re
import os
from botwebscrape import *
from botwebinfo import *
from botengrave import *
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
slash = SlashCommand(bot)
client = discord.Client()
allid=[]
id_pattern = re.compile(r'([A-Z]{5})', re.IGNORECASE)
alphaend_pattern = re.compile(r'.*[a-z]', re.IGNORECASE)
html_pattern = re.compile(r'^\`\`\`(html)?\n[\s\S]*\`\`\`$')
md_pattern = re.compile(r'^\`\`\`(md|markdown)?\n[\s\S]*\`\`\`$')
verify_pattern = re.compile(r'[^ ⠀][\s\S]{0,30}?[^ ⠀]#?[\d]{4}(,|, | )?[\d+\-*/×÷%xyz()\[\]\{\}]{1,50}=[\d+\-*/×÷%xyz()\[\]\{\}]{1,50}(,|, | )?[\S ]{3,20}(,|, | )?(Red|Orange|Yellow|Green|Light( |_)?Green|Dark( |_)?Green|Cyan|Blue|Light( |_)?Blue|Dark( |_)?Blue|Purple|Pink|Brown)', re.IGNORECASE)
poll_pattern = re.compile(r'([\w]+?)(:\w{2,32}:|[\uD800-\uDBFF])')
UNITS = {'s':'seconds', 'm':'minutes', 'h':'hours', 'd':'days', 'w':'weeks'}
typer=0
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
markdowner = Markdown(extras=["strike", "footnotes"])
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

#@bot.event
#async def on_invite_create(invite):
#  if invite.guild.id == 809368482344075265 or invite.guild.id == 807164404960854026:
#    await invite.delete()

#@bot.event
#  if after.roles.count(before.guild.get_role(810729029790597190)) == 0 and after.guild.id == 809368482344075265 and after.id == 687474789342117900:
#    await after.add_roles(before.guild.get_role(810729029790597190), reason = "Mysterious")

@bot.event
async def on_member_join(member):
  if member.guild.id == 824524455924727839:
    if member.bot:
      await member.add_roles(member.guild.get_role(824524665842040852))
      await member.guild.get_channel(824524893152477206).create_text_channel(member.name.lower().replace(" ","-"),slowmode_delay=1, topic = f"Use and talk about the bot {member.name}.", overwrites={member.guild.default_role: discord.PermissionOverwrite(read_messages=False), member.guild.get_role(824526276835803176): discord.PermissionOverwrite(read_messages=True), member: discord.PermissionOverwrite(read_messages=True)})
    else:
      embed = discord.Embed(title = "Welcome", desc="Hello and welcome to Bot Laboratoratory! You can add any bot to this server by [proposing](https://discord.gg/etb53Cvheh). Simply send the bot's invite and we will discuss about it. Have fun!")
      await member.send(embed=embed)
  elif member.guild.id == 823405852131328001:
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
  elif sniper5.get(keyname, 1) == 1:
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
      1
  elif message.author.id == 814292078984167425:# and (message.content.count('Joe')==1 or message.content.count('Joh')==1 or message.content.count('Bitch')==1 or message.content.count('Piss')==1):
    await message.delete()#delay = 3)"""#(message.guild.id != 823405852131328001 or message.content.startswith("=verify"))
  if message.author.id != 796686363604680755:
    for count2 in message.guild.emojis:
        if message.content.count(f":{count2.name}:") and count2.animated:
          try:
            await message.delete()
          except:
            1
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
          async with aiohttp.ClientSession() as session:
            webhook = Webhook.partial(identify, token, adapter=RequestsWebhookAdapter())
            await webhook.send(message.content, username=message.author.name, avatar_url=message.author.avatar_url)
          break
    if banned_ids.count(message.author.id)==0 and message.content.startswith("=") and message.content.startswith("==")==False:
      await bot.process_commands(message)
    elif message.content.startswith("="):
      await message.channel.send("You are banned from the bot. Reason: "+banned_text[banned_ids.index(message.author.id)])

@bot.command()
async def unicode(ctx, *, query):
  embed = discord.Embed(title = "Search results for: "+query)
  allchars = search_charnames(query)
  for count, count2 in zip(allchars, range(0,25)):
    try:
      embed.add_field(name=count[0], value="\u"+count[0]+" "+count[1], inline=False)
    except:
      embed.add_field(name=count[0], value=count[1], inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def verify(ctx):
  if ctx.message.guild.id == 823405852131328001:
    if ctx.author.roles.count(ctx.guild.get_role(823407479303569419))==1:
      overdict = ctx.message.guild.get_channel(823410283723620362).overwrites
      verifiedmem = list(overdict)[0]
      theinvite = await bot.get_guild(806083349688877077).get_channel(806085319521992705).create_invite(max_age=300, max_uses=1)
      desc = "You are verified! Please use [this invite]("+theinvite.url+") to join the Historical Community server. It would expire in 5 minutes. Have fun!"
      embed = discord.Embed(title="Verified", description=desc)
      await ctx.author.send(embed=embed)
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
  cmaphsv = plt.cm.hsv
  mycolors = []
  for count in range(0, len(numlist)):
    mycolors.append(cmaphsv(count/len(numlist)))
  plt.pie(y, labels=labels, colors=mycolors, autopct=lambda pct: func(pct, y), textprops = {'color':"w"})
  plt.legend(loc="lower right")
  plt.title("Reaction Status")
  plt.savefig("reactions.png", transparent=True)
  await ctx.send(file = discord.File('reactions.png'))
  plt.clf()

#@bot.command()

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
      optn = re.sub(poll_pattern, r'\1', em.demojize(count))
      rect = re.sub(poll_pattern, r'\2', em.demojize(count))
      desc = desc + f"{rect} {optn} (0)\n"
      options.append(optn)
      reactions.append(em.emojize(rect))
    else:
      ti = ti + count + " "
  embed = discord.Embed(title = ti, description = em.emojize(desc))
  poll = await ctx.send(embed=embed)
  for count in reactions:
    await poll.add_reaction(count) 

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
  if ctx.author.id == 687474789342117900:
    await ctx.guild.get_member(796686363604680755).edit(nick = newnick)
    await ctx.send("Nickname changed.")
  else:
    await ctx.send("You don't have the required permissions.")

@bot.command()
async def tts(ctx, *, desc):
  await ctx.send(desc, tts = True)

"""@slash.slash(name="help", description = "View all commands of the bot.", options=[manage_commands.create_option(name = "cat", description = "Category of command you need help with.", option_type = 3, required = False)], guild_ids = [809368482344075265, 807164404960854026, 744520955585626132, 813688458819928066, 336642139381301249, 806083349688877077, 806011717418090497, 802834833554014208, 805441351033552916])
async def _help(ctx: SlashContext, *, cat = None):
  embed = bothelp(cat)
  await ctx.respond()
  await ctx.send(embed=embed)"""

@bot.command()
async def raw(ctx, msg : discord.Message):
  embed = discord.Embed(title = "Raw message", url = msg.jump_url, description = "```"+msg.content+"```")
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
async def botban(ctx, user : discord.User, *, text="No reason was provided"):
  if ctx.author.id == 687474789342117900:
    banned_ids.append(user.id)
    banned_text.append(text)
    await ctx.send("Banned user from using the bot.")

@bot.command()
async def botunban(ctx, user : discord.User):
  if ctx.author.id == 687474789342117900 and banned_ids.count(user.id) == 1:
    banned_text.remove(banned_text[banned_ids.index(user.id)])
    banned_ids.remove(user.id)
    await ctx.send("Unbanned user from using the bot.")

@bot.command()
async def botadmin(ctx, user : discord.User):
  if ctx.author.id == 687474789342117900:
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
    print(6)
    await ctx.send("You don't have the required permissions.")

@bot.command()
async def engrave(ctx, product = "list", *, text = "Your text goes here."):
  embed = botengrave(product, text)
  await ctx.send(embed=embed)

@bot.command()
async def python(ctx, *, script):
  output = botpython(script)
  await ctx.send(output)

"""@bot.command()
async def cleanup(ctx, *, text = None):
  for count in bot.get_guild(814407577042944040).channels:
    if count.name != "embed" and count.name != "spam":
      await count.delete()
  for count in bot.get_guild(814407577042944040).roles:
    if count.name == "fucker":
      await count.delete()"""

@bot.command()
async def regex(ctx, regularexp, *, text):
  theregex = r"(?P<LargestCapturingGroup>"+regularexp+")"
  newtext = re.sub(theregex, "**\g<LargestCapturingGroup>**", text)
  matches = len(re.findall(theregex, text))
  if matches == 1:
    ti = "There was 1 occurrence."
  elif matches == 0:
    ti = "There was no occurrences."
  elif matches >= 2:
    ti = "There were "+str(matches)+" occurrences."
  embed = discord.Embed(title = ti, description = newtext.replace("****",""))
  embed.set_author(name="Match Results for "+regularexp)
  embed.set_footer(text="Match Results are highlighted in bold")
  await ctx.send(embed=embed)

@bot.command()
async def regsub(ctx, regular1, regular2, *, text):
  newtext = re.sub(regular1, regular2, text)
  matches = len(re.findall(regular1, text))
  if matches == 1:
    ti = "There was 1 occurrence."
  elif matches == 0:
    ti = "There was no occurrences."
  elif matches >= 2:
    ti = "There were "+str(matches)+" occurrences."
  embed = discord.Embed(title = ti, description = "`"+newtext+"`")
  embed.set_author(name="Substitution Result for "+regular1)
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
  if output == "Invalid item. Please try again.":
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

@bot.command(alias=["simpcolour", "simplecolor", "simplecolour"])
async def simpcolor(ctx, *, name):
  fig, ax = plt.subplots()
  ax.axes.get_xaxis().set_visible(False)
  ax.axes.get_yaxis().set_visible(False)
  try:
    cmapv = plt.get_cmap(name)
    plt.setp(ax.spines.values(), color="w")
    gradient = np.vstack((np.linspace(0, 1, 256), np.linspace(0, 1, 256)))
    ax.set_facecolor("w")
    ax.imshow(gradient, aspect='auto', cmap=cmapv)
    plt.savefig("color.png", transparent=True)
  except:
    plt.setp(ax.spines.values(), color=name)
    ax.set_facecolor(name)
    plt.savefig("color.png", transparent=True)
    plt.clf()
  file = discord.File("color.png")
  await ctx.send(file=file)

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
async def hist(ctx, numbers, *, title="No_title_required"):
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
        field=":"+count.emoji.name+":"+count.name
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
async def speedtest(ctx, *, text = None):
  total=0
  now1 = datetime.datetime.now()
  message = await ctx.send("Pong!")
  mcs = (datetime.datetime.now() - now1).microseconds
  total = total + mcs
  for count in range(1,6):
    now1 = datetime.datetime.now()
    await message.edit(content="Pong! "+str(mcs)+" microseconds  (Test "+str(count)+")")
    mcs = (datetime.datetime.now() - now1).microseconds
    total = total + mcs
  avg = int(total/6)
  await message.edit(content=f"Pong!\nTotal time: "+str(total)+f" mcs\nAverage time: "+str(avg)+" mcs")

@bot.command()
async def screenshot(ctx, url = None, form = "all"):
  a = botscreenshot(url, form)
  if a == "Invalid format! Please use the format `=screenshot [url]`.":
    await ctx.send(a)
  else:
    #try:
    await ctx.send(file=discord.File('web_screenshot1.png'))
    os.remove('web_screenshot1.png')
    #except:
    #  1
    #try:
    await ctx.send(file=discord.File('web_screenshot2.png'))
    os.remove('web_screenshot2.png')
    #except:
    #  1

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
async def emojiinfo(ctx,emojiarg : discord.Emoji):
  ti="Emoji Info"
  creator=await ctx.guild.fetch_emoji(emojiarg.id)
  desc=str(emojiarg)+emojiarg.name+"\nCreated by "+str(creator.user.mention)+" at "+str(emojiarg.created_at.strftime("%d %b, %Y (%a) %H:%M:%S"))
  embed=discord.Embed(title=ti, description=desc)
  embed.add_field(name="ID", value=emojiarg.id, inline=True)
  await ctx.send(embed=embed)

@bot.command()
async def reverse(ctx, *, text):
  text = text[::-1]
  await ctx.send(text)

@bot.command()
async def emoji(ctx, *, text):
  output = botemoji(text)
  await ctx.send(output)

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
  desc=role.mention
  embed=discord.Embed(title=ti,color=role.color, description=desc)
  memberlist=role.members
  if len(memberlist) == 0:
    f0v = "No members assigned with this role."
  else:
    f0v = ""
    for count in memberlist:
      f0v = f0v + count.mention + " "
    f0v = f0v[:-2]
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
async def autochannel(ctx, channel):
  async def voice(channel: discord.VoiceChannel):
    global embed
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
  async def text(channel: discord.TextChannel):
    global embed
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
  #try:
  await text(channel)
  #except:
  #  await voice(channel)
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
    f0v=f"{user.name}#{user.discriminator} (__Nickname:__  {user.display_name})"
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
  embed.add_field(name="Status", value=f3vd, inline=True)
  try:
    embed.add_field(name="Activity", value=f3vc, inline=True)
  except:
    1
  embed.add_field(name="Badges", value=f5v, inline=False)
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

"""@bot.command(pass_context=True)
async def spam(ctx,times,*,message):
  if (int(times)<5 and message.count("@")==0) or bot_admins.count(ctx.author.id)!=0:
    try:
      await ctx.message.delete()
    except:
      1
    for count in range(0,int(times)):
      await ctx.send(message)
  else:
    await ctx.send("Please spam less than 5 times without any pings.")"""

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
  """for count in bot.get_guild(814407577042944040).channels:
    if count.name != "embed" and count.name != "spam":
      await count.delete()
  for count in bot.get_guild(814407577042944040).roles:
    if count.name == "fucker":
      await count.delete()"""

from discord_slash import SlashCommand # Importing the newly installed library.

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.

@slash.slash(name="ping", guild_ids=[744520955585626132, 814407577042944040])
async def _ping(ctx):
  await ctx.send(f"Pong! ({client.latency*1000}ms)")

@slash.slash(name="calc", guild_ids=[744520955585626132, 814407577042944040], options=[create_option(name="equation",description="Enter a math equation here.",option_type=3,required=False,)])
async def _calc(ctx):
  output = botcalc(arg)
  if output == "Add_Reaction":
    await ctx.message.add_reaction("👍")
  else:
    await ctx.send(output)

bot.run('Nzk2Njg2MzYzNjA0NjgwNzU1.X_bh_g.8LrZQX__nLUKyXDgpOt5bLnEN7Q')
#client.run('Nzk2Njg2MzYzNjA0NjgwNzU1.X_bh_g.8LrZQX__nLUKyXDgpOt5bLnEN7Q')
