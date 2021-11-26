from shared import *

f = open('units.json', 'r')
udb = json.loads(f.read())
f.close()

exchange_currencies = typing.Literal[tuple(db['currencies'])]
length_units = typing.Literal[tuple()]

@commands.command()
async def convert(ctx, num: typing.Optional[int] = 1, unit : str = "m"):
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
  embed = discord.Embed(title=f"{num} {unit} is equal to…", description=desc)
  await ctx.reply(embed=embed)

@commands.command()
async def exchange(ctx, currency:exchange_currencies="USD", amount:int=1, *, disposed=None):
  r=requests.get(f"https://api.exchangerate.host/latest?base={currency}&amount={amount}").json()['rates']
  desc = ""
  for x, y in r.items():
    desc += f"**{x}**: {y}\n"
  embed = discord.Embed(title=f"{amount} {currency} is equal to…", description=desc)
  await ctx.reply(embed=embed)

def setup(bot):
  bot.add_command(convert)
  bot.add_command(exchange)