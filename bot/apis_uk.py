import html
from shared import *

uke_dict = {'H':"Highest ", 'L':"Lowest ", 'MIN':"min ", 'MAX':"max "}

@commands.command()
async def uk_aqi(ctx, *, disposed= None):
  r=requests.get("https://api.tfl.gov.uk/AirQuality/").json()
  embed = discord.Embed(title="UK Air Quality Indices")
  embed.set_footer(text=r['disclaimerText'])
  for r_ in r['currentForecast']:
    fv = f"\n{r_['nO2Band']} NO₂ (Nitrogen Dioxide)\n{r_['o3']} O₃ (Ozone)\n{r_['sO2Band']} SO₂ (Sulphur Dioxide)\n{r_['pM25Band']} PM₂.₅ (Fine Particles patter){r_['pM10Band']} PM₁₀ (Coarse Particulate Matter)"
    embed.add_field(name=f"{r_['forecastType']}: {r_['forecastBand']}", value=html.unescape(r_['forecastText'].replace("&lt;br/&gt;", " "))+fv)
  await ctx.reply(embed=embed)

@commands.command()
async def uk_extremes(ctx, *, disposed= None):
  r=requests.get("http://datapoint.metoffice.gov.uk/public/data/txt/wxobs/ukextremes/json/latest?key=69eba5b0-9c89-4198-b973-b4576f60f0f5").json()['UkExtremes']['Regions']['Region']
  embed = discord.Embed(title="UK Extremes")
  for r_ in r:
    x = r_['Extremes']['Extreme']
    fv = ""
    for x_ in x:
      fv += f"Longest sun hours" if x_['type']=='HSUN' else "Highest rainfall " if x_['type']=='HRAIN' else f"{uke_dict[x_['type'][0]]}{uke_dict[x_['type'][1:4]]} temp"
      fv += f": {x_['$']} " + ("°C" if 'T' in x_['type'] else "mm" if 'RAIN' in x_['type'] else "hours") + f"\n"
    embed.add_field(name=r_['name'].replace("South East", "SE").replace(",", ", "), value=fv)
  await ctx.reply(embed=embed)

def setup(bot):
  bot.add_command(uk_aqi)
  bot.add_command(uk_extremes)
