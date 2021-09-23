import re
import typing
from datetime import timedelta
from difflib import SequenceMatcher
import discord
from discord.ext import commands

from bot import bot_admins
from shared import *

UNITS = {'s':'seconds', 'm':'minutes', 'h':'hours', 'd':'days', 'w':'weeks'}

@commands.command()
async def ban(ctx, user: discord.User, delete : int =0, *, reason="No reason provided"):
  if ctx.channel.permissions_for(ctx.author).ban_members or bot_admins.count(ctx.author.id) != 0:
    try:
      await ctx.guild.ban(user, delete_message_days=delete, reason=reason)
    except:
      await ctx.send("The bot doesn't have the required permission: Ban members.")
      return
    embed1 = discord.Embed(title=f"You were banned from the server.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    embed2 = discord.Embed(title=f"{user.name} was banned.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    try:
      await user.send(embed=embed1)
    except:
      1
    await ctx.send(embed=embed2)
  else:
    await ctx.send("You don't have the required permission: Ban members.")

@commands.command()
async def getrole(ctx, roles : commands.Greedy[discord.Role], member: discord.Member = None):
  if member == None:
    member = ctx.author
  if has_perms(ctx.channel, ctx.author, 28):
    roles=member.roles
    addrole_count = removerole_count = 0
    for count in roles:
      if roles.count(count)==1:
        await member.remove_roles(count)
      else:
        await member.add_roles(count)
    if addrole_count and removerole_count:
      await ctx.send(f"Added {str(addrole_count)} and removed {str(removerole_count)} roles to {str(member)}.")
    elif addrole_count:
      await ctx.send(f"Added {str(addrole_count)} roles to {str(member)}.")
    elif removerole_count:
      await ctx.send(f"Removed {str(removerole_count)} roles to {str(member)}.")
    else:
      await ctx.send("No roles had been manipulated.")
  else:
    await ctx.send("You don't have the required permission: Manage roles.")

@commands.command()
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
  if has_perms(ctx.channel, ctx.author, 1):
    try:
      await user.kick(reason=reason)
    except:
      await ctx.send("The bot doesn't have the required permission: Kick members.")
      return
    embed1 = discord.Embed(title=f"You were kicked from the server.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    embed2 = discord.Embed(title=f"{user.name} was kicked.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    try:
      await user.send(embed=embed1)
    except:
      pass
    await ctx.send(embed=embed2)
  else:
    await ctx.send("You don't have the required permission: Kick members.")

@commands.command()
async def makeinvite(ctx, timetocount, uses : int = 0):
  if has_perms(ctx.channel, ctx.author, 0):
    seconds = int(timedelta(**{
      UNITS.get(m.group('unit').lower(), 'seconds'): int(m.group('val'))
      for m in re.finditer(r'(?P<val>\d+)(?P<unit>[smhdw]?)', timetocount, flags=re.I)
    }).total_seconds())
    theinvite = await ctx.channel.create_invite(max_age = seconds, max_uses = uses)
    await ctx.send("An invite was generated with "+str(seconds)+" seconds of valid duration: "+theinvite.url)
  else:
    await ctx.send("You don't have the required permission: Generate Invites.")

@commands.command(aliases=['makerole'])
async def makeroles(ctx, times:int=1):
  if has_perms(ctx.channel, ctx.author, 28):
    for count in range(0,times):
      await ctx.guild.create_role(name=f"Sample role {str(count+1)}")
    await ctx.send("Successfully created roles.")
  else:
    await ctx.send("You don't have the required permission: Manage Roles.")

@commands.command(aliases=['setperms', 'setpermission', 'setpermissions', 'rolepermission', 'rolespermission', 'rolepermissions', 'rolespermissions'])
async def setperm(ctx, permission_input:typing.Union[int, str], *roles:discord.Role):
  if has_perms(ctx.channel, ctx.author, 28):
    if type(permission_input) == int:
      permission = discord.Permissions(permission_input)
    else:
      permission_input = permission_input.lower()
      permission = re.sub(r'[^A-z]|\^', '', permission_input)
      for count, count2 in custom_permissions.items():
        if SequenceMatcher(None, permission, count).ratio() >= 0.75:
          permission = count2
          break
    for count in roles:
      await count.edit(permissions=permission)
    await ctx.send("Successfully set permissions.")
  else:
    await ctx.send("You don't have the required permission: Manage Roles.")

@commands.command()
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

@commands.command()
async def unban(ctx, user: discord.User, *, reason="No reason provided"):
  if ctx.channel.permissions_for(ctx.author).ban_members or bot_admins.count(ctx.author.id) != 0:
    try:
      await ctx.guild.unban(user, reason=reason)
    except:
      await ctx.send("The bot doesn't have the required permission: Ban members.")
      return
    embed1 = discord.Embed(title=f"You were unbanned from the server.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    embed2 = discord.Embed(title=f"{user.name} was unbanned.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    try:
      await user.send(embed=embed1)
    except:
      pass
    await ctx.send(embed=embed2)
  else:
    await ctx.send("You don't have the required permission: Ban members.")

@commands.command()
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

@commands.command()
async def purgereactions(ctx, messages, emoji: discord.Emoji = None):
  if emoji == None:
    async for message in ctx.channel.history(limit=int(messages)+1):
      await message.clear_reactions()
  else:
    async for message in ctx.channel.history(limit=int(messages)+1):
      await message.clear_reaction(emoji)

@commands.command()
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

@commands.command()
async def purgerole(ctx, num, roleinput : discord.Role):
  try:
    await ctx.message.delete()
  except:
    pass
  if ctx.channel.permissions_for(ctx.author).manage_messages or bot_admins.count(ctx.author.id)!=0:
    num = int(num)
    purged = 0
    async for count in ctx.channel.history(limit=1000):
      if roleinput in count.author.roles:
        await count.delete()
        purged = purged + 1
        if purged >= num:
          break
    await ctx.send("User purging completed.", delete_after = 5)
  else:
    await ctx.send("You don't have the required permission: Manage messages.")

@commands.command()
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

@commands.command()
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

@commands.command()
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

def setup(bot):
  bot.add_command(ban)
  bot.add_command(getrole)
  bot.add_command(kick)
  bot.add_command(makeinvite)
  bot.add_command(makeroles)
  bot.add_command(setperm)
  bot.add_command(slowmode)
  bot.add_command(unban)
  bot.add_command(purge)
  bot.add_command(purgereactions)
  bot.add_command(purgeregex)
  bot.add_command(purgerole)
  bot.add_command(purgeuser)
  bot.add_command(purgepy)
  bot.add_command(purgepygex)
