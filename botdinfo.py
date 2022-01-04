from shared import *

cmaphsv = plt.cm.hsv

@commands.command(aliases=["att", "atch"])
async def attachment(ctx, message: discord.Message=None, index: int = 1):
  if message==None:
    potential_reference = ctx.message.reference
    if potential_reference:
      message=await ctx.bot.get_channel(potential_reference.channel_id).fetch_message(potential_reference.message_id)
    else:
      await ctx.reply("Please reply to a message or add a message ID/Link.")
      return
  if len(message.attachments) < index:
      await ctx.reply("The message does not include (that many) attachments.")
      return
  attachment_ = message.attachments[index-1]
  ti=f"Attachment Information: {attachment_.filename}"
  if attachment_.width:
    desc=f"{attachment_.width} (W) × {attachment_.height} (H)"
  else:
    desc=""
  embed = discord.Embed(title=ti, description=desc, url=attachment_.url)
  f0v = attachment_.id
  f1v = sizer(attachment_.size)
  f2v = attachment_.content_type
  f3v = f"[here]({attachment_.proxy_url})"
  embed.add_field(name="ID", value=f0v, inline=True)
  embed.add_field(name="Size", value=f1v, inline=True)
  embed.add_field(name="MIME Type", value=f2v, inline=True)
  embed.add_field(name="Alternative URL (Does not always work!)", value=f3v, inline=False)
  await ctx.reply(embed=embed)

@commands.command(aliases=['av'])
async def avatar(ctx,user: discord.Member=None):
  if not user:
    user=ctx.author
  base_url1 = user.default_avatar
  base_url2 = user.avatar
  base_url3 = user.guild_avatar
  desc = f"Avatar of {user.mention}\n"
  embed=discord.Embed(title="Avatars", description=desc)
  if base_url1:
    base_url1 = base_url1.url
    embed.add_field(name=f"Default avatar", value=base_url1, inline=False)
  if base_url2:
    base_url2 = base_url2.url
    for x in ['png', 'jpg', 'webp']:
      desc = ""
      base_url2 = user.avatar.url.replace('.png', f'.{x}')
      for y in range(5, 13):
        size = str(2**y)
        temp = base_url2.replace("?size=1024", f"?size={size}")
        desc += f"[{size}]({temp}) "
      embed.add_field(name=f"Custom {x.upper()}s", value=desc)
  if base_url3:
    base_url3 = base_url3.url
    for x in ['png', 'jpg', 'webp']:
      desc = ""
      base_url3 = user.avatar.url.replace('.png', f'.{x}')
      for y in range(5, 13):
        size = str(2**y)
        temp = base_url3.replace("?size=1024", f"?size={size}")
        desc += f"[{size}]({temp}) "
      embed.add_field(name=f"Server {x.upper()}s", value=desc)
  embed.set_image(url=user.display_avatar.url)
  await ctx.reply(embed=embed)

@commands.command(aliases = ['badge', 'flag', 'flags'])
async def badges(ctx, integer="help"):
  if integer == "help":
    embed = badges_guide
  else:
    try:
      try:
        int(integer)
      except:
        integer = ctx.author.public_flags.value
      embed = discord.Embed(title = f"Badges integer {integer}", description=badges_itop(int(integer)))
    except:
      embed = badges_guide
  await ctx.reply(embed=embed)

@commands.command(aliases=['bn'])
async def banner(ctx, user: typing.Union[discord.User, discord.Member]=None):
  if user:
    try:
      user = await ctx.bot.fetch_user(user.id)
      base_url = user.banner.url
    except:
      await ctx.reply("The user does not have a banner.")
      return
    desc = f"Banner of {user.mention}\n"
    embed=discord.Embed(title="Banner", description=desc)
    embed.set_image(url=base_url)
    for x in ['png', 'jpg', 'webp']:
      desc = ""
      second_base_url = base_url.replace('.png', f'.{x}')
      for y in range(4, 13):
        size = str(2**y)
        temp = second_base_url.replace("?size=512", f"?size={size}")
        desc += f"[{size}]({temp}) "
      embed.add_field(name=f"{x.upper()}s", value=desc)
  else:
    try:
      base_url = ctx.guild.banner.url
    except:
      await ctx.reply("The server does not have a banner.")
      return
    desc = f"Banner of the server\n"
    embed=discord.Embed(title="Banner", description=desc)
    embed.set_image(url=ctx.guild.banner.url)
    for x in ['png', 'jpg', 'webp']:
      desc = ""
      base_url = ctx.guild.banner.url.replace('.png', f'.{x}')
      for y in range(4, 13):
        size = str(2**y)
        temp = base_url.replace("?size=1024", f"?size={size}")
        desc += f"[{size}]({temp}) "
      embed.add_field(name=f"{x.upper()}s", value=desc)
  await ctx.reply(embed=embed)

@commands.command()
async def category(ctx, category_: discord.CategoryChannel = None):
  if not category_:
    if ctx.channel.category:
      category_ = ctx.channel.category
    else:
      await ctx.reply("Please specify a category.")
      return
  ti=f"Category Information: {category_.name}"
  desc=f"Created at {unix_timestamp(category_.created_at)}"
  embed = discord.Embed(title=ti, description=desc)
  f0valist=category_.text_channels
  f0v=" ".join([x.mention for x in f0valist])
  f1valist=category_.voice_channels
  f1v=" ".join([x.name for x in f1valist])
  f2valist=category_.stage_channels
  f2v=" ".join([x.name for x in f2valist])
  f3v=category_.id
  f4v=category_.position
  embed.add_field(name="ID", value=f3v, inline=True)
  embed.add_field(name="Position", value=f4v, inline=True)
  if len(f0valist)!=0:
    embed.add_field(name=f"Text Channels ({len(f0valist)})", value=f0v, inline=True)
  if len(f1valist)!=0:
    embed.add_field(name=f"Voice Channels ({len(f1valist)})", value=f1v, inline=True)
  if len(f2valist)!=0:
    embed.add_field(name=f"Stage Channels ({len(f2valist)})", value=f2v, inline=True)
  await ctx.reply(embed=embed)

@commands.command(aliases=['ch'])
async def channel(ctx, channel:typing.Union[discord.TextChannel, discord.VoiceChannel, discord.StageChannel]=None):
  if not channel:
    channel = ctx.channel
  if channel.type == discord.ChannelType.text:
    task = asyncio.create_task(bottchannel(channel))
    await task
    await ctx.reply(embed=task.result())
  elif channel.type == discord.ChannelType.voice:
    task = asyncio.create_task(botvchannel(channel))
    await task
    await ctx.reply(embed=task.result())
  elif channel.type == discord.ChannelType.stage_voice:
    task = asyncio.create_task(botstagec(channel))
    await task
    await ctx.reply(embed=task.result())
  elif channel.type in [discord.ChannelType.public_thread, discord.ChannelType.private_thread]:
    task = asyncio.create_task(botthread(channel))
    await task
    await ctx.reply(embed=task.result())
  else:
    embed = discord.Embed(desc = "Invalid input.")
    await ctx.reply(embed=embed)

async def bottchannel(channel):
  ti=f"Channel Information: {channel.name}"
  desc=f"{channel.mention} Created at {unix_timestamp(channel.created_at)}"
  embed=discord.Embed(title=ti, description=desc)
  f1v = channel.slowmode_delay
  f2v = [x.name for x in channel.threads]
  f3v=str(channel.topic)
  try:
    f5v=" ".join(await channel.invites())
  except:
    f5v="Cannot get invites without Manage Invites permission."
  f8v = ""
  for x in channel.members:
    f8v=f"{f8v}{x.mention} "
  f8v=f8v[:-1]
  if len(f8v) > 500:
    f8v = ""
    for x in channel.members:
      if len(f8v + x.name) > 500:
        break
      f8v = f"{f8v}{x.name}, "
    f8v = f"{f8v [:-2]} …"
  async for x in channel.history(limit=1, oldest_first=True):
    f9v=x
  if len(f3v)>=45:
    embed.add_field(name="Topic", value=f3v, inline=False)
  else:
    embed.add_field(name="Topic", value=f3v, inline=True)
  embed.add_field(name="Category", value=str(channel.category), inline=True)
  if f1v:
    embed.add_field(name="Slowmode delay", value=f"{f1v} seconds", inline=True)
  embed.add_field(name="Members", value=f8v, inline=False)
  if f2v:
    embed.add_field(name="Threads", value=f2v, inline=False)
  if f5v:
    embed.add_field(name="Invites", value=f5v, inline=True)
  embed.add_field(name="ID", value=channel.id, inline=True)
  embed.add_field(name="First message", value="[here](https://youtube.com/watch?v=Tt7bzxurJ1I)" if datetime.now().minute == 14 else f"[here]({f9v.jump_url})", inline=True)
  if channel.is_nsfw()==True:
    embed.add_field(name="NSFW", value="This is an NSFW channel.", inline=True)
  if channel.is_news()==True:
    embed.add_field(name="News", value="This is a news channel.", inline=True)
  return embed

async def botvchannel(channel):
  ti=f"Voice Channel Information: {channel.name}"
  desc=f"{channel.mention} created at {unix_timestamp(channel.created_at)}"
  embed=discord.Embed(title=ti, description=desc)
  f1v = channel.video_quality_mode
  try:
    f2vlist=await channel.invites()
    f2v=""
    for x in f2vlist:
      f2v=f"{f2v}{x.url}  "
    f2v=f2v[:-2]
  except:
    f2v = "Cannot get invites without Manage Invites permission."
  f5vlist=channel.members
  f5v=" ".join([x.mention for x in f5vlist])
  f3v=str(channel.bitrate//1000)+" kbps"
  if str(channel.user_limit)=="0":
    f4v="Infinite"
  else:
    f4v=f"{len(f5vlist)}/{channel.user_limit} members"
  f6v = channel.rtc_region
  embed.add_field(name="Category", value=str(channel.category), inline=True)
  embed.add_field(name="Invites", value=f2v, inline=False)
  embed.add_field(name="Bitrate", value=f3v, inline=True)
  embed.add_field(name="Max. Members", value=f4v, inline=True)
  embed.add_field(name="Server region", value=voice_region_format(channel.rtc_region), inline=True)
  if f1v == discord.VideoQualityMode.auto:
    embed.add_field(name="Video quality", value="Auto", inline=True)
  else:
    embed.add_field(name="Video quality", value="Full (720p)", inline=True)
  if len(f5vlist)!=0:
    embed.add_field(name="Current Members", value=f5v, inline=True)
  return embed

async def botstagec(channel):
  ti=f"Stage Channel Information: {channel.name}"
  if channel.topic:
    desc=f"{channel.mention}  {channel.topic}\nCreated at {unix_timestamp(channel.created_at)}"
  else:
    desc=f"{channel.name}\nCreated at {unix_timestamp(channel.created_at)}"
  embed=discord.Embed(title=ti, description=desc)
  f2vlist=await channel.invites()
  f2v="  ".join([x.url for x in f2vlist])
  f3v=f"{channel.bitrate//1024} kbps"
  if channel.user_limit:
    f4v=f"{channel.user_limit} members"
  else:
    f4v="Infinite"
  f5valist=channel.listeners
  f5va=" ".join([x.mention for x in f5valist])
  f5vblist=channel.speakers
  f5vb=" ".join([x.mention for x in f5vblist])
  f6vlist=channel.requesting_to_speak
  f6v=" ".join([x.mention for x in f6vlist])
  f7vx=channel.instance
  embed.add_field(name="Category", value=str(channel.category), inline=True)
  if len(f2vlist)!=0:
    embed.add_field(name="Invites", value=f2v, inline=False)
  embed.add_field(name="Bitrate", value=f3v, inline=True)
  embed.add_field(name="Max. Members", value=f4v, inline=True)
  if len(f5valist)!=0:
    embed.add_field(name="Members listening", value=f5va, inline=True)
  if len(f5vblist)!=0:
    embed.add_field(name="Members speaking", value=f5vb, inline=True)
  if len(f6vlist)!=0:
    embed.add_field(name="Members requesting to speak", value=f6v, inline=True)
  if f7vx:
    f7v = f"Topic: {f7vx.topic}\nDiscovery: {'disabled' if f7vx.discoverable_disabled else 'enabled'}\nPrivacy level: {'server members only' if f7vx.privacy_level == discord.StagePrivacyLevel.closed else 'everyone on Discord'}"

async def botthread(channel):
  ti=f"Thread Information: {channel.name}"
  desc=f"{channel.mention} Created by {channel.owner.mention}\nArchives at {unix_timestamp(channel.archive_timestamp)}"
  embed=discord.Embed(title=ti, description=desc)
  f1v = channel.slowmode_delay
  f8v = ""
  for x in channel.members:
    if len(f"{f8v}<@{x.id}> ") >= 500:
      f8v += "…"
    f8v+= f"<@{x.id}> "
  async for x in channel.history(limit=1, oldest_first=True):
    f9v=x
  embed.add_field(name="Category", value=str(channel.category), inline=True)
  if f1v:
    embed.add_field(name="Slowmode delay", value=f"{f1v} seconds", inline=True)
  embed.add_field(name="Members", value=f8v, inline=False)
  embed.add_field(name="ID", value=channel.id, inline=True)
  embed.add_field(name="First message", value=f"[here]({f9v.jump_url})", inline=True)
  if channel.is_nsfw():
    embed.add_field(name="NSFW", value="This is an NSFW thread.", inline=True)
  if channel.is_news():
    embed.add_field(name="News", value="This is a news thread.", inline=True)
  if channel.is_private():
    embed.add_field(name="Private", value="This is a private thread.", inline=True)
  return embed

@commands.command(aliases=['emi'])
async def emojiinfo(ctx, emoji_: typing.Union[discord.Emoji, str]):
  try:
    try:
      creator = await ctx.guild.fetch_emoji(emoji_.id)
      desc = f"{str(emoji_)} {emoji_.name}\nCreated by {str(creator.user.mention)} at {unix_timestamp(emoji_.created_at)}"
    except:
      desc = f"{emoji_}\n`Created by` field can only be retrieved with the manage-emojis permission.\nCreated at {unix_timestamp(emoji_.created_at)}"
    embed = discord.Embed(title=f"Emoji Info: {emoji_.name}", description=desc)
    embed.add_field(name="ID", value=emoji_.id, inline=True)
    embed.set_image(url = emoji_.url)
  except:
    cemoji = ems.db.get_emoji_by_alias(emoji_)
    if not cemoji:
      cemoji = ems.db.get_emoji_by_code(emoji_)
    if not cemoji:
      await ctx.send(f"Emoji not found!\nNote: regional indicators are not emojis in the technical sense.")
      return
    embed = discord.Embed(title="Emoji Info", description = (cemoji[1]+" \:" + ':, \:'.join(cemoji[0]) +":"))
    embed.add_field(name="Category", value=cemoji[3], inline=True)
    if cemoji[4]:
      embed.add_field(name="Unicode Version", value=cemoji[4], inline=True)
    if len(cemoji[2]) > 0:
      embed.add_field(name="Tags", value=", ".join(cemoji[2]), inline=True)
  await ctx.reply(embed=embed)

@commands.command(aliases=['ems'])
async def emojis(ctx, *, disposed = None):
  desc = ""
  sent_desc = ""
  for x in ctx.guild.emojis:
    #temp_desc = f"<:{y.name}:{y.id}>{' (Animated)' if y.animated else ''}"
    temp_desc = f"{x}{' (Animated)' if x.animated else ''}"
    desc += f":{(x.name+':'):<35} {temp_desc:<60}{x.url}\n"
    sent_desc += f"{x} "
  f = open('output.txt', 'w')
  f.write(desc)
  f.flush()
  f.close()
  try:
    await ctx.reply(sent_desc, file=discord.File('output.txt'))
  except:
    await ctx.reply(file=discord.File('output.txt'))
  try_delete('output.txt')

@commands.command(aliases=['il'])
async def invitelink(ctx, *, invite_input: discord.Invite):
  invite_has_info = False
  try:
    allinvites=await invite_input.guild.invites()
    for x in allinvites:
      if x == invite_input:
        invite = x
        break
    assert invite
    invite_has_info = True
  except:
    invite = invite_input
  ti=f"Invite Information: {invite.code}"
  f2v = f"{invite.channel.mention} ({invite.channel.type})"
  f3v = invite.url
  f4v = invite.id
  if invite_has_info:
    desc=f"Created at {unix_timestamp(invite.created_at)} by {invite.inviter}"
    f1v = invite.temporary
    age = invite.max_age
    if age==0:
      f5v="Never Expires"
    elif age>86400:
      f5v=f"{age/86400} day(s)"
    elif age>3600:
      f5v=f"{age/3600} hour(s)"
    else:
      f5v=f"{age/60} minute(s)"
    if f5v == "Never Expires":
      f7v = "Never"
    else:
      f7v=f"{unix_timestamp(invite.created_at+timedelta(seconds=age))}"
    if invite.max_uses == 0:
      f0v=str(invite.uses)
    else:
      f0v = f"{invite.uses}/{invite.max_uses}"
  else:
    desc= f"Created by {invite.inviter}\nNote: Some information cannot be retrieved as the invite does not come from the current server!"
  embed=discord.Embed(title=ti, description=desc)
  f6v=str(invite.revoked)
  invite_guild = invite.guild
  if invite_guild:
    embed.title = f"Invite Information: {invite.code} ({invite_guild.name})"
    if invite_guild.banner:
      base_url1 = invite_guild.banner.url
      embed.set_image(url=base_url1)
      for x in ['png', 'jpg', 'webp']:
        desc = ""
        base_url1 = invite_guild.banner.url.replace('.png', f'.{x}')
        for y in range(4, 13):
          size = str(2**y)
          temp = base_url1.replace("?size=1024", f"?size={size}")
          desc += f"[{size}]({temp}) "
        embed.add_field(name=f"{'Ser.' if x == 'webp' else 'Server'} {x.upper()} banners", value=desc)
    if invite_guild.banner:
      base_url1 = invite_guild.banner.url
      embed.set_image(url=base_url1)
      for x in ['png', 'jpg', 'webp']:
        desc = ""
        base_url1 = invite_guild.banner.url.replace('.png', f'.{x}')
        for y in range(5, 13):
          size = str(2**y)
          temp = base_url1.replace("?size=1024", f"?size={size}")
          desc += f"[{size}]({temp}) "
        embed.add_field(name=f"Server {x.upper()} icons", value=desc)
    embed.add_field(name="Server Verification Level", value=str(invite_guild.verification_level))
    if invite_guild.description:
      embed.add_field(name="Server Description", value=invite_guild.description, inline=False)
  else:
    embed.add_field(name="Server", value=f"Invite link", inline=True)
  if invite_has_info:
    embed.add_field(name="Uses", value=f0v, inline=True)
    embed.add_field(name="Temporary?", value=f1v, inline=True)
  embed.add_field(name="URL", value=f3v, inline=True)
  embed.add_field(name="Channel", value=f2v, inline=True)
  #embed.add_field(name="ID", value=f4v, inline=True)
  if invite_has_info:
    embed.add_field(name="Expires", value=f7v, inline=True)
    embed.add_field(name="Valid Duration", value=f5v, inline=True)
  embed.add_field(name="Expired?", value=f6v, inline=True)
  await ctx.reply(embed=embed)

@commands.command(aliases=["lu"])
async def leftuser(ctx, *, userinput):
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
  embed.set_thumbnail(url=lfuser.display_avatar.url)
  f0v=f"{lfuser.name}#{lfuser.discriminator}"
  f1v={unix_timestamp(lfuser.created_at)}
  f1ts = str(datetime.now(timezone.utc) - lfuser.created_at)
  if " days, " not in f1ts:
    f1va = re.sub(r'(\d{1,2}):(\d{2}):(\d{2})', r'\1 hours \2 minutes \3 seconds', f1ts) + f"\n≈ "+f1ts.split(":")[0]+" hours"
  else:
    days = int(re.sub(r'([\d]+) days, [\s\S]*', r'\1', f1ts))
    f1va = re.sub(r'([\d]+) days, (\d{1,2}):(\d{2}):(\d{2})', r'\1 days \2 hrs \3 mins \4 secs', f1ts)[:-7] + f"\n≈ "+str((int(f1ts.split(" days, ")[0]))//365) + " years " + str(int(f1ts.split(" days, ")[0]) % 365) + " days"
  embed.add_field(name="Name", value=f0v, inline=False)
  embed.add_field(name="Time since user registered", value=f1va, inline=True)
  embed.add_field(name="Registered", value=f1v, inline=True)
  await ctx.reply(embed=embed)

@commands.command(aliases=["msg", "ms"])
async def message(ctx, message: discord.Message=None):
  if message==None:
    potential_reference = ctx.message.reference
    if potential_reference:
      message=await ctx.bot.get_channel(potential_reference.channel_id).fetch_message(potential_reference.message_id)
    else:
      await ctx.reply("Please reply to a message or add a message ID/Link.")
      return
  desc=f"Sent by {message.author.mention} at {unix_timestamp(message.created_at)}"
  if message.edited_at != None:
    desc += f"Edited at {unix_timestamp(message.edited_at)}"
  contents = message.content
  if contents:
    desc += f"\n**Message content: **\n{contents}"
  f0vraw = message.reactions
  f0v = ""
  for x in f0vraw:
    if x.custom_emoji:
      f0v += f":{x.emoji}:   ({x.count})"
    else:
      f0v += f"{x.emoji}   ({x.count})"
  f1vraw = message.attachments
  f1v = ""
  for x in f1vraw:
    if x.is_spoiler():
      f1v += f"[{x.filename}]({x.url}) ({sizer(x.size)}, marked as spoiler)\n"
    else:
      f1v += f"[{x.filename}]({x.url}) ({sizer(x.size)})\n"
  f2vraw = message.channel_mentions
  f2v = ""
  for x in f2vraw:
    f2v += x.mention + " "
  f3vraw = message.role_mentions
  f3v = ""
  for x in f3vraw:
    f3v += x.mention + " "
  f4vraw = message.mentions
  f4v = ""
  for x in f4vraw:
    f4v += x.mention + " "
  f5vraw = message.components
  msg_buttons = msg_menus = msg_dbuttons = msg_dmenus = 0
  for x in f5vraw:
    if x.type == discord.ComponentType.action_row:
      for y in x.children:
        if y.type == discord.ComponentType.button:
          if y.disabled:
            msg_dbuttons += 1
          else:
            msg_buttons += 1
        else:
          if y.disabled:
            msg_dmenus += 1
          else:
            msg_menus += 1
    else:
      if x.type == discord.ComponentType.button:
        if x.disabled:
          msg_dbuttons += 1
        else:
          msg_buttons += 1
      else:
        if x.disabled:
          msg_dmenus += 1
        else:
          msg_menus += 1
  embed=discord.Embed(title="Message Information", description=desc[:2047], url=message.jump_url)
  embed.add_field(name="In channel", value=message.channel.mention, inline=True)
  if message.pinned:
    embed.add_field(name="Pinned", value="This message is pinned.", inline=True)
  if message.mention_everyone:
    embed.add_field(name="@everyone", value="This message mentioned everyone.", inline=True)
  embed.add_field(name="ID", value=str(message.id), inline=True)
  if message.webhook_id != None:
    embed.add_field(name="Webhook message", value="This message is sent by a webhook.", inline=True)
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
    embed.add_field(name="System message", value=f"This is a system message indicating that someone pinned [a message]({message.reference.jump_url}).", inline=False)
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
  if message.flags.urgent:
    embed.add_field(name="Special message", value="This message is sent by Discord's Trust and Safety Team and is urgent.", inline=False)
  if message.flags.ephemeral:
    embed.add_field(name="Ephemeral message", value="This is an ephemeral message (can only be seen by you).", inline=False)
  if message.flags.is_crossposted:
    embed.add_field(name="Followed message", value="This is a message followed from an announcement channel in another server.", inline=False)
  if message.flags.crossposted:
    embed.add_field(name="Published message", value="This is a published message in an announcement channel.", inline=False)
  if message.flags.source_message_deleted:
    embed.add_field(name="Source deleted", value="This message's original source has been deleted.", inline=False)
  if message.flags.has_thread:
    embed.add_field(name="Thread", value="This message is associated with a thread.", inline=False)
  if message.flags.suppress_embeds:
    embed.add_field(name="Suppresed embeds", value="This message's embed(s) are suppressed.", inline=False)
  if message.application != None:
    embed.add_field(name=message.application["name"], value=f"This message is created by {message.application['name']}.\n{message.application['description']}", inline=False)
  if len(f0vraw) != 0:
    embed.add_field(name=f"Reactions ({len(f0vraw)})", value=f0v, inline=False)
  if len(f1vraw) != 0:
    embed.add_field(name=f"Attachments ({len(f1vraw)})", value=f1v, inline=False)
  if len(message.embeds) != 0:
    embed.add_field(name="Embeds", value=f"{len(message.embeds)} embed(s) are added to the message.", inline=False)
  if len(f5vraw) != 0:
    embed.add_field(name="Components", value=f"Working buttons & menus: {msg_buttons}, {msg_menus}\nDisabled buttons & menus: {msg_dbuttons}, {msg_dmenus}", inline=False)
  if len(f2vraw) != 0:
    embed.add_field(name=f"Channel mentions ({len(f2vraw)})", value=f2v, inline=False)
  if len(f3vraw) != 0:
    embed.add_field(name=f"Role mentions ({len(f3vraw)})", value=f3v, inline=False)
  if len(f4vraw) != 0:
    embed.add_field(name=f"User mentions ({len(f4vraw)})", value=f4v, inline=False)
  await ctx.reply(embed=embed)

@commands.command()
async def overwrites(ctx, channel_:typing.Union[discord.TextChannel, discord.VoiceChannel, discord.StageChannel, discord.CategoryChannel] = None):
  if not channel_:
    channel_ = ctx.channel
  desc = f"{channel_.mention}\n"
  for x, y in channel_.overwrites.items().__reversed__():
    desc += f"**{x.mention}**\nAllowed: {y.pair()[0].value} Denied: {y.pair()[1].value}\n"
  embed = discord.Embed(title=f"Overwrites information", description=desc[:4096])
  await ctx.reply(embed=embed)

@commands.command(aliases = ['perm', 'perms', 'permission'])
async def permissions(ctx, integer="help"):
  if integer == "help":
    embed = perms_guide
  else:
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
      embed.add_field(name = "Membership permissions", value=ms_itop(int(integer)), inline=False)
      embed.add_field(name = "Text permissions", value=tc_itop(int(integer)), inline=False)
      embed.add_field(name = "Voice permissions", value=vc_itop(int(integer)), inline=False)
    except:
      try:
        for x, y in custom_permissions.items():
          if SequenceMatcher(None, integer, x).ratio() >= 0.75:
            embed = discord.Embed(title = f"Custom permission {integer}")
            embed.add_field(name = "Server permissions", value=server_itop(y.value), inline=False)
            embed.add_field(name = "Membership permissions", value=ms_itop(y.value), inline=False)
            embed.add_field(name = "Text permissions", value=tc_itop(y.value), inline=False)
            embed.add_field(name = "Voice permissions", value=vc_itop(y.value), inline=False)
            break
        embed
      except:
        embed = perms_guide
  await ctx.reply(embed=embed)

@commands.command(aliases= ['permgen', 'permsgen', 'permgenerate', 'permsgenerate', 'permission_gen', 'permissions_gen' 'permission_generate'])
async def permission_generate(ctx, *, disposed = None):
  permission_view = ui.View(timeout=None)
  for x in permission_menus:
    permission_view.add_item(x)
  #for x in permission_buttons:
  #  permission_view.add_item(x)
  #print(len(permission_view))
  msg = await ctx.reply("Select the permissions! You can select multiple options.", view = permission_view)
  permission_messages[msg] = {"permission_server_selection": [], "permission_membership_selection": [], "permission_text_selection": [], "permission_voice_selection": []}

@commands.command()
async def raw(ctx, msg : discord.Message = None):
  if msg==None:
    potential_reference = ctx.message.reference
    if potential_reference:
      msg=await ctx.bot.get_channel(potential_reference.channel_id).fetch_message(potential_reference.message_id)
    else:
      await ctx.reply("Please reply to a message or add a message ID/Link.")
      return
  embed = discord.Embed(title = "Raw message", url = msg.jump_url, description = "```"+msg.content.replace('```', r'\`\`\`')+"```")
  await ctx.reply(embed=embed)

@commands.command()
async def rawraw(ctx, msg : discord.Message = None):
  if msg==None:
    potential_reference = ctx.message.reference
    if potential_reference:
      msg=await ctx.bot.get_channel(potential_reference.channel_id).fetch_message(potential_reference.message_id)
    else:
      await ctx.reply("Please reply to a message or add a message ID/Link.")
      return
  embed = discord.Embed(title = "Raw message", url = msg.jump_url, description = f"```{discord.utils.escape_markdown(msg.content, as_needed=True)}```")
  await ctx.reply(embed=embed)

@commands.command(aliases=["rea"])
async def reactions(ctx, *, msg : discord.Message = None):
  if msg==None:
    potential_reference = ctx.message.reference
    if potential_reference:
      msg=await ctx.bot.get_channel(potential_reference.channel_id).fetch_message(potential_reference.message_id)
    else:
      await ctx.reply("Please reply to a message or add a message ID/Link.")
      return
  reactions = msg.reactions
  numlist = []
  mylabels = []
  for x in reactions:
    numlist.append(x.count)
    try:
      mylabels.append(ems.decode(x.emoji))
    except:
      mylabels.append(f"*{x.emoji.name}")
  mylabels = tuple(mylabels)
  y = np.array(numlist)
  mycolors = []
  for x in range(len(numlist)):
    mycolors.append(cmaphsv(x/len(numlist)))
  patches, labels, pct_texts = plt.pie(y, labels=mylabels, colors=mycolors, rotatelabels=True,
  pctdistance=0.6, autopct=lambda pct: func(pct, y),textprops = db["font_dicts"]["label"])
  for label, pct_text in zip(labels, pct_texts):
    pct_text.set_rotation(label.get_rotation())
    pct_text.update(db["font_dicts"]["light_label"])
  #plt.legend(labels, list(mylabels), prop=db["font_dicts"]["legend"])#, labelcolor=mycolors)
  plt.title("Reaction Status", fontdict=db["font_dicts"]["title"])
  plt.savefig("reactions.png", transparent=True)
  plt.savefig("reactions.svg", transparent=True)
  await ctx.reply(files = [discord.File('reactions.png'), discord.File('reactions.svg')])
  plt.clf()

@commands.command(aliases=["ro"])
async def role(ctx,role: discord.Role=None):
  if role==None:
    role=ctx.author.top_role
  ti=f"Role Information: {role.name}"
  desc=f"{role.mention} created at {unix_timestamp(role.created_at)}"
  embed=discord.Embed(title=ti,color=role.color, description=desc)
  memberlist=role.members
  if len(memberlist) == 0:
    f0v = "No members assigned with this role."
  else:
    f0v = ""
    for x in memberlist:
      f0v = f"{f0v}{x.mention} "
    f0v = f0v[:-1]
  mention=role.mentionable
  f1v=("Mentionable by everyone" if mention else "Not mentionable by everyone")
  f2v="Yes" if role.hoist else "No"
  embed.add_field(name="Mentions", value=f1v, inline=True)
  embed.add_field(name="Displayed separately?", value=f2v, inline=True)
  embed.add_field(name="Role ID", value=role.id, inline=True)
  embed.add_field(name="Position from top", value=role.position, inline=True)
  embed.add_field(name="Color", value=role.color, inline=True)
  embed.add_field(name="Permission integer", value=str(role.permissions.value), inline=True)
  if role.is_integration():
    embed.add_field(name="Integration", value="This role is managed by an integration.", inline=False)
  if role.is_bot_managed():
    embed.add_field(name="Bot", value="This is a bot role.", inline=False)
  if role.is_premium_subscriber():
    embed.add_field(name="Bot", value="This is the Discord Booster role.", inline=False)
  embed.add_field(name="Members ("+str(len(memberlist))+")", value=f0v[:5950-len(embed)], inline=False)
  #embed.add_field(name="Channel Permissions", value=f3vb, inline=False)
  await ctx.reply(embed=embed)

@commands.command(aliases=["guild", "se"])
async def server(ctx, *, text = "regular"):
  guild=ctx.guild
  ti=guild.name
  desc=f"Created at {unix_timestamp(guild.created_at)} by {guild.owner.mention}\nRegion: {guild.region}"
  try:
    base_url = guild.icon.url
    desc += f"\nServer Icon: "
    for x in range(5, 13):
      size = str(2**x)
      temp = base_url.replace("?size=1024", f"?size={size}")
      desc += f"[{size}]({temp}) "
  except:
    pass
  try:
    base_url = guild.banner.url
    desc += f"\nServer Banner: "
    for x in range(4, 13):
      size = str(2**x)
      temp = base_url.replace("?size=1024", f"?size={size}")
      desc += f"[{size}]({temp}) "
  except:
    pass
  try:
    base_url = guild.splash.url
    desc += f"\nServer Invite Splash: "
    for x in range(4, 13):
      size = str(2**x)
      temp = base_url.replace("?size=1024", f"?size={size}")
      desc += f"[{size}]({temp}) "
  except:
    pass
  embed=discord.Embed(title=ti, description=desc)
  try:
    embed.set_author(name="Server Information",icon_url=guild.icon.url)
  except:
    embed.set_author(name="Server Information")
  if text == "mod":
    try:
      f1vlist=await guild.bans()
      f1v=""
      for x in f1vlist:
        f1v=f"{f1v}{x.user.mention} "
      f1v=f1v[:-1]
    except:
      f1v="Unable to get banned members without the Ban Members permission."
      if len(f1v)==0:
        f1v = "No banned members."
    if len(f1v)!=0:
      embed.add_field(name="Banned Users", value=f1v, inline=True)
    try:
      f2v=" ".join(await guild.invites())
      if len(f2v)==0:
        f2v = "No invites."
    except:
      f2v="Unable to get invites without the Manage Server permission."
    embed.add_field(name="Invites", value=f2v, inline=True)
  else:
    f0v=""
    for x in guild.text_channels:
      if len(f"{f0v}{x.mention}, ") > 1024:
        f0v = ""
        for y in guild.text_channels:
          if len(f"{f0v}{y.name}, ") > 1024:
            f0v += "… "
            break
          f0v += f"{y.name}, "
        break
      f0v += f"{x.mention}, "
    f1v=""
    f0v=f0v[:-1]
    if len(guild.voice_channels)==0:
      f1v="No Voice Channels"
    else:
      f1v = ""
      for x in guild.voice_channels:
        f1v = f"{f1v}{x.name}, "
      f1v = f1v[:-2]
      if len(f1v) > 500:
        f1v = ""
        for x in guild.voice_channels:
          if len(f"{f1v}{x.name}") > 500:
            break
          f1v = f"{f1v}{x.name}, "
        f1v = f1v [:-2] + "…"
    if len(guild.stage_channels)==0:
      f1vc="No Voice Channels"
    else:
      f1vc = ""
      for x in guild.stage_channels:
        f1vc = f"{f1vc}{x.name}, "
      f1vc = f1vc[:-2]
      if len(f1vc) > 500:
        f1vc = ""
        for x in guild.stage_channels:
          if len(f"{f1vc}{x.name}") > 500:
            break
          f1vc = f"{f1vc}{x.name}, "
        f1vc = f"{f1vc[:-2]}…"
    f1vb=""
    if len(guild.categories)==0:
      f1vb="No Categories"
    else:
      for x in guild.categories:
        f1vb=f"{f1vb}{x.name}, "
      f1vb = f1vb[:-2]
    f1va = ""
    f1valist = guild.roles
    f1valist.reverse()
    for x in f1valist:
      if len(f"{f1va}{x.mention}") > 1024:
        break
      f1va = f"{f1va}{x.mention} "
    f1va = f1va[:-1]
    f2v = f"{guild.bitrate_limit//1000} kbps"
    f3v = f"{guild.filesize_limit//1048576} MB"
    f4v = str(guild.emoji_limit)
    f5v = guild.mfa_level
    if f5v==1:
      f5v="Required"
    else:
      f5v="Not Required"
    f6v=str(guild.verification_level)
    ecf=guild.explicit_content_filter
    if ecf==discord.ContentFilter.disabled:
      f7v="Disabled"
    elif ecf==discord.ContentFilter.no_role:
      f7v="Members without roles"
    elif ecf==discord.ContentFilter.all_members:
      f7v="All Members"
    f8v=""
    for x in guild.members:
      f8v=f"{f8v}{x.mention} "
    f8v=f8v[:-1]
    if len(f8v) > 500:
      f8v = ""
      for x in guild.members:
        if len(f"{f8v}{x.name}") > 500:
          break
        f8v = f"{f8v}{x.name}, "
      f8v = f"{f8v[:-2]}…"
    f10va = str(guild.id)
    f13v = guild.description
    if f13v == None:
      f13v = "No description"
    embed.add_field(name=f"Text Channels ({len(guild.text_channels)})", value=f0v, inline=False)
    embed.add_field(name=f"Categories ({len(guild.categories)})", value=f1vb, inline=False)
    embed.add_field(name=f"Voice Channels ({len(guild.voice_channels)})", value=f1v, inline=True)
    embed.add_field(name=f"Stage Channels ({len(guild.stage_channels)})", value=f1vc, inline=True)
    embed.add_field(name=f"Roles ({len(guild.roles)})", value=f1va, inline=False)
    embed.add_field(name=f"Members ({guild.member_count})", value=f8v, inline=False)
    embed.add_field(name="Max bitrate", value=f2v, inline=True)
    embed.add_field(name="Max filesize", value=f3v, inline=True)
    embed.add_field(name="Max emojis", value=f4v, inline=True)
    embed.add_field(name="2FA for Moderation", value=f5v, inline=True)
    embed.add_field(name="Verification Level", value=f6v, inline=True)
    embed.add_field(name="Explict Content Filter", value=f7v, inline=True)
    if guild.afk_channel!=None:
      f9v=f"{guild.afk_timeout//60} minute(s)"
      embed.add_field(name="AFK Timeout", value=f9v, inline=True)
      embed.add_field(name="AFK Channel", value=guild.afk_channel.mention, inline=True)
    embed.add_field(name="Server boosts", value=str(guild.premium_subscription_count), inline=True)
    if guild.default_notifications == discord.NotificationLevel.all_messages:
      embed.add_field(name="Default Notifications", value="All messages", inline=True)
    else:
      embed.add_field(name="Default Notifications", value="Mentions only", inline=True)
    embed.add_field(name="ID", value=f10va, inline=True)
    if "WELCOME_SCREEN_ENABLED" in guild.features:
      embed.add_field(name="Welcome Screen", value="The server has enabled the welcome screen.", inline=True)
    if "MEMBER_VERIFICATION_GATE_ENABLED" in guild.features:
      embed.add_field(name="Membership Screening", value="The server has enabled membership screening.", inline=True)
    if "COMMUNITY" in guild.features:
      embed.add_field(name="Community", value="This is a community server.", inline=True)
    if "PUBLIC" in guild.features:
      embed.add_field(name="Public", value="This is a public server.", inline=True)
    if "PARTNERED" in guild.features:
      embed.add_field(name="Partnered", value="This is a partnered server (with Discord).", inline=True)
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
    await ctx.reply(embed=embed)
  except:
    f1va = ""
    for x in f1valist:
      if len(f"{f1va}{x.name}") > 500:
        break
      f1va += f"{x.name}, "
    f1va = f"{f1va[:-2]}…"
    embed.set_field_at(3, name=f"Roles ({len(guild.roles)})", value=f1va, inline=False)
    await ctx.reply(embed=embed)

@commands.command(aliases=["sta"])
async def status(ctx, member : discord.Member = None):
  if member==None:
    member=ctx.author
  if member.is_on_mobile==True:
    desc = str(member.status)+" on mobile"
  else:
    desc = str(member.status)+" on desktop"
  embed = discord.Embed(title=f"Status: {member.name}", description=desc)
  for x in member.activities:
    if x.type==discord.ActivityType.custom:
      if x.emoji==None:
        field=x.name
      else:
        try:
          field=":"+x.emoji.name+": "+x.name
        except:
          try:
            field=x.name
          except:
            field=":"+x.emoji.name+":"
      embed.add_field(name="Status", value=field, inline=False)
    if x.type==discord.ActivityType.playing:
      field=x.name+f"\nStarted: {unix_timestamp(x.start)}"
      embed.add_field(name="Game", value=field, inline=False)
    if x.type==discord.ActivityType.streaming:
      field=f"[{x.platform}: {x.name}]({x.url})\nStarted: {unix_timestamp(x.start)}"
      embed.add_field(name="Game", value=field, inline=False)
      embed.set_thumbnail(url=x.large_image_url)
    if x.type==discord.ActivityType.listening:
      field=f"{x.artist}: {x.title}\nStarted: "
      embed.add_field(name=f"Spotify: {x.album}", value=field, inline=False)
      embed.set_thumbnail(url=x.album_cover_url)
  await ctx.reply(embed=embed)

@commands.command(aliases=["stu"])
async def statuses(ctx, *, disposed = None):
  bot_onlines = bot_dnds = bot_idles = bot_offlines = 0
  usr_onlines = usr_dnds = usr_idles = usr_offlines = 0
  for x in ctx.guild.members:
    if x.bot:
      if x.status == discord.Status.online:
        bot_onlines += 1
      elif x.status == discord.Status.dnd:
        bot_dnds += 1
      elif x.status == discord.Status.idle:
        bot_idles += 1
      else:
        bot_offlines += 1
    else:
      if x.status == discord.Status.online:
        usr_onlines += 1
      elif x.status == discord.Status.dnd:
        usr_dnds += 1
      elif x.status == discord.Status.idle:
        usr_idles += 1
      else:
        usr_offlines += 1
  fig = plt.figure(tight_layout=False)
  statuses_grid = gridspec.GridSpec(3,2)
  ax1 = fig.add_subplot(statuses_grid[0, 0])
  ax2 = fig.add_subplot(statuses_grid[0, 1])
  ax3 = fig.add_subplot(statuses_grid[1:,0:])
  #Bots
  numlist = [bot_onlines, bot_dnds, bot_idles, bot_offlines]
  patches, labels, pct_texts = ax1.pie(np.array(numlist), labels=("Online", "DND", "Idle", "Offline"),
    colors=["#3ba55d", "#ed4245", "#faa91a", "#747f8d"], rotatelabels=True, pctdistance=0.625,
  autopct=lambda pct: func(pct, numlist), textprops = db["font_dicts"]["tiny"])
  for label, pct_text in zip(labels, pct_texts):
    pct_text.set_rotation(label.get_rotation())
    pct_text.update(db["font_dicts"]["light_mini"])
  ax1.set_title("Bot statuses", fontdict=db["font_dicts"]["semi_title"])
  #Humans
  numlist = [usr_onlines, usr_dnds, usr_idles, usr_offlines]
  patches, labels, pct_texts = ax2.pie(np.array(numlist), labels=("Online", "DND", "Idle", "Offline"),
    colors=["#3ba55d", "#ed4245", "#faa91a", "#747f8d"], rotatelabels=True, pctdistance=0.625,
  autopct=lambda pct: func(pct, numlist), textprops = db["font_dicts"]["tiny"])
  for label, pct_text in zip(labels, pct_texts):
    pct_text.set_rotation(label.get_rotation())
    pct_text.update(db["font_dicts"]["light_mini"])
  ax2.set_title("Human statuses", fontdict=db["font_dicts"]["semi_title"])
  #Sum
  numlist = [bot_onlines + usr_onlines, bot_dnds + usr_dnds, bot_idles + usr_idles, bot_offlines + usr_offlines]
  patches, labels, pct_texts = ax3.pie(np.array(numlist), labels=("Online", "DND", "Idle", "Offline"),
    colors=["#3ba55d", "#ed4245", "#faa91a", "#747f8d"], rotatelabels=True, pctdistance=0.55,
  autopct=lambda pct: func(pct, numlist), textprops = db["font_dicts"]["label"])
  for label, pct_text in zip(labels, pct_texts):
    pct_text.set_rotation(label.get_rotation())
    pct_text.update(db["font_dicts"]["light_label"])
  ax3.set_title("All statuses", fontdict=db["font_dicts"]["semi_title"])
  fig.legend(["Online", "DND", "Idle", "Offline"], labelcolor = ["#3ba55d", "#ed4245", "#faa91a", "#747f8d"], )
  plt.savefig("statuses.png", transparent=True)
  plt.savefig("statuses.svg", transparent=True)
  await ctx.reply(files = [discord.File('statuses.png'), discord.File('statuses.svg')])
  plt.clf()
  try_delete('statuses.png', 'statuses.svg')

@commands.command(aliases=["stick", "st"])
async def sticker(ctx, message: discord.Message=None):
  if message==None:
    potential_reference = ctx.message.reference
    if potential_reference:
      message=await ctx.bot.get_channel(potential_reference.channel_id).fetch_message(potential_reference.message_id)
    else:
      await ctx.reply("Please reply to a message or add a message ID/Link.")
      return
  _sticker = message.stickers
  if not _sticker:
    await ctx.reply("The message does not contain any stickers.")
    return
  _sticker = await _sticker[0].fetch()
  sticker_pack = await _sticker.pack()
  desc=f"**{_sticker.name}**\nSent by {message.author.mention} at {unix_timestamp(message.created_at)}\nDescription: {_sticker.description}"
  embed=discord.Embed(title="Sticker Information", description=desc, url=message.jump_url)
  embed.add_field(name="Tags", value=", ".join(_sticker.tags), inline=False)
  embed.add_field(name="ID", value=_sticker.id, inline=True)
  embed.add_field(name="Type", value=("PNG" if _sticker.type==discord.StickerFormatType.png else ("APNG" if _sticker.type==discord.StickerFormatType.apng else "Lottie")), inline=True)
  embed.add_field(name=f"Pack ({_sticker.sort_value}/{len(sticker_pack.stickers)})", value=f"**ID:** {sticker_pack.id}\n**Cover: **{sticker_pack.cover_sticker.name}\n**{sticker_pack.name}**\nDescription: {sticker_pack.description}", inline=False)
  #embed.set(_sticker.url)
  await ctx.reply(embed=embed)

@commands.command(aliases=['sts'])
async def stickers(ctx, *, disposed = None):
  desc = ""
  for x in ctx.guild.stickers:
    desc += f"{x.emoji} {x.name} (ID: {x.id})\n  {x.description}\n"
  f = open('output.txt', 'w')
  f.write(desc)
  f.flush()
  f.close()
  await ctx.reply(file=discord.File('output.txt'))
  try_delete('output.txt')

@commands.command(aliases=['tm'])
async def template(ctx, *, tempinput):
  try:
    temp = await ctx.bot.fetch_template(tempinput)
  except:
    await ctx.reply("Invalid input. Please try again.")
    return
  ti=f"Template Information: {temp.name} ({temp.code})"
  desc=f"Created at {unix_timestamp(temp.created_at)} by {temp.creator.mention}"
  embed=discord.Embed(title=ti, description=desc)
  f0v=temp.description
  f1v=temp.uses
  f2v={unix_timestamp(temp.updated_at)}
  f3v=temp.source_guild
  embed.add_field(name="Description", value=f0v, inline=False)
  embed.add_field(name="Uses", value=f1v, inline=True)
  embed.add_field(name="Synced", value=f2v, inline=True)
  embed.add_field(name="Original Server", value=f3v, inline=True)
  await ctx.reply(embed=embed)

@commands.command(aliases=["member", "mem", "us"])
async def user(ctx, user: discord.Member = None, channel: discord.TextChannel = None):
  if user==None:
    user=ctx.author
  if channel==None:
    channel=ctx.channel
  bottrue = user.bot
  if bottrue == True:
    desc=f"{user.mention} (bot)"
  else:
    desc=f"{user.mention} (human)"
  fetched_user = await ctx.bot.fetch_user(user.id)
  fetched_color = fetched_user.accent_color
  embed=discord.Embed(title="User Information", color=fetched_color if fetched_color else user.color, description=desc)
  if user.name==user.display_name:
    f0v=f"{user.name}#{user.discriminator}"
  else:
    f0v=f"{user.name}#{user.discriminator} (__Nickname:__  `{user.display_name}`)"
  f1v=f"{unix_timestamp(user.created_at)}\nFrom now:\n"
  f1ts = str(datetime.now(timezone.utc) - user.created_at)
  if " days, " not in f1ts:
    f1v + re.sub(r'(\d{1,2}):(\d{2}):(\d{2})', r'\1 hours \2 minutes \3 seconds', f1ts) + f"\n≈ {f1ts.split(':')[0]} hours"
  else:
    days = int(re.sub(r'([\d]+) days, [\s\S]*', r'\1', f1ts))
    f1v += re.sub(r'([\d]+) days, (\d{1,2}):(\d{2}):(\d{2})', r'\1 days \2 hrs \3 mins \4 secs', f1ts)[:-7] + f"\n≈ {(int(f1ts.split(' days, ')[0]))//365} years {int(f1ts.split(' days, ')[0]) % 365} days"
  f2v=f"{unix_timestamp(user.joined_at)}\nFrom now:\n"
  f2ts = str(datetime.now(timezone.utc) - user.joined_at)
  if " days, " not in f2ts:
    f2v += re.sub(r'(\d{1,2}):(\d{2}):(\d{2})', r'\1 hours \2 minutes \3 seconds', f2ts) + f"\n≈ {f2ts.split(':')[0]} hours"
  else:
    f2v += re.sub(r'([\d]+) days, (\d{1,2}):(\d{2}):(\d{2})', r'\1 days \2 hrs \3 mins \4 secs', f2ts)[:-7] + f"\n≈ {(int(f2ts.split(' days, ')[0]))//365} years {int(f2ts.split(' days, ')[0]) % 365} days"
  if user.premium_since:
    f6v=f"{unix_timestamp(user.premium_since)}\nFrom now:\n"
    f6ts = str(datetime.now(timezone.utc) - user.joined_at)
    if " days, " not in f6ts:
      f6v += re.sub(r'(\d{1,2}):(\d{2}):(\d{2})', r'\1 hours \2 minutes \3 seconds', f6ts) + f"\n≈ {f6ts.split(':')[0]} hours"
    else:
      f6v += re.sub(r'([\d]+) days, (\d{1,2}):(\d{2}):(\d{2})', r'\1 days \2 hrs \3 mins \4 secs', f6ts)[:-7] + f"\n≈ {(int(f6ts.split(' days, ')[0]))//365} years {int(f6ts.split(' days, ')[0]) % 365} days"
  else:
    f6v = "No server boosting"
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
        f3vc = f"Playing {f3vcraw.name} since {unix_timestamp(f3vcraw.start)}\n{f3vcraw.details}"
      except:
        f3vc = f"Playing {f3vcraw.name}"
    elif f3vcraw.type.streaming:
      f3vc = f"Streaming [{f3vcraw.name}({f3vcraw.game})]({f3vcraw.url}) via {f3vcraw.platform}\n{f3vcraw.details}"
    elif f3vcraw.type.listening:
      f3vc = f"Listening to {f3vcraw.artist}: {f3vcraw.album}: {f3vcraw.title}\nStarted: {unix_timestamp(f3vcraw.created_at)}\n{f3vcraw.details}"
    elif f3vcraw.type.watching:
      try:
        f3vc = f"Watching [{f3vcraw.name}]({f3vcraw.url}) since {unix_timestamp(f3vcraw.start)}\n{f3vcraw.details}"
      except:
        f3vc = f"Watching {f3vcraw.name} since {unix_timestamp(f3vcraw.start)}"
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
    for x in allroles:
      f4v = f"{f4v}{x.mention} "
    f4v = f4v[:-1]
  else:
    f4v="No roles"
  f5v = ""
  user_public_flags = user.public_flags
  f5v = f5v + (f"**Staff:** The user is a Discord Employee.\n"                             if user_public_flags.staff else "")
  f5v = f5v + (f"**Partner:** The user is the owner of a Partnered Server.\n"              if user_public_flags.partner else "")
  f5v = f5v + (f"**HypeSquad Events:** The user is a HypeSquad Events member.\n"                  if user_public_flags.hypesquad else "")
  f5v = f5v + (f"**Early Support:** The user is an Early Supporter.\n"                     if user_public_flags.early_supporter else "")
  f5v = f5v + (f"**Team User:** The user is a Team User.\n"                                if user_public_flags.team_user else "")
  f5v = f5v + (f"**Bug Hunter:** The user is a Bug Hunter.\n"                              if user_public_flags.bug_hunter else "")
  f5v = f5v + (f"**Bug Hunter 2:** The user is a Bug Hunter (Level 2).\n"                  if user_public_flags.bug_hunter_level_2 else "")
  f5v = f5v + (f"**System:** The user is a system user (represents Discord officially).\n" if user_public_flags.system else "")
  f5v = f5v + (f"**Early Developer:** The user is an Early Verified Bot Developer.\n"      if user_public_flags.verified_bot_developer else "")
  f5v = f5v + (f"**✔︎Bot:** The user is a Verified Bot.\n"                                  if user_public_flags.verified_bot else "")
  f5v = f5v + (f"**HypeSquad:** The user is in the HypeSquad Bravery House.\n"             if user_public_flags.hypesquad_bravery else "")
  f5v = f5v + (f"**HypeSquad:** The user is in the HypeSquad Brilliance House.\n"          if user_public_flags.hypesquad_brilliance else "")
  f5v = f5v + (f"**HypeSquad:** The user is in the HypeSquad Balance House.\n"             if user_public_flags.hypesquad_balance else "")
  f5v = "No badges" if f5v == "" else f5v

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
  embed.add_field(name="Boosting since", value=f6v, inline=False)
  embed.add_field(name=f"Badges (Integer: {user_public_flags.value})", value=f5v, inline=False)
  await ctx.reply(embed=embed)

@commands.command()
async def widget(ctx, *, disposed = None):
  try:
    widget_ = await ctx.guild.widget()
  except:
    await ctx.reply("This server does not have a widget.")
    return
  invite_has_info = False
  ti=f"Widget Information: {widget_.name}"
  desc= f"{widget_.invite_url}\nCreated at {unix_timestamp(widget_.created_at)}"
  embed=discord.Embed(title=ti, description=desc)
  f0v = ", ".join([x.name for x in widget_.channels])
  f1v = ", ".join([f"{x.name}#{x.discriminator}" for x in widget_.members])
  embed.add_field(name="Channels", value=f0v, inline=False)
  embed.add_field(name="Members listed", value=f1v[:1024], inline=False)
  embed.url = widget_.json_url
  await ctx.reply(embed=embed)

def setup(bot):
  bot.add_command(avatar)
  bot.add_command(badges)
  bot.add_command(banner)
  bot.add_command(category)
  bot.add_command(channel)
  bot.add_command(emojiinfo)
  bot.add_command(emojis)
  bot.add_command(invitelink)
  bot.add_command(leftuser)
  bot.add_command(message)
  bot.add_command(overwrites)
  bot.add_command(permissions)
  bot.add_command(permission_generate)
  bot.add_command(raw)
  bot.add_command(rawraw)
  bot.add_command(reactions)
  bot.add_command(role)
  bot.add_command(server)
  bot.add_command(sticker)
  bot.add_command(stickers)
  bot.add_command(status)
  bot.add_command(statuses)
  bot.add_command(template)
  bot.add_command(user)
  bot.add_command(widget)
