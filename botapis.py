from discord.ext import commands
import requests
import html
import random

@commands.command(aliases=["rabbit", "rabbits", "bunnies"])
async def bunny(ctx, number=1):
  if number<10:
    await ctx.reply(botbunny(number))
  else:
    await ctx.reply("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command()
async def cat(ctx, number=1):
  if number<10:
    await ctx.reply(botcat(number))
  else:
    await ctx.reply("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command(aliases=["food"])
async def dish(ctx, number=1):
  if number<10:
    await ctx.reply(botdish(number))
  else:
    await ctx.reply("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command()
async def dog(ctx, number=1):
  if number<10:
    await ctx.reply(botdog(number))
  else:
    await ctx.reply("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command()
async def duck(ctx, number=1):
  if number<10:
    await ctx.reply(botduck(number))
  else:
    await ctx.reply("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command()
async def fox(ctx, number=1):
  if number<10:
    await ctx.reply(botfox(number))
  else:
    await ctx.reply("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command()
async def joke(ctx, number=1):
  if number<10:
    await ctx.reply(botjoke(number))
  else:
    await ctx.reply("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command()
async def koala(ctx, number=1):
  if number<10:
    await ctx.reply(botkoala(number))
  else:
    await ctx.reply("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command()
async def lizard(ctx, number=1):
  if number<10:
    await ctx.reply(botlizard(number))
  else:
    await ctx.reply("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command(aliases=["apod"])
async def nasa(ctx):
  await ctx.reply(botnasa())

@commands.command()
async def panda(ctx, number=1):
  if number<10:
    await ctx.reply(botpanda(number))
  else:
    await ctx.reply("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command()
async def quote(ctx, number=1):
  if number<6:
    await ctx.reply(botquote(number))
  else:
    await ctx.reply("There are too many quotes to show! I can only display up to 5 quotes.")

@commands.command()
async def shiba(ctx, number=1):
  if number<10:
    await ctx.reply(botshiba(number))
  else:
    await ctx.reply("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command()
async def states(ctx, country="UK"):
  await ctx.reply(botstates(country.upper()))

@commands.command(aliases=["quiz", "questions"])
async def trivia(ctx, number=1):
  if number<4:
    await ctx.reply(bottrivia(number))
  else:
    await ctx.reply("There are too many questions to show! I can only display up to 3 questions.")


def botbunny(number):
  desc = ""
  for count in range(1, number+1):
    r = requests.get('https://api.bunnies.io/v2/loop/random/?media=gif')
    desc += f"{r.json()['media']['gif']}\n"
  return desc

def botcat(number):
  desc = ""
  for count in range(1, number+1):
    r=requests.get("https://api.thecatapi.com/v1/images/search")
    desc += f"{r.json()[0]['url']}\n"
  return desc

def botdish(number):
  desc = ""
  for count in range(1, number+1):
    r = requests.get('https://foodish-api.herokuapp.com/api/')
    desc += f"{r.json()['image']}\n"
  return desc

def botdog(number):
  desc = ""
  for count in range(1, number+1):
    r=requests.get("https://dog.ceo/api/breeds/image/random")
    desc += f"{r.json()['message']}\n"
  return desc

def botduck(number):
  desc = ""
  for count in range(1, number+1):
    r = requests.get('https://random-d.uk/api/v1/random')
    desc += f"{r.json()['url']}\n"
  return desc

def botfox(number):
  desc = ""
  for count in range(1, number+1):
    r = requests.get('https://randomfox.ca/floof/')
    desc += f"{r.json()['image']}\n"
  return desc

def botjoke(number):
  desc = ""
  for count in range(1, number+1):
    r = requests.get('https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit').json()
    if r.get("setup", None):
      desc += f"{r['setup']} ||{r['delivery']}||\n"
    else:
      desc += f"{r['joke']}\n"
  return desc

def botkoala(number):
  desc = ""
  for count in range(1, number+1):
    r=requests.get("https://some-random-api.ml/img/koala")
    desc += f"{r.json()['link']}\n"
  return desc

def botlizard(number):
  desc = ""
  for count in range(1, number+1):
    r = requests.get('https://nekos.life/api/v2/img/lizard')
    desc += f"{r.json()['url']}\n"
  return desc

def botnasa():
  r = requests.get('https://apodapi.herokuapp.com/api').json()
  desc = f"**{r['title']}** by {r['copyright']}\n{r['hdurl']}\n\n{r['description']}"
  return desc[:1023]

def botpanda(number):
  desc = ""
  for count in range(1, number+1):
    r=requests.get("https://some-random-api.ml/img/panda")
    desc += f"{r.json()['link']}\n"
  return desc

def botparagraph(number):
  r = requests.get(f'http://metaphorpsum.com/paragraphs/1/{number}').content
  return r

def botquote(number):
  desc = ""
  for count in range(1, number+1):
    r=requests.get("http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json").json()
    desc += f"> {r['quoteText']}\n—By {r['quoteAuthor']}\n\n"
  return desc

def botshiba(number):
  desc = ""
  for count in range(1, number+1):
    r=requests.get("http://shibe.online/api/shibes")
    desc += f"{r.json()[0]}\n"
  return desc

def botstates(country):
  r=requests.get(f"https://rawcdn.githack.com/kamikazechaser/administrative-divisions-db/master/api/{country}.json")
  desc = ", ".join(r.json())
  return desc

def bottrivia(number):
  desc = ""
  try:
    r=requests.get(f"https://opentdb.com/api.php?amount={number}&encoding=base64").json()["results"]
  except:
    return "The country code could not be found!"
  for count in r:
    desc += f"**{count['category']} - {count['difficulty']}**  - {html.unescape(count['question'])}\n"
    if count["type"] == "multiple":
      list_temp = [html.unescape(x) for x in count["incorrect_answers"]] + [html.unescape(count["correct_answer"])]
      random.shuffle(list_temp)
      for x in list_temp:
        desc += f'  • {x}\n'
      desc += f"Answer: ||{html.unescape(count['correct_answer'])}||\n"
    else:
      desc += f"True or False?\nAnswer: ||{html.unescape(count['correct_answer'])}||\n"
  return desc


def setup(bot):
  bot.add_command(bunny)
  bot.add_command(cat)
  bot.add_command(dish)
  bot.add_command(dog)
  bot.add_command(duck)
  bot.add_command(fox)
  bot.add_command(joke)
  bot.add_command(koala)
  bot.add_command(lizard)
  bot.add_command(nasa)
  bot.add_command(panda)
  bot.add_command(quote)
  bot.add_command(shiba)
  bot.add_command(states)
  bot.add_command(trivia)
