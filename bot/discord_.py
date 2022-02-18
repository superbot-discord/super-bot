from _bot import bs
from shared import chance, commands, discord, Embed, has_perms, specialbool, time_display, ui
# specialbool no longer needed once =snipe context command is removed

sniper = {} # List of deleted messages
sniping = {} # Dict of channel:bool showing the availability of sniping
sniperdict = {} # List of messages sent by =snipe or /snipe

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
  embed = Embed(title= f"Snipped message ({number}/{len(sniper[msg.channel])})", description= sniper[msg.channel][number-1][0])
  embed.set_footer(text= sniper[msg.channel][number-1][1])
  await msg.edit((msg.content if msg.content else ""), embed= embed, components= snipe_buttons)

class SnipeL(ui.listener.Listener):
  def __init__(self, user_id: int):
    self.target_users = [user_id]

  @ui.Listener.button(custom_id= "Snipe1")
  async def snipe1(self_, ctx: ui.ButtonInteraction):
    await snipe_update(ctx, ctx.message, 1)

  @ui.Listener.button(custom_id= "Snipe2")
  async def snipe2(self_, ctx: ui.ButtonInteraction):
    await snipe_update(ctx, ctx.message, max(sniperdict[ctx.message][0]-1, 1))

  @ui.Listener.button(custom_id= "Snipe4")
  async def snipe4(self_, ctx: ui.ButtonInteraction):
    await snipe_update(ctx, ctx.message, min(sniperdict[ctx.message][0]+1, sniperdict[ctx.message][1]))

  @ui.Listener.button(custom_id= "Snipe5")
  async def snipe5(self_, ctx: ui.ButtonInteraction):
    await snipe_update(ctx, ctx.message, sniperdict[ctx.message][1])

  @ui.Listener.button(custom_id= "Snipe3")
  async def snipe3(self_, ctx: ui.ButtonInteraction):
    sniperdict[ctx.message] -= 1
    if has_perms(ctx.channel, ctx.author, 13):
      if ctx.message.pinned:
        await ctx.message.unpin()
      else:
        await ctx.message.pin()
        pinmsg = await ctx.channel.fetch_message(ctx.channel.last_message_id)
        await pinmsg.delete()
    else:
      await ctx.respond("Unable to Pin/Unpin messages without the Manage Server permission.", hidden= True)
      return
  
  @ui.Listener.wrong_user()
  async def wrong_user(self, ctx):
    await ctx.respond("Please use `/snipe` on your own in order to browse snipped messages.", hidden= True)


@commands.command()
async def editembed(ctx, message : discord.Message = None, *,text):
  if message == None:
    potential_reference = ctx.message.reference
    if potential_reference:
      message = await ctx.bot.get_channel(potential_reference.channel_id).fetch_message(potential_reference.message_id)
    else:
      await ctx.reply("Please reply to a message or add a message ID/Link.")
      return
  embed = botembed(text)
  await message.edit(embed= embed)

@commands.command()
async def embed(ctx, *, text):
  embed = botembed(text)
  await ctx.send(embed= embed)

@commands.command()
async def ett(ctx, msg : discord.Message = None):
  if msg == None:
    potential_reference = ctx.message.reference
    if potential_reference:
      msg = await ctx.bot.get_channel(potential_reference.channel_id).fetch_message(potential_reference.message_id)
    else:
      await ctx.reply("Please reply to a message or add a message ID/Link.")
      return
  text = botett(msg)
  await ctx.reply("```"+text+"```")

@commands.command()
async def pretend(ctx, member: discord.Member, *, message):
  try:
    await ctx.message.delete()
  except:
    pass
  webhooks = await ctx.channel.webhooks()
  whl = list(filter(lambda x: x.name == "Pretender", webhooks))
  if whl:
    wh = whl[0]
  else:
    wh = await ctx.channel.create_webhook(name= "Pretender")
  await wh.send(message, username= member.name, avatar_url= member.display_avatar.url)

@commands.command()
async def pretendembed(ctx, member: discord.Member, *, text):
  embed = botembed(text)
  try:
    await ctx.message.delete()
  except:
    pass
  webhooks = await ctx.channel.webhooks()
  whl = list(filter(lambda x: x.name == "Pretender", webhooks))
  if whl:
    wh = whl[0]
  else:
    wh = await ctx.channel.create_webhook(name= "Pretender")
  await wh.send(embed= embed, username= member.name, avatar_url= member.display_avatar.url)

@commands.command(aliases=["fastembed", "qe"])
async def quickembed(ctx, *, text):
  textlist=text.splitlines()
  embed = Embed()
  try:
    embed.title            = textlist[0]
  except:
    pass
  try:
    embed.color          = int(textlist[1])
  except:
    pass
  try:
    embed.set_image    (url =textlist[2])
  except:
    pass
  try:
    embed.description      = f"\n".join(textlist[3:])
  except:
    pass
  await ctx.send(embed=embed)

@commands.command(aliases=['simpembed', 'simplembed', 'sembed'])
async def simpleembed(ctx, *, text):
  textlist=text.splitlines()
  embed = Embed()
  try:
    embed.title            = textlist[0]
  except:
    pass
  try:
    embed.description      = textlist[1].replace("{{{newline}}}", f"\n")
  except:
    pass
  try:
    embed.color          = int(textlist[2])
  except:
    pass
  try:
    embed.set_image    (url =textlist[3])
  except:
    pass
  for x in range((len(textlist)-3)//3):
    inline = textlist[3*x+4].lower()
    inline = inline.startswith("y") or inline.startswith("1") or inline.startswith("e") or inline.startswith("on")
    embed.add_field(name=textlist[3*x+5], value=textlist[3*x+6].replace("{{{newline}}}", f"\n"), inline=inline)
  await ctx.send(embed=embed)

def botett(msg):
  #for x in msg.embeds:
  x = msg.embeds[0]
  edict = x.to_dict()
  ekeys = list(edict)
  desc = "=embed "
  if 'title' in ekeys:
    desc += edict['title']
  desc += f"\n"
  if 'description' in ekeys:
    desc += edict['description'].replace(f"\n", "{{{newline}}}")
  desc += f"\n"
  if 'color' in ekeys:
    desc += str(edict['color'])
  desc += f"\n"
  if 'url' in ekeys:
    desc += edict['url']
  desc += f"\n"
  if 'author' in ekeys:
    eauthor = edict['author']
    authorkeys = list(eauthor)
    if 'name' in authorkeys:
      desc += eauthor['name']
  desc += f"\n"
  if 'footer' in ekeys:
    efooter = edict['footer']
    footerkeys = list(efooter)
    if 'text' in footerkeys:
      desc += efooter['text']
  desc += f"\n"
  if 'author' in ekeys:
    if 'url' in authorkeys:
      desc += eauthor['url']
  desc += f"\n"
  if 'image' in ekeys:
    desc += (edict['image'])['url']
  desc += f"\n"
  if 'thumbnail' in ekeys:
    desc += (edict['thumbnail'])['url']
  desc += f"\n"
  if 'author' in ekeys:
    if 'icon_url' in authorkeys:
      desc += eauthor['icon_url']
  desc += f"\n"
  if 'footer' in ekeys:
    if 'icon_url' in footerkeys:
      desc += efooter['icon_url']
  desc += f"\n"
  if 'fields' in ekeys:
    for x in edict['fields']:
      desc = f"{desc}{x['inline']}\n{x['name']}\n"+x['value'].replace(f'\n', '{{{newline}}}')+f"\n"
  return desc

def botembed(text):
  textlist=text.splitlines()
  embed = Embed()
  try:
    embed.title        = textlist[0]
  except:
    pass
  try:
    embed.description  = textlist[1].replace("{{{newline}}}", f"\n")
  except:
    pass
  try:
    embed.color        = int(textlist[2])
  except:
    pass
  try:
    embed.url          = textlist[3]
  except:
    pass
  try:
    embed.set_author   (name=textlist[4])
  except:
    pass
  try:
    embed.set_footer   (text=textlist[5])
  except:
    pass
  try:
    embed.set_author   (name=textlist[4], url=textlist[6])
  except:
    pass
  try:
    embed.set_image    (url =textlist[7])
  except:
    pass
  try:
    embed.set_thumbnail(url =textlist[8])
  except:
    pass
  try:
    embed.set_author   (name=textlist[4], url=textlist[6], icon_url=textlist[9])
  except:
    pass
  try:
    embed.set_footer   (text=textlist[5], icon_url=textlist[10])
  except:
    pass
  for x in range((len(textlist)-11)//3):
    inline = textlist[3*x+11].lower()
    inline = inline.startswith("y") or inline.startswith("1") or inline.startswith("e") or inline.startswith("on")
    embed.add_field(name=textlist[3*x+12], value=textlist[3*x+13].replace("{{{newline}}}", f"\n"), inline=inline)
  return embed

@commands.command(aliases=['sniper']) # Migrated
async def snipe(ctx, *, text= None):
  chnl = ctx.channel
  if not text:
    if sniping.get(chnl, True):
      if not sniper.get(chnl, None):
        embed = Embed(title= "Empty", description= "Nothing to snipe from this channel.")
        await ctx.reply(embed= embed)
        return
      else:
        embed = Embed(title= f"Snipped message (1/{len(sniper[chnl])})", description= sniper[chnl][0][0])
        embed.set_footer(text= sniper[chnl][0][1])
      if chance(1000):
        msg = await ctx.reply("Did someone just ghostping you?", embed= embed, components= snipe_buttons, listener= SnipeL(ctx.author.id))
      else:
        msg = await ctx.reply(embed= embed, components= snipe_buttons, listener= SnipeL(ctx.author.id))
      sniperdict[msg] = [1, len(sniper[chnl])]
    else:
      await ctx.reply("Snipping is disabled. Please ask someone with manage messages permission to re-enable it.")
  elif has_perms(ctx.channel, ctx.author, 4):
    if specialbool(text):
      sniping[chnl] = True
      await ctx.reply("Sniping is now enabled.")
    else:
      sniping[chnl] = False
      await ctx.reply("Sniping is now disabled.")
  else:
    await ctx.reply("""If you want to view sniped messages, please run `=snipe` without any arguments.
    If you intend to enable/disable sniping, you are missing the Manage Channels permission.""")

@commands.command() # Migrated
async def clearsnipe(ctx, *, chnl: discord.TextChannel = None):
  if chnl == None:
    chnl = ctx.channel
  if has_perms(chnl, ctx.author, 4):
    sniper[chnl] = []
    await ctx.reply(f"Cleared snipe database for {chnl.mention}.")
  else:
    await ctx.reply("You don't have the required permission: Manage channels.")


@bs.command(name="snipe", description="View up to 8 most recently deleted messages in this channel.")
async def snipe_(ctx: ui.SlashInteraction):
  chnl = ctx.channel
  if sniping.get(chnl, True):
    if not sniper.get(chnl, None):
      embed = Embed(title= "Empty", description= "Nothing to snipe from this channel.")
      await ctx.respond(embed=embed)
      return
    else:
      embed = Embed(title= f"Snipped message (1/{len(sniper[chnl])})", description= sniper[chnl][0][0])
      embed.set_footer(text= sniper[chnl][0][1])
    if chance(1000):
      msg = await ctx.respond("Did someone just ghostping you?", embed= embed, components=
                              snipe_buttons, listener= SnipeL(ctx.author.id))
    else:
      msg = await ctx.respond(embed= embed, components= snipe_buttons, listener= SnipeL(ctx.author.id))
    sniperdict[msg] = [1, len(sniper[chnl])]
  else:
    await ctx.respond("Snipping is disabled. Please ask someone with manage messages permission to re-enable it.")

@bs.command(name="snipe_toggle", description="Enable or disable sniping in this channel.",
           options=[ui.SlashOption(name= "Toggle", type= bool, description=
           "Whether to enable or disable sniping. Toggles the current option by default.")])
async def snipe_toggle(ctx: ui.SlashInteraction, toggle= None):
  chnl = ctx.channel
  if toggle == None:
    toggle = not sniping[chnl]
  sniping[chnl] = toggle
  await ctx.respond(f"Sniping is now {'enabled' if toggle else 'disabled'}.")

@bs.command(name="snipe_clear", description="Clears the snipe database for a channel.",
           options=[ui.SlashOption(name= "Channel", type= discord.TextChannel, description=
           "The channel to clear the database of. Defaults to the current channel.",
           channel_types= [discord.ChannelType.text])])
async def snipe_clear(ctx: ui.SlashInteraction, channel: discord.TextChannel = None):
  channel = ctx.channel if not channel else channel
  if has_perms(ctx.channel, ctx.author, 4):
    sniper[channel] = []
    await ctx.respond(f"Cleared snipe database for {channel.mention}.")
  else:
    await ctx.respond("You don't have the required permission: Manage channels.")

async def snipe_log(message: discord.Message):
  val = message.content
  val = val if val else "*No message content*"
  if message.attachments:
    val += f"\n".join([x.url for x in message.attachments])
  footer = f"By {message.author.name}#{message.author.discriminator} at {time_display(message.created_at)} UTC"
  footer+= f" • The message includes {len(message.embeds)} embeds"
  if not sniper.get(message.channel):
    sniper[message.channel] = []
  sniper[message.channel].insert(0, [val, footer])
  sniper[message.channel] = sniper[message.channel][:15]

def setup(bot):
  bot.add_command(editembed)
  bot.add_command(embed)
  bot.add_command(ett)
  bot.add_command(pretend)
  bot.add_command(pretendembed)
  bot.add_command(quickembed)
  bot.add_command(simpleembed)
  bot.add_command(snipe)
  bot.add_command(clearsnipe)
  bot.add_listener(snipe_log, 'on_message_delete')
