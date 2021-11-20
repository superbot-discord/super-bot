from shared import *
import html
import csv

uvi_pattern = re.compile(r'\d{8}(\d{2})(\d{2})')
uvi_pattern_= r'\1:\2'

@commands.command()
async def hk_forecast(ctx, *, disposed=None):
  await ctx.channel.trigger_typing()
  r1=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=en").json()
  r2=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=tc").json()
  embed = discord.Embed(title="HKO Forecast", description=f"{r1['generalSituation']}\n{r2['generalSituation']}")
  for d, d2 in zip(r1['weatherForecast'], r2['weatherForecast']):
    embed.add_field(name=f"{d['week']}", value=f"""{d['forecastWeather']} {d2['forecastWeather']}\nTemperature: {d['forecastMintemp']['value']}°C ~ {d['forecastMaxtemp']['value']}°C
    Humidity: {d['forecastMinrh']['value']}% ~ {d['forecastMaxrh']['value']}%\n{d['PSR']} probability of significant rain\nWind: {d['forecastWind']} {d2['forecastWind']}""", inline=False)
  f0v = f"Sea temperature at {r1['seaTemp']['place']}: {r1['seaTemp']['value']}°C\n"
  for r in r1['soilTemp']:
    f0v += f"Soil temperature at {r['place']} ({r['depth']['value']}m deep): {r['value']}°C\n"
  embed.add_field(name="Extra Information", value=f0v)
  await ctx.reply(embed=embed)
  await ctx.channel.trigger_typing()
  plt.rcdefaults()
  fig, (ax, ax2) = plt.subplots(2, 1)
  labels = [x['week'][0:3] for x in r1['weatherForecast']]
  labels[7], labels[8] = f"{labels[7]} 2", f"{labels[8]} 2"
  numlist_lt = [x['forecastMintemp']['value'] for x in r1['weatherForecast']]
  numlist_ht = [x['forecastMaxtemp']['value'] for x in r1['weatherForecast']]
  ax.plot(labels, numlist_lt, label="Minimum", color="#008FFF", marker="x")
  ax.plot(labels, numlist_ht, label="Maximum", color="#FF8F00", marker="x")
  ax2.set_ylim(0, 100)
  numlist_lh = [x['forecastMinrh']['value'] for x in r1['weatherForecast']]
  numlist_hh = [x['forecastMaxrh']['value'] for x in r1['weatherForecast']]
  ax2.plot(labels, numlist_lh, label="Minimum", color="#003CFF", marker=".")
  ax2.plot(labels, numlist_hh, label="Maximum", color="#FF3C00", marker=".")
  for count in ['top', 'bottom', 'left', 'right']:
    ax.spines[count].set_color("w")
    ax2.spines[count].set_color("w")
  ax.tick_params(axis='both', colors='w')
  ax.legend(title="Temp. (°C)")
  ax2.tick_params(axis='both', colors='w')
  ax2.legend(title="Humidity (%)")
  plt.savefig("forecast.png", transparent=True)
  plt.savefig("forecast.svg", transparent=True)
  plt.clf()
  await ctx.reply(files=[discord.File("forecast.png"), discord.File("forecast.svg")])
  try_delete('forecast.png', 'forecast.svg')

@commands.command()
async def hk_tide(ctx, *, disposed=None):
  await ctx.channel.trigger_typing()
  r=requests.get("https://data.weather.gov.hk/weatherAPI/hko_data/tide/ALL_en.csv")
  tide=r.content.decode("utf-8")[1:]
  reader = csv.DictReader(tide.splitlines())
  tides = [x for x in reader]
  embed = discord.Embed(title="HKO Tide Information", description=f"Information updated at {tides[0]['Time']} HKT (Update frequency: 5 minutes)")
  for t in tides:
    embed.add_field(name=t['Tide Station'], value=f"{t['Height(m)']} m", inline=True)
  await ctx.reply(embed=embed)

@commands.command()
async def hk_weather(ctx, *, disposed=None):
  await ctx.channel.trigger_typing()
  r1=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en").json()
  r2=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=tc").json()
  r3=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=en").json()
  r4=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=tc").json()
  r5=requests.get("https://data.weather.gov.hk/weatherAPI/hko_data/regional-weather/latest_15min_uvindex.csv")
  desc = f"{r3['generalSituation']} {r4['generalSituation']}\n{r3['forecastPeriod']}: {r3['forecastDesc']}\n{r4['forecastPeriod']}: {r4['forecastDesc']}\n{r3['outlook']} {r4['outlook']}"
  uvi_raw=r5.content.decode("utf-8")[:-1]
  reader = csv.DictReader(uvi_raw.splitlines())
  uvi = [x for x in reader]
  for u in uvi:
    desc += f"UV Index at \n{re.sub(uvi_pattern, uvi_pattern_, u['Date'])}: {u['past 15-minute mean UV Index']} (Update frequency: 15 minutes)"
  for count in ['warningMessage', 'mintempFrom00To09', 'rainfallFrom00To12']:
    if r1[count]:
      desc += f"{r1[count]} {r2[count]}\n"
  embed = discord.Embed(title="HKO Weather Information", description=desc)
  rain_dict = {html.unescape(f"{x1['place']} {x2['place']}"): y for x1, x2, y in zip(r1['rainfall']['data']   , r2['rainfall']['data']   , range(0, 18))}
  temp_dict = {html.unescape(f"{x1['place']} {x2['place']}"): y for x1, x2, y in zip(r1['temperature']['data'], r2['temperature']['data'], range(0, 27))}
  places_list = list(set(list(rain_dict) + list(temp_dict)))
  places_list.sort()
  for count in places_list:
    fv =  f"Rainfall: {r1['rainfall']['data']   [rain_dict[count]]['max']} mm\n"   if count in list(rain_dict) else ""
    fv += f"Temperature: {r1['temperature']['data'][temp_dict[count]]['value']}°C" if count in list(temp_dict) else ""
    embed.add_field(name=count, value=fv, inline=True)
  embed.add_field(name="Extra Information", value=f"""UV Index: {r1['uvindex']['data'][0]['value']} ({r1['uvindex']['data'][0]['desc']}) at {r1['uvindex']['data'][0]['place']}
  Humidity: {r1['humidity']['data'][0]['value']}% at {r1['humidity']['data'][0]['place']}""")
  embed.set_image(url=f"https://www.hko.gov.hk/images/HKOWxIconOutline/pic{r1['icon'][0]}.png")
  await ctx.reply(embed=embed)

@commands.command()
async def uk_extremes(ctx, *, disposed=None):
  r=requests.get("http://datapoint.metoffice.gov.uk/public/data/txt/wxobs/ukextremes/json/latest?key=69eba5b0-9c89-4198-b973-b4576f60f0f5").json()

def setup(bot):
  bot.add_command(hk_forecast)
  bot.add_command(hk_tide)
  bot.add_command(hk_weather)