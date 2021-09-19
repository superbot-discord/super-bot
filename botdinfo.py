import discord
from discord.ext import commands
import re
from datetime import datetime, timedelta, timezone

@commands.command()
async def role(ctx,role: discord.Role=None):
  embed = botrole(ctx, role)
  await ctx.send(embed=embed)

@commands.command()
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
  f3v=""
  f3v += ("Admin, "               if channel.permissions_for(user).administrator else "")
  f3v += ("Manage Server, "       if channel.permissions_for(user).manage_guild else "")
  f3v += ("Manage Roles, "        if channel.permissions_for(user).manage_roles else "")
  f3v += ("Manage Permissions, "  if channel.permissions_for(user).administrator else "")
  f3v += ("View Audit Logs, "     if channel.permissions_for(user).view_audit_log else "")
  f3v += ("View Server Insights, "if channel.permissions_for(user).view_guild_insights else "")
  f3v += ("Kick Members, "        if channel.permissions_for(user).kick_members else "")
  f3v += ("Ban Members, "         if channel.permissions_for(user).ban_members else "")
  f3v += ("Manage Nicknames, "    if channel.permissions_for(user).manage_nicknames else "")
  f3v += ("Manage Webhooks, "     if channel.permissions_for(user).manage_webhooks else "")
  f3v += ("Manage Emojis, "       if channel.permissions_for(user).manage_emojis else "")
  f3v += ("Change Nickname, "     if channel.permissions_for(user).manage_nicknames else "")
  f3v += ("Mention Everyone, "    if channel.permissions_for(user).mention_everyone else "")
  f3v += ("Create Invite, "       if channel.permissions_for(user).create_instant_invite else "")
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

def botrole(ctx, role):
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
  return embed

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

async def botserver(ctx, text):
  guild=ctx.guild
  ti=guild.name
  desc="Created at "+guild.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")+" by "+str(guild.owner.mention)+f"\nRegion: "+str(guild.region)+f"\n[Server Icon]("+str(guild.icon_url)+")"
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

async def botinvitel(inviteinput):
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
  return embed

def botstatus(ctx, member):
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
  return embed

def setup(bot):
  bot.add_command(role)
  bot.add_command(user)