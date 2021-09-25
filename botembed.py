import aiohttp
import discord as discord
from discord import Webhook
from discord.ext import commands


@commands.command()
async def editembed(ctx, message : discord.Message, *,text):
  embed = botembed(text)
  await message.edit(embed=embed)

@commands.command()
async def embed(ctx, *, text):
  embed = botembed(text)
  await ctx.send(embed=embed)

@commands.command()
async def ett(ctx, msg : discord.Message):
  text = botett(msg)
  await ctx.send("```"+text+"```")


@commands.command(pass_context=True)
async def pretend(ctx, member : discord.Member, *, message):
  try:
    await ctx.message.delete()
  except:
    pass
  whl = await ctx.channel.webhooks()
  ourweb = False
  for count in whl:
    if count.name == "Pretender":
      ourweb = True
      token = count.token
      identify = count.id
  if len(whl) == 0 or ourweb == False:
    wh = await ctx.channel.create_webhook(name = "Pretender")
    token = wh.token
    identify = wh.id
  async with aiohttp.ClientSession() as session:
    webhook = Webhook.partial(identify, token, session=session)
    await webhook.send(message, username=member.name, avatar_url=member.avatar.url)

@commands.command(pass_context=True)
async def pretendembed(ctx, member : discord.Member, *, text):
  try:
    await ctx.message.delete()
  except:
    pass
  whl = await ctx.channel.webhooks()
  ourweb = False
  for count in whl:
    if count.name == "Pretender":
      ourweb = True
      token = count.token
      identify = count.id
  if len(whl) == 0 or ourweb == False:
    wh = await ctx.channel.create_webhook(name = "Pretender")
    token = wh.token
    identify = wh.id
  async with aiohttp.ClientSession() as session:
    webhook = Webhook.partial(identify, token, session=session)
  embed = botembed(text)
  await webhook.send(embed=embed, username=member.name, avatar_url=member.avatar.url)


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
  for count in range(0, (len(textlist)-3)//3):
    inline = textlist[3*count+4].lower()
    inline = inline.startswith("y") or inline.startswith("1") or inline.startswith("e") or inline.startswith("on")
    embed.add_field(name=textlist[3*count+5], value=textlist[3*count+6].replace("{{{newline}}}", f"\n"), inline=inline)
  await ctx.send(embed=embed)

def botett(msg):
  #for count in msg.embeds:
  count = msg.embeds[0]
  edict = count.to_dict()
  ekeys = list(edict)
  desc = "=embed "
  if ekeys.count('title') == 1:
    desc = desc + edict['title']
  desc = desc + f"\n"
  if ekeys.count('description') == 1:
    desc = desc + edict['description'].replace(f"\n", "{{{newline}}}")
  desc = desc + f"\n"
  if ekeys.count('color') == 1:
    desc = desc + str(edict['color'])
  desc = desc + f"\n"
  if ekeys.count('url') == 1:
    desc = desc + edict['url']
  desc = desc + f"\n"
  if ekeys.count('author') == 1:
    eauthor = edict['author']
    authorkeys = list(eauthor)
    if authorkeys.count('name') == 1:
      desc = desc + eauthor['name']
  desc = desc + f"\n"
  if ekeys.count('footer') == 1:
    efooter = edict['footer']
    footerkeys = list(efooter)
    if footerkeys.count('text') == 1:
      desc = desc + efooter['text']
  desc = desc + f"\n"
  if ekeys.count('author') == 1:
    if authorkeys.count('url') == 1:
      desc = desc + eauthor['url']
  desc = desc + f"\n"
  if ekeys.count('image') == 1:
    desc = desc + (edict['image'])['url']
  desc = desc + f"\n"
  if ekeys.count('thumbnail') == 1:
    desc = desc + (edict['thumbnail'])['url']
  desc = desc + f"\n"
  if ekeys.count('author') == 1:
    if authorkeys.count('icon_url') == 1:
      desc = desc + eauthor['icon_url']
  desc = desc + f"\n"
  if ekeys.count('footer') == 1:
    if footerkeys.count('icon_url') == 1:
      desc = desc + efooter['icon_url']
  desc = desc + f"\n"
  if ekeys.count('fields') == 1:
    for count in edict['fields']:
      desc = desc + str(count['inline']) + f"\n" + count['name'] + f"\n" + count['value'].replace(f"\n", "{{{newline}}}") + f"\n"
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
  for count in range(0, (len(textlist)-11)//3):
    inline = textlist[3*count+11].lower()
    inline = inline.startswith("y") or inline.startswith("1") or inline.startswith("e") or inline.startswith("on")
    embed.add_field(name=textlist[3*count+12], value=textlist[3*count+13].replace("{{{newline}}}", f"\n"), inline=inline)
  return embed

def setup(bot):
  bot.add_command(editembed)
  bot.add_command(embed)
  bot.add_command(ett)
  bot.add_command(pretend)
  bot.add_command(pretendembed)
  bot.add_command(quickembed)
  bot.add_command(simpleembed)
