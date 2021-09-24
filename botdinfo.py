import asyncio
import re
import typing
from datetime import datetime, timedelta, timezone
from difflib import SequenceMatcher

import emojis as em
import matplotlib.pyplot as plt
import numpy as np

import discord as discord
from discord.ext import commands
from shared import *

cmaphsv = plt.cm.hsv
func = lambda pct, allvals : "{:d} ({:.1f}%)".format(int(pct/100*np.sum(allvals)), int(pct))

@commands.command()
async def avatar(ctx,user: discord.Member=None):
  base_url = user.avatar.url
  if not user:
    user=ctx.author
  desc = f"Avatar of {user.mention}\n"
  for count in range(5, 13):
    size = str(2**count)
    temp = base_url.replace("?size=1024", f"?size={size}")
    desc += f"[{size}]({temp}) "
  embed=discord.Embed(title="Avatar", description=desc)
  embed.set_image(url=base_url)
  await ctx.send(embed=embed)

@commands.command()
async def channel(ctx, channel:typing.Union[discord.TextChannel, discord.VoiceChannel, discord.StageChannel]=None):
  if not channel:
    channel = ctx.channel
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

async def bottchannel(ctx, channel):
  if channel==None:
    channel=ctx.channel
  ti="Channel Information: "+channel.name
  desc=channel.mention
  embed=discord.Embed(title=ti, description=desc)
  f0v=channel.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  f3v=str(channel.topic)
  f4v=str(channel.category)
  f5v=" ".join(await channel.invites())
  f8v = ""
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
  async for count in channel.history(limit=1, oldest_first=True):
    f9v=count
  embed.add_field(name="Created", value=f0v, inline=True)
  if channel.is_nsfw()==True:
    embed.add_field(name="NSFW", value="This is an NSFW channel.", inline=True)
  if channel.is_news()==True:
    embed.add_field(name="News", value="This is a news channel.", inline=True)
  embed.add_field(name="Topic", value=f3v, inline=True)
  embed.add_field(name="Category", value=f4v, inline=True)
  embed.add_field(name="Members", value=f8v, inline=False)
  if f5v:
    embed.add_field(name="Invites", value=f5v, inline=True)
  embed.add_field(name="ID", value=channel.id, inline=True)
  embed.add_field(name="First message", value=f"[here]({f9v.jump_url})", inline=True)
  return embed

async def botvchannel(channel):
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
  return embed

async def botstagec(channel):
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

@commands.command()
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
    cemoji = em.db.get_emoji_by_alias(emojiarg)
    if cemoji == None:
      cemoji = em.db.get_emoji_by_code(emojiarg)
    embed = discord.Embed(title="Emoji Info", description = (cemoji[1] + " :" + ":, :".join(cemoji[0]) + ":"))
    embed.add_field(name="Category", value=cemoji[3], inline=True)
    embed.add_field(name="Unicode Version", value=cemoji[4], inline=True)
    if len(cemoji[2]) > 0:
      embed.add_field(name="Tags", value=", ".join(cemoji[2]), inline=True)
  await ctx.send(embed=embed)

@commands.command()
async def invitelink(ctx,inviteinput: discord.Invite):
  allinvites=await inviteinput.channel.invites()
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

@commands.command()
async def leftuser(ctx, *, userinput):
  global bot
  lfuser = await ctx.bot.fetch_user(int(userinput))
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
  f1ts = str(datetime.now(timezone.utc) - lfuser.created_at)
  if f1ts.count(" days, ") == 0:
    f1va = re.sub(r'(\d{1,2}):(\d{2}):(\d{2})', r'\1 hours \2 minutes \3 seconds', f1ts) + f"\n≈ "+f1ts.split(":")[0]+" hours"
  else:
    days = int(re.sub(r'([\d]+) days, [\s\S]*', r'\1', f1ts))
    f1va = re.sub(r'([\d]+) days, (\d{1,2}):(\d{2}):(\d{2})', r'\1 days \2 hrs \3 mins \4 secs', f1ts)[:-7] + f"\n≈ "+str((int(f1ts.split(" days, ")[0]))//365) + " years " + str(int(f1ts.split(" days, ")[0]) % 365) + " days"
  embed.add_field(name="Name", value=f0v, inline=False)
  embed.add_field(name="Time since user registered", value=f1va, inline=True)
  embed.add_field(name="Registered", value=f1v, inline=True)
  await ctx.send(embed=embed)

@commands.command(aliases=["msg"])
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

@commands.command(aliases = ['perm', 'perms', 'permission'])
async def permissions(ctx, integer="help"):
  try:
    try:
      int(integer)
    except:
      try:
        integer = commands.RoleConverter().convert(ctx, integer).permissions.value
      except:
        integer = ctx.channel.permissions_for(commands.MemberConverter().convert(ctx, integer)).value
    embed = discord.Embed(title = f"Permission integer {integer}")
    embed.add_field(name = "Server permissions", value=server_itop(int(integer)), inline=False)
    embed.add_field(name = "Text permissions", value=tc_itop(int(integer)), inline=False)
    embed.add_field(name = "Voice permissions", value=vc_itop(int(integer)), inline=False)
  except:
    try:
      for count,count2 in custom_permissions.items():
        if SequenceMatcher(None, integer, count).ratio() >= 0.75:
          embed = discord.Embed(title = f"Custom permission {integer}")
          embed.add_field(name = "Server permissions", value=server_itop(count2.value), inline=False)
          embed.add_field(name = "Text permissions", value=tc_itop(count2.value), inline=False)
          embed.add_field(name = "Voice permissions", value=vc_itop(count2.value), inline=False)
          break
      embed
    except:
      embed = perms_guide
  await ctx.send(embed=embed)

@commands.command()
async def raw(ctx, msg : discord.Message):
  embed = discord.Embed(title = "Raw message", url = msg.jump_url, description = "```"+discord.utils.escape_markdown(msg.content, as_needed=True)+"```")
  await ctx.send(embed=embed)

@commands.command()
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

@commands.command()
async def role(ctx,role: discord.Role=None):
  if role==None:
    role=ctx.author.top_role
  ti="Role Information: "+role.name
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
  f1v=("Mentionable" if mention else "Not mentionable")
  f1v=f1v+f"\nMention: `<&{str(role.id)}>`"
  f2v="Yes" if role.hoist else "No"
  embed.add_field(name="Mentions", value=f1v, inline=True)
  embed.add_field(name="Displayed separately?", value=f2v, inline=True)
  embed.add_field(name="Role ID", value=role.id, inline=True)
  embed.add_field(name="Position in hierarchy", value=role.position, inline=True)
  embed.add_field(name="Color", value=role.color, inline=True)
  if role.is_integration():
    f7v="This role is managed by an integration, such as a bot."
    embed.add_field(name="Integration", value=f7v, inline=False)
  embed.add_field(name="Members ("+str(len(memberlist))+")", value=f0v, inline=False)
  #embed.add_field(name="Channel Permissions", value=f3vb, inline=False)
  await ctx.send(embed=embed)

@commands.command(aliases = ["guild"])
async def server(ctx, text = "regular"):
  guild=ctx.guild
  ti=guild.name
  desc="Created at "+guild.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")+" by "+str(guild.owner.mention)+f"\nRegion: "+str(guild.region)+f"\n[Server Icon]("+str(guild.icon.url)+")"
  embed=discord.Embed(title=ti, description=desc)
  embed.set_author(name="Server Information",icon_url=guild.icon.url)
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
      f2v=" ".join(await guild.invites())
    except:
      f2v="Unable to get invites without Manage-server permission."
    if len(f2v)!=0:
      embed.add_field(name="Invites", value=f2v, inline=True)
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
    if len(guild.stage_channels)==0:
      f1vc="No Voice Channels"
    else:
      f1vc = ""
      for count in guild.stage_channels:
        f1vc = f1vc + count.name + ", "
      f1vc = f1vc[:-2]
      if len(f1vc) > 500:
        f1vc = ""
        for count in guild.stage_channels:
          if len(f1vc + count.name) > 500:
            break
          f1vc = f1vc+count.name+", "
        f1vc = f1vc [:-2] + "…"
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
    embed.add_field(name="Categories ("+str(len(guild.categories))+")", value=f1vb, inline=False)
    embed.add_field(name="Voice Channels ("+str(len(guild.voice_channels))+")", value=f1v, inline=True)
    embed.add_field(name="Stage Channels ("+str(len(guild.stage_channels))+")", value=f1vc, inline=True)
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
    if "WELCOME_SCREEN_ENABLED" in guild.features:
      embed.add_field(name="Welcome Screen", value="The server has enabled the welcome screen.", inline=True)
    if "MEMBER_VERIFICATION_GATE_ENABLED" in guild.features:
      embed.add_field(name="Membership Screening", value="The server has enabled membership screening.", inline=True)
    if "COMMUNITY" in guild.features:
      embed.add_field(name="Community", value="This is a community server.", inline=True)
    if "PUBLIC" in guild.features:
      embed.add_field(name="Public", value="This is a public server.", inline=True)
    if "PARTNERED" in guild.features:
      embed.add_field(name="Partnered", value="This is a partnered (with Discord) server.", inline=True)
    if "VERIFIED" in guild.features:
      embed.add_field(name="Verified", value="This is a verified server.", inline=True)
    embed.add_field(name="Description", value=f13v, inline=False)
    try:
      f11v=" ".join(guild.emojis)
      if len(f11v)!=0:
        embed.add_field(name="Emojis", value=f11v, inline=True)
    except:
      pass
    try:
      embed.set_image(url=guild.banner.url)
    except:
      pass
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

@commands.command()
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

@commands.command()
async def template(ctx, *, tempinput):
  try:
    temp = ctx.bot.fetch_template(tempinput)
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

@commands.command(aliases=["member"])
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
  f1ts = str(datetime.now(timezone.utc) - user.created_at)
  if f1ts.count(" days, ") == 0:
    f1va = re.sub(r'(\d{1,2}):(\d{2}):(\d{2})', r'\1 hours \2 minutes \3 seconds', f1ts) + f"\n≈ "+f1ts.split(":")[0]+" hours"
  else:
    days = int(re.sub(r'([\d]+) days, [\s\S]*', r'\1', f1ts))
    f1va = re.sub(r'([\d]+) days, (\d{1,2}):(\d{2}):(\d{2})', r'\1 days \2 hrs \3 mins \4 secs', f1ts)[:-7] + f"\n≈ "+str((int(f1ts.split(" days, ")[0]))//365) + " years " + str(int(f1ts.split(" days, ")[0]) % 365) + " days"
  f2v=user.joined_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  f2ts = str(datetime.now(timezone.utc) - user.joined_at)
  if f2ts.count(" days, ") == 0:
    f2va = re.sub(r'(\d{1,2}):(\d{2}):(\d{2})', r'\1 hours \2 minutes \3 seconds', f2ts) + f"\n≈ "+f2ts.split(":")[0]+" hours"
  else:
    f2va = re.sub(r'([\d]+) days, (\d{1,2}):(\d{2}):(\d{2})', r'\1 days \2 hrs \3 mins \4 secs', f2ts)[:-7] + f"\n≈ "+str((int(f2ts.split(" days, ")[0]))//365) + " years " + str(int(f2ts.split(" days, ")[0]) % 365) + " days"
  allroles=user.roles
  f3v_raw1 = channel.permissions_for(user).value
  f3v_raw2 = user.guild_permissions.value
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
  embed.add_field(name="Server Permissions", value=server_itop(f3v_raw2), inline=False)
  embed.add_field(name="Text Channel Permissions", value=tc_itop(f3v_raw1), inline=False)
  embed.add_field(name="Voice/Stage Channel Permissions", value=vc_itop(f3v_raw2), inline=False)
  embed.add_field(name="Status", value=f3vd, inline=True)
  try:
    embed.add_field(name="Activity", value=f3vc, inline=True)
  except:
    pass
  embed.add_field(name="Permission integer", value=str(f3v_raw2), inline=True)
  embed.add_field(name="Badges", value=f5v, inline=False)
  await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(avatar)
  bot.add_command(channel)
  bot.add_command(emojiinfo)
  bot.add_command(invitelink)
  bot.add_command(leftuser)
  bot.add_command(message)
  bot.add_command(permissions)
  bot.add_command(raw)
  bot.add_command(reactions)
  bot.add_command(role)
  bot.add_command(server)
  bot.add_command(status)
  bot.add_command(template)
  bot.add_command(user)
