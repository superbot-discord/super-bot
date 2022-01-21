#from discord.ext import tasks
from shared import (commands, datetime, db, discord, Embed, ems,
                    has_perms, json, os, re, SequenceMatcher, timezone, traceback, ui,
                    view_overwrite)


bot_ = commands.Bot(command_prefix= commands.when_mentioned_or("="), intents= discord.Intents.all(),
                    allowed_mentions= discord.AllowedMentions(everyone= False, users= True,
                    roles= False, replied_user= False), case_insensitive= True, strip_after_prefix= True)
bu = ui.UI(bot_)
bs = ui.Slash(bot_)
banned_ids = []
banned_text = []

if __name__ == '__main__':
  bot_.remove_command('help')
  #bot_.load_extension("admin_")
  bot_.load_extension("apis__int")
  bot_.load_extension("apis_hk")
  bot_.load_extension("apis_uk")
  bot_.load_extension("basic")
  bot_.load_extension("calc")
  bot_.load_extension("convert")
  bot_.load_extension("development")
  bot_.load_extension("dinfo")
  bot_.load_extension("discord_")
  bot_.load_extension("engrave")
  bot_.load_extension("image")
  bot_.load_extension("info")
  bot_.load_extension("led")
  bot_.load_extension("moderate")
  bot_.load_extension("partners")
  bot_.load_extension("plot")
  bot_.load_extension("text")
  bot_.load_extension("webinfo")
  bot_.load_extension("webscrape")

  f = open('./assets/emojis.json', 'r')
  emojis_db = json.loads(f.read())
  f.close()

  emoji_options = []
  for x in emojis_db:
    emoji_options.append({'name': x, 'value': x.partition(" ")[0]})
  emoji_options = emoji_options[:25]

  poll_options={}
  polls=[]
  poll_pattern = re.compile(r'([\w]+?)(:\w{1,32}:|[\uD800-\uDBFF])')


  #@tasks.loop(hours=24)
  #async def sba_marks():
  #  sba_channel = bot_.get_channel(909445785509326859)
  #  await sba_channel.send(f"5m")

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
    embed = Embed(title = ti, description = ems.encode(desc))
    poll = await ctx.send(embed=embed)
    for x in reactions:
      await poll.add_reaction(x)
    polls.append(poll.id)
    poll_options[poll.id] = poll_options_cache

  # @slash.command(name="poll", description="Starts a reaction-based poll in the channel.", options=[
  #   ui.SlashOption(name= "Option 1 Emoji", type= str, required= True, choices= emoji_options),
  #   ui.SlashOption(name= "Option 1", type= str, required= True),
  #   ui.SlashOption(name= "Option 2 Emoji", type= str, required= True, choices= emoji_options),
  #   ui.SlashOption(name= "Option 2", type= str, required= True)
  # ])
  # async def poll_(ctx, option_1_emoji, option_1, option_2_emoji, option_2):
  #   pass

  @bot_.command()
  @commands.is_owner()
  async def nick(ctx, *, new_nick):
    try:
      await ctx.guild.me.edit(nick=(None if new_nick == "clear" else new_nick))
      await ctx.reply("Changed nickname.")
    except discord.Forbidden:
      await ctx.reply("Unable to change nickname.")

  @bot_.command()
  async def botpurge(ctx, *, num: int = 1):
    try:
      await ctx.message.delete()
    except discord.Forbidden:
      pass
    if has_perms(ctx.channel, ctx.author, 13):
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

  @bs.command(name= "ping_1", description= "Views the response time and latency of the bot.")
  async def ping_(ctx):
    now1 = datetime.now(timezone.utc)
    message = await ctx.respond("Pong!")
    response_time = datetime.now(timezone.utc) - now1
    mcs = str(int(response_time.microseconds)+int((response_time.total_seconds())%60))
    await message.edit(content=f"Pong! 🏓\n```Message delay: {mcs:<10}microseconds\nBot latency  : {round(bot_.latency*1000000, 2):<10}microseconds```")

  @bot_.command(aliases= ["online"])
  async def ping(ctx, *, disposed= None):
    now1 = datetime.now(timezone.utc)
    message = await ctx.send("Pong!")
    response_time = datetime.now(timezone.utc) - now1
    mcs = str(int(response_time.microseconds)+int((response_time.total_seconds())%60))
    await message.edit(content=f"Pong! 🏓\n```Message delay: {mcs:<10}microseconds\nBot latency  : {round(bot_.latency*1000000, 2):<10}microseconds```")


  @bs.message_command(name= "Spoil spoilers")
  async def spoil_(ctx, message):
    await ctx.respond(message.content.replace("||", ""), hidden= True)

  @bs.user_command(name= "Test")
  async def rickroller_(ctx, message):
    await ctx.respond("Never gonna give you up!", hidden= True)


  @bot_.event
  async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
      message = ctx.message
      used_prefix = ctx.prefix
      used_command = message.content.split()[0][len(used_prefix):].lower()
      available_commands = [cmd.name for cmd in bot_.commands]
      matches = {cmd: SequenceMatcher(None, cmd, used_command).ratio() for cmd in available_commands}
      command = max(matches.items(), key=lambda item: item[1])[0]
      if SequenceMatcher(None, command, used_command).ratio() <= 0.7:
        await ctx.reply(f"Your might have made a (serious) typo and your command has been ignored.", delete_after=4)
      try:
        arguments = message.content.split(" ", 1)[1]
      except IndexError:
        arguments = ""
      new_content = f"{used_prefix}{command} {arguments}".strip()
      message.content = new_content
      await ctx.reply(f"Your might have made a typo and your command has been interpreted as `{command}`.", delete_after=4)
      await bot_.process_commands(message)
    elif isinstance(error, commands.MissingRequiredArgument):
      await ctx.reply(f"You missed one or more arguments! {len(ctx.command.clean_params.keys())} argument(s) are required.\nNote: Multiline arguments are treated as one argument. Optional arguments are counted as well.")
    elif isinstance(error, commands.UserInputError):
      await ctx.reply("One or more of your arguments is/are not in the correct format! Please read the documentation.")
    elif isinstance(error, commands.NotOwner):
      await ctx.reply("Unfortunately, only the owner of the bot is allowed to use this.")
    elif isinstance(error, commands.CommandInvokeError):
      error_ = error.original
      if isinstance(error_, FileNotFoundError):
        await ctx.reply("Unfortunately, the file could not be generated.")
      else:
        try:
          await ctx.send(f"Sorry! An error occured:\n```{''.join(traceback.format_exception(type(error), error, error.__traceback__))}```\n If the error persists, please kindly inform JohannLau#6541 about this issue.")
        except discord.HTTPException:
          print(''.join(traceback.format_exception(type(error), error, error.__traceback__)))
          await ctx.reply(f"Sorry! An error occured. The error was too long but it had been shown to JohannLau#6541. If the error persists, Please kindly inform him about this issue.")
    elif isinstance(error, discord.HTTPException):
      if error.code == 40005:
        await ctx.reply("Unfortunately, the output file is too large.")
      elif error.code == 50006:
        await ctx.reply("Unfortunately, there is no output.")
      elif error.code == 50035:
        await ctx.reply("Unfortunately, the output text is too long.")
    else:
      try:
        await ctx.send(f"Sorry! An error occured:\n```{''.join(traceback.format_exception(type(error), error, error.__traceback__))}```\n If the error persists, please kindly inform JohannLau#6541 about this issue.")
      except discord.HTTPException:
        print(''.join(traceback.format_exception(type(error), error, error.__traceback__)))
        await ctx.reply(f"Sorry! An error occured. The error was too long but it had been shown to JohannLau#6541. If the error persists, Please kindly inform him about this issue.")

  # @bot_.event
  # async def on_thread_update(before, after):
  #   if after.id == 887562599191941121 and after.archived:
  #     await after.edit(archived= False)
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
      cache = Embed(title = cache_embed.title, description = ems.encode(desc))
      await msg.edit(embed= cache)

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
      cache = Embed(title = cache_embed.title, description = ems.encode(desc))
      await msg.edit(embed= cache)

  @bot_.event
  async def on_message(message):
    try:
      if message.guild.id == 852899227004305458 and message.author.id != 796686363604680755 and message.channel.id in [856053769149874196, 864757953121878026, 864754633910255646]:
        await message.add_reaction("<:UpArrowSquare:864762633194569728>")
        await message.add_reaction("<:DownArrowSquare:864762633625534485>")
        #                         SuperBot #news      #github             LSC Bots CraftBot   SuperBot            DolphinBot          WalkerBot           Waffles
      elif message.channel.id in [931899053376163850, 931899079653470218, 888254659502936074, 888254911740018708, 888256046496382988, 888256348268138556, 890227476452753448]:
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

  @bot_.event
  async def on_ready():
    global owner
    activity = discord.Activity(
      type=discord.ActivityType.playing,
      name=f"with =help in {len(bot_.guilds)} servers", timestamps = db["status_timestamps"])
    await bot_.change_presence(status= discord.Status.idle, activity= activity)
    print(f"Bot is ready!")


  print("Bot is getting started…")
  # try:
  bot_.run(os.environ['TOKEN'])
  # except:
  #   pass
