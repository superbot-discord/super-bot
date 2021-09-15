import asyncio
import datetime
import hashlib
import os
import random as ra
import re
import base64
import typing
from cmath import *
from datetime import datetime, timedelta, timezone
from difflib import SequenceMatcher
from math import *

import aiohttp
import ascii as asc
import emojis as ems
import matplotlib.pyplot as plt
import numpy as np
import PIL
import pytesseract
import pytube
import qr_img
import requests
from captcha.image import ImageCaptcha
from discord import Webhook
from discord.ext import commands
# from discord_slash import SlashCommand, SlashContext
# from discord_slash.utils.manage_commands import create_choice, create_option
from pdf2image import convert_from_path
from unicode_charnames import search_charnames

from botanimals import *
from botbasic import *
from botdinfo import *
from botembed import *
from botengrave import *
from botinfo import *
from botmoderate import *
from botplot import *
from botpycalc import *
from botwebinfo import *
from botwebscrape import *
from simplecolour import simple_colours_raw

# simple_colours_options = []
# for count in simple_colours_raw:
  # simple_colours_options.append(create_choice(value=count[1], name=count[0]))

banned_ids = []
banned_text = []
bot_admins = [687474789342117900]
bot = commands.Bot(command_prefix=commands.when_mentioned_or("="), intents=discord.Intents.all(), case_insensitive=True)
bot.remove_command('help')
bot.load_extension("botdinfo")
bot.load_extension("botplot")
bot.load_extension("botanimals")
bot.load_extension("botengrave")
bot.load_extension("botpycalc")
# slash = SlashCommand(bot)
id_pattern = re.compile(r'([A-Z]{5})', re.IGNORECASE)
verify_pattern = re.compile(r'[^ ⠀][\s\S]{0,30}?[^ ⠀]#?[\d]{4}(,|, | )?[\d+\-*/×÷%xyz()\[\]\{\}]{1,50}=[\d+\-*/×÷%xyz()\[\]\{\}]{1,50}(,|, | )?[\S ]{3,20}(,|, | )?(Red|Orange|Yellow|Green|Light( |_)?Green|Dark( |_)?Green|Cyan|Blue|Light( |_)?Blue|Dark( |_)?Blue|Purple|Pink|Brown)', re.IGNORECASE)
poll_pattern = re.compile(r'([\w]+?)(:\w{2,32}:|[\uD800-\uDBFF])')
UNITS = {'s':'seconds', 'm':'minutes', 'h':'hours', 'd':'days', 'w':'weeks'}
image = ImageCaptcha()
typer=0
cmaphsv = plt.cm.hsv
sniper1=sniper2=sniper3=sniper4=sniper5=sniperdate1=sniperdate2=sniperdate3=sniperdate4=sniperdate5=sniperdict=sniping=poll_options={}
snipereactions=polls=allid=[]
overwrite = discord.PermissionOverwrite()
overwrite.view_channel = True

botadmin = lambda context : context.author.id == 687474789342117900
func = lambda pct, allvals : "{:d} ({:.1f}%)".format(int(pct/100*np.sum(allvals)), int(pct))
number_to_emoji = lambda a: a.replace("1",":one: ").replace("2",":two: ").replace("3",":three: ").replace("4",":four: ").replace("5",":five: ").replace("6",":six: ").replace("7",":seven: ").replace("8",":eight: ").replace("9",":nine: ").replace("0",":zero: ")
sizer = lambda bytes: f"{round(bytes/1024,4):,}KB" if bytes<1048576 else (f"{round(bytes/1048576,4):,}MB" if bytes<1073741824 else f"{round(bytes/1073741824,4):,}GB")
format_length=lambda secs: f"{str(secs//86400)} days plus {str(secs%21600//3600).zfill(2)}:{str(secs%3600//60).zfill(2)}:{str(secs%60).zfill(2)}" if secs >= 86400 else (f"{str(secs//3600).zfill(2)}:{str(secs%3600//60).zfill(2)}:{str(secs%60).zfill(2)}" if secs >= 3600 else f"{str(secs//60).zfill(2)}:{str(secs%60).zfill(2)}")

@bot.event
async def on_voice_state_update(member, before, after):
  try:
    if before.channel.id == 822750915466493982 and after.channel == None:
      supchat = member.guild.get_channel(822753048510070784)
      await supchat.purge(limit=1000)
      await supchat.set_permissions(member, overwrite=None)
  except:
    pass
  try:
    if before.channel == None and after.channel.id == 822750915466493982:
      supchat = member.guild.get_channel(822753048510070784)
      await supchat.purge(limit=1000)
      await supchat.set_permissions(member, overwrite=overwrite)
  except:
    pass

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
  msg = reaction.message
  if msg in snipereactions and user.id != 796686363604680755:
    keyname = str(msg.guild.id)+str(msg.channel.id)
    if reaction.emoji == '⏪':
      sniperdict[msg] = 1
    elif reaction.emoji == '⬅️' and sniperdict[msg] > 1:
      sniperdict[msg] = sniperdict[msg] - 1
    elif reaction.emoji == '📌' and msg.pinned == False and msg.channel.permissions_for(msg.guild.get_member(796686363604680755)).manage_messages:
      await msg.pin()
      pinmsg = await msg.channel.fetch_message(msg.channel.last_message_id)
      await pinmsg.delete()
    elif reaction.emoji == '📌' and msg.pinned == False and msg.channel.permissions_for(msg.guild.get_member(796686363604680755)).manage_messages:
      await msg.unpin()
    elif reaction.emoji == '📌':
      await msg.channel.send("Unable to Pin/Unpin messages without `Manage Server` permission.")
      return
    elif reaction.emoji == '➡️' and sniperdict[msg] <5 and eval('sniper'+str(sniperdict[msg]+1)+'.get(keyname, 1)') != 1:
      sniperdict[msg] = sniperdict[msg] + 1
    elif reaction.emoji == '⏩' and sniper5.get(keyname, 1) != 1:
      sniperdict[msg] = 5
    elif reaction.emoji == '⏩' and sniper4.get(keyname, 1) != 1:
      sniperdict[msg] = 4
    elif reaction.emoji == '⏩' and sniper3.get(keyname, 1) != 1:
      sniperdict[msg] = 3
    elif reaction.emoji == '⏩' and sniper2.get(keyname, 1) != 1:
      sniperdict[msg] = 2
    elif reaction.emoji == '⏩' and sniper1.get(keyname, 1) != 1:
      sniperdict[msg] = 1
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
    ti = "Snipped message ("+str(sniperdict[msg])+r"/"+str(maxc)+")"
    desc = eval('sniper'+str(sniperdict[msg])+'[keyname]')
    foot = eval('sniperdate'+str(sniperdict[msg])+'[keyname]')
    embed = discord.Embed(title=ti, description=desc)
    embed.set_footer(text=foot)
    await msg.edit(embed=embed)
  elif msg.id in polls and user.id != 796686363604680755:
    cache_embed = msg.embeds[0]
    desc = ""
    msg_dict = poll_options[msg.id]
    for count in msg_dict.keys():
      current_reaction = ems.encode(msg_dict[count])
      await msg.add_reaction(current_reaction)
      for count2 in msg.reactions:
        if count2.emoji == current_reaction:
          current_reaction = count2.emoji
          counter = 0
          async for count3 in count2.users():
            if count3.id != 796686363604680755:
              counter = counter + 1
          desc = desc + f"{count2.emoji} {count} ("+ str(counter) +f")\n"
    cache = discord.Embed(title = cache_embed.title, description = em.encode(desc))
    await msg.edit(embed=cache)

@bot.event
async def on_reaction_remove(reaction, user):
  msg = reaction.message
  if msg.id in polls and user.id != 796686363604680755:
    cache_embed = msg.embeds[0]
    desc = ""
    msg_dict = poll_options[msg.id]
    for count in msg_dict.keys():
      current_reaction = ems.encode(msg_dict[count])
      await msg.add_reaction(current_reaction)
      for count2 in msg.reactions:
        if count2.emoji == current_reaction:
          current_reaction = count2.emoji
          counter = 0
          async for count3 in count2.users():
            if count3.id != 796686363604680755:
              counter = counter + 1
          desc = desc + f"{count2.emoji} {count} ("+ str(counter) +f")\n"
    cache = discord.Embed(title = cache_embed.title, description = em.encode(desc))
    await msg.edit(embed=cache)

# @bot.event
# async def on_command_error(ctx, error):
#   if isinstance(error, commands.CommandNotFound):
#     message = ctx.message
#     used_prefix = ctx.prefix
#     used_command = message.content.split()[0][len(used_prefix):]
#     available_commands = [cmd.name for cmd in bot.commands]
#     matches = {cmd: SequenceMatcher(None, cmd, used_command).ratio() for cmd in available_commands}
#     command = max(matches.items(), key=lambda item: item[1])[0]
#     try:
#       arguments = message.content.split(" ", 1)[1]
#     except IndexError:
#       arguments = ""
#     new_content = f"{used_prefix}{command} {arguments}".strip()
#     message.content = new_content
#     await ctx.send(f'Your might have made a typo and your command has been interpreted as {command}.', delete_after=4)
#     await bot.process_commands(message)
#   elif isinstance(error, commands.MissingRequiredArgument):
#     await ctx.send(f'You missed one or more arguments! {len(ctx.command.clean_params.keys())} argument(s) are required.\nNote: Multiline arguments are treated as one argument.')
#   else:
#     print(error.with_traceback(error.__traceback__))


@bot.event
async def on_message(message):
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
              pass
            async with aiohttp.ClientSession() as session:
              webhook = Webhook.partial(identify, token, session=session)
              await webhook.send(desc, username=message.author.name, avatar_url=message.author.avatar.url)
            break
    except:
      pass
    if banned_ids.count(message.author.id)==0 and message.content.startswith("=") and message.content.startswith("==")==False:
      await bot.process_commands(message)
    elif message.content.startswith("="):
      await message.channel.send("You are banned from the bot. Reason: "+banned_text[banned_ids.index(message.author.id)])

@bot.command()
async def unicode(ctx, *, query):
  allchars = search_charnames(query)
  embed = discord.Embed(title = "Search results for: "+query)
  for count, count2 in zip(allchars, range(0,25)):
    embed.add_field(name = count[1].title(), value = "U+" + count[0] + eval("u\" \\u"+count[0]+"\""))
  await ctx.send(embed=embed)

@bot.command()
async def encode(ctx, code, *, text):
  if SequenceMatcher(None, code, 'sha512').ratio()>0.6:
    coder = hashlib.sha512()
    coder.update(bytes(text, encoding='utf-8'))
    await ctx.send(coder.hexdigest())
  elif SequenceMatcher(None, code, 'sha384').ratio()>0.6:
    coder = hashlib.sha384()
    coder.update(bytes(text, encoding='utf-8'))
    await ctx.send(coder.hexdigest())
  elif SequenceMatcher(None, code, 'sha256').ratio()>0.6:
    coder = hashlib.sha256()
    coder.update(bytes(text, encoding='utf-8'))
    await ctx.send(coder.hexdigest())
  elif SequenceMatcher(None, code, 'sha224').ratio()>0.6:
    coder = hashlib.sha224()
    coder.update(bytes(text, encoding='utf-8'))
    await ctx.send(coder.hexdigest())
  elif SequenceMatcher(None, code, 'sha128').ratio()>0.6:
    coder = hashlib.sha1()
    coder.update(bytes(text, encoding='utf-8'))
    await ctx.send(coder.hexdigest())
  elif SequenceMatcher(None, code, 'base64').ratio()>0.6:
    coder = base64.b64encode(bytes(text, encoding='utf-8'))
    await ctx.send(coder.decode("utf-8"))
  elif SequenceMatcher(None, code, 'base32').ratio()>0.6:
    coder = base64.b32encode(bytes(text, encoding='utf-8'))
    await ctx.send(coder.decode("utf-8"))
  elif SequenceMatcher(None, code, 'base16').ratio()>0.6:
    coder = base64.b16encode(bytes(text, encoding='utf-8'))
    await ctx.send(coder.decode("utf-8"))
  else:
    await ctx.send("Encoding not found!")

@bot.command()
async def decode(ctx, code, *, text):
  if SequenceMatcher(None, code, 'base64').ratio()>0.6:
    coder = base64.b64decode(bytes(text, encoding='utf-8'))
    await ctx.send(coder.decode("utf-8"))
  elif SequenceMatcher(None, code, 'base32').ratio()>0.6:
    coder = base64.b32decode(bytes(text, encoding='utf-8'))
    await ctx.send(coder.decode("utf-8"))
  elif SequenceMatcher(None, code, 'base16').ratio()>0.6:
    coder = base64.b16decode(bytes(text, encoding='utf-8'))
    await ctx.send(coder.decode("utf-8"))
  else:
    await ctx.send("Encoding not found!")

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
async def verify(ctx):
  if ctx.message.guild.id == 823405852131328001 and ctx.author.roles.count(ctx.guild.get_role(823407479303569419))==1:
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
  labels = []
  for counter in reactions:
    numlist.append(counter.count)
    try:
      labels.append(em.decode(counter.emoji))
    except:
      labels.append("*"+counter.emoji.name)
  labels = tuple(labels)
  y = np.array(numlist)
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
  chnl = ctx.channel
  keyname = str(ctx.guild.id)+str(chnl.id)
  if text == None:
    if sniping.get(keyname, 1) == 1 or sniping[keyname] == True:
      if sniper1.get(keyname, 1) == 1:
        ti = "Error"
        desc = "Nothing to snipe from this channel."
        embed = discord.Embed(title=ti, description=desc)
        await ctx.send(embed=embed)
        return
      else:
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
  elif chnl.permissions_for.manage_messages:
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
  poll_options_cache = {}
  for count in textlist: # ([\w]+?)(:\w{2,32}:|[\uD800-\uDBFF])
    match = poll_pattern.fullmatch(em.decode(count))
    if match:
      optn = re.sub(poll_pattern, r'\1', ems.decode(count))
      rect = re.sub(poll_pattern, r'\2', ems.decode(count))
      desc = desc + f"{rect} {optn} (0)\n"
      options.append(optn)
      poll_options_cache[optn] = rect
      reactions.append(ems.encode(rect))
    else:
      ti = ti + count + " "
  embed = discord.Embed(title = ti, description = em.encode(desc))
  poll = await ctx.send(embed=embed)
  for count in reactions:
    await poll.add_reaction(count)
  polls.append(poll.id)
  poll_options[poll.id] = poll_options_cache

@bot.command()
async def unscramble(ctx, text, length="0"):
  output = botunscramble(text, length)
  await ctx.send(embed=output, file=discord.File("output.txt"))
  os.remove('output.txt')

pytube.YouTube.author

@bot.command()
async def youtube(ctx, *, link):
  if link.startswith("search"):
    videos = pytube.Search(link.replace("search ", "", 1)).results[0:20]
    desc = ""
    for count in videos:
      desc+=f"**[{count.title}]({count.watch_url})**\n{count.views:,} Views | By [{pytube.Channel(count.channel_url).channel_name}]({count.channel_url})\n"
    embed = discord.Embed(title="Search results", description=desc)
    embed.set_footer(text="Use =youtube [Link] to download videos.")
    await ctx.send(embed=embed)
  elif link.startswith("channel"):
    chnl = pytube.Channel(link)
    videos = chnl.videos
    desc = f"**Videos ({len(chnl.videos):,})**:\n"
    for count,count2 in zip(videos, range(0,12)):
      desc+=f"[{count.title}]({count.watch_url})\n{count.views:,} Views | {str(count.rating*20)}% Liked\n\n"
    embed = discord.Embed(title=chnl.channel_name, description=desc, url=chnl.videos_url)
    embed.set_footer(text=f"{chnl.views:,} Channel views | Use =youtube [Link] to download videos. | Analysing additional info…")
    yt_msg = await ctx.send(embed=embed)
    totallen = 0
    totalrating = 0
    for count in videos:
      totallen += count.length
      totalrating += count.rating
    embed.add_field(name="Average length", value=format_length(round(totallen/len(videos))), inline=True)
    embed.add_field(name="Average rating", value=round(totalrating/len(videos), 3), inline=True)
  else:
    try:
      playlist = pytube.Playlist(link)
      text = ""
      for count in playlist.videos:
        text=text+str(count)+"  "+count.streams.filter(mime_type="video/mp4").filter(progressive="True").filter(type="video").order_by("resolution").first().url+f"\n"
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
      yt_streams = youtube.streams
      filtered1 = yt_streams.filter(progressive=True,file_extension='mp4').order_by("resolution")
      video1 = filtered1[len(filtered1)-1]
      additional_desc = " Warning: Do not use a small data plan for videos this large!" if video1.filesize >= 52428800 else ""
      desc = f"This video has a size of around {sizer(video1.filesize)}.{additional_desc}"
      embed = discord.Embed(title="Download (Click here)", url=video1.url, description=f"{desc}\nNote: This message will be edited with more information.")
      filtered2 = yt_streams.filter(type="video").order_by("resolution")
      video2 = filtered2[len(filtered2)-1]
      filtered3 = yt_streams.filter(type="audio").order_by("abr")
      video3 = filtered3[len(filtered3)-1]
      filtered4 = yt_streams.filter(type="video").order_by("resolution")
      video4 = filtered4[int(len(filtered4)/2)]
      filtered5 = yt_streams.filter(type="audio").order_by("abr")
      video5 = filtered5[len(filtered5)-1]
      filtered6 = yt_streams.filter(type="video").order_by("filesize")
      video6 = filtered6[0]
      filtered7 = yt_streams.filter(type="audio").order_by("filesize")
      video7 = filtered7[0]
      filtered8 = yt_streams.filter(type="video", progressive=True).order_by("filesize")
      video8 = filtered8[0]
      extra_downloads=f'''[Frames only - Best quality]\t{sizer(video2.filesize)}\t{video2.url}\n\n[Audio - Best quality]\t\t{sizer(video3.filesize)}\t{video3.url}\n
[Video - Medium quality]\t{sizer(video4.filesize)}\t{video4.url}\n\n[Audio - Medium quality\t\t{sizer(video5.filesize)}\t{video5.url}\n
[Video - Minimum size]\t\t{sizer(video6.filesize)}\t{video6.url}\n\n[Audio - Minimum size]\t\t{sizer(video7.filesize)}\t{video7.url}\n
[Video+audio - Minimum size]\t{sizer(video6.filesize)}\t{video8.url}'''
      f = open('extra_downloads.txt', "w")
      f.write(extra_downloads)
      f.close()
      ytmsg = await ctx.send(embed=embed, file=discord.File('extra_downloads.txt'))
      os.remove('extra_downloads.txt')
      embed = discord.Embed(title="Download (Click here)", url=video1.url, description=desc)
      embed.add_field(name="Title", value=youtube.title, inline=False)
      if len(youtube.description[:1023].replace(" ", "")) == 0:
        embed.add_field(name="Description", value="No description provided", inline=False)
      else:
        embed.add_field(name="Description", value=youtube.description[:1023], inline=False)
      if len(youtube.keywords) == 0:
        embed.add_field(name="Tags", value="No tags provided", inline=False)
      else:
        embed.add_field(name="Tags", value=(", ".join(youtube.keywords))[:1023], inline=False)
      embed.add_field(name="Views", value=f'{youtube.views:,}', inline=True)
      embed.add_field(name="Date uploaded", value=youtube.publish_date.strftime("%d %b, %Y (%a)"), inline=True)
      embed.add_field(name="Length", value=format_length(youtube.length), inline=True)
      chnl = pytube.Channel(youtube.channel_url)
      embed.add_field(name="Rating", value=f"{str(round(youtube.rating*20, 3))}%", inline=True)
      embed.add_field(name="Channel", value=f"[{chnl.channel_name}]({youtube.channel_url}) ({len(chnl.videos)} videos)", inline=True)
      if youtube.age_restricted:
        embed.add_field(name="Restricted", value="This video is age-restricted.", inline=True)
      embed.set_thumbnail(url=youtube.thumbnail_url)
      await ytmsg.edit(embed=embed)

@bot.command()
async def clearsnipe(ctx, *, chnl : discord.TextChannel = None):
  if chnl == None:
    chnl = ctx.channel
  if chnl.permissions_for(ctx.author).manage_channels or bot_admins.count(ctx.author.id)!=0:
    sniper1.pop(str(ctx.guild.id)+str(chnl.id))
    sniper2.pop(str(ctx.guild.id)+str(chnl.id))
    sniper3.pop(str(ctx.guild.id)+str(chnl.id))
    sniper4.pop(str(ctx.guild.id)+str(chnl.id))
    sniper5.pop(str(ctx.guild.id)+str(chnl.id))
    await ctx.send('Cleared snipe database for '+chnl.mention+'.')
  else:
    await ctx.send("You don't have the required permission: Manage channels.")

@bot.command()
async def nick(ctx, *, newnick):
  if ctx.channel.permissions_for(ctx.author).manage_nicknames:
    await ctx.guild.get_member(796686363604680755).edit(nick = newnick)
    await ctx.send("Nickname changed.")

@bot.command()
async def tts(ctx, *, desc):
  await ctx.send(desc, tts = True)

@bot.command()
async def raw(ctx, msg : discord.Message):
  embed = discord.Embed(title = "Raw message", url = msg.jump_url, description = "```"+discord.utils.escape_markdown(msg.content, as_needed=True)+"```")
  await ctx.send(embed=embed)

@bot.command(aliases=["commands"])
async def help(ctx, *, cat=None):
  embed = bothelp(cat)
  await ctx.send(embed=embed)

@bot.command()
async def invite(ctx, *, text=None):
  await ctx.send(embed=botinvite())

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
    pass
  if ctx.channel.permissions_for(ctx.author).manage_messages or bot_admins.count(ctx.author.id)!=0:
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
    await ctx.send("You don't have the required permission: Manage messages.")

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
  embed = botstatus(ctx, member)
  await ctx.send(embed=embed)

@bot.command(aliases=["online"])
async def ping(ctx, *, text = None):
  now1 = datetime.datetime.now(timezone.utc)
  message = await ctx.send("Pong!")
  mcs = str(int((datetime.datetime.now(timezone.utc) - now1).microseconds)+int(((datetime.datetime.now(timezone.utc) - now1).total_seconds())%60))
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
    pass
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
    webhook = Webhook.partial(identify, token, session=session)
    await webhook.send(message, username=member.name, avatar_url=member.avatar.url)

@bot.command(pass_context=True)
async def pretendembed(ctx, member : discord.Member, *, text):
  try:
    await ctx.message.delete()
  except:
    pass
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
    webhook = Webhook.partial(identify, token, session=session)
  embed = botembed(text)
  await webhook.send(embed=embed, username=member.name, avatar_url=member.avatar.url)

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
  if ctx.channel.permissions_for(ctx.author).manage_messages or bot_admins.count(ctx.author.id)!=0:
    num=int(num)
    deleted = await ctx.channel.purge(limit=num+1)
    msg = await ctx.send("Purging completed.")
    desc = ""
    authors = [count.author.name + count.author.discriminator for count in deleted]
    authors = list(dict.fromkeys(authors))
    counter = 0
    for count in deleted:
      contents = count.content
      if 'fuck' in contents or 'shit' in contents or 'asshole' in contents or 'dick' in contents:
        counter = counter + 1
    await msg.edit(f"Purging completed.\nDeleted {counter} messages with bad words", delete_after = 5)
  else:
    await ctx.send("You don't have the required permission: Manage messages.")

@bot.command()
async def purgeregex(ctx, num, *, regex):
  try:
    await ctx.message.delete()
  except:
    pass
  if ctx.channel.permissions_for(ctx.author).manage_messages or bot_admins.count(ctx.author.id)!=0:
    purge_pattern = eval("re.compile(r'"+regex+"')")
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
        await ctx.send("The bot doesn't have the required permission (Manage messages) or the regex was malformed.")
        break
    await ctx.send("Regex purging completed.", delete_after = 5)
  else:
    await ctx.send("You don't have the required permission: Manage messages.")

@bot.command()
async def purgepygex(ctx, num, regex, *, pyscript):
  try:
    await ctx.message.delete()
  except:
    pass
  if ctx.channel.permissions_for(ctx.author).manage_messages or bot_admins.count(ctx.author.id)!=0:
    purge_pattern = eval("re.compile(r'"+regex+"'")
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
        await ctx.send("The bot doesn't have the required permission (Manage messages) or the regex/script was malformed.")
        break
    await ctx.send("Python Regex purging completed.", delete_after = 5)
  else:
    await ctx.send("You don't have the required permission: Manage messages.")

@bot.command()
async def purgepy(ctx, num, pyscript):
  try:
    await ctx.message.delete()
  except:
    pass
  if ctx.channel.permissions_for(ctx.author).manage_messages or bot_admins.count(ctx.author.id)!=0:
    num = int(num)
    purged = 0
    async for msg in ctx.channel.history(limit=1000):
      try:
        if eval(pyscript) == True:
          await msg.delete()
          purged = purged + 1
          if purged >= num:
            break
      except:
        await ctx.send("The bot doesn't have the required permission (Manage messages) or the script was malformed.")
        break
    await ctx.send("Python purging completed.", delete_after = 5)
  else:
    await ctx.send("You don't have the required permission: Manage messages.")

@bot.command()
async def purgeuser(ctx, num, userinput : discord.User):
  try:
    await ctx.message.delete()
  except:
    pass
  if ctx.channel.permissions_for(ctx.author).manage_messages or bot_admins.count(ctx.author.id)!=0:
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
    await ctx.send("You don't have the required permission: Manage messages.")

@bot.command(aliases=["colour"])
async def color(ctx, *, name):
    output = botcolor(name)
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
    except:
      desc = str(emojiarg)+"\n`Created by` field can only be retrieved with the manage-emojis permission.\nCreated at "+str(emojiarg.created_at.strftime("%d %b, %Y (%a) %H:%M:%S"))
    embed = discord.Embed(title=f"Emoji Info: {emojiarg.name}", description=desc)
    embed.add_field(name="ID", value=emojiarg.id, inline=True)
    embed.set_image(url = emojiarg.url)
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
    end = datetime.datetime.now(timezone.utc) + timedelta(seconds = sec)
    seconds = int((end - datetime.datetime.now(timezone.utc)).total_seconds())
    idcode = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]
    exec("terminate"+idcode.lower()+str(ctx.guild.id)+"=0",globals())
    newidcode=idcode.lower()
    allid.append(idcode+str(ctx.guild.id))
    desc = "Initializing countdown…"
    message = await ctx.send(desc)
    while seconds>=1 and eval("terminate"+idcode.lower()+str(ctx.guild.id))==0:
      seconds = int((end - datetime.datetime.now(timezone.utc)).total_seconds())
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
      newsec=number_to_emoji(newsec)
      newmin=number_to_emoji(newmin)
      newhrs=number_to_emoji(newhrs)
      newday=number_to_emoji(newday)
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
    end = datetime.datetime.now(timezone.utc) + timedelta(seconds = sec)
    seconds = int((end - datetime.datetime.now(timezone.utc)).total_seconds())
    newidcode = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]
    exec("terminate"+newidcode.lower()+str(ctx.guild.id)+"=0",globals())
    allid.append(newidcode+str(ctx.guild.id))
    desc = "Initializing countdown…"
    message = await ctx.send(desc)
    while seconds>=1 and eval("terminate"+newidcode.lower()+str(ctx.guild.id))==0:
      seconds = int((end - datetime.datetime.now(timezone.utc)).total_seconds())
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
  #if ctx.channel.permissions_for(ctx.author).manage_roles or bot_admins.count(ctx.author.id)!=0:
  if ctx.channel.permissions_for(ctx.author).manage_roles or ctx.author.id == 687474789342117900 or role.id == 805462470604095539 or role.id == 805462557472194581 or role.id == 822743463883702302:
    roles=member.roles
    if roles.count(role)==1:
      await member.remove_roles(role)
      await ctx.send("Removed "+str(role)+" role from "+str(member)+".")
    else:
      await member.add_roles(role)
      await ctx.send("Added "+str(role)+" role to "+str(member)+".")
    
  else:
    await ctx.send("You don't have the required permission: Manage roles.")

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
async def choice(ctx,*options):
  ti="Random choice"
  rand=ra.choice(options)
  desc="Your random option is "+rand
  embed=discord.Embed(title=ti, description=desc)
  await ctx.send(embed=embed)

@bot.command()
async def avatar(ctx,user: discord.Member=None):
  ti="Avatar"
  if user==None:
    user=ctx.author
  desc=f"Avatar of {user.mention}"
  embed=discord.Embed(title=ti, description=desc)
  embed.set_image(url=user.avatar.url)
  await ctx.send(embed=embed)

@bot.command(aliases = ["guild"])
async def server(ctx, text = "regular"):
  task = asyncio.create_task(botserver(ctx, text))
  await task
  await ctx.send(embed=task.result())

@bot.command()
async def template(ctx, *, tempinput):
  try:
    temp = bot.fetch_template(tempinput)
  except:
    await ctx.send("Invalid input. Please try again.")
    return
  ti="Template Information: "+temp.name+" ("+temp.code+")"
  desc="Created at "+temp.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")+" by "+str(temp.creator)
  embed=discord.Embed(title=ti, description=desc)
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
  task = asyncio.create_task(botinvitel(inviteinput))
  await task
  await ctx.send(embed=task.result())

@bot.command()
async def channel(ctx, channel : typing.Union[discord.TextChannel, discord.VoiceChannel, discord.StageChannel]):
  if channel.type == discord.ChannelType.text:
    task = asyncio.create_task(bottchannel(ctx, channel))
    await task
    await ctx.send(embed=task.result())
  elif channel.type == discord.ChannelType.voice:
    task = asyncio.create_task(botvchannel(channel))
    await task
    await ctx.send(embed=task.result())
  elif channel.type == discord.ChannelType.stage:
    task = asyncio.create_task(botstagec(channel))
    await task
    await ctx.send(embed=task.result())
  else:
    embed = discord.Embed(desc = "Invalid input.")
    await ctx.send(embed=embed)

@bot.command(aliases=["msg"])
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
    if count.is_spoiler:
      f1v += f"[{count.filename}]({count.url}) ({sizer(count.size)}, marked as spoiler)"
    else:
      f1v += f"[{count.filename}]({count.url}) ({sizer(count.size)})"
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
    embed.add_field(name=message.application["name"], value=f"This message is created by {message.application['name']}.\n{message.application['description']}", inline=False)
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
  embed.set_thumbnail(url=lfuser.avatar.url)
  f0v=f"{lfuser.name}#{lfuser.discriminator}"
  f1v=lfuser.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  f1ts = str(datetime.datetime.now(timezone.utc) - lfuser.created_at)
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
  embed.set_thumbnail(url=user.avatar.url)
  if user.name==user.display_name:
    f0v=f"{user.name}#{user.discriminator}"
  else:
    f0v=f"{user.name}#{user.discriminator} (__Nickname:__  `{user.display_name}`)"
  f1v=user.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  f1ts = str(datetime.datetime.now(timezone.utc) - user.created_at)
  if f1ts.count(" days, ") == 0:
    f1va = re.sub(r'(\d{1,2}):(\d{2}):(\d{2})', r'\1 hours \2 minutes \3 seconds', f1ts) + f"\n≈ "+f1ts.split(":")[0]+" hours"
  else:
    days = int(re.sub(r'([\d]+) days, [\s\S]*', r'\1', f1ts))
    f1va = re.sub(r'([\d]+) days, (\d{1,2}):(\d{2}):(\d{2})', r'\1 days \2 hrs \3 mins \4 secs', f1ts)[:-7] + f"\n≈ "+str((int(f1ts.split(" days, ")[0]))//365) + " years " + str(int(f1ts.split(" days, ")[0]) % 365) + " days"
  f2v=user.joined_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  f2ts = str(datetime.datetime.now(timezone.utc) - user.joined_at)
  if f2ts.count(" days, ") == 0:
    f2va = re.sub(r'(\d{1,2}):(\d{2}):(\d{2})', r'\1 hours \2 minutes \3 seconds', f2ts) + f"\n≈ "+f2ts.split(":")[0]+"hours"
  else:
    f2va = re.sub(r'([\d]+) days, (\d{1,2}):(\d{2}):(\d{2})', r'\1 days \2 hrs \3 mins \4 secs', f2ts)[:-7] + f"\n≈ "+str((int(f2ts.split(" days, ")[0]))//365) + " years " + str(int(f2ts.split(" days, ")[0]) % 365) + " days"
  allroles=user.roles
  f3v=""
  f3v += ("Admin, " if channel.permissions_for(user).administrator else "")
  f3v += ("Manage Server, " if channel.permissions_for(user).manage_guild else "")
  f3v += ("Manage Roles, " if channel.permissions_for(user).manage_roles else "")
  f3v += ("Manage Permissions, " if channel.permissions_for(user).administrator else "")
  f3v += ("View Audit Logs, " if channel.permissions_for(user).view_audit_log else "")
  f3v += ("View Server Insights, " if channel.permissions_for(user).view_guild_insights else "")
  f3v += ("Kick Members, " if channel.permissions_for(user).kick_members else "")
  f3v += ("Ban Members, " if channel.permissions_for(user).ban_members else "")
  f3v += ("Manage Nicknames, " if channel.permissions_for(user).manage_nicknames else "")
  f3v += ("Manage Webhooks, " if channel.permissions_for(user).manage_webhooks else "")
  f3v += ("Manage Emojis, " if channel.permissions_for(user).manage_emojis else "")
  f3v += ("Change Nickname, " if channel.permissions_for(user).manage_nicknames else "")
  f3v += ("Mention Everyone, " if channel.permissions_for(user).mention_everyone else "")
  f3v += ("Create Invite, " if channel.permissions_for(user).create_instant_invite else "")
  f3v=f3v[:-2]
  if f3v=="":
    f3v="No permissions"
  f3vb=""
  f3vb += ("View Channel, "         if channel.permissions_for(user).view_channel else "")
  f3vb += ("Read Messages, "        if channel.permissions_for(user).read_messages else "")
  f3vb += ("Read Message History, " if channel.permissions_for(user).read_message_history else "")
  f3vb += ("Send Messages, "        if channel.permissions_for(user).send_messages else "")
  f3vb += ("Send TTS Messages, "    if channel.permissions_for(user).send_tts_messages else "")
  f3vb += ("Add Reactions, "        if channel.permissions_for(user).add_reactions else "")
  f3vb += ("External Emojis, "      if channel.permissions_for(user).external_emojis else "")
  f3vb += ("Attach Files, "         if channel.permissions_for(user).attach_files else "")
  f3vb += ("Embed Links, "          if channel.permissions_for(user).embed_links else "")
  f3vb=f3vb[:-2]
  if f3vb=="":
    f3vb="No permissions"
  
  f3ve=""
  f3ve += ("Connect, "            if user.guild_permissions.connect else "")
  f3ve += ("Speak (Audio), "      if user.guild_permissions.speak else "")
  f3ve += ("Stream (Video), "     if user.guild_permissions.stream else "")
  f3ve += ("Use Voice Activity, " if user.guild_permissions.use_voice_activation else "")
  f3ve += ("Priority Speaker, "   if user.guild_permissions.priority_speaker else "")
  f3ve += ("Mute Memvers, "       if user.guild_permissions.mute_members else "")
  f3ve += ("Deafen Members, "     if user.guild_permissions.deafen_members else "")
  f3ve += ("Move Members, "       if user.guild_permissions.move_members else "")
  f3ve += ("Request to Speak, "   if user.guild_permissions.request_to_speak else "")
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
    pass
  f4v=""
  if len(allroles) > 1:
    allroles.reverse()
    allroles = allroles[:-1]
    for count in allroles:
      f4v = f4v + count.mention+" "
    f4v = f4v[:-1]
  else:
    f4v="No roles"
  f5v = ""
  f5v = f5v + (f"**Staff:** The user is a Discord Employee.\n"                             if user.public_flags.staff else "")
  f5v = f5v + (f"**Partner:** The user is a Discord Partner.\n"                            if user.public_flags.partner else "")
  f5v = f5v + (f"**Hypesquad:** The user is a HypeSquad Events member.\n"                  if user.public_flags.hypesquad else "")
  f5v = f5v + (f"**Early Support:** The user is an Early Supporter.\n"                     if user.public_flags.early_supporter else "")
  f5v = f5v + (f"**Team User:** The user is a Team User.\n"                                if user.public_flags.team_user else "")
  f5v = f5v + (f"**Bug Hunter:** The user is a Bug Hunter.\n"                              if user.public_flags.bug_hunter else "")
  f5v = f5v + (f"**Bug Hunter 2:** The user is a Bug Hunter (Level 2).\n"                  if user.public_flags.bug_hunter_level_2 else "")
  f5v = f5v + (f"**System:** The user is a system user (represents Discord officially).\n" if user.public_flags.system else "")
  f5v = f5v + (f"**Developer:** The user is a Verified Bot Developer.\n"                   if user.public_flags.verified_bot_developer else "")
  f5v = f5v + (f"**✔︎Bot:** The user is a Verified Bot.\n"                                  if user.public_flags.verified_bot else "")
  f5v = f5v + (f"**Hypesquad:** The user is in the Hypesquad Bravery House.\n"             if user.public_flags.hypesquad_bravery else "")
  f5v = f5v + (f"**Hypesquad:** The user is in the Hypesquad Brilliance House.\n"          if user.public_flags.hypesquad_brilliance else "")
  f5v = f5v + (f"**Hypesquad:** The user is in the Hypesquad Balance House.\n"             if user.public_flags.hypesquad_balance else "")
  f5v = "No badges" if len(f5v) == 0 else None
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
    pass
  embed.add_field(name="Badges", value=f5v, inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def ban(ctx, user: discord.User, delete : int =0, *, reason="No reason provided"):
  task = asyncio.create_task(botban(ctx, user, delete, reason))
  await task

@bot.command()
async def unban(ctx, user: discord.User, *, reason="No reason provided"):
  task = asyncio.create_task(botunban(ctx, user, reason))
  await task

@bot.command()
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
  task = asyncio.create_task(botkick(ctx, user, reason))
  await task

@bot.command()
async def slowmode(ctx, sec = None, *channels:typing.Union[discord.TextChannel,str]):
  if sec != None:
    if sec.isdigit() == False:
      sec = 0
    if int(sec) < 0 or int(sec) > 21600 or int(sec)%1 != 0:
      await ctx.send("Invalid input! Please enter an integer below or equal to 21600.")
      return
    if len(channels) == 0:
      allchannel = [ctx.channel]
    elif channels[0] == ("all"):
      allchannel = ctx.guild.text_channels
    else:
      allchannel = channels
    channellist = []
    for count in allchannel:
      if type(count) == str:
        continue
      if count.permissions_for(ctx.author).manage_channels or bot_admins.count(ctx.author.id)!=0:
        orsec = str(count.slowmode_delay)
        await count.edit(slowmode_delay = sec)
        channellist.append(count.mention)
    if len(channellist)==0:
      await ctx.send("You don't have the required permission: Manage channels.")
    elif len(channellist)==1:
      await ctx.send("Set slowmode from "+orsec+" second(s) to "+sec+" second(s) for "+" ".join(channellist)+".")
    else:
      await ctx.send("Set slowmode to "+sec+" second(s) for these channels: "+" ".join(channellist)+".")
  elif sec == None:
    await ctx.send("The current slowmode is "+str(ctx.channel.slowmode_delay)+" second(s).")

# @slash.slash(name="purge", description="Purge a number of messages in the current channel.", options=[create_option(name="number",description="Amount of messages to purge in the current channel.",option_type=4,required=True)])
# async def _purge(ctx, num:int):
#   if ctx.channel.permissions_for(ctx.author).manage_messages or bot_admins.count(ctx.author.id)!=0:
#     await ctx.channel.purge(limit=num+1)
#     await ctx.send("Purging completed.", delete_after = 5)
#   else:
#     await ctx.send("You don't have the required permission: Manage messages.")

# @slash.slash(name="ban", description="Bans a member.", options=[create_option(name="member",description="The member to ban.",option_type=6,required=True), create_option(name="purge-days",description="The number of days of messages to purge from the user.",option_type=4,required=False), create_option(name="reason",description="The reason to ban the member, which shows in the audit logs.",option_type=3,required=False)])
# async def _ban(ctx, user: discord.User, delete : int =0, reason="No reason provided"):
#   task = asyncio.create_task(botban(ctx, user, delete, reason))
#   await task

# @slash.slash(name="kick", description="Kicks a member.", options=[create_option(name="member",description="The member to kick.",option_type=6,required=True), create_option(name="reason",description="The reason to kick the member, which shows in the audit logs.",option_type=3,required=False)])
# async def _kick(ctx, user: discord.Member, reason="No reason provided"):
#   task = asyncio.create_task(botkick(ctx, user, reason))
#   await task

# @slash.slash(name="unban", description="Unbans a member.", options=[create_option(name="member",description="The member to ban.",option_type=6,required=True), create_option(name="reason",description="The reason to ban the member, which shows in the audit logs.",option_type=3,required=False)])
# async def _unban(ctx, user: discord.User, *, reason="No reason provided"):
#   task = asyncio.create_task(botunban(ctx, user, reason))
#   await task

# @slash.slash(name="slowmode", description="Set the slowmode delay for the current channel.", options=[create_option(name="delay",description="Adjust the slowmode threshold for the current channel.",option_type=4,required=True)])
# async def _slowmode(ctx, time:int):
#   if ctx.channel.permissions_for(ctx.author).manage_channels or bot_admins.count(ctx.author.id)!=0:
#     if 21600>=time>=0:
#       await ctx.channel.edit(slowmode_delay = time)
#       await ctx.send("Set slowmode to "+str(time)+" second(s) for this channel.")
#     else:
#       await ctx.send("Please enter an integer between 0 and 21600 (inclusive).")
#   else:
#     await ctx.send("You do not have the required permission: Manage channel.")

# @slash.slash(name="calc", description="Evaluate a mathematical equation..", options=[create_option(name="equation",description="A math equation to calculate.",option_type=3,required=True)])
# async def _calc(ctx, equation:str):
#   output = botcalc(equation)
#   if output == "Add_Reaction":
#     await ctx.message.add_reaction("👍")
#   else:
#     await ctx.send(output)

# @slash.slash(name="random", description="Draws a random integer between two numbers.", options=[create_option(name="lower",description="The lower bound.",option_type=4,required=True), create_option(name="upper",description="The upper bound.",option_type=4,required=True)])
# async def _random(ctx, lower:int, upper:int):
#   ti="Random number between "+str(lower)+" and "+str(upper)
#   rand=ra.randint(lower,upper)
#   desc="Your random number is "+str(rand)
#   embed=discord.Embed(title=ti, description=desc)
#   await ctx.send(embed=embed)

# @slash.slash(name="server", description="Shows information about the current server.")
# async def _server(ctx):
#   pass

# @slash.subcommand(base = "server", name = "regular", description = "Shows regular information about the current server.")
# async def _server_regular(ctx):
#   task = asyncio.create_task(botserver(ctx, "regular"))
#   await task
#   await ctx.send(embed=task.result())

# @slash.subcommand(base = "server", name = "mod", description = "Shows banned members and valid invites for the current server.")
# async def _server_mod(ctx):
#   task = asyncio.create_task(botserver(ctx, "mod"))
#   await task
#   await ctx.send(embed=task.result())

# @slash.slash(name="role", description="Shows information about a role.", options=[create_option(name="role",description="The role to show information for.",option_type=8,required=True)])
# async def _role(ctx, role:discord.Role):
#   embed = botrole(ctx, role)
#   await ctx.send(embed=embed)

# @slash.slash(name="channel", description="Shows information about a channel.", options=[create_option(name="channel",description="The channel to show information for.",option_type=7,required=True)])
# async def _channel(ctx, channel:discord.abc.GuildChannel):
#   if channel.type == discord.ChannelType.text:
#     task = asyncio.create_task(bottchannel(ctx, channel))
#     await task
#     await ctx.send(embed=task.result())
#   elif channel.type == discord.ChannelType.voice:
#     task = asyncio.create_task(botvchannel(ctx, channel))
#     await task
#     await ctx.send(embed=task.result())

# @slash.slash(name="simplecolor", description="Gets information about a named color.", options=[create_option(name="colour",description="The name of the colour.",option_type=3,required=True,choices=simple_colours_options)])
# async def _simplecolor(ctx, name):
#   botsimpcolor(name)
#   try:
#     file = discord.File("color.png")
#     await ctx.send(file=file)
#   except:
#     await ctx.send("Invalid colour name, please try again.")

# @slash.slash(name="status", description="Shows the status of a member.", options=[create_option(name="member",description="The name of the colour.",option_type=6,required=True)])
# async def _status(ctx, member : discord.Member = None):
#   embed = botstatus(ctx, member)
#   await ctx.send(embed=embed)


# @slash.slash(name="dog", description="Shows one or more dog picture(s).", options=[create_option(name="number",description="Number of pictures to show.",option_type=4,required=False)])
# async def _dog(ctx, number=1):
#   if number<9:
#     await ctx.send(botdog(number))
#   else:
#     await ctx.send("There are too many pictures to show! I can only display up to 9 pictures.")

# @slash.slash(name="cat", description="Shows one or more cat picture(s).", options=[create_option(name="number",description="Number of pictures to show.",option_type=4,required=False)])
# async def _cat(ctx, number=1):
#   if number<9:
#     await ctx.send(botcat(number))
#   else:
#     await ctx.send("There are too many pictures to show! I can only display up to 9 pictures.")

# @slash.slash(name="ping", description="Checks whether the bot is online.")
# async def _ping(ctx : SlashContext):
#   await ctx.send("Pong!")

@bot.event
async def on_ready():
  print('Bot is preparing itself…')
  activity = discord.Activity(type=discord.ActivityType.playing, name="with =help")
  await bot.change_presence(status=discord.Status.idle, activity=activity)
  # await slash.sync_all_commands(SlashCommand)
  print("Bot is ready!")

print("Bot is getting started…")
bot.run('Nzk2Njg2MzYzNjA0NjgwNzU1.X_bh_g.6uKl_EPp5r5XZpSxCxPTIuA69aE')
