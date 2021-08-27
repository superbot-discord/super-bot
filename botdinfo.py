from datetime import timedelta
import discord

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

async def botinvitel(invite):
  # ch=inviteinput.channel
  # allinvites=await ch.invites()
  # for count in allinvites:
  #   if count==inviteinput:
  #     invite=count
  #     break
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