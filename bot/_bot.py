#from discord.ext import tasks
from shared import *

banned_ids =  []
banned_text = []
bot_ = commands.Bot(command_prefix=commands.when_mentioned_or("="),intents=discord.Intents.all(),
                    allowed_mentions=discord.AllowedMentions(everyone=False, users=True,
                    roles=False, replied_user=False), case_insensitive=True, strip_after_prefix=True)
ui_ = ui.UI(bot_)

bot_.remove_command('help')
bot_.load_extension("apis__int")
bot_.load_extension("apis_hk")
bot_.load_extension("apis_uk")
bot_.load_extension("basic")
bot_.load_extension("calc")
bot_.load_extension("convert")
bot_.load_extension("development")
bot_.load_extension("dinfo")
bot_.load_extension("embed")
bot_.load_extension("engrave")
bot_.load_extension("image")
bot_.load_extension("info")
bot_.load_extension("led")
bot_.load_extension("moderate")
bot_.load_extension("partners")
bot_.load_extension("plot")
bot_.load_extension("statuscode")
bot_.load_extension("text")
bot_.load_extension("webinfo")
bot_.load_extension("webscrape")

sniper={}
sniping={}
sniperdict={}
poll_options={}
polls=[]

snipe_buttons = [
  ui.Button(color='primary', custom_id="Snipe1", emoji="⏪"),
  ui.Button(color='primary', custom_id="Snipe2", emoji="⬅️"),
  ui.Button(color='primary', custom_id="Snipe3", emoji="📌"),
  ui.Button(color='primary', custom_id="Snipe4", emoji="➡️"),
  ui.Button(color='primary', custom_id="Snipe5", emoji="⏩")
]

async def snipe_update(ctx: ui.ButtonInteraction, msg: discord.Message, number: int):
  await ctx.respond()
  sniperdict[msg][0] = number
  embed = discord.Embed(title= f"Snipped message ({number}/{len(sniper[msg.channel])})", description= sniper[msg.channel][number-1][0])
  embed.set_footer(text= sniper[msg.channel][number-1][1])
  await msg.edit((msg.content if msg.content else "a"), embed= embed, components= snipe_buttons)

class SnipeL(ui.listener.Listener):
  @ui.Listener.button("Snipe1")
  async def snipe1(self_, ctx: ui.ButtonInteraction):
    await snipe_update(ctx, ctx.message, 1)

  @ui.Listener.button("Snipe2")
  async def snipe2(self_, ctx: ui.ButtonInteraction):
    await snipe_update(ctx, ctx.message, max(sniperdict[ctx.message][0]-1, 1))

  @ui.Listener.button("Snipe4")
  async def snipe4(self_, ctx: ui.ButtonInteraction):
    await snipe_update(ctx, ctx.message, min(sniperdict[ctx.message][0]+1, sniperdict[ctx.message][1]))

  @ui.Listener.button("Snipe5")
  async def snipe5(self_, ctx: ui.ButtonInteraction):
    await snipe_update(ctx, ctx.message, sniperdict[ctx.message][1])

  @ui.Listener.button("Snipe3")
  async def snipe3(self_, ctx: ui.ButtonInteraction):
    sniperdict[ctx.message] -= 1
    if ctx.channel.permissions_for(ctx.guild.get_member(796686363604680755)).manage_messages:
      if ctx.message.pinned:
        await ctx.message.unpin()
      else:
        await ctx.message.pin()
        pinmsg = await ctx.channel.fetch_message(ctx.channel.last_message_id)
        await pinmsg.delete()
    else:
      await ctx.respond("Unable to Pin/Unpin messages without the Manage Server permission. Error: `[L]`", hidden= True)
      return


"""
@bot_.event
async def on_interaction(interaction):
  interaction_select_option = interaction.data.get("values", None)
  interaction_original_message = interaction.message
  interaction_custom_id = interaction.data["custom_id"]
  if interaction_select_option:
    if interaction_custom_id in ["single-selection", "multi-selection"]:
      interaction_first_option = interaction_select_option[0]
      if interaction_first_option.startswith("help_"):
        await interaction.edit_original_message(embed=eval(interaction_first_option))
"""

@bot_.command(aliases=['sniper'])
async def snipe(ctx, *, text=None):
  chnl = ctx.channel
  if not text:
    if sniping.get(chnl, True):
      if not sniper.get(chnl, None):
        embed = discord.Embed(title= "Empty", description= "Nothing to snipe from this channel.")
        await ctx.reply(embed=embed)
        return
      else:
        embed = discord.Embed(title= f"Snipped message (1/{len(sniper[chnl])})", description= sniper[chnl][0][0])
        embed.set_footer(text= sniper[chnl][0][1])
      if chance(1000):
        msg = await ctx.reply("Did someone just ghostping you?", embed= embed, components= snipe_buttons, listener= SnipeL())
      else:
        msg = await ctx.reply("a", embed= embed, components= snipe_buttons, listener= SnipeL())
      sniperdict[msg] = [1, len(sniper[chnl])]
    else:
      await ctx.reply("Snipping is disabled. Please ask someone with manage messages permission to re-enable it. [Error: `lol_you_tried`]")
  elif has_perms(ctx.channel, ctx.author, 13):
    if specialbool(text):
      sniping[chnl] = True
      await ctx.reply("Sniping is now enabled.")
    else:
      sniping[chnl] = False
      await ctx.reply("Sniping is now disabled.")
  else:
    await ctx.reply("""If you want to view sniped messages, please run `=snipe` without any arguments.
    If you intend to enable/disable sniping, you are missing the Manage Channels permission.""")

@bot_.event
async def on_message_delete(message):
  keyname = f"{message.guild.id}{message.channel.id}"
  val = message.content
  if not val.replace(" ",""):
    return
  adt = f"By {message.author.name}#{message.author.discriminator} at {time_display(message.created_at)}"
  if not sniper.get(message.channel):
    sniper[message.channel] = []
  sniper[message.channel].insert(0, [val, adt])
  sniper[message.channel] = sniper[message.channel][:5]

@bot_.command()
async def clearsnipe(ctx, *, chnl : discord.TextChannel = None):
  if chnl == None:
    chnl = ctx.channel
  if chnl.permissions_for(ctx.author).manage_channels or botadmin(ctx):
    sniper[chnl] = []
    await ctx.reply(f"Cleared snipe database for {chnl.mention}.")
  else:
    await ctx.reply("You don't have the required permission: Manage channels. Error: [`lol_imagine_trying_you_peasant`]")

#@tasks.loop(hours=24)
#async def sba_marks():
#  sba_channel = bot_.get_channel(909445785509326859)
#  await sba_channel.send(f"5m")
#  i dont know you so well, your hearts been aching but i dont give a shit

@bot_.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    message = ctx.message
    used_prefix = ctx.prefix
    used_command = message.content.split()[0][len(used_prefix):].lower()
    available_commands = [cmd.name for cmd in bot_.commands]
    matches = {cmd: SequenceMatcher(None, cmd, used_command).ratio() for cmd in available_commands}
    command = max(matches.items(), key=lambda item: item[1])[0]
    if SequenceMatcher(None, used_command, used_command).ratio() <= 0.7:
      await ctx.reply(f'Your might have made a (serious) typo and your command has been ignored. [Error: `grammarly_can_help_you`]', delete_after=4)
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
    await ctx.reply('One or more of your arguments is/are not in the correct format! Please read the documentation. Error: `touch_grass`')
  elif isinstance(error, commands.NotOwner):
    await ctx.reply('Unfortunately, only the owner of the bot is allowed to use this.')
  elif isinstance(error, commands.CommandInvokeError):
    error_ = error.original
    if isinstance(error_, FileNotFoundError):
      await ctx.reply('Unfortunately, the file could not be generated.')
  elif isinstance(error, discord.HTTPException):
    if error.code == 40005:
      await ctx.reply('Unfortunately, the output file is too large.')
    elif error.code == 50006:
      await ctx.reply('Unfortunately, there is no output.')
    elif error.code == 50035:
      await ctx.reply('Unfortunately, the output text is too long.')
  else:
    try:
      await ctx.send(f"Sorry! An error occured:\n```{''.join(traceback.format_exception(type(error), error, error.__traceback__))}```\n If the error persists, please kindly inform JohannLau#6541 about this issue.")
    except discord.HTTPException:
      print(''.join(traceback.format_exception(type(error), error, error.__traceback__)))
      await ctx.reply(f"Sorry! An error occured. The error was too long but it had been shown to JohannLau#6541. If the error persists, Please kindly inform him about this issue. [Error: `when_did_humans_exceed_bots`]")

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
  except discord.NotFound:
    pass
  try:
    if before.channel == None and after.channel.id == 822750915466493982:
      supchat = member.guild.get_channel(822753048510070784)
      await supchat.purge(limit=1000)
      await supchat.set_permissions(member, overwrite=view_overwrite)
  except discord.NotFound:
    pass

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
@commands.is_owner()
async def purgeserver(ctx, text, condition="True", *, disposed = None):
  text = text.lower()
  if text.startswith("role"):
    allroles = ctx.guild.roles()
    for _role in allroles:
      if eval(condition):
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
  except discord.Forbidden:
    await ctx.reply("Unable to change nickname.")

@bot_.command()
async def botpurge(ctx, *, num : int = 1):
  try:
    await ctx.message.delete()
  except discord.Forbidden:
    pass
  if ctx.channel.permissions_for(ctx.author).manage_messages or botadmin(ctx):
    purged = 0
    async for x in ctx.channel.history(limit=1000):
      if x.author.id == 796686363604680755:
        await x.delete()
        purged = purged + 1
        if purged >= num:
          break
    await ctx.send("Bot purging completed.", delete_after = 5)
  else:
    await ctx.send("You don't have the required permission: Manage messages.")

@bot_.command(aliases=["online"])
async def ping(ctx, *, disposed = None):
  now1 = datetime.now(timezone.utc)
  message = await ctx.send("Pong!")
  mcs = str(int((datetime.now(timezone.utc) - now1).microseconds)+int(((datetime.now(timezone.utc) - now1).total_seconds())%60))
  await message.edit(content=f"Pong! 🏓\n```Message delay: {mcs} microseconds\nBot latency  : {round(bot_.latency*1000000, 2)} microseconds```")

@ui_.slash.command(name="ping", description="Checks whether the bot is online or not.")
async def ping(ctx):
  now1 = datetime.now(timezone.utc)
  message = await ctx.respond("Pong!")
  mcs = str(int((datetime.now(timezone.utc) - now1).microseconds)+int(((datetime.now(timezone.utc) - now1).total_seconds())%60))
  await message.edit(content=f"Pong! 🏓\n```Message delay: {mcs} microseconds\nBot latency  : {round(bot_.latency*1000000, 2)} microseconds```")

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
  bot_.run('Nzk2Njg2MzYzNjA0NjgwNzU1.X_bh_g.t51TSXlWn07tXR0IalasHr3a59I')
except:
  pass
