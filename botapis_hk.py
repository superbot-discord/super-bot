from shared import *
import html
import csv

hko_dt_pattern = re.compile(r'\d{8}(\d{2})(\d{2})')
hko_dt_pattern_= r'\1:\2'
hko_dt_pattern2 =re.compile(r'\d{8}(\d{2})(\d{2})-\d{8}(\d{2})(\d{2})')
hko_dt_pattern2_=r'\1:\2~\3:\4'

fake_headers = {'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0"}
aqi_range1 = lambda min, max: min if min == max else f"{min}~{max}"
aqi_range2 = lambda min, max: min if min == max else f"{min} ~ {max}"

@commands.command()
async def hk_aqi(ctx, *, disposed=None):
  await ctx.channel.trigger_typing()
  r1=requests.get("https://ogciopsi.blob.core.windows.net/dataset/aqhi/aqhi.json").json()
  r2=requests.get("https://ogciopsi.blob.core.windows.net/dataset/aqhi/aqhi-forecast.json").json()
  r3=requests.get("https://dashboard.data.gov.hk/api/aqhi-individual?format=json", headers=fake_headers).json()
  embed = discord.Embed(title="HK OGCIO AQI Info", description=f"""**Current (All HK)**\nGeneral: {aqi_range1(r1[0]['aqhi_min'], r1[0]['aqhi_max'])} ({aqi_range2(r1[0]['health_risk_min'], r1[0]['health_risk_max'])})
  Roadside: {aqi_range1(r1[1]['aqhi_min'], r1[1]['aqhi_max'])} ({aqi_range2(r1[1]['health_risk_min'], r1[1]['health_risk_max'])})\n**Tomorrow (All HK) AM**
  General: {aqi_range2(r2[0]['health_risk_min'], r2[0]['health_risk_max'])}
  Roadside: {aqi_range2(r2[1]['health_risk_min'], r2[1]['health_risk_max'])}\n**Tomorrow (All HK) PM**
  General: {aqi_range2(r2[2]['health_risk_min'], r2[2]['health_risk_max'])}
  Roadside: {aqi_range2(r2[3]['health_risk_min'], r2[3]['health_risk_max'])}""")
  for a in r3:
    embed.add_field(name=a['station'], value=f"{a['aqhi']} ({a['health_risk']})")
  await ctx.reply(embed=embed)

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
async def hk_lightning(ctx, *, disposed=None):
  await ctx.channel.trigger_typing()
  r1=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/opendata.php?dataType=LHL&lang=en&rformat=csv")
  r2=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/opendata.php?dataType=LHL&lang=tc&rformat=csv")
  lightning=r1.content.decode("utf-8")[1:-1]
  reader = csv.DictReader(lightning.splitlines())
  lightnings = [x for x in reader]
  lightning_=r2.content.decode("utf-8")[1:-1]
  reader_ = csv.DictReader(lightning_.splitlines())
  lightnings_ = [x for x in reader_]
  embed = discord.Embed(title="HKO Lightning Information", description=f"Information within {re.sub(hko_dt_pattern2, hko_dt_pattern2_, lightnings[0]['DateTime'])} HKT (Update frequency: 1 hour)")
  for l, l2 in zip(lightnings, lightnings_):
    embed.add_field(name=f"{l['Region']}: {l['Type']}\n{l2['Region']}: {l2['Type']}", value=f"Lightnings: {l['lightning count']}", inline=True)
  await ctx.reply(embed=embed)

@commands.command()
async def hk_moon(ctx, *, disposed=None):
  await ctx.channel.trigger_typing()
  r=requests.get(f"https://data.weather.gov.hk/weatherAPI/opendata/opendata.php?dataType=MRS&year=2021&rformat=csv")
  sun =r.content.decode("utf-8")[1:-1]
  reader = csv.DictReader(sun.splitlines())
  current_day = int(datetime.now(tz=timezone(timedelta(hours=8))).strftime("%j"))
  moons = [x for x in reader][current_day-1:current_day+24]
  embed = discord.Embed(title="HKO Moon Information")
  embed.set_footer(text="""The owner has checked with the data source and it was not apparent why some data was empty (Maybe it was astronomically correct?)
  The same also happened to data in the data supplied for 2018~2023. Please do not contact the developers for information on that.""".replace(f"\n", ""))
  for m in moons:
    embed.add_field(name=m['YYYY-MM-DD'], value=f"Rise-Set: {m['RISE']} ~ {m['SET']}\nTransitional Period: {m['TRAN.']}")
  await ctx.reply(embed=embed)
  plt.rcdefaults()
  fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)
  dates = [datetime.strptime(x['YYYY-MM-DD'], "%Y-%m-%d") for x in moons]
  ax1_data = [datetime.strptime(x['RISE'],  "%H:%M") for x in moons]
  ax2_data = [datetime.strptime(x['TRAN.'], "%H:%M") for x in moons]
  ax3_data = [datetime.strptime(x['SET'],   "%H:%M") for x in moons]
  ax1.plot(dates, ax1_data, color="#FF7F00", marker="x")
  ax2.plot(dates, ax2_data, color="#FF2020", marker="x")
  ax3.plot(dates, ax3_data, color="#007FFF", marker="x")
  for ax in [ax1, ax2, ax3]:
    ax.xaxis.set_major_locator(mpl.dates.DayLocator(interval=2))
    ax.xaxis.set_minor_locator(mpl.dates.DayLocator())
    ax.xaxis.set_major_formatter(mpl.dates.DateFormatter("%m-%d"))
    ax.tick_params(axis='both', colors='w')
    for count in ['top', 'bottom', 'left', 'right']:
      ax.spines[count].set_color("w")
  ax1.yaxis.set_major_locator(mpl.dates.MinuteLocator(interval=2))
  ax1.yaxis.set_major_formatter(mpl.dates.DateFormatter("%H:%M"))
  ax2.yaxis.set_major_locator(mpl.dates.MinuteLocator(interval=2))
  ax2.yaxis.set_major_formatter(mpl.dates.DateFormatter("%H:%M"))
  ax3.yaxis.set_major_locator(mpl.dates.MinuteLocator(interval=1))
  ax3.yaxis.set_major_formatter(mpl.dates.DateFormatter("%H:%M"))
  plt.setp(ax3.get_xticklabels(), rotation=20, ha="right")
  plt.savefig("sun.png", transparent=True)
  plt.savefig("sun.svg", transparent=True)
  plt.clf()
  await ctx.reply(files=[discord.File("sun.png"), discord.File("sun.svg")])

@commands.command()
async def hk_sea_pressure(ctx, *, disposed=None):
  await ctx.channel.trigger_typing()
  r=requests.get("https://data.weather.gov.hk/weatherAPI/hko_data/regional-weather/latest_1min_pressure.csv")
  r1=requests.get("https://data.weather.gov.hk/weatherAPI/hko_data/regional-weather/latest_1min_pressure_uc.csv")
  pressure=r.content.decode("utf-8")[:-1]
  reader = csv.DictReader(pressure.splitlines())
  pressures = [x for x in reader]
  pressure_=r.content.decode("utf-8")[:-1]
  reader_ = csv.DictReader(pressure_.splitlines())
  pressures_ = [x for x in reader_]
  embed = discord.Embed(title="HKO Sea Pressure Information", description=f"Information updated at {re.sub(hko_dt_pattern, hko_dt_pattern_, pressures[0]['Date time'])} HKT (Update frequency: 10 minutes)")
  for p, p_ in zip(pressures, pressures_):
    embed.add_field(name=f"{p['Automatic Weather Station']} {p_['自動氣象站'].replace(' ', '')}", value=f"{p['Mean Sea Level Pressure(hPa)']} hPa", inline=True)
  await ctx.reply(embed=embed)

@commands.command()
async def hk_sun(ctx, *, disposed=None):
  await ctx.channel.trigger_typing()
  r=requests.get(f"https://data.weather.gov.hk/weatherAPI/opendata/opendata.php?dataType=SRS&year=2021&rformat=csv")
  sun =r.content.decode("utf-8")[1:-1]
  reader = csv.DictReader(sun.splitlines())
  current_day = int(datetime.now(tz=timezone(timedelta(hours=8))).strftime("%j"))
  suns = [x for x in reader][current_day-1:current_day+24]
  embed = discord.Embed(title="HKO Sun Information")
  for s in suns:
    embed.add_field(name=s['YYYY-MM-DD'], value=f"Rise-Set: {s['RISE']} ~ {s['SET']}\nTransitional Period: {s['TRAN.']}")
  await ctx.reply(embed=embed)
  plt.rcdefaults()
  fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)
  dates = [datetime.strptime(x['YYYY-MM-DD'], "%Y-%m-%d") for x in suns]
  ax1_data = [datetime.strptime(x['RISE'],  "%H:%M") for x in suns]
  ax2_data = [datetime.strptime(x['TRAN.'], "%H:%M") for x in suns]
  ax3_data = [datetime.strptime(x['SET'],   "%H:%M") for x in suns]
  ax1.plot(dates, ax1_data, color="#FF7F00", marker="x")
  ax2.plot(dates, ax2_data, color="#FF2020", marker="x")
  ax3.plot(dates, ax3_data, color="#007FFF", marker="x")
  for ax in [ax1, ax2, ax3]:
    ax.xaxis.set_major_locator(mpl.dates.DayLocator(interval=2))
    ax.xaxis.set_minor_locator(mpl.dates.DayLocator())
    ax.xaxis.set_major_formatter(mpl.dates.DateFormatter("%m-%d"))
    ax.tick_params(axis='both', colors='w')
    for count in ['top', 'bottom', 'left', 'right']:
      ax.spines[count].set_color("w")
  ax1.yaxis.set_major_locator(mpl.dates.MinuteLocator(interval=2))
  ax1.yaxis.set_major_formatter(mpl.dates.DateFormatter("%H:%M"))
  ax2.yaxis.set_major_locator(mpl.dates.MinuteLocator(interval=2))
  ax2.yaxis.set_major_formatter(mpl.dates.DateFormatter("%H:%M"))
  ax3.yaxis.set_major_locator(mpl.dates.MinuteLocator(interval=1))
  ax3.yaxis.set_major_formatter(mpl.dates.DateFormatter("%H:%M"))
  plt.setp(ax3.get_xticklabels(), rotation=20, ha="right")
  plt.savefig("sun.png", transparent=True)
  plt.savefig("sun.svg", transparent=True)
  plt.clf()
  await ctx.reply(files=[discord.File("sun.png"), discord.File("sun.svg")])

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
async def hk_visibility(ctx, *, disposed=None):
  await ctx.channel.trigger_typing()
  r=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/opendata.php?dataType=LTMV&lang=en&rformat=csv")
  visibility=r.content.decode("utf-8")[1:-1]
  reader = csv.DictReader(visibility.splitlines())
  visibilities = [x for x in reader]
  embed = discord.Embed(title="HKO Visibility Information", description=f"Information updated at {re.sub(hko_dt_pattern, hko_dt_pattern_, visibilities[0]['Date time'])} HKT (Update frequency: 10 minutes)")
  for v in visibilities:
    embed.add_field(name=v['Automatic Weather Station'], value=v['10 minute mean visibility'].replace("km", " km"), inline=True)
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
    desc += f"\nUV Index at {re.sub(hko_dt_pattern, hko_dt_pattern_, u['Date time'])}: {u['past 15-minute mean UV Index']} (Update frequency: 15 minutes)"
  for count in ['mintempFrom00To09', 'rainfallFrom00To12']:
    if r1[count]:
      desc += f"\n{r1[count]} {r2[count]}"
  if r1['warningMessage']:
    for w, w_ in zip(r1['warningMessage'], r2['warningMessage']):
      desc += f"\n{w} {w_}"
  embed = discord.Embed(title="HKO Weather Information", description=desc)
  rain_dict = {html.unescape(f"{x1['place']} {x2['place']}"): y for x1, x2, y in zip(r1['rainfall']['data']   , r2['rainfall']['data']   , range(0, 18))}
  temp_dict = {html.unescape(f"{x1['place']} {x2['place']}"): y for x1, x2, y in zip(r1['temperature']['data'], r2['temperature']['data'], range(0, 27))}
  places_list = list(set(list(rain_dict) + list(temp_dict)))
  places_list.sort()
  for count in places_list:
    fv =  f"Rainfall: {r1['rainfall']['data']   [rain_dict[count]]['max']} mm\n"   if count in list(rain_dict) else ""
    fv += f"Temperature: {r1['temperature']['data'][temp_dict[count]]['value']}°C" if count in list(temp_dict) else ""
    embed.add_field(name=count, value=fv, inline=True)
  f0v = "Humidity: {r1['humidity']['data'][0]['value']}% at {r1['humidity']['data'][0]['place']}"
  if r1.get('uvindex:', None):
    f0v += f"UV Index: {r1['uvindex']['data'][0]['value']} ({r1['uvindex']['data'][0]['desc']}) at {r1['uvindex']['data'][0]['place']}"
  embed.add_field(name="Extra Information", value=f0v)
  embed.set_image(url=f"https://www.hko.gov.hk/images/HKOWxIconOutline/pic{r1['icon'][0]}.png")
  await ctx.reply(embed=embed)

@commands.command()
async def hk_wind(ctx, *, disposed=None):
  await ctx.channel.trigger_typing()
  r=requests.get("https://data.weather.gov.hk/weatherAPI/hko_data/regional-weather/latest_10min_wind.csv")
  wind=r.content.decode("utf-8")[:-1]
  reader = csv.DictReader(wind.splitlines())
  winds = [x for x in reader]
  embed = discord.Embed(title="HKO Wind Information", description=f"Information updated at {re.sub(hko_dt_pattern, hko_dt_pattern_, winds[0]['Date time'])} HKT (Update frequency: 10 minutes)")
  for w in winds:
    embed.add_field(name=f"{w['Automatic Weather Station']} {db['compass_points'][w['10-Minute Mean Wind Direction(Compass points)']]}",
    value=f"""{w['10-Minute Mean Wind Direction(Compass points)']}{(' at'+w['10-Minute Mean Speed(km/hour)']+' km/h') if w['10-Minute Mean Speed(km/hour)']!="N/A" else ''}
    {('Maximum Gust: '+w['10-Minute Maximum Gust(km/hour)']+' km/h') if w['10-Minute Maximum Gust(km/hour)']!='N/A' else ''}""", inline=True)
  embed.set_footer(text="Speed and Gust Information might be empty for some weather stations. Directions and Speed are mean values in the past 10 minutes.")
  await ctx.reply(embed=embed)

def setup(bot):
  bot.add_command(hk_aqi)
  bot.add_command(hk_forecast)
  bot.add_command(hk_lightning)
  bot.add_command(hk_moon)
  bot.add_command(hk_sea_pressure)
  bot.add_command(hk_sun)
  bot.add_command(hk_tide)
  bot.add_command(hk_visibility)
  bot.add_command(hk_weather)
  bot.add_command(hk_wind)