from shared import *

uke_dict = {'H':"Highest ", 'L':"Lowest ", 'MIN':"min ", 'MAX':"max "}

@commands.command()
async def uk_extremes(ctx, *, disposed=None):
  r=requests.get("http://datapoint.metoffice.gov.uk/public/data/txt/wxobs/ukextremes/json/latest?key=69eba5b0-9c89-4198-b973-b4576f60f0f5").json()['UkExtremes']['Regions']['Region']
  embed = discord.Embed(title="UK Extremes")
  for r_ in r:
    x = r_['Extremes']['Extreme']
    fv = ""
    for x_ in x:
      fv += f"Longest sun hours" if x_['type']=='HSUN' else "Highest rainfall " if x_['type']=='HRAIN' else f"{uke_dict[x_['type'][0]]}{uke_dict[x_['type'][1:4]]} temp."
      fv += f": {x_['$']} " + ("°C" if 'T' in x_['type'] else "mm" if 'RAIN' in x_['type'] else "hours") + f"\n"
    embed.add_field(name=r_['name'], value=fv)
  await ctx.reply(embed=embed)

def setup(bot):
  bot.add_command(uk_extremes)
