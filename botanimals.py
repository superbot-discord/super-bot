from discord.ext import commands
import requests
import re

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

def botdog(number):
  desc = ""
  for count in range(1, number+1):
    r=requests.get(f"https://dog.ceo/api/breeds/image/random")
    link=re.sub('{"message":"([\S]*?)","status":"success"}', r'\1', r.content.decode("utf-8"))
    link=link.replace("\\", "")
    desc += f"{link}\n"
  return desc

def botcat(number):
  desc = ""
  for count in range(1, number+1):
    r=requests.get(f"https://api.thecatapi.com/v1/images/search")
    link=re.sub('[{"breeds":[\s\S]*?,"id":"[\s\S]*?","url":"([\S]*?)","width":[\d]*?,"height":[\d]*?}]', r'\1', r.content.decode("utf-8"))
    desc += f"{link}\n"
  return desc

def setup(bot):
  bot.add_command(dog)
  bot.add_command(cat)