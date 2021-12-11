#from discord.ext import tasks
from shared import *

#              LED Spammer
banned_ids =  [753526161732141067]
banned_text = []
bot_ = commands.Bot(command_prefix=commands.when_mentioned_or("="), intents=discord.Intents.all(), allowed_mentions=discord.AllowedMentions(everyone=False, users=True, roles=False, replied_user=False),
  case_insensitive=True, strip_after_prefix=True)
bot_.remove_command('help')
bot_.load_extension("botapis_animal")
bot_.load_extension("botapis_hk")
bot_.load_extension("botapis_uk")
bot_.load_extension("botbasic")
bot_.load_extension("botcalc")
bot_.load_extension("botconvert")
bot_.load_extension("botdevelopment")
bot_.load_extension("botdinfo")
bot_.load_extension("botembed")
bot_.load_extension("botengrave")
bot_.load_extension("botimage")
bot_.load_extension("botinfo")
bot_.load_extension("botled")
bot_.load_extension("botmoderate")
bot_.load_extension("botpartners")
bot_.load_extension("botplot")
bot_.load_extension("bottext")
bot_.load_extension("botwebinfo")
bot_.load_extension("botwebscrape")

sniper1={}
sniper2={}
sniper3={}
sniper4={}
sniper5={}
sniperdate1={}
sniperdate2={}
sniperdate3={}
sniperdate4={}
sniperdate5={}
sniperdict={}
sniping={}
poll_options={}
polls=[]
allid=[]

#@tasks.loop(hours=24)
#async def sba_marks():
#  sba_channel = bot_.get_channel(909445785509326859)
#  await sba_channel.send(f"5m <@757416033811169351> <@752335217339007067>\nFun fact: this is the {sba_marks.current_loop}{st_nd_th_format(sba_marks.current_loop)} time of SBA marks claiming since the last deploy!")

@bot_.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    message = ctx.message
    used_prefix = ctx.prefix
    used_command = message.content.split()[0][len(used_prefix):].lower()
    available_commands = [cmd.name for cmd in bot_.commands]
    matches = {cmd: SequenceMatcher(None, cmd, used_command).ratio() for cmd in available_commands}
    command = max(matches.items(), key=lambda item: item[1])[0]
    try:
      arguments = message.content.split(" ", 1)[1]
    except IndexError:
      arguments = ""
    new_content = f"{used_prefix}{command} {arguments}".strip()
    message.content = new_content
    await ctx.reply(f'Your might have made a typo and your command has been interpreted as `{command}`.', delete_after=4)
    await bot_.process_commands(message)
  elif isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f'You missed one or more arguments! {len(ctx.command.clean_params.keys())} argument(s) are required.\nNote: Multiline arguments are treated as one argument. Optional arguments are counted as well.')
  elif isinstance(error, commands.UserInputError):
    await ctx.reply(f'One or more of your arguments is/are not in the correct format! Please read the documentation.')
  elif isinstance(error, commands.NotOwner):
    await ctx.reply(f'Unfortunately, only the owner of the bot is allowed to use this.')
  else:
    try:
      await ctx.reply(f"An error occured:\n```{''.join(traceback.format_exception(type(error), error, error.__traceback__))}```\nIf you think that this is an issue with the bot, please kindly inform JohannLau#6541 about this issue.")
    except:
      print(''.join(traceback.format_exception(type(error), error, error.__traceback__)))
      await ctx.reply(f"Sorry! An error occured. The error was too long but it had been shown to JohannLau#6541. If the error persists, Please kindly inform him about this issue.")

# @bot_.event
# async def on_thread_update(before, after):
#   if after.id == 887562599191941121 and after.archived:
#     await after.edit(archived=False)
#     await after.send("I hate Discord's short auto-archive period when I don't buy Nitro, so I auto-unarchived it!")

# @bot_.event
# async def on_thread_join(thread):
#   if thread.guild.id == 805441351033552916 and not thread.me:
#     await thread.join()

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
      await supchat.set_permissions(member, overwrite=view_overwrite)
  except:
    pass

@bot_.event
async def on_message_delete(message):
  keyname = f"{message.guild.id}{message.channel.id}"
  val = message.content
  if val.replace(" ","") == "":
    return
  adt = f"By {message.author.name}#{str(message.author.discriminator)} at {unix_timestamp(message.created_at)}"
  if sniper1.get(keyname, 1) == 1:
    sniper1[keyname] = val
    sniperdate1[keyname] = adt
  elif sniper2.get(keyname, 1) == 1:
    sniper2[keyname], sniper1[keyname] = sniper1[keyname], val
    sniperdate2[keyname], sniperdate1[keyname] = sniperdate1[keyname], adt
  elif sniper3.get(keyname, 1) == 1:
    sniper3[keyname], sniper2[keyname], sniper1[keyname] = sniper2[keyname], sniper1[keyname], val
    sniperdate3[keyname], sniperdate2[keyname], sniperdate1[keyname] = sniperdate2[keyname], sniperdate1[keyname], adt
  elif sniper4.get(keyname, 1) == 1:
    sniper4[keyname], sniper3[keyname], sniper2[keyname], sniper1[keyname] = sniper3[keyname], sniper2[keyname], sniper1[keyname], val
    sniperdate4[keyname], sniperdate3[keyname], sniperdate2[keyname], sniperdate1[keyname] = sniperdate3[keyname], sniperdate2[keyname], sniperdate1[keyname], adt
  else:
    sniper5[keyname], sniper4[keyname], sniper3[keyname], sniper2[keyname], sniper1[keyname] = sniper4[keyname], sniper3[keyname], sniper2[keyname], sniper1[keyname], val
    sniperdate5[keyname], sniperdate4[keyname], sniperdate3[keyname], sniperdate2[keyname], sniperdate1[keyname] = sniperdate4[keyname], sniperdate3[keyname], sniperdate2[keyname], sniperdate1[keyname], adt

@bot_.event
async def on_reaction_add(reaction, user):
  msg = reaction.message
  if msg.id in polls and user.id != 796686363604680755:
    cache_embed = msg.embeds[0]
    desc = ""
    msg_dict = poll_options[msg.id]
    for x in msg_dict.keys():
      current_reaction = ems.encode(msg_dict[x])
      await msg.add_reaction(current_reaction)
      for y in msg.reactions:
        if y.emoji == current_reaction:
          current_reaction = y.emoji
          counter = 0
          async for z in y.users():
            if z.id != 796686363604680755:
              counter = counter + 1
          desc = desc + f"{y.emoji} {x} ("+ str(counter) +f")\n"
    cache = discord.Embed(title = cache_embed.title, description = ems.encode(desc))
    await msg.edit(embed=cache)

@bot_.event
async def on_reaction_remove(reaction, user):
  msg = reaction.message
  if msg.id in polls and user.id != 796686363604680755:
    cache_embed = msg.embeds[0]
    desc = ""
    msg_dict = poll_options[msg.id]
    for x in msg_dict.keys():
      current_reaction = ems.encode(msg_dict[x])
      await msg.add_reaction(current_reaction)
      for y in msg.reactions:
        if y.emoji == current_reaction:
          current_reaction = y.emoji
          counter = 0
          async for z in y.users():
            if z.id != 796686363604680755:
              counter = counter + 1
          desc = desc + f"{y.emoji} {x} ("+ str(counter) +f")\n"
    cache = discord.Embed(title = cache_embed.title, description = ems.encode(desc))
    await msg.edit(embed=cache)

@bot_.event
async def on_message(message):
  try:
    if message.guild.id == 852899227004305458 and message.author.id != 796686363604680755 and message.channel.id in [856053769149874196, 864757953121878026, 864754633910255646]:
      await message.add_reaction("<:UpArrowSquare:864762633194569728>")
      await message.add_reaction("<:DownArrowSquare:864762633625534485>")
      #                         SuperBot #news      #new-features       #github             LSC Bots CraftBot   SuperBot            DolphinBot          WalkerBot           Waffles
    elif message.channel.id in [805459414001778739, 805462208414089217, 880076327783370812, 888254659502936074, 888254911740018708, 888256046496382988, 888256348268138556, 890227476452753448]:
      await message.publish()
    if message.author.id not in banned_ids and message.content.startswith("==")==False:
      await bot_.process_commands(message)
    elif message.author.id in banned_ids and (message.content.startswith("=") or message.content.startswith("<@796686363604680755>")):
      await message.channel.send("You are banned from the bot. Reason: "+banned_text[banned_ids.index(message.author.id)])
  except:
    pass

@bot_.event
async def on_interaction(interaction):
  interaction_select_option = interaction.data.get("values", None)
  interaction_original_message = interaction.message
  if interaction.type == discord.InteractionType.component:
    interaction_custom_id = interaction.data["custom_id"]
    if interaction_custom_id in ["primary", "secondary", "green", "red"]:
      await interaction.followup.send(f"You pressed on the {interaction_custom_id} button.", ephemeral=True)
    elif interaction_select_option:
      if interaction_custom_id in ["single-selection", "multi-selection"]:
        interaction_first_option = interaction_select_option[0]
        if interaction_first_option.startswith("help_"):
          await interaction.edit_original_message(embed=eval(interaction_first_option))
        else:
          await interaction.followup.send(f"You selected {', '.join(interaction_select_option)} in the {interaction_custom_id} menu.", ephemeral=True)
      elif interaction_custom_id in ["permission_server_selection", "permission_text_selection", "permission_voice_selection"]:
        permission_messages[interaction_original_message][interaction_custom_id] = interaction.data["values"]
        permission_integer = 0
        for x in permission_messages[interaction_original_message].values():
          for y in x:
            permission_integer += (2**int(y) if y != 'None' else 0)
        await interaction.followup.send(f"Decimal permission integer: {permission_integer}", ephemeral=True)
    elif interaction_custom_id in ["Snipe1", "Snipe2", "Snipe3", "Snipe4", "Snipe5"]:
      keyname = f"{interaction_original_message.guild.id}{interaction_original_message.channel.id}"
      if interaction_custom_id == "Snipe1":
        sniperdict[interaction_original_message] = 1
      elif interaction_custom_id == "Snipe2" and sniperdict[interaction_original_message] > 1:
        sniperdict[interaction_original_message] = sniperdict[interaction_original_message] - 1
      elif interaction_custom_id == "Snipe3" and interaction_original_message.pinned == False:
        if interaction_original_message.channel.permissions_for(interaction_original_message.guild.get_member(796686363604680755)).manage_messages:
          if not interaction_original_message.pinned:
            await interaction_original_message.pin()
            pinmsg = await interaction_original_message.channel.fetch_message(interaction_original_message.channel.last_message_id)
            await pinmsg.delete()
          else:
            await interaction_original_message.unpin()
        else:
          await interaction.followup.send("Unable to Pin/Unpin messages without `Manage Server` permission.", ephemeral=True)
          return
      elif interaction_custom_id == "Snipe4":
        if sniperdict[interaction_original_message] < 5 and eval(f"sniper{sniperdict[interaction_original_message]+1}.get(keyname, 1)") != 1:
          sniperdict[interaction_original_message] += 1
        elif sniper5.get(keyname, 1) != 1:
          sniperdict[interaction_original_message] = 5
        elif sniper4.get(keyname, 1) != 1:
          sniperdict[interaction_original_message] = 4
        elif sniper3.get(keyname, 1) != 1:
          sniperdict[interaction_original_message] = 3
        elif sniper2.get(keyname, 1) != 1:
          sniperdict[interaction_original_message] = 2
        elif sniper1.get(keyname, 1) != 1:
          sniperdict[interaction_original_message] = 1
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
      ti = f"Snipped message ({sniperdict[interaction_original_message]}/{maxc})"
      desc = eval(f"sniper{sniperdict[interaction_original_message]}[keyname]")
      foot = eval(f"sniperdate{sniperdict[interaction_original_message]}[keyname]")
      embed = discord.Embed(title=ti, description=desc)
      embed.set_footer(text=foot)
      await interaction_original_message.edit(embed=embed)

@bot_.command(aliases=['sniper'])
async def snipe(ctx, *, text = None):
  chnl = ctx.channel
  keyname = str(ctx.guild.id)+str(chnl.id)
  if text == None:
    if sniping.get(keyname, 1) == 1 or sniping[keyname] == True:
      if sniper1.get(keyname, 1) == 1:
        embed = discord.Embed(title="Error", description="Nothing to snipe from this channel.")
        await ctx.reply(embed=embed)
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
        ti = f"Snipped message (1/{maxc})"
        desc = sniper1[keyname]
        foot = sniperdate1[keyname]
      embed = discord.Embed(title=ti, description=desc)
      embed.set_footer(text=foot)
      snipe_view = ui.View(timeout=120)
      for x in snipe_buttons:
        snipe_view.add_item(x)
      if chance(1000):
        cmsg = await ctx.reply("Did someone just ghostping you?", embed=embed, view=snipe_view)
      else:
        cmsg = await ctx.reply(embed=embed, view=snipe_view)
      sniperdict[cmsg] = 1
    else:
      await ctx.reply("Snipping is disabled. Please ask someone with manage messages permission to re-enable it.")
  elif has_perms(ctx.channel, ctx.author, 13):
    if text.startswith("y") or text.startswith("t") or text.startswith("e") or text.replace(" ","")=="1":
      sniping[keyname] = True
      await ctx.reply("Sniping is now enabled.")
    else:
      sniping[keyname] = False
      await ctx.reply("Sniping is now disabled.")

@bot_.event
async def on_voice_state_update(member, before, after):
  if member.id == 796686363604680755:
    pass

@bot_.command()
async def poll(ctx, *, text):
  options = []
  reactions = []
  textlist = text.split(" ")
  ti = ""
  desc = ""
  poll_options_cache = {}
  for x in textlist: # ([\w]+?)(:\w{2,32}:|[\uD800-\uDBFF])
    match = poll_pattern.fullmatch(ems.decode(x))
    if match:
      optn = re.sub(poll_pattern, r'\1', ems.decode(x))
      rect = re.sub(poll_pattern, r'\2', ems.decode(x))
      desc = desc + f"{rect} {optn} (0)\n"
      options.append(optn)
      poll_options_cache[optn] = rect
      reactions.append(ems.encode(rect))
    else:
      ti += f"{x} "
  embed = discord.Embed(title = ti, description = ems.encode(desc))
  poll = await ctx.reply(embed=embed)
  for x in reactions:
    await poll.add_reaction(x)
  polls.append(poll.id)
  poll_options[poll.id] = poll_options_cache

@bot_.command()
async def clearsnipe(ctx, *, chnl : discord.TextChannel = None):
  if chnl == None:
    chnl = ctx.channel
  if chnl.permissions_for(ctx.author).manage_channels or botadmin(ctx):
    sniper1.pop(str(ctx.guild.id)+str(chnl.id))
    sniper2.pop(str(ctx.guild.id)+str(chnl.id))
    sniper3.pop(str(ctx.guild.id)+str(chnl.id))
    sniper4.pop(str(ctx.guild.id)+str(chnl.id))
    sniper5.pop(str(ctx.guild.id)+str(chnl.id))
    await ctx.reply('Cleared snipe database for '+chnl.mention+'.')
  else:
    await ctx.reply("You don't have the required permission: Manage channels.")

@bot_.command()
@commands.is_owner()
async def purgeserver(ctx, text, condition="1==1", *, disposed = None):
  text = text.lower()
  if text.startswith("role"):
    allroles = ctx.guild.roles()
    for _role in allroles:
      if condition:
        await _role.delete()
    await ctx.reply("Role purging completed.")

@bot_.command()
@commands.check(botadmin)
async def botban(ctx, user : discord.User, *, text="No reason was provided"):
  banned_ids.append(user.id)
  banned_text.append(text)
  await ctx.reply("Banned user from using the bot.")

@bot_.command()
@commands.check(botadmin)
async def botunban(ctx, user : discord.User):
  if user.id in banned_ids:
    banned_text.remove(banned_text[banned_ids.index(user.id)])
    banned_ids.remove(user.id)
    await ctx.reply("Unbanned user from using the bot.")

# @bot_.command()
# @commands.is_owner()
# async def botadmin(ctx, user : discord.User):
#   bot_admins.append(user.id)
#   await ctx.reply("Added user as bot admin.")

@bot_.command()
@commands.is_owner()
async def nick(ctx, *, new_nick):
  try:
    await ctx.guild.me.edit(nick=(None if new_nick == "clear" else new_nick))
    await ctx.reply("Changed nickname.")
  except:
    await ctx.reply("Unable to change nickname.")

@bot_.command()
async def botpurge(ctx, *, num):
  try:
    await ctx.message.delete()
  except:
    pass
  if ctx.channel.permissions_for(ctx.author).manage_messages or botadmin(ctx):
    num = int(num)
    purged = 0
    async for x in ctx.channel.history(limit=1000):
      if x.author.id == 796686363604680755:
        await x.delete()
        purged = purged + 1
        if purged >= num:
          break
        
    await ctx.reply("Bot purging completed.", delete_after = 5)
  else:
    await ctx.reply("You don't have the required permission: Manage messages.")

@bot_.command(aliases=["online"])
async def ping(ctx, *, disposed = None):
  now1 = datetime.now(timezone.utc)
  message = await ctx.send("Pong!")
  mcs = str(int((datetime.now(timezone.utc) - now1).microseconds)+int(((datetime.now(timezone.utc) - now1).total_seconds())%60))
  await message.edit(content=f"Pong! 🏓\n```Message delay: {mcs} microseconds\nBot latency  : {round(bot_.latency*1000000, 2)} microseconds```")

@bot_.command()
async def terminate(ctx, *, idc):
  if id_pattern.fullmatch(idc) and len(idc)==5:
    if f"{idc.upper()}{ctx.guild.id}" in allid:
      exec(f"terminate{idc.lower()}{ctx.guild.id}=1",globals())
      allid.remove(idc.upper()+str(ctx.guild.id))
      await ctx.reply("Timer terminated!")
    else:
      await ctx.reply("Please provide a valid timer code. A timer code could be found at the beginning of a running timer.")
  else:
    await ctx.reply("Please provide an 5-alphabet ID code. Example: `ABCDE`")

@bot_.command()
async def rtimer(ctx, timetocount, *, Text = None):
    sec = int(timedelta(**{
      UNITS.get(m.group('unit').lower(), 'seconds'): int(m.group('val'))
      for m in re.finditer(r'(?P<val>\d+)(?P<unit>[smhdw]?)', timetocount, flags=re.I)
    }).total_seconds())
    end = datetime.now(timezone.utc) + timedelta(seconds = sec)
    seconds = int((end - datetime.now(timezone.utc)).total_seconds())
    idcode = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]
    exec(f"terminate{idcode.lower()}{ctx.guild.id}=0",globals())
    newidcode=idcode.lower()
    allid.append(idcode+str(ctx.guild.id))
    desc = "Initializing countdown…"
    message = await ctx.reply(desc)
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
async def ttimer(ctx, timetocount, *, Text = None):
    sec = int(timedelta(**{
      UNITS.get(m.group('unit').lower(), 'seconds'): int(m.group('val'))
      for m in re.finditer(r'(?P<val>\d+)(?P<unit>[smhdw]?)', timetocount, flags=re.I)
    }).total_seconds())
    end = datetime.now(timezone.utc) + timedelta(seconds = sec)
    seconds = int((end - datetime.now(timezone.utc)).total_seconds())
    newidcode = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]
    exec(f"terminate{newidcode.lower()}{ctx.guild.id}=0",globals())
    allid.append(newidcode+str(ctx.guild.id))
    desc = "Initializing countdown…"
    message = await ctx.reply(desc)
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
  activity = discord.Activity(
    type=discord.ActivityType.playing,
    name=f"with =help in {len(bot_.guilds)} servers",
    #buttons=db["status_buttons"],
    timestamps = db["status_timestamps"])
  await bot_.change_presence(status=discord.Status.idle, activity=activity)
  # datetime(now_.year, now_.month, now_.day, (0 if now_.hour==23 else now_.hour+1), 0, 0)
  #sba_marks.start()
  #for x in bot_.get_guild(805441351033552916).threads:
  #  if not x.me:
  #   await x.join()
  print(f"Bot is ready!\n")
  #now_ = datetime.now()
  #await asyncio.sleep(timedelta(minutes=60-now_.minute, seconds=60-now_.second).total_seconds())
  #scratch = bot_.get_guild(867962875422081024)
  #johann = scratch.get_member(687474789342117900)
  #await johann.add_roles(scratch.get_role(871716868862406756))
  #for x in bot_.guilds:
  #  print(x.name)
  #  print('  ', x.owner.name)
  #  if x.member_count < 10:
  #    for y in x.members:
  #      print(f'\t',y.name)
  # agree_emoji = bot_.get_emoji(885515344863703121)
  # message_1 = await bot_.get_channel(894820155761246231).fetch_message(894820888321622058)
  # message_2 = await bot_.get_channel(894820155761246231).fetch_message(894821177137197067)
  # message_3 = await bot_.get_channel(894820155761246231).fetch_message(894820846206590986)
  # await message_1.add_reaction(agree_emoji)
  # await message_2.add_reaction(agree_emoji)
  # await message_3.add_reaction(agree_emoji)

print("Bot is getting started…")
try:
  bot_.run('Nzk2Njg2MzYzNjA0NjgwNzU1.X_bh_g.6uKl_EPp5r5XZpSxCxPTIuA69aE')
except:
  pass
