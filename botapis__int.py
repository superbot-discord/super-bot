from shared import *
exchange_currencies = typing.Literal[tuple(db['currencies'])]

@commands.command()
async def exchange(ctx, currency:exchange_currencies="USD", amount:int=1, *, disposed=None):
  r=requests.get(f"https://api.exchangerate.host/latest?base={currency}&amount={amount}").json()['rates']
  desc = ""
  for x, y in r.values():
    desc += f"**{x}**: {y}\n"
  embed = discord.Embed(title=f"{amount} {currency} is equal to…", description=desc)
  await ctx.reply(embed=embed)

def setup(bot):
  bot.add_command(exchange)