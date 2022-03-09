from _bot import bs
from shared import (asyncio, commands, custom_permissions, datetime, db, discord, Embed,
                    has_perms, re, SequenceMatcher, specialbool, timedelta, timestamp_pattern,
                    timezone, try_delete, try_delete_message, typing, ui, UNITS, unix_timestamp)


class SearchFlags(commands.FlagConverter):
  channels         : typing.Tuple[discord.TextChannel,...] = []
  search           : typing.Tuple[str,...]                 = []
  exact_search     : str                                   = ""
  maximum          : int                                   = 100
  pinned           : specialbool                           = None
  mention_everyone : specialbool                           = None
  mention_role     : specialbool                           = None
  mention_member   : specialbool                           = None
  mention_channel  : specialbool                           = None
  invite_links     : specialbool                           = None
  timestamp        : specialbool                           = None
  embeds           : specialbool                           = None
  files            : specialbool                           = None


@commands.command() # Will be removed
async def ban(ctx, user: discord.User, delete: int = 0, *, reason="No reason provided"):
  if has_perms(ctx.channel, ctx.author, 2):
    try:
      await ctx.guild.ban(user, delete_message_days= delete, reason= f"{reason} (requested by {ctx.author.name}#{ctx.author.discriminator})")
    except discord.Forbidden:
      await ctx.reply("The bot doesn't have the required permission: Ban members.")
      return
    embed1 = Embed(title= f"You were banned from the server.", description= f"Reason: {reason}\nBy: {ctx.author.mention}")
    embed2 = Embed(title= f"{user.name} was banned.", description= f"Reason: {reason}\nBy: {ctx.author.mention}")
    try:
      await user.send(embed=embed1)
    except:
      pass
    await ctx.reply(embed=embed2)
  else:
    await ctx.reply("You don't have the required permission: Ban members.")


@commands.command()
async def getrole(ctx, roles: commands.Greedy[discord.Role], member: discord.Member = None):
  if member == None:
    member = ctx.author
  if has_perms(ctx.channel, ctx.author, 28) or False not in [x in db["getrole_bypass_ids"] for x in roles]:
    member_roles = member.roles
    addrole_count = removerole_count = 0
    for x in roles:
      if x in member_roles:
        await member.remove_roles(x)
        removerole_count -= 1
      else:
        addrole_count    += 1
        await member.add_roles(x)
    if addrole_count and removerole_count:
      await ctx.reply(f"Added {str(addrole_count)} and removed {str(removerole_count)} roles to {str(member)}.")
    elif addrole_count:
      await ctx.reply(f"Added {str(addrole_count)} roles to {str(member)}.")
    elif removerole_count:
      await ctx.reply(f"Removed {str(removerole_count)} roles to {str(member)}.")
    else:
      await ctx.reply("No roles had been manipulated.")
  else:
    await ctx.reply("You don't have the required permission: Manage roles.")


@commands.command() # Will be removed
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
  if has_perms(ctx.channel, ctx.author, 1):
    try:
      await user.kick(reason= f"{reason} (requested by {ctx.author.name}#{ctx.author.discriminator})")
    except discord.Forbidden:
      await ctx.reply("The bot doesn't have the required permission: Kick members.")
      return
    embed1 = Embed(title=f"You were kicked from the server.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    embed2 = Embed(title=f"{user.name} was kicked.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    try:
      await user.send(embed=embed1)
    except:
      pass
    await ctx.reply(embed=embed2)
  else:
    await ctx.reply("You don't have the required permission: Kick members.")


@commands.command()
async def makeinvite(ctx, timetocount = "0", uses: int = 0):
  if has_perms(ctx.channel, ctx.author, 0):
    seconds = int(timedelta(**{
      UNITS.get(m.group('unit').lower(), 'seconds'): int(m.group('val'))
      for m in re.finditer(r'(?P<val>\d+)(?P<unit>[smhdw]?)', timetocount, flags=re.I)
    }).total_seconds())
    theinvite = await ctx.channel.create_invite(max_age = seconds, max_uses = uses)
    await ctx.reply(f"An invite was generated with {seconds} seconds of valid duration and {uses} maximum users: {theinvite.url}\nNote: a zero indicates infinity.")
  else:
    await ctx.reply("You don't have the required permission: Generate Invites.")


@commands.command(aliases=['makerole'])
async def makeroles(ctx, times: int = 1, *, name="Sample role $num"):
  if has_perms(ctx.channel, ctx.author, 28):
    current_server = ctx.guild
    for x in range(1, times + 1):
      await current_server.create_role(name=name.replace("$num", str(x)))
    await ctx.reply("Successfully created role(s).")
  else:
    await ctx.reply("You don't have the required permission: Manage Roles.")

@bs.command(name="make_roles", description="Creates up to 15 roles quickly. Warning: you may revert this only by manually removing the roles.", options=[
           ui.SlashOption(name="Number", description="The number of roles to generate.", type=int,
           required=True, min_value=1, max_value=15), ui.SlashOption(name="Name",
           description="The name of the roles. Use '$num' as a placeholder. Defaults to 'Sample role $num'.",
           type=str, required=False), ui.SlashOption(name="Permission",
           description="The permission integer to give to all roles.", type=int, required=False)])


@commands.command(aliases=['makethread'])
async def makethreads(ctx, times: int = 1, archive: typing.Literal['1', '2', '3', '4'] = '2', *, name="Sample thread $number"):
  if has_perms(ctx.channel, ctx.author, 32):
    current_channel = ctx.channel
    for x in range(1, times+1):
      await current_channel.create_thread(name=name.replace("$number", str(x)), type=discord.ChannelType.public_thread, auto_archive_duration=db["thread_archive"].get(archive, 2))
    await ctx.reply("Successfully created thread(s).")
  else:
    await ctx.reply("You don't have the required permission: Manage Threads.")


@commands.command()
async def purge(ctx, num: int):
  try_delete_message(ctx.message)
  if has_perms(ctx.channel, ctx.author, 13):
    deleted = await ctx.channel.purge(limit = num + 1)
    msg = await ctx.send("Purging completed.")
    authors = f'\n'.join({f"{x.author.name}#{x.author.discriminator}{' **bot**' if x.author.bot else ''}" for x in deleted})
    await msg.edit(f"Purged {len(deleted)} messages from:\n{authors}", delete_after = 5)
  else:
    await ctx.reply("You don't have the required permission: Manage messages.")


@commands.command()
async def purgepy(ctx, num: int, pyscript):
  try_delete_message(ctx.message)
  if has_perms(ctx.channel, ctx.author, 13):
    num=int(num)
    deleted = await ctx.channel.purge(limit= num + 1, check = lambda msg: eval(pyscript))
    msg = await ctx.send("Purging completed.")
    authors = f'\n'.join({f"{x.author.name}#{x.author.discriminator}{' **bot**' if x.author.bot else ''}" for x in deleted})
    await msg.edit(f"Purged {len(deleted)} messages from:\n{authors}", delete_after = 5)
  else:
    await ctx.reply("You don't have the required permission: Manage messages.")


@commands.command()
async def purgepygex(ctx, num: int, regex, *, pyscript):
  try_delete_message(ctx.message)
  if has_perms(ctx.channel, ctx.author, 13):
    purge_pattern = re.compile(regex)
    deleted = await ctx.channel.purge(limit= num + 1, check= lambda msg: eval(pyscript) and purge_pattern.fullmatch(msg.content))
    msg = await ctx.send("Purging completed.")
    authors = f'\n'.join({f"{x.author.name}#{x.author.discriminator}{' **bot**' if x.author.bot else ''}" for x in deleted})
    await msg.edit(f"Purged {len(deleted)} messages from:\n{authors}", delete_after = 5)
  else:
    await ctx.reply("You don't have the required permission: Manage messages.")


@commands.command()
async def purgereactions(ctx, num: int, emoji: discord.Emoji = None):
  try_delete_message(ctx.message)
  if has_perms(ctx.channel, ctx.author, 13):
    if emoji == None:
      async for message in ctx.channel.history(limit= num + 1):
        await message.clear_reactions()
    else:
      async for message in ctx.channel.history(limit= num + 1):
        await message.clear_reaction(emoji)
  else:
    await ctx.reply("You don't have the required permission: Manage messages.")


@commands.command()
async def purgeregex(ctx, num: int, *, regex):
  try_delete_message(ctx.message)
  if has_perms(ctx.channel, ctx.author, 13):
    purge_pattern = re.compile(regex)
    deleted = await ctx.channel.purge(limit= num + 1, check= lambda msg: purge_pattern.fullmatch(msg.content))
    msg = await ctx.send("Purging completed.")
    authors = f'\n'.join({f"{x.author.name}#{x.author.discriminator}{' **bot**' if x.author.bot else ''}" for x in deleted})
    await msg.edit(f"Purged {len(deleted)} messages from:\n{authors}", delete_after = 5)
  else:
    await ctx.reply("You don't have the required permission: Manage messages.")


@commands.command()
async def purgerole(ctx, num: int, role: discord.Role):
  try_delete_message(ctx.message)
  if has_perms(ctx.channel, ctx.author, 13):
    deleted = await ctx.channel.purge(limit= num + 1, check= lambda msg: role in msg.author.roles)
    msg = await ctx.reply("Purging completed.")
    authors = f'\n'.join({f"{x.author.name}#{x.author.discriminator}{' **bot**' if x.author.bot else ''}" for x in deleted})
    await msg.edit(f"Purged {len(deleted)} messages from:\n{authors}", delete_after = 5)
  else:
    await ctx.reply("You don't have the required permission: Manage messages.")


@commands.command()
async def purgeuser(ctx, num: int, *userinput: discord.User):
  try_delete_message(ctx.message)
  if has_perms(ctx.channel, ctx.author, 13):
    deleted = await ctx.channel.purge(limit=num+1, check = lambda msg: msg.author in userinput)
    msg = await ctx.reply("Purging completed.")
    authors = f'\n'.join({f"{x.author.name}#{x.author.discriminator}{' **bot**' if x.author.bot else ''}" for x in deleted})
    await msg.edit(f"Purged {len(deleted)} messages from:\n{authors}", delete_after = 5)
  else:
    await ctx.reply("You don't have the required permission: Manage messages.")


@commands.command()
async def react(ctx, emoji: discord.Emoji, message=None):
  if message == None:
    potential_reference = ctx.message.reference
    if potential_reference:
      message = await ctx.bot.get_channel(potential_reference.channel_id).fetch_message(potential_reference.message_id)
    else:
      await ctx.reply("Please reply to a message or add a message ID/Link.")
      return
  await message.add_reaction(emoji)
  await asyncio.sleep(5)
  await message.remove_reaction(emoji, ctx.guild.get_member(796686363604680755))


@commands.command()
async def search(ctx, *, flags: SearchFlags):
  exact_search     = flags.exact_search
  query            = flags.search
  pinned           = flags.pinned
  mention_everyone = flags.mention_everyone
  mention_role     = flags.mention_role
  mention_member   = flags.mention_member
  mention_channel  = flags.mention_channel
  invite_links     = flags.invite_links
  timestamps       = flags.timestamp
  embeds           = flags.embeds
  files            = flags.files
  desc = f"Length\tURL\n"
  if not flags.channels:
    channels = ctx.channel
  else:
    channels = flags.channels
  if type(channels) != tuple:
    channels = [channels]
  if type(query) != tuple:
    query = [query]
  for channel_count in channels:
    async for message_count in channel_count.history(limit=flags.maximum):
      contents     = message_count.content
      match        = True
      if embeds and message_count.embeds:
        embed    = message_count.embeds[0].to_dict()
      elif embeds or (embeds == False and message_count.embeds):
        match = False
        break
      else:
        embed    = {}
      if (files and len(message_count.attachments)) or (files == False and not len(message_count.attachments)):
        match = False
        continue
      for query_count in query:
        if query_count not in contents and query_count not in embed:
          match = False
          break
        else:
          continue
      if exact_search not in contents and exact_search not in embed:
        match = False
        continue
      if (pinned and not message_count.pinned) or (pinned == False and message_count.pinned):
        match = False
        continue
      if (mention_everyone and message_count.mention_everyone) or (mention_everyone == False and not message_count.mention_everyone):
        match = False
        continue
      if (mention_role and not len(message_count.role_mentions)) or (mention_role == False and len(message_count.role_mentions)):
        match = False
        continue
      if (mention_member and not len(message_count.mentions)) or (mention_member == False and len(message_count.mentions)):
        match = False
        continue
      if (mention_channel and not len(message_count.channel_mentions)) or (mention_channel == False and len(message_count.channel_mentions)):
        match = False
        continue
      if (invite_links and not "https://discord.gg/" in contents) or (invite_links == False and "https://discord.gg/" in contents):
        match = False
        continue
      if (timestamps and not timestamp_pattern.search(contents)) or (timestamps == False and timestamp_pattern.search(contents)):
        match = False
        continue
      if match:
        desc += f"{len(contents)}\t{message_count.jump_url}\t{message_count.channel.name}\n"
  f = open('search.txt', 'w')
  f.write(desc)
  f.close()
  await ctx.reply(file=discord.File('search.txt'))
  try_delete('search.txt')


@commands.command(aliases=['setperms', 'setpermission', 'setpermissions', 'rolepermission', 'rolespermission', 'rolepermissions', 'rolespermissions'])
async def setperm(ctx, permission_input: typing.Union[int, str], *roles: discord.Role):
  if has_perms(ctx.channel, ctx.author, 28):
    if type(permission_input) == int:
      permission = discord.Permissions(permission_input)
    else:
      permission_input = permission_input.lower()
      permission = re.sub(r'[^A-z]|\^', '', permission_input)
      for x, y in custom_permissions.items():
        if SequenceMatcher(None, permission, x).ratio() >= 0.75:
          permission = y
          break
    for x in roles:
      await x.edit(permissions=permission)
    await ctx.reply("Successfully set permissions.")
  else:
    await ctx.reply("You don't have the required permission: Manage Roles.")


@commands.command()
async def slowmode(ctx, sec=None, *channels: typing.Union[discord.TextChannel,str]):
  if sec:
    sec = int(timedelta(**{
      UNITS.get(m.group('unit').lower(), 'seconds'): int(m.group('val'))
      for m in re.finditer(r'(?P<val>\d+)(?P<unit>[smhdw]?)', sec, flags=re.I)
    }).total_seconds())
    if sec.isdigit() == False:
      sec = 0
    if sec < 0 or sec > 21600 or sec%1 != 0:
      await ctx.reply("Invalid input! Please enter a duration below or equal to 21600 seconds (6 hours).")
      return
    if len(channels) == 0:
      allchannel = [ctx.channel]
    elif channels[0] == ("all"):
      allchannel = ctx.guild.text_channels
    else:
      allchannel = channels
    channellist = []
    for x in allchannel:
      if type(x) == str:
        continue
      if has_perms(x, ctx.author, 4):
        orsec = x.slowmode_delay
        await x.edit(slowmode_delay = sec)
        channellist.append(x.mention)
    if len(channellist) == 0:
      await ctx.reply("You don't have the required permission: Manage channels.")
    elif len(channellist) == 1:
      await ctx.reply(f"Set slowmode from {orsec} second(s) to {sec} second(s) for {channellist[0]}.")
    else:
      await ctx.reply(f"Set slowmode to {sec} second(s) for these channels: {' '.join(channellist)}.")
  else:
    await ctx.reply(f"The current slowmode is {ctx.channel.slowmode_delay} second(s).")


@commands.command()
async def tts(ctx, *, desc):
  if has_perms(ctx.channel, ctx.author, 12):
    await ctx.reply(desc, tts= True)
  else:
    await ctx.reply("You don't have the required permission: Send TTS messages.")


@bs.command(name="timeout", description="Adds or removes a timeout to/from a user.", options=[
           ui.SlashOption(name="User", description="The user to manipulate the timeout of.",
           type=discord.Member, required=True), ui.SlashOption(name="Duration",
           description="The duration of the timeout in wdhms units, e.g. 1m20s=80s. Use 0 to remove timeout.",
           type=str, required=True), ui.SlashOption(name="Reason", description="The reason to manipulate the timeout.",
           type=str, required=False)])
async def timeout_(ctx: ui.SlashInteraction, user, duration, reason=None):
  if has_perms(ctx.channel, ctx.author, 40):
    sec = int(timedelta(**{
      UNITS.get(m.group('unit').lower(), 'seconds'): int(m.group('val'))
      for m in re.finditer(r'(?P<val>\d+)(?P<unit>[smhdw]?)', duration, flags=re.I)
    }).total_seconds())
    end = datetime.now(timezone.utc) + timedelta(seconds = sec)
    if reason:
      await user.edit(timeout = end, reason= f"{reason} (requested by {ctx.author.name}#{ctx.author.discriminator})")
    else:
      await user.edit(timeout = end)
    embed = Embed(title=f"{user.name} was timed out.", description=f"Until: {unix_timestamp(end)}\nReason: {reason}\nBy: {ctx.author.mention}")
    await ctx.send(embed = embed)
  else:
    await ctx.reply("You don't have the required permission: Moderate members.")


@commands.command() # Migrated
async def timeout(ctx, member: discord.Member, duration="0s", *, reason="No reason provided"):
  if has_perms(ctx.channel, ctx.author, 40):
    sec = int(timedelta(**{
      UNITS.get(m.group('unit').lower(), 'seconds'): int(m.group('val'))
      for m in re.finditer(r'(?P<val>\d+)(?P<unit>[smhdw]?)', duration, flags=re.I)
    }).total_seconds())
    end = datetime.now(timezone.utc) + timedelta(seconds = sec)
    if reason:
      await member.edit(timeout = end, reason= f"{reason} (requested by {ctx.author.name}#{ctx.author.discriminator})")
    else:
      await member.edit(timeout = end)
    embed = Embed(title=f"{member.name} was timed out.", description=f"Until: {unix_timestamp(end)}\nReason: {reason}\nBy: {ctx.author.mention}")
    await ctx.send(embed = embed)
  else:
    await ctx.reply("You don't have the required permission: Moderate members.")


@commands.command()
async def unban(ctx, user: discord.User, *, reason="No reason provided"):
  if has_perms(ctx.channel, ctx.author, 2):
    try:
      await ctx.guild.unban(user, reason= f"{reason} (requested by {ctx.author.name}#{ctx.author.discriminator})")
    except:
      await ctx.reply("The bot doesn't have the required permission: Ban members.")
      return
    embed1 = Embed(title=f"You were unbanned from the server.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    embed2 = Embed(title=f"{user.name} was unbanned.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    try:
      await user.send(embed=embed1)
    except:
      pass
    await ctx.reply(embed=embed2)
  else:
    await ctx.reply("You don't have the required permission: Ban members.")


@commands.command() # Migrated
async def untimeout(ctx, member: discord.Member, *, reason="No reason provided"):
  if has_perms(ctx.channel, ctx.author, 40):
    if reason:
      await member.edit(timeout = None, reason= f"{reason} (requested by {ctx.author.name}#{ctx.author.discriminator})")
    else:
      await member.edit(timeout = None)
    await ctx.send("Un-Timeout success")
  else:
    await ctx.reply("You don't have the required permission: Moderate members.")


def setup(bot):
  bot.add_command(ban)
  bot.add_command(getrole)
  bot.add_command(kick)
  bot.add_command(makeinvite)
  bot.add_command(makeroles)
  bot.add_command(makethreads)
  bot.add_command(react)
  bot.add_command(search)
  bot.add_command(setperm)
  bot.add_command(slowmode)
  bot.add_command(tts)
  bot.add_command(unban)
  bot.add_command(purge)
  bot.add_command(purgereactions)
  bot.add_command(purgeregex)
  bot.add_command(purgerole)
  bot.add_command(purgeuser)
  bot.add_command(purgepy)
  bot.add_command(purgepygex)
  bot.add_command(timeout)
  bot.add_command(untimeout)
