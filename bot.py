import random as ra
import re
from datetime import datetime, timedelta, timezone
from math import *

import discord as discord
import emojis as ems
from discord.ext import commands

from shared import *

banned_ids = []
banned_text = []
bot_admins = [687474789342117900]
bot_ = commands.Bot(command_prefix=commands.when_mentioned_or("="), intents=discord.Intents.all(), case_insensitive=True)
bot_.remove_command('help')
bot_.load_extension("botanimals")
bot_.load_extension("botbasic")
bot_.load_extension("botdevelopment")
bot_.load_extension("botdinfo")
bot_.load_extension("botembed")
bot_.load_extension("botengrave")
bot_.load_extension("botimage")
bot_.load_extension("botinfo")
bot_.load_extension("botmoderate")
bot_.load_extension("botplot")
bot_.load_extension("botcalc")
bot_.load_extension("bottext")
bot_.load_extension("botwebinfo")
bot_.load_extension("botwebscrape")
id_pattern = re.compile(r'([A-Z]{5})', re.IGNORECASE)
verify_pattern = re.compile(r'[^ ⠀][\s\S]{0,30}?[^ ⠀]#?[\d]{4}(,|, | )?[\d+\-*/×÷%xyz()\[\]\{\}]{1,50}=[\d+\-*/×÷%xyz()\[\]\{\}]{1,50}(,|, | )?[\S ]{3,20}(,|, | )?(Red|Orange|Yellow|Green|Light( |_)?Green|Dark( |_)?Green|Cyan|Blue|Light( |_)?Blue|Dark( |_)?Blue|Purple|Pink|Brown)', re.IGNORECASE)
poll_pattern = re.compile(r'([\w]+?)(:\w{2,32}:|[\uD800-\uDBFF])')
UNITS = {'s':'seconds', 'm':'minutes', 'h':'hours', 'd':'days', 'w':'weeks'}

typer=0
sniper1=sniper2=sniper3=sniper4=sniper5=sniperdate1=sniperdate2=sniperdate3=sniperdate4=sniperdate5=sniperdict=sniping=poll_options={}
snipereactions=polls=allid=[]
overwrite = discord.PermissionOverwrite()
overwrite.view_channel = True
getbotinstance = lambda: bot_

@bot_.event
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

@bot_.event
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

@bot_.event
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
    cache = discord.Embed(title = cache_embed.title, description = ems.encode(desc))
    await msg.edit(embed=cache)

@bot_.event
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
    cache = discord.Embed(title = cache_embed.title, description = ems.encode(desc))
    await msg.edit(embed=cache)

@bot_.event
async def on_message(message:discord.Message):
  if message.guild.id == 852899227004305458 and message.author.id != 796686363604680755 and message.channel.id in [856053769149874196, 864757953121878026, 864754633910255646]:
    await message.add_reaction("<:UpArrowSquare:864762633194569728>")
    await message.add_reaction("<:DownArrowSquare:864762633625534485>")
  elif message.channel.id in [805459414001778739, 805462208414089217, 880076327783370812]:
    await message.publish()
  if message.author.id not in banned_ids and message.content.startswith("=") and message.content.startswith("==")==False:
    await bot_.process_commands(message)
  elif message.author.id in banned_ids and message.content.startswith("=") and message.content.startswith("==")==False:
    await message.channel.send("You are banned from the bot. Reason: "+banned_text[banned_ids.index(message.author.id)])

@bot_.command(aliases=['sniper'])
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
  elif has_perms(ctx.channel, ctx.author, 13):
    if text.startswith("y") or text.startswith("t") or text.startswith("e") or text.replace(" ","")=="1":
      sniping[keyname] = True
      await ctx.send("Sniping is now enabled.")
    else:
      sniping[keyname] = False
      await ctx.send("Sniping is now disabled.")

@bot_.command()
async def poll(ctx, *, text):
  options = []
  reactions = []
  textlist = text.split(" ")
  ti = ""
  desc = ""
  poll_options_cache = {}
  for count in textlist: # ([\w]+?)(:\w{2,32}:|[\uD800-\uDBFF])
    match = poll_pattern.fullmatch(ems.decode(count))
    if match:
      optn = re.sub(poll_pattern, r'\1', ems.decode(count))
      rect = re.sub(poll_pattern, r'\2', ems.decode(count))
      desc = desc + f"{rect} {optn} (0)\n"
      options.append(optn)
      poll_options_cache[optn] = rect
      reactions.append(ems.encode(rect))
    else:
      ti = ti + count + " "
  embed = discord.Embed(title = ti, description = ems.encode(desc))
  poll = await ctx.send(embed=embed)
  for count in reactions:
    await poll.add_reaction(count)
  polls.append(poll.id)
  poll_options[poll.id] = poll_options_cache

@bot_.command()
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

@bot_.command()
@commands.is_owner()
async def purgeserver(ctx, text, condition="1==1", *, nothing = None):
  text = text.lower()
  if text.startswith("role"):
    allroles = ctx.guild.roles()
    for _role in allroles:
      if condition:
        await _role.delete()
    await ctx.send("Role purging completed.")

@bot_.command()
@commands.is_owner()
async def botban(ctx, user : discord.User, *, text="No reason was provided"):
  banned_ids.append(user.id)
  banned_text.append(text)
  await ctx.send("Banned user from using the bot.")

@bot_.command()
@commands.is_owner()
async def botunban(ctx, user : discord.User):
  if banned_ids.count(user.id) == 1:
    banned_text.remove(banned_text[banned_ids.index(user.id)])
    banned_ids.remove(user.id)
    await ctx.send("Unbanned user from using the bot.")

@bot_.command()
@commands.is_owner()
async def botadmin(ctx, user : discord.User):
  bot_admins.append(user.id)
  await ctx.send("Added user as bot admin.")

@bot_.command()
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

@bot_.command(aliases=["online"])
async def ping(ctx, *, text = None):
  now1 = datetime.now(timezone.utc)
  message = await ctx.send("Pong!")
  mcs = str(int((datetime.now(timezone.utc) - now1).microseconds)+int(((datetime.now(timezone.utc) - now1).total_seconds())%60))
  await message.edit(content=f"Pong! 🏓\n```Message delay: {mcs} microseconds\nBot latency  : {round(bot_.latency*1000000, 2)} microseconds```")

@bot_.command()
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

@bot_.command()
async def rtimer(ctx, timetocount,*,Text=None):
    sec = int(timedelta(**{
      UNITS.get(m.group('unit').lower(), 'seconds'): int(m.group('val'))
      for m in re.finditer(r'(?P<val>\d+)(?P<unit>[smhdw]?)', timetocount, flags=re.I)
    }).total_seconds())
    end = datetime.now(timezone.utc) + timedelta(seconds = sec)
    seconds = int((end - datetime.now(timezone.utc)).total_seconds())
    idcode = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]
    exec("terminate"+idcode.lower()+str(ctx.guild.id)+"=0",globals())
    newidcode=idcode.lower()
    allid.append(idcode+str(ctx.guild.id))
    desc = "Initializing countdown…"
    message = await ctx.send(desc)
    while seconds>=1 and eval("terminate"+idcode.lower()+str(ctx.guild.id))==0:
      seconds = int((end - datetime.now(timezone.utc)).total_seconds())
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

@bot_.command()
async def ttimer(ctx, timetocount,*,Text=None):
    sec = int(timedelta(**{
      UNITS.get(m.group('unit').lower(), 'seconds'): int(m.group('val'))
      for m in re.finditer(r'(?P<val>\d+)(?P<unit>[smhdw]?)', timetocount, flags=re.I)
    }).total_seconds())
    end = datetime.now(timezone.utc) + timedelta(seconds = sec)
    seconds = int((end - datetime.now(timezone.utc)).total_seconds())
    newidcode = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]
    exec("terminate"+newidcode.lower()+str(ctx.guild.id)+"=0",globals())
    allid.append(newidcode+str(ctx.guild.id))
    desc = "Initializing countdown…"
    message = await ctx.send(desc)
    while seconds>=1 and eval("terminate"+newidcode.lower()+str(ctx.guild.id))==0:
      seconds = int((end - datetime.now(timezone.utc)).total_seconds())
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

@bot_.event
async def on_ready():
  activity = discord.Activity(type=discord.ActivityType.playing, name=f"with =help in {len(bot_.guilds)} servers")
  await bot_.change_presence(status=discord.Status.idle, activity=activity)
  print("Bot is ready!")

print("Bot is getting started…")
try:
  bot_.run('Nzk2Njg2MzYzNjA0NjgwNzU1.X_bh_g.6uKl_EPp5r5XZpSxCxPTIuA69aE')
except:
  pass