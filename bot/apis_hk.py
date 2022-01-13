from shared import *
import html
import csv

hko_dt_pattern = re.compile(r'\d{8}(\d{2})(\d{2})')
hko_dt_pattern_= r'\1:\2'
hko_dt_pattern2 =re.compile(r'\d{8}(\d{2})(\d{2})-\d{8}(\d{2})(\d{2})')
hko_dt_pattern2_=r'\1:\2~\3:\4'
gmb_weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

fake_headers = {'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0"}
mtr_time   = lambda rt: re.sub(r'\d{4}-\d{2}-\d{2} (\d{2}:\d{2}:\d{2})', r'\1', rt)
aqi_range1 = lambda min, max: min if min == max else f"{min}~{max}"
aqi_range2 = lambda min, max: min if min == max else f"{min} ~ {max}"
gmb_weekday= lambda x:"Everyday " if x==[True]*7 else ("Mon ~ Sat" if x==[True]*6+[False] else ("Mon ~ Fri" if x==[True]*5+[False]*2 else (
  "Sat ~ Sun" if x==[False]*5+[True]*2 else ", ".join([gmb_weekdays[y] for y in x if y]))))
gmb_ph = {True:"including", False:"excluding"}

kmb_stops = requests.get("https://data.etabus.gov.hk/v1/transport/kmb/stop").json()['data']
kmb_routes= requests.get("https://data.etabus.gov.hk/v1/transport/kmb/route/").json()['data']
gmb_routes_HKI = requests.get("https://data.etagmb.gov.hk/route/HKI/").json()['data']['routes']
gmb_routes_KLN = requests.get("https://data.etagmb.gov.hk/route/KLN/").json()['data']['routes']
gmb_routes_NT  = requests.get("https://data.etagmb.gov.hk/route/NT/").json()['data']['routes']

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
async def hk_ferry_1(ctx, *, disposed=None):
  await ctx.channel.trigger_typing()
  r1=requests.get("https://www.hongkongwatertaxi.com.hk/eta/?route=HHCL").json()['data'][0]
  r2=requests.get("https://www.hongkongwatertaxi.com.hk/eta/?route=CLHH").json()['data'][0]
  embed = discord.Embed(title="Fortune Ferry Information")
  for r in [r1, r2]:
    embed.add_field(name=r['route_en'].replace("-", "→").replace("Hung Hom", "Hung Hom 紅磡").replace("Central", "Central 中環"), value=f"Next departure at {r['depart_time']}{(' (Vessel Code: '+r['vesselcode']+')') if r.get('vesselcode', None) else ''}")
  await ctx.reply(embed=embed)

@commands.command()
async def hk_forecast(ctx, *, disposed=None):
  await ctx.channel.trigger_typing()
  r1=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=en").json()
  r2=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=tc").json()
  embed = discord.Embed(title="HKO Forecast", description=f"{r1['generalSituation']}\n{r2['generalSituation']}")
  for d, d2 in zip(r1['weatherForecast'], r2['weatherForecast']):
    embed.add_field(name=f"{d['week']}", value=f"""{d['forecastWeather']} {d2['forecastWeather']}\nTemperature: {d['forecastMintemp']['value']}°C ~ {d['forecastMaxtemp']['value']}°C
    Humidity: {d['forecastMinrh']['value']}% ~ {d['forecastMaxrh']['value']}%\n{d['PSR']} probability of significant rain\nWind: {d['forecastWind']} {d2['forecastWind']}""", inline= False)
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
  for x in ['top', 'bottom', 'left', 'right']:
    ax.spines[x].set_color("w")
    ax2.spines[x].set_color("w")
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
async def hk_gmb(ctx, region, line):
  region = region.upper()
  line = line.upper()
  if region not in ['HKI', 'KLN', 'NT']:
    await ctx.reply("Invalid region. Please use `HKI`, `KLN` or `NT` (case-insensitive).")
    return
  r1=list(filter(lambda x: x == line, eval(f'gmb_routes_{region}')))[0]
  if not len(r1):
    await ctx.reply("Invalid route.")
    return
  r2 = requests.get(f"https://data.etagmb.gov.hk/route/{region}/{line}").json()['data'][0]
  for r2_ in r2['directions']:
    async with ctx.channel.typing():
      r3=requests.get(f"https://data.etagmb.gov.hk/route-stop/{r2['route_id']}/{r2_['route_seq']}").json()['data']['route_stops']
      desc = "```"+f"\n".join([f"{x['frequency']} mins/car: {gmb_weekday(x['weekdays'])} {x['start_time']} ~ {x['end_time']} ({gmb_ph[x['public_holiday']]} PHs)" for x in r2_['headways']])+"```"
      for r3_ in r3:
        r4=requests.get(f"https://data.etagmb.gov.hk/eta/route-stop/{r2['route_id']}/{r2_['route_seq']}/{r3_['stop_seq']}").json()['data']['eta']
        desc += f"\n**{r3_['name_tc']} {r3_['name_en']}**"
        if r4:
          desc += f"\nCar(s) at {', '.join([datetime.fromisoformat(x['timestamp']).strftime('%H:%M:%S') for x in r4])}"
      embed=discord.Embed(title=f"{r2_['orig_en']} {r2_['orig_tc']} → {r2_['dest_en']} {r2_['dest_tc']}", description=desc)
      await ctx.reply(embed=embed)

@commands.command()
async def hk_kmb(ctx, line):
  line = line.upper()
  r1=list(filter(lambda x: x['route'] == line,kmb_routes))
  if not r1:
    await ctx.reply("Invalid route.")
    return
  for r1_ in r1:
    async with ctx.channel.typing():
      for x in [r1_['dest_en'], r1_['orig_en']]:
        x=x.title()
      route_url = f"{r1_['route']}/{db['kmb_bound'][r1_['bound']]}/{r1_['service_type']}"
      r2=requests.get(f"https://data.etabus.gov.hk/v1/transport/kmb/route-stop/{route_url}").json()['data']
      desc = ""
      for s in r2:
        rt1=list(filter(lambda x: x['stop'] == s['stop'], kmb_stops))[0]
        rt2=requests.get(f"https://data.etabus.gov.hk/v1/transport/kmb/eta/{s['stop']}/{r1_['route']}/{r1_['service_type']}").json()['data'][:2]
        desc += f"\n**{s['seq']}: {rt1['name_en'].title()} {rt1['name_tc']}**"
        if len(rt2):
          rt2_etas=[datetime.fromisoformat(x['eta']).strftime('%H:%M:%S') for x in rt2]
          desc += f"\nBus(es) at {', '.join(rt2_etas)}"
      embed=discord.Embed(title=r1_['route']+(f" {r1_['orig_en']} {r1_['orig_tc']} → {r1_['dest_en']} {r1_['dest_tc']}" if r1_['bound']=='outbound' else f" {r1_['dest_en']} {r1_['dest_tc']} → {r1_['orig_en']} {r1_['orig_tc']}"), description=desc)
      await ctx.reply(embed=embed)

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
    embed.add_field(name=f"{l['Region'].replace('Hong Kong Island', 'HKI')}: {l['Type']}\n{l2['區域']}: {l2['類別']}", value=f"Lightnings: {l['lightning count']}", inline= True)
  await ctx.reply(embed=embed)

@commands.command()
async def hk_lr(ctx, station : int):
  if station not in db["mtr"]["lr_stations"]:
    await ctx.reply(f"Please supply a 1~3-digit station code! Available codes are `{'` `'.join(db['mtr']['stations'])}`")
    return
  r=requests.get(f"https://rt.data.gov.hk/v1/transport/mtr/lrt/getSchedule?station_id={station}").json()['platform_list']
  embed=discord.Embed(title="Light Rail ETA")
  for p in r:
    desc = ""
    if p.get('route_list', None):
      for t in p['route_list']:
        desc += f"""<:Train1:912268792808243200>{'<:Transparent:912206780015190038>'if t['train_length']==1 else'<:Train2:912268792908890132>'}**{t['route_no']}** to {t['dest_en']} ({t['dest_ch']}) {db['mtr']['lr_status'][t['arrival_departure']]} {f"in {t['time_en']}" if t['time_en'][0].isdigit() else f"({t['time_en']})"}\n"""
      embed.add_field(name=f"Platform {p['platform_id']}", value=desc, inline= False)
  if len(embed.fields):
    await ctx.reply(embed=embed)
  else:
    await ctx.reply("No information could be fetched.")

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
  The same also happened in the data supplied for 2018~2023. Please do not contact the developers for information on that.""".replace(f"\n", ""))
  for m in moons:
    embed.add_field(name=m['YYYY-MM-DD'], value=f"Rise-Set: {m['RISE']} ~ {m['SET']}\nTransitional Period: {m['TRAN.']}")
  await ctx.reply(embed=embed)

@commands.command()
async def hk_mtr(ctx, station, line):
  if station not in db["mtr"]["stations"]:
    await ctx.reply(f"Please supply a 3-digit station code! Available codes are `{'` `'.join(db['mtr']['stations'])}`")
    return
  if line not in db["mtr"]["lines"]:
    await ctx.reply(f"Please supply a 3-digit line code! Available codes are `{'` `'.join(db['mtr']['lines'])}`")
    return
  r=list(requests.get(f"https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php?line={line}&sta={station}").json()['data'].values())[0]
  embed=discord.Embed(title="MTR Trains")
  if r.get('UP', None):
    embed.add_field(name="Up", value=f"\n".join([f"To {x['dest']} from platform {x['plat']} in {x['ttnt']} minutes ({mtr_time(x['time'])})" for x in r['UP']]))
  if r.get('DOWN', None):
    embed.add_field(name="Down", value=f"\n".join([f"To {x['dest']} from platform {x['plat']} in {x['ttnt']} minutes ({mtr_time(x['time'])})" for x in r['DOWN']]))
  await ctx.reply(embed=embed)

@commands.command()
async def hk_nwfb(ctx, line):
  r1=requests.get(f"https://rt.data.gov.hk/v1/transport/citybus-nwfb/route/nwfb/{line}/").json()['data']
  if not r1:
    await ctx.reply("Invalid route.")
    return
  r2=requests.get(f"https://rt.data.gov.hk/v1/transport/citybus-nwfb/route-stop/nwfb/{line}/inbound").json()['data']
  desc = ""
  for s in r2:
    await ctx.channel.trigger_typing()
    rt1=requests.get(f"https://rt.data.gov.hk/v1/transport/citybus-nwfb/stop/{s['stop']}").json()['data']
    rt2=requests.get(f"https://rt.data.gov.hk/v1/transport/citybus-nwfb/eta/nwfb/{s['stop']}/{line}").json()['data']
    rt2=list(filter(lambda x: x['eta'], rt2))
    rt2.sort(key=lambda x: x['eta_seq'])
    desc += f"\n{s['seq']}: {rt1['name_en']} {rt1['name_tc']}"
    if rt2:
      rt2_eta=datetime.fromisoformat(rt2[0]['eta'])
      desc += f" (Bus at {rt2_eta.strftime('%H:%M:%S')})"
  embed=discord.Embed(title=f"{r1['route']} {r1['dest_en']} {r1['dest_tc']} → {r1['orig_en']} {r1['orig_tc']}", description=desc)
  await ctx.reply(embed=embed)
  await ctx.channel.trigger_typing()
  r1=requests.get(f"https://rt.data.gov.hk/v1/transport/citybus-nwfb/route/nwfb/{line}/").json()['data']
  r2=requests.get(f"https://rt.data.gov.hk/v1/transport/citybus-nwfb/route-stop/nwfb/{line}/outbound").json()['data']
  desc = ""
  for s in r2:
    rt1=requests.get(f"https://rt.data.gov.hk/v1/transport/citybus-nwfb/stop/{s['stop']}").json()['data']
    rt2=requests.get(f"https://rt.data.gov.hk/v1/transport/citybus-nwfb/eta/nwfb/{s['stop']}/{line}").json()['data']
    rt2=list(filter(lambda x: x['eta'], rt2))
    rt2.sort(key=lambda x: x['eta_seq'])
    desc += f"\n{s['seq']}: {rt1['name_en']} {rt1['name_tc']}"
    if rt2:
      rt2_eta=datetime.fromisoformat(rt2[0]['eta'])
      desc += f" (Bus at {rt2_eta.strftime('%H:%M:%S')})"
  embed=discord.Embed(title=f"{r1['route']} {r1['orig_en']} {r1['orig_tc']} → {r1['dest_en']} {r1['dest_tc']}", description=desc)
  await ctx.reply(embed=embed)

@commands.command()
async def hk_sea_pressure(ctx, *, disposed=None):
  await ctx.channel.trigger_typing()
  r=requests.get("https://data.weather.gov.hk/weatherAPI/hko_data/regional-weather/latest_1min_pressure.csv")
  r1=requests.get("https://data.weather.gov.hk/weatherAPI/hko_data/regional-weather/latest_1min_pressure_uc.csv")
  pressure=r.content.decode("utf-8")[:-1]
  reader = csv.DictReader(pressure.splitlines())
  pressures = [x for x in reader]
  pressure_=r1.content.decode("utf-8")[:-1]
  reader_ = csv.DictReader(pressure_.splitlines())
  pressures_ = [x for x in reader_]
  embed = discord.Embed(title="HKO Sea Pressure Information", description=f"Information updated at {re.sub(hko_dt_pattern, hko_dt_pattern_, pressures[0]['Date time'])} HKT (Update frequency: 10 minutes)")
  for p, p_ in zip(pressures, pressures_):
    embed.add_field(name=f"{p['Automatic Weather Station']} {p_['自動氣象站'].replace(' ', '')}", value=f"{p['Mean Sea Level Pressure(hPa)']} hPa", inline= True)
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
    for x in ['top', 'bottom', 'left', 'right']:
      ax.spines[x].set_color("w")
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
    embed.add_field(name=t['Tide Station'], value=f"{t['Height(m)']} m", inline= True)
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
    embed.add_field(name=v['Automatic Weather Station'], value=v['10 minute mean visibility'].replace("km", " km"), inline= True)
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
  for x in ['mintempFrom00To09', 'rainfallFrom00To12']:
    if r1[x]:
      desc += f"\n{r1[x]} {r2[x]}"
  if r1['warningMessage']:
    for w, w_ in zip(r1['warningMessage'], r2['warningMessage']):
      desc += f"\n{w} {w_}"
  embed = discord.Embed(title="HKO Weather Information", description=desc)
  rain_dict = {html.unescape(f"{x1['place']} {x2['place']}"): y for x1, x2, y in zip(r1['rainfall']['data']   , r2['rainfall']['data']   , range(18))}
  temp_dict = {html.unescape(f"{x1['place']} {x2['place']}"): y for x1, x2, y in zip(r1['temperature']['data'], r2['temperature']['data'], range(27))}
  places_list = list(set(list(rain_dict) + list(temp_dict)))
  places_list.sort()
  for x in places_list:
    fv =  f"Rainfall: {r1['rainfall']['data']   [rain_dict[x]]['max']} mm\n"   if x in list(rain_dict) else ""
    fv += f"Temperature: {r1['temperature']['data'][temp_dict[x]]['value']}°C" if x in list(temp_dict) else ""
    embed.add_field(name=x, value=fv, inline= True)
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
    value=f"""{w['10-Minute Mean Wind Direction(Compass points)']}{(' at '+w['10-Minute Mean Speed(km/hour)']+' km/h') if w['10-Minute Mean Speed(km/hour)']!="N/A" else ''}
    {('Maximum Gust: '+w['10-Minute Maximum Gust(km/hour)']+' km/h') if w['10-Minute Maximum Gust(km/hour)']!='N/A' else ''}""", inline= True)
  embed.set_footer(text="Speed and Gust Information might be empty for some weather stations. Directions and Speed are mean values in the past 10 minutes.")
  await ctx.reply(embed=embed)

def setup(bot):
  bot.add_command(hk_aqi)
  bot.add_command(hk_ferry_1)
  bot.add_command(hk_forecast)
  bot.add_command(hk_gmb)
  bot.add_command(hk_kmb)
  bot.add_command(hk_lightning)
  bot.add_command(hk_lr)
  bot.add_command(hk_moon)
  bot.add_command(hk_mtr)
  bot.add_command(hk_nwfb)
  bot.add_command(hk_sea_pressure)
  bot.add_command(hk_sun)
  bot.add_command(hk_tide)
  bot.add_command(hk_visibility)
  bot.add_command(hk_weather)
  bot.add_command(hk_wind)