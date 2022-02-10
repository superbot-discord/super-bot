import html
from urllib.parse import quote as urlescape

from _bot import bs
from functions import trim
from shared import chance, commands, discord, ra, requests, text_wrapper, try_delete, ui

# All migrated in the file except =joke and =states
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

products = [
  {'name': "Airtags", 'value': "PX532AM"},
  {'name': "Apple Pencil", 'value': "PU8F2AM"},
  {'name': "Airpods Pro", 'value': "PLWK3AM"},
  {'name': "Airpods (2nd Generation)", 'value': "PV7N2AM"},
  {'name': "Airpods (3rd Generation)", 'value': "PMTC3AM"},
  {'name': "Airpods Max", 'value': "AM"},
  {'name': "iPad", 'value': "ID"},
  {'name': "iPad Air", 'value': "IA"},
  {'name': "iPad Mini", 'value': "IM"},
  {'name': "iPad Pro", 'value': "IP"},
  {'name': "iPod", 'value': "IO"}
]

product_colors = {
  'AM': [1, 2, 3, 6, 7],
  'ID': [1, 2],
  'IA': [1, 2, 4, 6, 10],
  'IM': [1, 7, 8, 11],
  'IP': [1, 2],
  'IO': [1, 2, 3, 5, 7, 9]
}

product_codes = {
  'AM1': "PGYH3AM", 'AM2': "PGYJ3AM", 'AM3': "PGYL3AM", 'AM6': "PGYN3AM", 'AM7': "PGYM3AM",
  'ID1': "PK2K3LL", 'ID2': "PK2L3LL",
  'IA1': "PYFM2LL", 'IA2': "PYFN2LL", 'IA4': "PYFQ2LL", 'IA6': "PYFR2LL", 'IA10':"PYFP2LL",
  'IM1': "PK7T3LL", 'IM7': "PLWR3LL", 'IM8': "PK7X3LL", 'IM11':"PK7V3LL",
  'IP1': "PHQR3LL", 'IP2': "PHQT3LL",
  'IO1': "PVHW2LL", 'IO2': "PVHV2LL", 'IO3': "PVHU2LL", 'IO5': "PVHT2LL", 'IO7': "PVHY2LL",
  'IO9': "PVHX2LL"
}

colors = [
  {'name': "Generic", 'value': 0},
  {'name': "Space Grey", 'value': 1},
  {'name': "Silver", 'value': 2},
  {'name': "Blue", 'value': 3},
  {'name': "Sky Blue", 'value': 4},
  {'name': "Gold", 'value': 5},
  {'name': "Green", 'value': 6},
  {'name': "Pink", 'value': 7},
  {'name': "Purple", 'value': 8},
  {'name': "Red", 'value': 9},
  {'name': "Rose Gold", 'value': 10},
  {'name': "Starlight", 'value': 11},
  {'name': "Please select the product before choosing a color.", 'value': 12}
]

async def color_gen(ctx: ui.AutocompleteInteraction):
  product_chosen = list(filter(lambda x: x['name'] == 'product', ctx.data['options']))
  product_chosen = product_chosen[0] if product_chosen else None
  if not product_chosen:
    return [colors[12]]
  elif product_chosen['value'].startswith("P"):
    return [colors[0]]
  else:
    return [colors[x] for x in product_colors[product_chosen['value']]]


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
  apod = botnasa()
  await ctx.reply(apod[0])
  if apod[1]:
    await ctx.send(file= discord.File("apod.txt"))
  try_delete("apod.txt")

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

@bs.command(name="engrave", description="Engraves a piece of text on an Apple product.", options=[
           ui.SlashOption(name="Product", description= "The product to engrave on.", type=str,
           required=True, choices=products), ui.SlashOption(name= "Color",
           description="The color of the product. Choices are based on the product.", type=int,
           required=True, choices=colors, choice_generator=color_gen), ui.SlashOption(name="Line_1",
           description="The first line to engrave.", type=str, required=True), ui.SlashOption(name=
           "Line_2", description="The second line to engrave. Applicable for iPads and iPods only."
           , type=str, required=False)])
async def engrave_(ctx: ui.SlashInteraction, product, color, line_1, line_2 = None):
  line_1 = urlescape(line_1, safe='')
  if product.startswith("P"):
    desc = f"https://www.apple.com/shop/preview/engrave/{product}/A?th={line_1}&s=2&f=mixed"
  else:
    product = product_codes[f"{product}{color}"]
    if line_2:
      line_2 = urlescape(line_2, safe='')
      desc = f"https://www.apple.com/shop/preview/v2/engrave/{product}/A?th={line_1}&s=2"
    else:
      desc = f"https://www.apple.com/shop/preview/v2/engrave/{product}/A?th={line_1}&tl={line_2}&s=2"
  await ctx.respond(desc)

@bs.command(name= "nasa_apod", description= "Shows NASA's Astronomy Picture Of the Day.")
async def nasa_apod(ctx: ui.SlashInteraction):
  apod = botnasa()
  await ctx.respond(apod[0])
  if apod[1]:
    await ctx.send(file= discord.File("apod.txt"))
  try_delete("apod.txt")

@bs.command(name= "trivia", description= "Shows up to 3 trivia questions.", options=[
           ui.SlashOption(name= "Number", type= int, required= False, min_value= 1, max_value= 3,
           description= "The no. of questions to show, between 1 and 3 inclusive. Defaults to 1.")])
async def trivia_(ctx: ui.SlashInteraction, number: int = 1):
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
  r = requests.get("https://api.nasa.gov/planetary/apod?api_key=7wF7KVXkmapwOlTkTt6i6dp9p3ismZLJHeP0OSFp").json()
  hd_str = f"\nHigh-Definition: {r['hdurl']}" if r.get('hdurl', None) else ""
  desc = f"**{r['title']}**\nStandard-Definition: {r['url']}{hd_str}\n\n{r['explanation']}"
  file = False
  if len(desc) > 1024:
    f = open("apod.txt", "w")
    hd_str = f"\n{r['hdurl']}" if r.get('hdurl', None) else ""
    f.write(f"{r['title']}\n{r['url']}{hd_str}\n\n{text_wrapper.fill(r['explanation'])}")
    f.close()
    file = True
  return [trim(desc, 1024), file]

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
