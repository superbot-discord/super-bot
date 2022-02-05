import html

from _bot import bs
from functions import trim
from shared import commands, chance, ra, requests, ui

"""country_option = ui.SlashOption(name= "Country/Region Code", description= "The country code", type= str, required=
                                True, autocomplete= True)
countries = [ # 19 x 12 = 228 items
  "AD","AE","AF","AG","AI","AL","AM","AO","AR","AS","AT","AU","AX","AZ","BA","BB","BD","BE","BF",
  "BG","BH","BI","BJ","BM","BN","BO","BQ","BR","BS","BT","BW","BY","BZ","CA","CD","CF","CG","CH",
  "CI","CK","CL","CM","CN","CO","CR","CU","CV","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE",
  "EG","ER","ES","ET","FI","FJ","FM","FO","FR","GA","GB","GD","GE","GF","GG","GH","GL","GM","GN",
  "GP","GQ","GR","GT","GU","GW","GY","HK","HN","HR","HT","HU","ID","IE","IL","IM","IN","IQ","IR",
  "IS","IT","JE","JM","JO","JP","KE","KG","KH","KI","KM","KN","KP","KR","KW","KY","KZ","LA","LB",
  "LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MH","MK","ML","MM","MN",
  "MO","MP","MQ","MR","MS","MT","MU","MV","MW","MX","MY","MZ","NA","NC","NE","NG","NI","NL","NO",
  "NP","NR","NZ","OM","PA","PE","PF","PG","PH","PK","PL","PM","PR","PS","PT","PW","PY","QA","RE",
  "RO","RS","RU","RW","SA","SB","SC","SD","SE","SH","SI","SJ","SK","SL","SM","SN","SO","SR","SS",
  "ST","SV","SY","SZ","TD","TF","TG","TH","TJ","TK","TL","TM","TN","TO","TR","TT","TV","TW","TZ",
  "UA","UG","UM","US","UY","UZ","VC","VE","VI","VN","VU","WF","WS","XK","YE","YT","ZA","ZM","ZW"
]"""

class TriviaRevealL(ui.listener.Listener):
  def __init__(self, answer_1, answer_2, answer_3, multi):
    self.a1 = answer_1
    self.a2 = answer_2
    self.a3 = answer_3
    self.multi = multi

  @ui.Listener.button(custom_id= "reveal1")
  async def show_a1(self_, ctx: ui.ButtonInteraction):
    await ctx.respond(f"The answer {'for Q1 ' if self_.multi else ''}is: {self_.a1}", hidden= True)
  
  @ui.Listener.button(custom_id= "reveal2")
  async def show_a2(self_, ctx: ui.ButtonInteraction):
    await ctx.respond(f"The answer for Q2 is: {self_.a2}", hidden= True)
  
  @ui.Listener.button(custom_id= "reveal3")
  async def show_a3(self_, ctx: ui.ButtonInteraction):
    await ctx.respond(f"The answer for Q3 is: {self_.a3}", hidden= True)

@commands.command(aliases=["birb"])
async def bird(ctx, number=1):
  if number<10:
    await ctx.reply(botbird(number))
  else:
    await ctx.reply("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command(aliases=["birb_fact"])
async def bird_fact(ctx, number=1):
  if number<10:
    await ctx.reply(botbird_fact(number))
  else:
    await ctx.reply("There are too many results to show! I can only display up to 9 facts.")

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

@commands.command()
async def cat_fact(ctx, number=1):
  if number<10:
    await ctx.reply(botcat_fact(number))
  else:
    await ctx.reply("There are too many results to show! I can only display up to 9 facts.")

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
async def dog_fact(ctx, number=1):
  if number<10:
    await ctx.reply(botdog_fact(number))
  else:
    await ctx.reply("There are too many results to show! I can only display up to 9 facts.")

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
async def fox_fact(ctx, number=1):
  if number<10:
    await ctx.reply(botfox_fact(number))
  else:
    await ctx.reply("There are too many results to show! I can only display up to 9 facts.")

@commands.command()
async def joke(ctx, number=1):
  if number<10:
    await ctx.reply(botjoke(number))
  else:
    await ctx.reply("There are too many jokes to show! I can only display up to 9 jokes.")

@commands.command()
async def kangaroo(ctx, number=1):
  if number<10:
    await ctx.reply(botkangaroo(number))
  else:
    await ctx.reply("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command()
async def kangaroo_fact(ctx, number=1):
  if number<10:
    await ctx.reply(botkangaroo_fact(number))
  else:
    await ctx.reply("There are too many results to show! I can only display up to 9 facts.")

@commands.command()
async def koala(ctx, number=1):
  if number<10:
    await ctx.reply(botkoala(number))
  else:
    await ctx.reply("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command()
async def koala_fact(ctx, number=1):
  if number<10:
    await ctx.reply(botkoala_fact(number))
  else:
    await ctx.reply("There are too many results to show! I can only display up to 9 facts.")

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
async def panda_fact(ctx, number=1):
  if number<10:
    await ctx.reply(botpanda_fact(number))
  else:
    await ctx.reply("There are too many results to show! I can only display up to 9 facts.")

@commands.command()
async def quote(ctx, number=1):
  if number<6:
    await ctx.reply(botquote(number))
  else:
    await ctx.reply("There are too many quotes to show! I can only display up to 5 quotes.")

@commands.command()
async def raccoon(ctx, number=1):
  if number<10:
    await ctx.reply(botraccoon(number))
  else:
    await ctx.reply("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command()
async def raccoon_fact(ctx, number=1):
  if number<10:
    await ctx.reply(botraccoon_fact(number))
  else:
    await ctx.reply("There are too many results to show! I can only display up to 9 facts.")

@commands.command()
async def shiba(ctx, number=1):
  if number<10:
    await ctx.reply(botshiba(number))
  else:
    await ctx.reply("There are too many pictures to show! I can only display up to 9 pictures.")

@commands.command(aliases=["provinces", "districts"])
async def states(ctx, country="US"):
  await ctx.reply(botstates(country.upper()))

@commands.command(aliases=["quiz", "questions"])
async def trivia(ctx, number=1):
  if number < 4:
    data = bottrivia(number)
    multi = number > 1
    await ctx.reply(data[0], components= data[2],listener= TriviaRevealL(*data[1], multi))
  else:
    await ctx.reply("There are too many questions to show! I can only display up to 3 questions.")

animal_choices = [{'name': "Bird", 'value': "bird"}, {'name': "Bunny", 'value': "bunny"},
                  {'name': "Cat", 'value': "cat"}, {'name': "Dog", 'value': "dog"},
                  {'name': "Duck", 'value': "duck"}, {'name': "Fox", 'value': "fox"},
                  {'name': "Kangaroo", 'value': "kangaroo"}, {'name': "Koala", 'value': "koala"},
                  {'name': "Lizard", 'value': "lizard"}, {'name': "Panda", 'value': "panda"},
                  {'name': "Raccoon", 'value': "raccoon"}, {'name': "Shiba Inu", 'value': "shiba"},
]
animal_fact_choices = list(filter(lambda x: x['value'] not in ['bunny', 'duck', 'lizard', 'shiba'],
                                  animal_choices))

@bs.command(name= "animal_image", description= "Shows up to 9 images of an animal.", options=[
           ui.SlashOption(name= "Animal", description= "The animal to show image(s) of.",
           type= str, required= True, choices= animal_choices), ui.SlashOption(name= "Number",
           description= "The no. of images to show, between 1 and 9 inclusive. Defaults to 1.",
           type= int, required= False, min_value= 1, max_value= 9)])
async def animal_image(ctx: ui.SlashInteraction, animal: str, number: int = 1):
  await ctx.respond(eval(f"bot{animal}({number})"))

@bs.command(name= "animal_fact", description= "Shows up to 9 fun facts about an animal.", options=[
           ui.SlashOption(name= "Animal", description= "The animal to show fact(s) about.",
           type= str, required= True, choices= animal_fact_choices), ui.SlashOption(name= "Number",
           description= "The no. of fun facts to show, between 1 and 9 inclusive. Defaults to 1.",
           type= int, required= False, min_value= 1, max_value= 9)])
async def animal_fact(ctx: ui.SlashInteraction, animal: str, number: int = 1):
  await ctx.respond(eval(f"bot{animal}_fact({number})"))

@bs.command(name= "trivia", description= "Shows up to 3 trivia questions.", options=[
           ui.SlashOption(name= "Number", type= int, required= False, min_value= 1, max_value= 3,
           description= "The no. of questions to show, between 1 and 3 inclusive. Defaults to 1.")])
async def _trivia(ctx: ui.SlashInteraction, number: int = 1):
  data = bottrivia(number)
  multi = number > 1
  await ctx.respond(data[0], components= data[2],listener= TriviaRevealL(*data[1], multi))

def botbird(number):
  desc = ""
  for x in range(number):
    r = requests.get('https://some-random-api.ml/img/birb').json()['link']
    desc += f"{r}\n"
  return desc

def botbird_fact(number):
  desc = ""
  for x in range(number):
    r=requests.get("https://some-random-api.ml/facts/bird").json()['fact']
    desc += f"{r}\n"
  return desc

def botbunny(number):
  desc = ""
  for x in range(number):
    r = requests.get('https://api.bunnies.io/v2/loop/random/?media=gif').json()['media']['gif']
    desc += f"{r}\n"
  return desc

def botcat(number):
  desc = ""
  for x in range(number):
    r=requests.get("https://api.thecatapi.com/v1/images/search").json()[0]['url'] if chance(2) else requests.get("https://some-random-api.ml/img/cat").json()['link']
    desc += f"{r}\n"
  return desc

def botcat_fact(number):
  desc = ""
  for x in range(number):
    r=requests.get("https://some-random-api.ml/facts/cat").json()['fact']
    desc += f"{r}\n"
  return desc

def botdish(number):
  desc = ""
  for x in range(number):
    r = requests.get('https://foodish-api.herokuapp.com/api/').json()['image']
    desc += f"{r}\n"
  return desc

def botdog(number):
  desc = ""
  for x in range(number):
    r=requests.get("https://dog.ceo/api/breeds/image/random").json()['message'] if chance(2) else requests.get("https://some-random-api.ml/img/dog").json()['link']
    desc += f"{r}\n"
  return desc

def botdog_fact(number):
  desc = ""
  for x in range(number):
    r=requests.get("https://some-random-api.ml/facts/dog").json()['fact']
    desc += f"{r}\n"
  return desc

def botduck(number):
  desc = ""
  for x in range(number):
    r = requests.get('https://random-d.uk/api/v1/random').json()['url']
    desc += f"{r}\n"
  return desc

def botfox(number):
  desc = ""
  for x in range(number):
    r = requests.get('https://randomfox.ca/floof/').json()['image'] if chance(2) else requests.get("https://some-random-api.ml/img/fox").json()['link']
    desc += f"{r}\n"
  return desc

def botfox_fact(number):
  desc = ""
  for x in range(number):
    r=requests.get("https://some-random-api.ml/facts/fox").json()['fact']
    desc += f"{r}\n"
  return desc

def botjoke(number):
  desc = ""
  for x in range(number):
    r = requests.get('https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit').json()
    if r.get("setup", None):
      desc += f"{r['setup']} ||{r['delivery']}||\n"
    else:
      desc += f"{r['joke']}\n"
  return desc

def botkangaroo(number):
  desc = ""
  for x in range(number):
    r = requests.get('https://some-random-api.ml/animal/kangaroo').json()['image']
    desc += f"{r}\n"
  return desc

def botkangaroo_fact(number):
  desc = ""
  for x in range(number):
    r = requests.get('https://some-random-api.ml/animal/kangaroo').json()['fact']
    desc += f"{r}\n"
  return desc

def botkoala(number):
  desc = ""
  for x in range(number):
    r=requests.get("https://some-random-api.ml/img/koala").json()['link']
    desc += f"{r}\n"
  return desc

def botkoala_fact(number):
  desc = ""
  for x in range(number):
    r=requests.get("https://some-random-api.ml/facts/koala").json()['fact']
    desc += f"{r}\n"
  return desc

def botlizard(number):
  desc = ""
  for x in range(number):
    r = requests.get('https://nekos.life/api/v2/img/lizard').json()['url']
    desc += f"{r}\n"
  return desc

def botnasa():
  r = requests.get('https://apodapi.herokuapp.com/api').json()
  desc = f"**{r['title']}** by {r['copyright']}\n{r['hdurl']}\n\n{r['description']}"
  return trim(desc, 1024)

def botpanda(number):
  desc = ""
  for x in range(number):
    r=requests.get(f"https://some-random-api.ml/img/{'' if chance(2) else 'red_'}panda").json()['link']
    desc += f"{r}\n"
  return desc

def botpanda_fact(number):
  desc = ""
  for x in range(number):
    r=requests.get("https://some-random-api.ml/facts/{'' if chance(2) else 'red_'}panda").json()['fact']
    desc += f"{r}\n"
  return desc

def botparagraph(number):
  r = requests.get(f'http://metaphorpsum.com/paragraphs/1/{number}').content
  return r

def botquote(number):
  desc = ""
  for x in range(number):
    r=requests.get("http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json").json()
    desc += f"> {r['quoteText']}\n—By {r['quoteAuthor']}\n\n"
  return desc

def botraccoon(number):
  desc = ""
  for x in range(number):
    r = requests.get('https://some-random-api.ml/animal/raccoon').json()['image']
    desc += f"{r}\n"
  return desc

def botraccoon_fact(number):
  desc = ""
  for x in range(number):
    r = requests.get('https://some-random-api.ml/animal/raccoon').json()['fact']
    desc += f"{r}\n"
  return desc

def botshiba(number):
  desc = ""
  for x in range(number):
    r=requests.get("http://shibe.online/api/shibes").json()[0]
    desc += f"{r}\n"
  return desc

def botstates(country):
  r=requests.get(f"https://rawcdn.githack.com/kamikazechaser/administrative-divisions-db/master/api/{country}.json").json()
  desc = ", ".join(r)
  return desc

def bottrivia(number):
  desc = ""
  answers = []
  try:
    r = requests.get(f"https://opentdb.com/api.php?amount={number}&encoding=base64").json()["results"]
  except:
    return ["Invalid input!", [], None]
  for x in r:
    desc += f"**{x['category']} - {x['difficulty']}**  - {html.unescape(x['question'])}\n"
    if x['type'] == "multiple":
      list_temp = [html.unescape(x) for x in x['incorrect_answers']] + [html.unescape(x['correct_answer'])]
      ra.shuffle(list_temp)
      for y in list_temp:
        desc += f'  • {y}\n'
    else:
      desc += f"True or False?\n"
    answers.append(html.unescape(x['correct_answer']))
    desc += f"\n"
  components = [ui.Button(label=f"Reveal{f' Q{x+1}' if len(answers) > 1 else ''}", color= 'green',
                custom_id= f"reveal{x+1}") for x in range(3) if len(answers) > x]
  answers = [answers[x] if len(answers) > x else None for x in range(3)] # pad answers to length 3
  return [desc, answers, components]

def setup(bot):
  bot.add_command(bird)
  bot.add_command(bird_fact)
  bot.add_command(bunny)
  bot.add_command(cat)
  bot.add_command(cat_fact)
  bot.add_command(dish)
  bot.add_command(dog)
  bot.add_command(dog_fact)
  bot.add_command(duck)
  bot.add_command(fox)
  bot.add_command(fox_fact)
  bot.add_command(joke)
  bot.add_command(kangaroo)
  bot.add_command(kangaroo_fact)
  bot.add_command(koala)
  bot.add_command(koala_fact)
  bot.add_command(lizard)
  bot.add_command(nasa)
  bot.add_command(panda)
  bot.add_command(panda_fact)
  bot.add_command(quote)
  bot.add_command(raccoon)
  bot.add_command(raccoon_fact)
  bot.add_command(shiba)
  bot.add_command(states)
  bot.add_command(trivia)
  print("Started loading modules")
