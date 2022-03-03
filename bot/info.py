import calendar
import pytz
import signal
import statistics
from _bot import bs
from functions import enum_list
from shared import (BeautifulSoup, commands, datetime, discord, Embed, Image, ImageDraw, ImageFont,
                    json, math, re, requests, timedelta, try_delete, ui)


hexstring_pattern = re.compile(r'#?([0-9A-F]{2})([0-9A-F]{2})([0-9A-F]{2})', re.IGNORECASE)
rgbtoper = lambda input: f"{round(input/0.0255)/100}%"
whitney = ImageFont.truetype("fonts/whitney.otf", 55)
cal = calendar.TextCalendar()
cal.firstweekday = 6
months_choices = [{'name': x, 'value': y} for x, y in zip(calendar.month_name, range(12))][1:]
weekdays_choices = [
  {'name': "Saturday", 'value': 5},
  {'name': "Sunday", 'value': 6},
  {'name': "Monday", 'value': 0}
]
mobile_choices = [
  {'name': "Default", 'value': 3},
  {'name': "Mobile-friendly", 'value': 1}
]
cur_year = datetime.now().year


calc_buttons_1 = [
  ui.Button(color='red', custom_id="c", label="AC"),
  ui.Button(color='red', custom_id="d", label="del"),
  ui.Button(color='green', custom_id="(", label="("),
  ui.Button(color='green', custom_id=")", label=")"),
  ui.Button(color='green', custom_id="*", label="×"),

  ui.Button(color='grey', custom_id="p", label="Sci", new_line=True),
  ui.Button(color='blurple', custom_id="7", label="7"),
  ui.Button(color='blurple', custom_id="8", label="8"),
  ui.Button(color='blurple', custom_id="9", label="9"),
  ui.Button(color='green', custom_id="/", label="/"),

  ui.Button(color='green', custom_id="r", label="√(", new_line=True),
  ui.Button(color='blurple', custom_id="4", label="4"),
  ui.Button(color='blurple', custom_id="5", label="5"),
  ui.Button(color='blurple', custom_id="6", label="6"),
  ui.Button(color='green', custom_id="-", label="-"),

  ui.Button(color='green', custom_id="x", label="^(", new_line=True),
  ui.Button(color='blurple', custom_id="1", label="1"),
  ui.Button(color='blurple', custom_id="2", label="2"),
  ui.Button(color='blurple', custom_id="3", label="3"),
  ui.Button(color='green', custom_id="+", label="+"),

  ui.Button(color='grey', custom_id="E", label="e", new_line=True),
  ui.Button(color='grey', custom_id="P", label="π"),
  ui.Button(color='blurple', custom_id="0", label="0"),
  ui.Button(color='blurple', custom_id=".", label="."),
  ui.Button(color='green', custom_id="=", label="="),
]

calc_buttons_sci = [
  ui.Button(color='red', custom_id="c", label="AC"),
  ui.Button(color='red', custom_id="d", label="del"),
  ui.Button(color='green', custom_id="(", label="("),
  ui.Button(color='green', custom_id=")", label=")"),
  ui.Button(color='green', custom_id="*", label="×"),

  ui.Button(color='grey', custom_id="p", label="Back", new_line=True),
  ui.Button(color='green', custom_id="si", label="sin"),
  ui.Button(color='green', custom_id="co", label="cos"),
  ui.Button(color='green', custom_id="ta", label="tan"),
  ui.Button(color='green', custom_id="/", label="/"),

  ui.Button(color='green', custom_id="r", label="√(", new_line=True),
  ui.Button(color='green', custom_id="%", label="mod"),
  ui.Button(color='green', custom_id="npr", label="nPr"),
  ui.Button(color='green', custom_id="ncr", label="nCr"),
  ui.Button(color='green', custom_id="-", label="-"),

  ui.Button(color='green', custom_id="x", label="^(", new_line=True),
  ui.Button(color='green', custom_id="!", label="!"),
  ui.Button(color='green', custom_id="l", label="ln"),
  ui.Button(color='green', custom_id="L", label="log"),
  ui.Button(color='green', custom_id="+", label="+"),

  ui.Button(color='grey', custom_id="E", label="e", new_line=True),
  ui.Button(color='grey', custom_id="P", label="π"),
  ui.Button(color='grey', custom_id="T", label="τ"),
  ui.Button(color='green', custom_id=",", label=","),
  ui.Button(color='green', custom_id="=", label="="),
]

calc_buttons_sci_ = [
  ui.Button(color='red', custom_id="c", label="AC"),
  ui.Button(color='red', custom_id="d", label="del"),
  ui.Button(color='green', custom_id="(", label="("),
  ui.Button(color='green', custom_id=")", label=")"),
  ui.Button(color='green', custom_id="*", label="×"),

  ui.Button(color='grey', custom_id="p", label="Back", new_line=True),
  ui.Button(color='green', custom_id="si", label="sin"),
  ui.Button(color='green', custom_id="co", label="cos"),
  ui.Button(color='green', custom_id="ta", label="tan"),
  ui.Button(color='green', custom_id="/", label="/"),

  ui.Button(color='green', custom_id="r", label="√(", new_line=True),
  ui.Button(color='green', custom_id="%", label="mod"),
  ui.Button(color='green', custom_id="npr", label="nPr"),
  ui.Button(color='green', custom_id="ncr", label="nCr"),
  ui.Button(color='green', custom_id="-", label="-"),

  ui.Button(color='green', custom_id="x", label="^(", new_line=True),
  ui.Button(color='green', custom_id="!", label="!"),
  ui.Button(color='green', custom_id="l", label="ln"),
  ui.Button(color='green', custom_id="L", label="log"),
  ui.Button(color='green', custom_id="+", label="+"),

  ui.Button(color='grey', custom_id="E", label="e", new_line=True),
  ui.Button(color='grey', custom_id="P", label="π"),
  ui.Button(color='grey', custom_id="T", label="τ"),
  ui.Button(color='green', custom_id=",", label=",", disabled=True),
  ui.Button(color='green', custom_id="=", label="="),
]

calc_parenthesis = [
  "(", "math.sin(", "math.cos(", "math.tan(", "math.factorial(", "math.log(", "math.log10(",
  "math.sqrt(", "math.perm(", "math.comb("]

def sig_handler(signum, frame):
  raise Exception("Time exceeded")
signal.signal(signal.SIGALRM, sig_handler)

class CalcL(ui.listener.Listener):
  def __init__(self, user_id):
    self.target_users = [user_id]
    self.exp = []
    self.disp = []
    self.scientific = False # F: Normal   T: Scientific
    self.comma = False
    self.wait_comma = False
    self.just_evaled = False
    self.result = "Use = to calculate"
  
  async def update(self, ctx: ui.ButtonInteraction):
    try:
      await ctx.respond(ninja_mode=True)
    except discord.errors.HTTPException:
      pass
    if self.scientific:
      if self.wait_comma and not self.comma:
        self.comma = True
        await ctx.message.edit(f"```\n{''.join(self.disp)}\n{self.result}```", components=calc_buttons_sci)
        return
      elif not self.wait_comma and self.comma:
        self.comma = False
        await ctx.message.edit(f"```\n{''.join(self.disp)}\n{self.result}```", components=calc_buttons_sci_)
        return
    await ctx.message.edit(f"```\n{''.join(self.disp)}\n{self.result}```")
  
  async def concat(self, ctx: ui.ButtonInteraction, e, d=None):
    if len(self.exp) >= 200:
      await ctx.respond("Maximum expression length reached!", hidden=True)
      return
    if self.just_evaled:
        self.exp = [e]
        self.disp = [d if d else e]
        self.just_evaled = False
    else:
      self.exp.append(e)
      self.disp.append(d if d else e)
    await self.update(ctx)

  @ui.Listener.button(custom_id="c")
  async def s1(self, ctx: ui.ButtonInteraction):
    self.exp = []
    self.disp = []
    self.result = "Use = to calculate"
    await self.update(ctx)

  @ui.Listener.button(custom_id="d")
  async def s2(self, ctx: ui.ButtonInteraction):
    self.exp = self.exp[:-1]
    self.disp = self.disp[:-1]
    await self.update(ctx)

  @ui.Listener.button(custom_id="=")
  async def s3(self, ctx: ui.ButtonInteraction):
    await ctx.respond(ninja_mode=True)
    self.calc = lambda e: eval("".join(e))
    cl = 0
    op = 0
    for x in self.exp:
      if x in calc_parenthesis:
        op += 1
      elif x == ")":
        cl += 1
    if op > cl:
      self.exp.extend([")"] * (op - cl))
    signal.alarm(3)
    try:
      self.result = self.calc(self.exp)
    except SyntaxError:
      self.result = "Error"
    except ZeroDivisionError:
      self.result = "Can't divide by zero"
    except ValueError:
      self.result = "Incorrect argument"
    except Exception:
      self.result = "Timed out"
    finally:
      signal.alarm(0)
    if self.result not in ["Error", "Timed out"]:
      self.just_evaled = True
    await self.update(ctx)

  @ui.Listener.button(custom_id="p")
  async def s4(self, ctx: ui.ButtonInteraction):
    await ctx.respond(ninja_mode=True)
    self.scientific = not self.scientific
    await ctx.message.edit(components=(calc_buttons_sci if self.comma else calc_buttons_sci_) if self.scientific else calc_buttons_1)

  @ui.Listener.button(custom_id="si")
  async def f1(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "math.sin(", "sin(")

  @ui.Listener.button(custom_id="co")
  async def f2(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "math.cos(", "cos(")

  @ui.Listener.button(custom_id="ta")
  async def f3(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "math.tan(", "tan(")

  @ui.Listener.button(custom_id="npr")
  async def f4(self, ctx: ui.ButtonInteraction):
    self.wait_comma = True
    await self.concat(ctx, "math.perm(", "npr(")
  
  @ui.Listener.button(custom_id="ncr")
  async def f5(self, ctx: ui.ButtonInteraction):
    self.wait_comma = True
    await self.concat(ctx, "math.comb(", "ncr(")
  
  @ui.Listener.button(custom_id="!")
  async def f6(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "math.factorial(", "factorial(")

  @ui.Listener.button(custom_id="l")
  async def f7(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "math.log(", "ln(")

  @ui.Listener.button(custom_id="L")
  async def f8(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "math.log10(", "log(")

  @ui.Listener.button(custom_id="0")
  async def n0(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "0")

  @ui.Listener.button(custom_id="1")
  async def n1(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "1")

  @ui.Listener.button(custom_id="2")
  async def n2(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "2")

  @ui.Listener.button(custom_id="3")
  async def n3(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "3")

  @ui.Listener.button(custom_id="4")
  async def n4(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "4")

  @ui.Listener.button(custom_id="5")
  async def n5(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "5")

  @ui.Listener.button(custom_id="6")
  async def n6(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "6")

  @ui.Listener.button(custom_id="7")
  async def n7(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "7")

  @ui.Listener.button(custom_id="8")
  async def n8(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "8")

  @ui.Listener.button(custom_id="9")
  async def n9(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "9")

  @ui.Listener.button(custom_id=".")
  async def n10(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, ".")

  @ui.Listener.button(custom_id="+")
  async def e0(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "+")

  @ui.Listener.button(custom_id="-")
  async def e1(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "-")

  @ui.Listener.button(custom_id="*")
  async def e2(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "*", "×")

  @ui.Listener.button(custom_id="/")
  async def e3(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "/", "÷")

  @ui.Listener.button(custom_id="%")
  async def e4(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "%")

  @ui.Listener.button(custom_id="(")
  async def e5(self, ctx: ui.ButtonInteraction):
    if self.exp[-1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      await self.concat(ctx, "*", "×")
    await self.concat(ctx, "(")

  @ui.Listener.button(custom_id=")")
  async def e6(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, ")")

  @ui.Listener.button(custom_id=",")
  async def e7(self, ctx: ui.ButtonInteraction):
    self.wait_comma = False
    await self.concat(ctx, ",")

  @ui.Listener.button(custom_id="r")
  async def e8(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "math.sqrt(", "√(")

  @ui.Listener.button(custom_id="x")
  async def e9(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "**(", "^(")

  @ui.Listener.button(custom_id="E")
  async def c1(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "math.e", "e")

  @ui.Listener.button(custom_id="P")
  async def c2(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "math.pi", "π")

  @ui.Listener.button(custom_id="τ")
  async def c3(self, ctx: ui.ButtonInteraction):
    await self.concat(ctx, "math.tau", "τ")
  
  @ui.Listener.wrong_user()
  async def wrong_user(self, ctx):
    await ctx.respond("Please use `/calculator` on your own.", hidden=True)


f = open('./assets/database_periodic.json', 'r')
pdb = json.loads(f.read())['elements']
f.close()


@bs.command(name="calculator", description="Opens a calculator with conventional and scientific functions.")
async def calculator(ctx: ui.SlashInteraction):
  await ctx.respond(components=calc_buttons_1, listener=CalcL(ctx.author.id))


@bs.command(name="calendar", description="Views a monthly or yearly calendar.", options=[
           ui.SlashOption(name="Year", description="The year of the calendar. Defaults to the current year.",
           type=int, required=False), ui.SlashOption(name="Month",
           description="The month of the calendar. Defaults to all months.", type=int,
           required=False, choices=months_choices), ui.SlashOption(name="First Day",
           description="The first day of a week. Defaults to Sunday.", type=int, required=False,
           choices=weekdays_choices), ui.SlashOption(name="Mode",
           description="The mode to use. Decides the number of months shown per row.", type=int,
           required=False, choices=mobile_choices)])
async def calendar(ctx: ui.SlashInteraction, year=cur_year, month=None, first_day=6, mode=3):
  cal.firstweekday = first_day
  if month:
    desc = cal.formatmonth(year, month, 2, 1)
  else:
    desc = cal.formatyear(year, 2, 1, 3, mode)
  await ctx.respond(f"```{desc}```")


@commands.command(aliases=["colour"])
async def color(ctx, *, name):
  colors = re.split(',|\s|;|/|\||\\|&', name)
  match = hexstring_pattern.fullmatch(colors[0])
  if all(arg and arg.isdigit() and 0 <= int(arg) < 256 for arg in colors) and len(colors)>2:
    r, g, b = map(int, colors)
  elif colors[0].isdigit() and 0 <= int(colors[0]) < 2 ** 24:
    n = int(colors[0])
    r, g, b = n >> 16, (n >> 8) & 255, n & 255
  elif match:
    r, g, b = (int(val, 16) for val in match.groups())
  else:
    await ctx.reply("Please specify a correct colour value.")
    return
  r1, g1, b1 = (rgbtoper(r), rgbtoper(g), rgbtoper(b))
  deci = (r << 16) + (g << 8) + b
  hex_ = f'{deci:02x}'.upper()
  if len(hex_) != 6:
    while len(hex_) < 6:
      hex_="0"+hex_
  page = requests.get(f"https://www.colorhexa.com/{hex_}")
  soup = BeautifulSoup(page.content, 'html.parser')
  result1 = soup.find(id= 'header-title')
  ti = re.sub(r'([\w]+?) \/ #[\da-f]{6} hex color',r'\1',result1.text)
  result2 = soup.find_all("strong")[2].text
  embed = Embed(title=f"Colour information: {ti}", description=result2, color=deci)
  embed.add_field(name="RGB", value=f"{r}, {g}, {b}\n{r1}, {g1}, {b1}", inline= True)
  embed.add_field(name="Hex Code", value=f"#{hex_}", inline= True)
  embed.add_field(name="Decimal Value", value=deci, inline= True)
  embed.set_thumbnail(url="attachment://color.png")
  img = Image.new('RGB', (64, 64), (r, g, b))
  img.save('color.png')
  await ctx.reply(embed=embed, file=discord.File('color.png'))
  try_delete('color.png')


@bs.command(name="element", description="Views information about a chemical element.", options=[
           ui.SlashOption(name="Query", description="The number, symbol or part of name of the element.",
           type=str, required=True)])
async def element_(ctx: ui.SlashInteraction, query):
  query = query.lower()
  if len(query) > 2:
    pdb_ = list(filter(lambda x: query in x['name'].lower() or query == str(x['number']) or query in x['symbol'].lower(), pdb))
  else:
    pdb_ = list(filter(lambda x: query == str(x['number']) or query == x['symbol'].lower(), pdb))
  if not len(pdb_):
    await ctx.respond("No elements could be found!")
    return
  if len(pdb_) == 1:
    element_ = pdb_[0]
    desc = f"{element_['category'].title()}\nGroup {element_['xpos']}, Period {element_['ypos']}\n{element_['summary']}"
    embed = Embed(title=f"{element_['name']} ({element_['number']} {element_['symbol']})", description=desc, url=element_['source'])
    embed.add_field(name="Atomic Mass", value= f"{element_['atomic_mass']} Dalton")
    embed.add_field(name="Melting Point", value=f"{element_['melt']} Kelvin")
    embed.add_field(name="Boiling Point", value=f"{element_['boil']} Kelvin")
    embed.add_field(name="Shells (inner first)", value=", ".join([str(x) for x in element_['shells']]))
    embed.add_field(name="STP Density", value=f"{element_['density']} g/L")
    embed.add_field(name="STP Phase", value=f"{element_['phase']}")
    cpk = element_['cpk-hex'] if element_['cpk-hex'] else "ffffff"
    img = Image.new('RGB', (128, 128), "#" + cpk)
    sum_ = sum([int(cpk[i:i+2], 16) for i in range(0, len(cpk), 2)])
    text_color = "#ffffff" if sum_ < 400 else "#000000"
    draw = ImageDraw.Draw(img)
    draw.text((64, 64), element_['symbol'], font=whitney, fill=text_color, align='center', anchor="mm")
    img.save('element.png')
    embed.set_thumbnail(url="attachment://element.png")
    for x, y in {"Appearance": 'appearance', "Discovered by": 'discovered_by', "Named after": 'named_by'}.items():
      if element_[y]:
        embed.add_field(name=x, value=element_[y])
    if element_['spectral_img']:
      embed.set_image(url=element_['spectral_img'])
    await ctx.respond(embed=embed, file=discord.File('element.png'))
    try_delete('element.png')
    return
  embed = Embed(title=f"Search results", description=enum_list([f"[**{x['number']}** {x['symbol']}: {x['name']}]({x['source']})" for x in pdb_], 4096, "\n"))
  await ctx.respond(embed=embed)


@commands.command() # Migrated
async def element(ctx, *, query):
  query = query.lower()
  if len(query) > 2:
    pdb_ = list(filter(lambda x: query in x['name'].lower() or query == str(x['number']) or query in x['symbol'].lower(), pdb))
  else:
    pdb_ = list(filter(lambda x: query == str(x['number']) or query == x['symbol'].lower(), pdb))
  if not len(pdb_):
    await ctx.reply("No elements could be found!")
    return
  if len(pdb_) == 1:
    element_ = pdb_[0]
    desc = f"{element_['category'].title()}\nGroup {element_['xpos']}, Period {element_['ypos']}\n{element_['summary']}"
    embed = Embed(title=f"{element_['name']} ({element_['number']} {element_['symbol']})", description=desc, url=element_['source'])
    embed.add_field(name="Atomic Mass", value= f"{element_['atomic_mass']} Dalton")
    embed.add_field(name="Melting Point", value=f"{element_['melt']} Kelvin")
    embed.add_field(name="Boiling Point", value=f"{element_['boil']} Kelvin")
    embed.add_field(name="Shells (inner first)", value=", ".join([str(x) for x in element_['shells']]))
    embed.add_field(name="STP Density", value=f"{element_['density']} g/L")
    embed.add_field(name="STP Phase", value=f"{element_['phase']}")
    cpk = element_['cpk-hex']
    img = Image.new('RGB', (64, 64), "#" + cpk)
    sum_ = sum([int(cpk[i:i+2], 16) for i in range(0, len(cpk), 2)])
    text_color = "#ffffff" if sum_ < 384 else "#000000"
    draw = ImageDraw.Draw(img)
    draw.text((32, 32), element_['symbol'], font=whitney, fill=text_color, align='center', anchor="mm")
    img.save('element.png')
    embed.set_thumbnail(url="attachment://element.png")
    for x, y in {"Appearance": 'appearance', "Discovered by": 'discovered_by', "Named after": 'named_by'}.items():
      if element_[y]:
        embed.add_field(name=x, value=element_[y])
    if element_['spectral_img']:
      embed.set_image(url=element_['spectral_img'])
    await ctx.reply(embed=embed, file=discord.File('element.png'))
    try_delete('element.png')
    return
  else:
    embed = Embed(title=f"Search results", description=enum_list([f"[**{x['number']}** {x['symbol']}: {x['name']}]({x['source']})" for x in pdb_], 4096, "\n"))
  await ctx.reply(embed=embed)


@bs.command(name="regex", description="Runs a regex search on a piece of text.", options=[
           ui.SlashOption(name="Regular Expression", description="The regex to search for.",
           type=str, required=True), ui.SlashOption(name="Text", description="The text to search in.",
           type=str, required=True)])
async def regex_(ctx, regular_expression, *, text):
  theregex = f"(?P<LargestCapturingGroup>{regular_expression})"
  newtext = re.sub(theregex, "**\g<LargestCapturingGroup>**", text)
  matches = len(re.findall(theregex, text))
  if matches == 1:
    ti = "There was 1 occurrence."
  elif matches == 0:
    ti = "There was no occurrences."
  elif matches >= 2:
    ti = f"There were {matches} occurrences."
  embed = Embed(title = ti, description = newtext.replace("****",""))
  embed.set_author(name=f"Match Results for {regular_expression}")
  embed.set_footer(text="Match Results are highlighted in bold")
  await ctx.reply(embed=embed)


@commands.command()
async def regsub(ctx, regular1, regular2, *, text):
  newtext = re.sub(regular1, regular2, text)
  matches = len(re.findall(regular1, text))
  if matches == 1:
    ti = "There was 1 occurrence."
  elif matches == 0:
    ti = "There was no occurrences."
  elif matches >= 2:
    ti = f"There were {matches} occurrences."
  embed = Embed(title = ti, description = f"`{newtext}`")
  embed.set_author(name=f"Substitution Result for {regular1}")
  await ctx.reply(embed=embed)


@commands.command()
async def stats(ctx, *numbers: int):
  numbers = list(numbers) if len(numbers) > 1 else [numbers]
  desc = f"Field\t\t\tValue\t\t\tExplanation\nArithmetic Mean\t\t{statistics.mean(numbers):<16}\t∑÷n\t\t\t\tAlso known as average\nGeometric Mean\t\t{statistics.geometric_mean(numbers):<16}\tⁿ√(∏)\t\t\t\tGood for handling exponents\nHarmonic Mean\t\t{statistics.harmonic_mean(numbers):<16}\tn÷(1÷a+1÷b+…)\t\t\tUsed to calculate the average speed of a trip\nMedian\t\t\t"
  desc += (f"{statistics.median(numbers):<16}" if statistics.median_high(numbers)==statistics.median_low(numbers) else f"{f'{statistics.median_low(numbers)} & {statistics.median_high(numbers)} → {statistics.median(numbers)}':<16}") + f"\tMiddle item of the data (average of the two items in the middle if there are an even number of items)\nVariance\t\t{statistics.variance(numbers):<16}\t((Mean-a)²+(Mean-b)²+…)÷n\tDeviation of the data; cannot be used directly\nStandard Deviation\t{statistics.stdev(numbers):<16}\t√(Variance)\t\t\tDeviation of the data; in large data sets, ~68% will be within Mean±Standard-Deviation"
  desc += f"\nVariance*\t\t{statistics.pvariance(numbers):<16}\t((Mean-a)²+(Mean-b)²+…)÷(n-1)\tDeviation of the data; cannot be used directly\nStandard Deviation*\t{statistics.stdev(numbers):<16}\t√(Variance*)\t\t\tDeviation of the data; in large data sets, ~68% will be within Mean±Standard-Deviation\n\n*In Variance* and SD*, the sum of squares is divided by n-1 instead of n. This method (Bessel's correction) is used when the data is a small selection (sample) of the large data set (population)."
  f=open("statistics.txt", "w")
  f.write(desc)
  f.close()
  await ctx.send(file=discord.File('statistics.txt'))
  try_delete('statistics.txt')


@commands.command()
async def time(ctx, *, timezoneinput="0"):
  if timezoneinput.replace(".","").isnumeric():
    timezone=float(timezoneinput)
    if 15>timezone>-15 and timezone%0.25==0:
      tnow = datetime.now() + timedelta(minutes = int(timezone*60))
      await ctx.reply(f"Time in UTC {timezoneinput} is {tnow.strftime('%d %B %Y (%A), %H:%M:%S')}")
    else:
      return "Invalid timezone! Timezone must be below 15, above -15 and divisible by 0.25."
  elif timezoneinput=="all":
    desc = f"**[ISO 3166 Country Codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements)**:\n```AD AE AF AG AI AL AM AO AQ AR AS AT AU AW AX AZ BA BB BD BE BF BG BH BI BJ BL BM BN BO BQ BR BS BT BV BW BY BZ CA CC CD CF CG CH CI CK CL CM CN CO CR CU CV CW CX CY CZ DE DJ DK DM DO DZ EC EE EG EH ER ES ET FI FJ FK FM FO FR GA GB GD GE GF GG GH GI GL GM GN GP GQ GR GS GT GU GW GY HK HM HN HR HT HU ID IE IL IM IN IO IQ IR IS IT JE JM JO JP KE KG KH KI KM KN KP KR KW KY KZ LA LB LC LI LK LR LS LT LU LV LY MA MC MD ME MF MG MH MK ML MM MN MO MP MQ MR MS MT MU MV MW MX MY MZ NA NC NE NF NG NI NL NO NP NR NU NZ OM PA PE PF PG PH PK PL PM PN PR PS PT PW PY QA RE RO RS RU RW SA SB SC SD SE SG SH SI SJ SK SL SM SN SO SR SS ST SV SX SY SZ TC TD TF TG TH TJ TK TLa TM TN TO TR TT TV TW TZ UA UG UM US UY UZ VA VC VE VG VI VN VU WF WS YE YT ZA ZM ZW```\nIn addition, **[TZ Database Names](http://worldtimeapi.org/api/timezone.txt)** and **UTC Timezone Numbers** (between -15 and 15, divisible by 0.25) are supported."
    embed = Embed(title="All timezone formats supported", description=desc)
    await ctx.reply(embed=embed)
  elif len(timezoneinput)==2 and timezoneinput.isalpha():
    try:
      tz = pytz.timezone(pytz.country_timezones[timezoneinput][0])
      await ctx.reply(f"Time in {pytz.country_timezones(timezoneinput)[0]} is {datetime.now(tz=tz).strftime('%d %B %Y (%A), %H:%M:%S')}")
    except:
      await ctx.reply("Timezone not found. Please use `=time all` for a list of all timezones.")
  else:
    try:
      tz = pytz.timezone(timezoneinput)
      await ctx.reply(f"Time in {timezoneinput} is {datetime.now(tz=tz).strftime('%d %B %Y (%A), %H:%M:%S')}")
    except:
      await ctx.reply("Timezone not found. Please use `=time all` for a list of all timezones.")


def setup(bot):
  bot.add_command(color)
  bot.add_command(element)
  bot.add_command(regsub)
  bot.add_command(stats)
  bot.add_command(time)
