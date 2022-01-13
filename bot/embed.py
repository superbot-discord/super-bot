import aiohttp
from nextcord import Webhook
from shared import *

@commands.command()
async def editembed(ctx, message : discord.Message = None, *,text):
  if message==None:
    potential_reference = ctx.message.reference
    if potential_reference:
      message=await ctx.bot.get_channel(potential_reference.channel_id).fetch_message(potential_reference.message_id)
    else:
      await ctx.reply("Please reply to a message or add a message ID/Link.")
      return
  embed = botembed(text)
  await message.edit(embed=embed)

@commands.command()
async def embed(ctx, *, text):
  embed = botembed(text)
  await ctx.send(embed=embed)

@commands.command()
async def ett(ctx, msg : discord.Message = None):
  if msg==None:
    potential_reference = ctx.message.reference
    if potential_reference:
      msg=await ctx.bot.get_channel(potential_reference.channel_id).fetch_message(potential_reference.message_id)
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
  whl = filter(lambda x: x.name == "Pretender", webhooks)
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
  whl = filter(lambda x: x.name == "Pretender", webhooks)
  if whl:
    wh = whl[0]
  else:
    wh = await ctx.channel.create_webhook(name= "Pretender")
  await wh.send(embed= embed, username= member.name, avatar_url= member.display_avatar.url)

@commands.command(aliases=["fastembed", "qe"])
async def quickembed(ctx, *, text):
  textlist=text.splitlines()
  embed = discord.Embed()
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
  embed = discord.Embed()
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
  embed = discord.Embed()
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

def setup(bot):
  bot.add_command(editembed)
  bot.add_command(embed)
  bot.add_command(ett)
  bot.add_command(pretend)
  bot.add_command(pretendembed)
  bot.add_command(quickembed)
  bot.add_command(simpleembed)
