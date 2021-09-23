from assets.discord.ext import commands
import assets.requests as requests

@commands.command()
async def dog(ctx, number=1):
  if number<9:
    await ctx.send(botdog(number))
  else:
    await ctx.send("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command()
async def cat(ctx, number=1):
  if number<9:
    await ctx.send(botcat(number))
  else:
    await ctx.send("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command()
async def panda(ctx, number=1):
  if number<9:
    await ctx.send(botpanda(number))
  else:
    await ctx.send("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command()
async def shiba(ctx, number=1):
  if number<9:
    await ctx.send(botshiba(number))
  else:
    await ctx.send("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command()
async def koala(ctx, number=1):
  if number<9:
    await ctx.send(botkoala(number))
  else:
    await ctx.send("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command()
async def bunny(ctx, number=1):
  if number<9:
    await ctx.send(botbunny(number))
  else:
    await ctx.send("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command()
async def duck(ctx, number=1):
  if number<9:
    await ctx.send(botduck(number))
  else:
    await ctx.send("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command()
async def fox(ctx, number=1):
  if number<9:
    await ctx.send(botfox(number))
  else:
    await ctx.send("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command()
async def lizard(ctx, number=1):
  if number<9:
    await ctx.send(botlizard(number))
  else:
    await ctx.send("There are too many pictures to show! I can only display up to 9 pictures.")


def botdog(number):
  desc = ""
  for count in range(1, number+1):
    r=requests.get(f"https://dog.ceo/api/breeds/image/random")
    desc += f"{r.json()['message']}\n"
  return desc

def botcat(number):
  desc = ""
  for count in range(1, number+1):
    r=requests.get(f"https://api.thecatapi.com/v1/images/search")
    desc += f"{r.json()[0]['url']}\n"
  return desc

def botpanda(number):
  desc = ""
  for count in range(1, number+1):
    r=requests.get(f"https://some-random-api.ml/img/panda")
    desc += f"{r.json()['link']}\n"
  return desc

def botshiba(number):
  desc = ""
  for count in range(1, number+1):
    r=requests.get(f"http://shibe.online/api/shibes")
    desc += f"{r.json()[0]}\n"
  return desc

def botkoala(number):
  desc = ""
  for count in range(1, number+1):
    r=requests.get(f"https://some-random-api.ml/img/koala")
    desc += f"{r.json()['link']}\n"
  return desc

def botbunny(number):
  desc = ""
  for count in range(1, number+1):
    r = requests.get('https://api.bunnies.io/v2/loop/random/?media=gif')
    desc += f"{r.json()['media']['gif']}\n"
  return desc

def botduck(number):
  desc = ""
  for count in range(1, number+1):
    r = requests.get('https://random-d.uk/api/v1/random')
    desc += f"{r.json()['message']}\n"
  return desc

def botfox(number):
  desc = ""
  for count in range(1, number+1):
    r = requests.get('https://randomfox.ca/floof/')
    desc += f"{r.json()['image']}\n"
  return desc

def botlizard(number):
  desc = ""
  for count in range(1, number+1):
    r = requests.get('https://nekos.life/api/v2/img/lizard')
    desc += f"{r.json()['url']}\n"
  return desc


def setup(bot):
  bot.add_command(bunny)
  bot.add_command(cat)
  bot.add_command(dog)
  bot.add_command(duck)
  bot.add_command(fox)
  bot.add_command(koala)
  bot.add_command(lizard)
  bot.add_command(panda)
  bot.add_command(shiba)