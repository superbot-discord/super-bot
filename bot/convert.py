from decimal import Decimal, getcontext
from _bot import bs
from shared import commands, db, Embed, json, requests, typing, ui

f = open('./assets/units.json', 'r')
udb = json.loads(f.read())
f.close()

class ConvertLL(ui.listener.Listener):
  def __init__(self, embeds):
    self.embeds = embeds

  @ui.Listener.select(custom_id="convertl")
  async def convertl(self_, ctx: ui.SelectInteraction):
    await ctx.respond(embed=self_.embeds[ctx.selected_values[0]], hidden=True)

units_l = {x: y for z in udb['length'].values() for x, y in z.items()}
unit_l_choices = [{'name': x.title(), 'value': x} for x, y in units_l.items()]
unit_l_options = [ui.SelectOption(value=x, label=x) for x in udb['length'].keys()]
unit_select = ui.SelectMenu(placeholder="Scale", custom_id="convertl", options=unit_l_options)

def round_better(num, digits: int = 0):
  if isinstance(num, float):
    if num.is_integer():
      return int(num)
  elif isinstance(num, Decimal):
    if num == round(num):
      return num
  return round(num, digits)


exchange_currencies = typing.Literal[tuple(db['currencies'])] # type: ignore
length_units = typing.Literal[tuple(udb['lengthI'])] # type: ignore

@bs.command(name="convert_length", description="Converts between length units.", options=[
           ui.SlashOption(name="Source", description="The numerical part of the source.", type=int,
           required=True), ui.SlashOption(name= "Unit", description="The unit of the source.",
           type=str, required=True, choices=unit_l_choices), ui.SlashOption(name="Precision",
           description="Number of significant digits, between 1 and 25 inclusive. Defaults to 8.",
           type=int, required=False, min_value=1, max_value=25)])
async def convert_(ctx: ui.SlashInteraction, source, unit, precision=8):
  in_m = Decimal(source) * Decimal(units_l[unit])
  getcontext().prec = precision
  embeds = {x: Embed(title=f"{source} {unit} is equal to:", description=
            "\n".join([f"{in_m/Decimal(z)} {w}" for w, z in y.items()]))
            for x, y in udb['length'].items()}
  await ctx.respond("Select a scale to convert:", components=[unit_select], listener=
                    ConvertLL(embeds))

@commands.command()
async def convert(ctx, num: typing.Optional[int] = 1, unit: str = "m"):
  unit = unit.rstrip("es").rstrip("s").replace(" ", "")
  unit = unit.lower() if ("M" not in unit and "G" not in unit and "N" not in unit) else unit
  unit_ = None
  for x in ["length"]:
    if unit in udb[f"{x}I"].keys():
      unit_ = num*udb[f"{x}I"][unit]
      x_ = x
      break
  if not unit_:
    await ctx.reply("Invalid unit. Please try again.")
    return
  desc = ""
  units = udb[f"{x_}O"]
  for x, y in units.items():
    desc += f"**{x.title()}** {unit_/y}\n"
  embed = Embed(title=f"{num} {unit} is equal to…", description=desc)
  await ctx.reply(embed=embed)

@commands.command()
async def exchange(ctx, currency: exchange_currencies = "USD", amount: int = 1, *, disposed=None):
  r=requests.get(f"https://api.exchangerate.host/latest?base={currency}&amount={amount}").json()['rates']
  desc = ""
  for x, y in r.items():
    desc += f"**{x}**: {y}\n"
  embed = Embed(title=f"{amount} {currency} is equal to…", description=desc)
  await ctx.reply(embed= embed)

def setup(bot):
  bot.add_command(convert)
  bot.add_command(exchange)