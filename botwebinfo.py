from os import name
from discord.ext.commands.core import command
import pytube
import wikipedia
from PyDictionary import PyDictionary
from pygoogletranslation import Translator
import html
from shared import *

dictionary    = PyDictionary()
translatorvar = Translator()
unsortedlangdict = translatorvar.glanguage().get("tl")
unsortedsrclangdict = translatorvar.glanguage().get("sl")
langkeys = list(unsortedlangdict.keys())
langkeys.sort()
langdict = {}
for count in langkeys:
  langdict[count] = unsortedlangdict[count]
srclangkeys = list(unsortedsrclangdict.keys())
srclangkeys.sort()
srclangdict = {}
for count in srclangkeys:
  srclangdict[count] = unsortedsrclangdict[count]
wikipedia.set_lang("en")

yt_pattern = re.compile(r'search\s[0-5]\s.*')

botadmin = lambda context : context.author.id == 687474789342117900

@commands.command()
async def definition(ctx, *, word):
  await ctx.channel.trigger_typing()
  desc = ""
  try:
    definitions = dictionary.meaning(word)
  except:
    await ctx.reply("Invalid word. Please try again.")
  for count, count3 in definitions.items():
    desc = desc + f"**{count}**\n"
    for count2 in count3:
      desc = desc + count2 + f"\n"
  embed = discord.Embed(title=f"Definition of {word}", description=desc[:1023])
  try:
    synonyms = dictionary.synonym(word)
    embed.add_field(name="Synonyms", value=", ".join(synonyms))
  except:
    pass
  try:
    antonyms = dictionary.antonym(word)
    embed.add_field(name="Antonyms", value=", ".join(antonyms))
  except:
    pass
  await ctx.reply(embed=embed)

@commands.command(aliases=['http', 'https', 'statuscode'])
async def error(ctx, code="404", *, disposed = None):
  try:
    if int(code) in (db["httpcat"]+db["httpdog"]):
      await ctx.reply(f'https://http.cat/{code}\nhttps://httpstatusdogs.com/img/{code}.jpg')
    else:
      await ctx.reply("Invalid code!")
  except:
    await ctx.reply("Invalid code!")

@commands.command(aliases=['httpcat', 'httpscat', 'httpcats', 'httpscats'])
async def errorcat(ctx, code="404", *, disposed = None):
  if int(code) in db["httpcat"]:
    await ctx.reply(f'https://http.cat/{code}')
  else:
    await ctx.reply("Invalid code!")

@commands.command(aliases=['httpdog', 'httpsdog', 'httpdogs', 'httpsdogs'])
async def errordog(ctx, code="404", *, disposed = None):
  if int(code) in db["httpdog"]:
    await ctx.reply(f'https://httpstatusdogs.com/img/{code}.jpg')
  else:
    await ctx.reply("Invalid code!")

@commands.command()
async def forecast(ctx, *, location):
  r2=requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid=a920f6ea8a76b95a520a52e904965b14").json()[0]
  r1=requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={r2['lat']}&lon={r2['lon']}&appid=a920f6ea8a76b95a520a52e904965b14&units=metric").json()
  f1=open('forecasts.html')
  f2c=eval("f'''"+f1.read()+"'''")
  f1.close()
  f2=open(f'forecasts_{ctx.message.id}.html', 'w')
  f2.write(f2c)
  f2.close()
  await ctx.reply("To view the results, download both files and open the `forecasts_XXXXXXXXXXXXXXXXXX.html` one. If prompted, select your browser, such as Firefox.",
  files = [discord.File(f'forecasts_{ctx.message.id}.html'), discord.File('forecasts_css.css')])
  try_delete(f'forecasts_{ctx.message.id}.html')

@commands.command()
async def gender(ctx, *, name):
  r=requests.get(f"https://api.genderize.io/?name={name}")
  gender_json = r.json()
  if gender_json["gender"]:
    await ctx.reply(f"{name} is {round(gender_json['probability']*100, 2)}% a {gender_json['gender']}.")
  else:
    await ctx.reply("No gender was found for the name.")

@commands.command()
async def hk_forecast(ctx, *, disposed=None):
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

@commands.command()
async def hk_weather(ctx, *, disposed=None):
  r1=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en").json()
  r2=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=tc").json()
  r3=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=en").json()
  r4=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=tc").json()
  desc = f"{r3['generalSituation']} {r4['generalSituation']}\n{r3['forecastPeriod']}: {r3['forecastDesc']}\n{r4['forecastPeriod']}: {r4['forecastDesc']}\n{r3['outlook']} {r4['outlook']}"
  for count in ['warningMessage', 'mintempFrom00To09', 'rainfallFrom00To12']:
    if r1[count]:
      desc += f"{r1[count]} {r2[count]}\n"
  embed = discord.Embed(title="HKO Weather Information", description=desc)
  rain_dict = {html.unescape(f"{x1['place']} {x2['place']}"): y for x1, x2, y in zip(r1['rainfall']['data']   , r2['rainfall']['data']   , range(0, 18))}
  temp_dict = {html.unescape(f"{x1['place']} {x2['place']}"): y for x1, x2, y in zip(r1['temperature']['data'], r2['temperature']['data'], range(0, 27))}
  places_list = list(set(list(rain_dict) + list(temp_dict)))
  places_list.sort(reverse=True)
  for count in places_list:
    fv =  f"Rainfall: {r1['rainfall']['data']   [rain_dict[count]]['max']} mm"     if count in list(rain_dict) else ""
    fv += f"Temperature: {r1['temperature']['data'][temp_dict[count]]['value']}°C" if count in list(temp_dict) else ""
    embed.add_field(name=count, value=fv, inline=True)
  embed.add_field(name="Extra Information", value=f"""UV Index: {r1['uvindex']['data'][0]['value']} ({r1['uvindex']['data'][0]['desc']}) at {r1['uvindex']['data'][0]['place']}
  Humidity: {r1['humidity']['data'][0]['value']}% at {r1['humidity']['data'][0]['place']}""")
  embed.set_thumbnail(url=f"https://www.hko.gov.hk/images/HKOWxIconOutline/pic{r1['icon'][0]}.png")
  await ctx.reply(embed=embed)

@commands.command()
async def minecraft(ctx, *, item="tnt"):
  await ctx.channel.trigger_typing()
  r=requests.get('https://minecraft.fandom.com/wiki/'+item)
  soup=BeautifulSoup(r.content, features="html.parser")
  table = soup.findAll('table')[0].findAll('tbody')[0]
  results = soup.findAll("p")
  for count in results:
    if len(count.findAll('b')) != 0 and count.parent.name != "td":
      desc = str(count)
      break
  try:
    desc = re.sub(r'<a (class=".+?" )?href="\/([\w/]+?)" title="([\s\S]+?)">([\s\S]+?)<\/a>', r'[\4](https://minecraft.fandom.com/\2)', desc)
    desc = re.sub(r'<b>([\s\S]*?)<\/b>', r'**\1**', desc)
    desc = re.sub(r'<i>([\s\S]*?)<\/i>', r'*\1*', desc)
    desc = desc.replace("<p>", "").replace("</p>", "")
    desc = re.sub(r'<([a-z]+?)( ([a-z]+?)=".*?")*?>(.*?)<\/\1>', '', desc)
    embed = discord.Embed(title = "Minecraft: "+item, description=desc, url=f"https://minecraft.fandom.com/wiki/{item}")
    try:
      for count in table.findAll('tr'):
        if count.findAll('td')[0].text.replace("<p>", "").replace("</p>", "").replace(" ", "").replace("\n", "") != "":
          embed.add_field(name=count.findAll('th')[0].text.replace("<p>", "").replace("</p>", ""), value=count.findAll('td')[0].text.replace("<p>", "").replace("</p>", ""))
    except:
      pass
    """for count in soup.findAll("h3"):
      if count.text.replace("[edit]", "") not in ["ID", "Metadata", "Share", "Views", "More", "Search", "Minecraft Wiki", "Games", "Useful pages", "Minecraft links", "Gamepedia", "Tools", "In other languages", "Namespaces", "Variants"]:
        desc = str(count.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element).replace("<p>", "").replace("</p>", "")
        desc = re.sub(r'<a (class=".+?" )?href="\/([\w/]+?)"( title="([\s\S]+?))?">([\s\S]+?)<\/a>', r'[\5](https://minecraft.fandom.com/\4)', desc)
        desc = re.sub(r'<b>([\s\S]*?)<\/b>', r'**\1**', desc)
        desc = re.sub(r'<i>([\s\S]*?)<\/i>', r'*\1*', desc)
        desc = re.sub(r'<([a-z]+?)( ([a-z]+?)=".*?")*?>([\s\S]*?)<\/\1>', '', desc)
        desc = re.sub(r'\s', '', desc)
        try:
          if len(desc.replace(" ", "").replace(f"\n", "").replace("[edit]", "")) != 0:
            embed.add_field(name=count.text.replace("[edit]", ""), value=desc, inline=False)
        except:
          pass
    """
    image = soup.findAll("img")[2]['data-src']
    embed.set_image(url = image)
    await ctx.reply(embed=embed)
  except:
    await ctx.reply("No Wiki page with that name found.")

@commands.command(aliaes=["redir", "redirs", "redirects", "red"])
async def redirect(ctx, *, url):
  await ctx.channel.trigger_typing()
  try:
    r = requests.get(url, allow_redirects=True)
    urllist = r.history
    if len(urllist) == 0:
      await ctx.reply("Invalid URL. Please try again.")
    elif len(urllist) == 1:
      await ctx.reply("No redirects found for that URL.")
    elif len(urllist) == 2:
      await ctx.reply("URL redirected to: "+urllist[1].url+" with status code "+str(urllist[1].status_code))
    else:
      urlend = len(urllist)-2
      await ctx.reply("Initial URL: "+urllist[0]+f"\n"+f"\n".join([f"{i.status_code}: {i.url}" for i in urllist[1:urlend]])+"Final URL: "+urllist[len(urllist)-1])
  except:
    await ctx.reply("Invalid URL. Please try again.")

@commands.command()
async def translate(ctx, lang = "list", fromlang = "auto", *, text = "Sample text"):
  if lang == "list" or lang == "all":
    await ctx.reply(embed=discord.Embed(description = f"**List of Language Input (Abbreviations)**\n```{'  '.join(list(srclangdict.keys()))}```\n\n**List of Language Input (Full Names)**\n{', '.join(list(srclangdict.values()))}"))
    await ctx.reply(embed=discord.Embed(description = f"**List of Language Output (Abbreviations)**\n```{' '.join(list(langdict.keys()))}```\n\n**List of Language Output (Full Names)**\n{', '.join(list(langdict.values()))}"))
  else:
    if "," in lang:
      lang_split = lang.split(",")
      lang = lang_split[0]
      fromlang = lang_split[1]
      if list(srclangdict.values()).count(fromlang) == 1:
        fromlang = list(srclangdict.keys())[list(srclangdict.values()).index(fromlang)]
    else:
      fromlang = "auto"
    if list(langdict.values()).count(lang) == 1:
      lang = list(langdict.keys())[list(langdict.values()).index(lang)]
      translation = translatorvar.translate(text, src=fromlang, dest=lang)
    try:
      await ctx.reply(f"**Translation from {srclangdict[fromlang]} to {langdict[lang]}:**\n{translation.text.replace('u003c', '<').replace('u003e', '>').replace('u0026', '&')}")
    except:
      await ctx.reply("Language not found! Please use `=translate list` to get a list of languages.")

@commands.command()
async def unscramble(ctx, text, length="0"):
  await ctx.channel.trigger_typing()
  try:
    ilength = int(length)
  except:
    ilength = 0
  if ilength != 0 and ilength > len(text):
    ilength = 0
  r=requests.get(f"https://wordunscrambler.me/unscramble/{text}")
  soup=BeautifulSoup(r.content, features="html.parser")
  raw_everything = soup.findAll('a', target="_blank")[:-7]
  everything = []
  for count in raw_everything:
    formatted = re.sub(r'<a class="wordWrapper" data-word="([\S\s]+?)" href="/dictionary/([\S\s]+?)" target="_blank" title="Lookup ([\S\s]+?) in Dictionary">', '', str(count))
    formatted = re.sub(r'</a>', '', formatted)
    formatted = re.sub(r"<span>(\w+?)<\/span>", r"\1", formatted)
    formatted = formatted.replace('<sub><span class="score-wrapper"></span></sub>', '')
    formatted = formatted.replace(" ", "").replace(f"\n","")
    formatted = re.sub(r'<span class="marked-letter">(\w)<\/span>', lambda pat: pat.group(1).upper(), formatted)
    everything.append(formatted)
  output = discord.Embed(title=f"Unscrambled results for {text}")
  _sorted = {}
  for count in everything:
    _sorted.setdefault(len(count), []).append(count)
  everything = list(_sorted.values())
  for count in everything:
    current = ""
    length = str(len(count[0].rstrip(" ").replace(f"\n","")))
    for count2 in count:
      if len(current+count2.rstrip(" ").replace(f"\n",""))<1021:
        current += "`" + count2.rstrip(" ").replace(f"\n","") + "` "
      else:
        current += "…"
        break
    if len(output)+len(current) > 5991:
      break
    if ilength == 0 or ilength == int(length):
      output.add_field(name = f"{length}-letters", value=current, inline=False)
  
  text = f"WORD: {text}\n\n"
  for count in everything:
    if ilength == 0 or ilength == len(count[0].rstrip(" ").replace(f"\n","")):
      text += f"\n" + str(len(count[0].rstrip(" ").replace(f"\n",""))) + "-LETTER WORDS\n"
      for count2 in count:
        formatted = count2.rstrip(" ").replace(f"\n","")
        text += f"{formatted}\n"
      
  f = open("output.txt", "w")
  f.write(text)
  f.flush()
  f.close()
  await ctx.reply(embed=output, file=discord.File("output.txt"))
  try_delete('output.txt')

@commands.command()
async def weather(ctx, *, location):
  r1=requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid=a920f6ea8a76b95a520a52e904965b14&units=metric").json()
  if r1["cod"] == "404":
    await ctx.reply("Invalid location! Please try again.")
    return
  r2=requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid=a920f6ea8a76b95a520a52e904965b14&units=imperial").json()
  r3=requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat={r1['coord']['lat']}&lon={r1['coord']['lon']}&appid=a920f6ea8a76b95a520a52e904965b14").json()['list'][0]
  ti=f"Weather for {r1['name']} ({r1['sys']['country']})"
  desc=f"{r1['weather'][0]['main']}: {r1['weather'][0]['description']}\n{abs(r1['coord']['lat'])}°{'N' if r1['coord']['lat']>0 else 'S'}\n{abs(r1['coord']['lon'])}°{'E' if r1['coord']['lon']>0 else 'W'}"
  embed=discord.Embed(title=f"{ti}", description=desc)
  embed.add_field(name="Temp. range", value=f"{r1['main']['temp_min']}°C ~ {r1['main']['temp_max']}°C\n{r2['main']['temp_min']}°F ~ {r2['main']['temp_max']}°F", inline=True)
  embed.add_field(name="Temp. feels like", value=f"{r1['main']['feels_like']}°C / {r2['main']['feels_like']}°F", inline=True)
  embed.add_field(name="Temperature", value=f"{r1['main']['temp']}°C / {r2['main']['temp']}°F", inline=True)
  embed.add_field(name="Wind speed", value=f"{r1['wind']['speed']} m/s / {r2['wind']['speed']} mph", inline=True)
  embed.add_field(name="Wind direction", value=f"{r1['wind']['deg']}°", inline=True)
  if r1['wind'].get('gust', None):
    embed.add_field(name="Wind gust", value=f"{r1['wind']['gust']} m/s / {r2['wind']['gust']} mph", inline=True)
  embed.add_field(name="Humidity", value=f"{r1['main']['humidity']}%", inline=True)
  embed.add_field(name="Sunrise", value=f"<t:{r1['sys']['sunrise']}:T> <t:{r1['sys']['sunrise']}:R>", inline=True)
  embed.add_field(name="Sunset", value=f"<t:{r1['sys']['sunset']}:T> <t:{r1['sys']['sunset']}:R>", inline=True)
  if r1['wind'].get('rain', None):
    embed.add_field(name="Rain in past hour", value=f"{r1['rain']['1h']} mm", inline=True)
  embed.add_field(name="Cloud Coverage", value=f"{r1['clouds']['all']}%", inline=True)
  embed.add_field(name="Pressure", value=f"{r1['main']['pressure']} hPa", inline=True)
  embed.add_field(name="Air Quality", value=f"""{r3['main']['aqi']} ({db['air_quality'][str(r3['main']['aqi'])]})\n{r3['components']['co']} μg/m3 CO (Carbon Monoxide)\n{r3['components']['no']} μg/m3 NO (Nitrogen Monoxide)
{r3['components']['no2']} μg/m3 NO₂ (Nitrogen Dioxide)\n{r3['components']['o3']} μg/m3 O₃ (Ozone)\n{r3['components']['so2']} μg/m3 SO₂ (Sulphur Dioxide)\n{r3['components']['pm2_5']} μg/m3 PM₂.₅ (Fine Particles patter)
{r3['components']['pm10']} μg/m3 PM₁₀ (Coarse Particulate Matter)\n{r3['components']['nh3']} μg/m3 NH₃ (Ammonia)""", inline=False)
  embed.set_thumbnail(url=f"http://openweathermap.org/img/wn/{r1['weather'][0]['icon']}@2x.png")
  await ctx.reply(embed=embed)

@commands.command()
async def wiki(ctx, *, query):
  await ctx.channel.trigger_typing()
  totallen = 0
  try:
    desc = wikipedia.summary(query)[:2047]
    totallen = totallen + len(wikipedia.summary(query)) + len(desc) + len(query)
    wpage = wikipedia.page(title=query, auto_suggest=True, redirect=True, preload=False)
    embed = discord.Embed(title=wpage.title, url="https://en.wikipedia.org/wiki/"+wpage.title.replace(" ","_"), description=desc)
    counter = 0
    for count in wpage.sections:
      if counter >=4 or totallen + len(wpage.section(count)) >= 6000:
        break
      if len(wpage.section(count))!=0:
        embed.add_field(name=count, value=wpage.section(count)[:499], inline=False)
        totallen = totallen + len(wpage.section(count))
        counter = counter + 1
    if len(wpage.images)>=1:
      embed.set_image(url = wpage.images[1])
    if len(wpage.images)>=2:
      embed.set_thumbnail(url = wpage.images[0])
  except:
    results = wikipedia.search(query, results=20, suggestion=False)
    desc = f"**Please make one of these searches:**\n`{'` `'.join(results)}`"
    embed = discord.Embed(title=query, description=desc)
  await ctx.reply(embed=embed)

@commands.command()
async def youtube(ctx, *, link):
  await ctx.channel.trigger_typing()
  if link.startswith("search "):
    query = re.sub(r'search\s([0-5]\s)?(.*)', r'\2', link)
    searching = pytube.Search(query)
    if yt_pattern.fullmatch(link):
      searches = int(link[7])
    else:
      searches = 1
    try:
      for count in range(searches+1):
        searching.get_next_results()
    except:
      pass
    try:
      videos = searching.results[20*(searches-1):20*searches]
    except:
      videos = searching.results[0:20]
    desc = ""
    for count in videos:
      desc+=f"**[{count.title}]({count.watch_url})**\n{format_length(count.length)} | {count.views:,} Views | By [{pytube.Channel(count.channel_url).channel_name}]({count.channel_url})\n"
    embed = discord.Embed(title="Search results", description=desc)
    embed.set_footer(text="Use =youtube [Link] to download videos.")
    await ctx.reply(embed=embed)
  elif link.startswith("channel "):
    chnl = pytube.Channel(link)
    videos = chnl.videos
    desc = f"**Videos ({len(chnl.videos):,})**:\n"
    for count,count2 in zip(videos, range(12)):
      desc+=f"[{count.title}]({count.watch_url})\n{count.views:,} Views | {round(count.rating*20, 3)}% Liked | {format_length(count.length)}\n\n"
    embed = discord.Embed(title=chnl.channel_name, description=desc, url=chnl.videos_url)
    embed.set_footer(text="Use =youtube [Link] to download videos. | Analysing additional info…")
    yt_msg = await ctx.reply(embed=embed)
    totallen = 0
    totalrating = 0
    totalview = 0
    for count in videos:
      totallen += count.length
      totalrating += count.rating
      totalview += count.views
    embed.add_field(name="Total views", value=f"{totalview:,}", inline=True)
    embed.add_field(name="Total length", value=format_length(totallen), inline=True)
    embed.add_field(name="Total rating", value=f"{str(round(totalrating*20, 3))}%", inline=True)
    embed.add_field(name="Average views", value=f"{round(totalview/len(videos), 3):,}", inline=True)
    embed.add_field(name="Average length", value=format_length(round(totallen/len(videos))), inline=True)
    embed.add_field(name="Average rating", value=f"{str(round(totalrating/len(videos)*20, 3))}%", inline=True)
    embed.set_footer(text="Use =youtube [Link] to download videos.")
    await yt_msg.edit(embed=embed)
  else:
    try:
      playlist = pytube.Playlist(link)
      text = ""
      for count in playlist.videos:
        text=text+str(count)+"  "+count.streams.filter(mime_type="video/mp4").filter(progressive="True").filter(type="video").order_by("resolution").first().url+f"\n"
      f = open("output.txt", "w")
      f.write(text)
      f.flush()
      f.close()
      await ctx.reply(file=discord.File("output.txt"))
      try_delete('output.txt')
    except:
      try:
        youtube = pytube.YouTube(link, allow_oauth_cache=False)
      except:
        youtube = pytube.Search(link).results[0]
      yt_streams = youtube.streams
      filtered1 = yt_streams.filter(progressive=True,file_extension='mp4').order_by("resolution")
      video1 = filtered1[len(filtered1)-1]
      additional_desc = " Warning: Do not use a small data plan for videos this large!" if video1.filesize >= 52428800 else ""
      desc = f"This video has a size of around {sizer(video1.filesize)}.{additional_desc}"
      embed = discord.Embed(title="Download (Click here)", url=video1.url, description=f"{desc}\nNote: This message will be edited with more information.")
      allvideos = yt_streams.filter(type="video")
      allaudios = yt_streams.filter(only_audio=True)
      filtered2 = allvideos.order_by("resolution")
      filtered2b = filtered2.filter(progressive=True)
      video2 = filtered2[len(filtered2)-1]
      filtered3 = allaudios.order_by("abr")
      video3 = filtered3[len(filtered3)-1]
      video4 = filtered2b[int(len(filtered2b)/2)]
      video4b = filtered2[int(len(filtered2)/2)]
      video5 = filtered3[len(filtered3)-1]
      filtered6 = allvideos.order_by("filesize")
      video7 = filtered6[0]
      filtered7 = allaudios.order_by("filesize")
      video8 = filtered7[0]
      filtered8 = filtered2b.order_by("filesize")
      video6 = filtered8[0]

      videox1 = None
      for count in filtered8.__reversed__():
        if count.filesize < 8000000:
          videox1 = count
          break
      
      videox2 = None
      for count in filtered7.__reversed__():
        if count.filesize < 8000000:
          videox2 = count
          break
      
      videox3 = None
      for count in filtered6.__reversed__():
        if count.filesize < 8000000:
          videox3 = count
          break
      videox1_text = format_video(videox1) if videox1 else "There is no progressive video less than 8MB."
      videox2_text = format_video(videox2) if videox2 else "There is no audio less than 8MB."
      videox3_text = format_video(videox3) if videox3 else "There is no video less than 8MB."

      extra_downloads=f'''Note: the embed title's URL links to 'Vi+Au - Best quality'.\n
Type and quality\t\tBitrate\t\tRes.\tFPS\tSize\t\tLink\n
Vi+Au - Best quality\t\t{format_video(video1)}
Video - Best quality\t\t{format_video(video2)}
Audio - Best quality\t\t{format_video(video3)}
Vi+Au - Medium quality\t\t{format_video(video4)}
Video - Medium quality\t\t{format_video(video4b)}
Audio - Medium quality\t\t{format_video(video5)}
Vi+Au - Less than 8MB\t\t{videox1_text}
Video - Less than 8MB\t\t{videox3_text}
Audio - Less than 8MB\t\t{videox2_text}
Vi+Au - Minimum size\t\t{format_video(video6)}
Video - Minimum size\t\t{format_video(video7)}
Audio - Minimum size\t\t{format_video(video8)}'''
      f = open('extra_downloads.txt', "w")
      f.write(extra_downloads)
      f.flush()
      f.close()
      ytmsg = await ctx.reply(embed=embed, file=discord.File('extra_downloads.txt'))
      try_delete('extra_downloads.txt')
      embed = discord.Embed(title="Download (Click here)", url=video1.url, description=desc)
      embed.add_field(name="Title", value=youtube.title, inline=False)
      if len(youtube.description[:1023].replace(" ", "")) == 0:
        embed.add_field(name="Description", value="No description provided", inline=False)
      else:
        embed.add_field(name="Description", value=youtube.description[:1023], inline=False)
      if len(youtube.keywords) == 0:
        embed.add_field(name="Tags", value="No tags provided", inline=False)
      else:
        embed.add_field(name="Tags", value=(", ".join(youtube.keywords))[:1023], inline=False)
      embed.add_field(name="Views", value=f'{youtube.views:,}', inline=True)
      embed.add_field(name="Date uploaded", value=unix_timestamp(youtube.publish_date, "D"), inline=True)
      embed.add_field(name="Length", value=format_length(youtube.length), inline=True)
      chnl = pytube.Channel(youtube.channel_url)
      embed.add_field(name="Rating", value=f"{str(round(youtube.rating*20, 3))}%", inline=True)
      embed.add_field(name="Channel", value=f"[{chnl.channel_name}]({youtube.channel_url}) ({len(chnl.videos)} videos)", inline=True)
      if youtube.age_restricted:
        embed.add_field(name="Restricted", value="This video is age-restricted.", inline=True)
      embed.set_thumbnail(url=youtube.thumbnail_url)
      await ytmsg.edit(embed=embed)

      # youtube_view = ui.View(timeout=0)
      # youtube_view.add_item(ui.Button(style=discord.ButtonStyle.success, row=0, label="Best quality", disabled=True))
      # youtube_view.add_item(ui.Button(style=discord.ButtonStyle.url, row=0, label="Video+Audio", url=video1.url))
      # youtube_view.add_item(ui.Button(style=discord.ButtonStyle.url, row=0, label="Video only", url=video2.url))
      # youtube_view.add_item(ui.Button(style=discord.ButtonStyle.url, row=0, label="Audio only", url=video3.url))
      # youtube_view.add_item(ui.Button(style=discord.ButtonStyle.primary, row=1, label="Medium quality", disabled=True))
      # youtube_view.add_item(ui.Button(style=discord.ButtonStyle.url, row=1, label="Video+Audio", url=video4.url))
      # youtube_view.add_item(ui.Button(style=discord.ButtonStyle.url, row=1, label="Video only", url=video4b.url))
      # youtube_view.add_item(ui.Button(style=discord.ButtonStyle.url, row=1, label="Audio only", url=video5.url))
      # youtube_view.add_item(ui.Button(style=discord.ButtonStyle.secondary, row=2, label="Less than 8MB", disabled=True))
      # youtube_view.add_item(ui.Button(style=discord.ButtonStyle.url, row=2, label="Video+Audio", url=videox1.url) if videox1 else ui.Button(style=discord.ButtonStyle.url, row=2, label="Video+Audio", url="https://example.com", disabled=True))
      # youtube_view.add_item(ui.Button(style=discord.ButtonStyle.url, row=2, label="Video only", url=videox3.url)  if videox1 else ui.Button(style=discord.ButtonStyle.url, row=2, label="Video only", url="https://example.com", disabled=True))
      # youtube_view.add_item(ui.Button(style=discord.ButtonStyle.url, row=2, label="Audio only", url=videox2.url)  if videox1 else ui.Button(style=discord.ButtonStyle.url, row=2, label="Audio only", url="https://example.com", disabled=True))
      # youtube_view.add_item(ui.Button(style=discord.ButtonStyle.danger, row=3, label="Medium quality", disabled=True))
      # youtube_view.add_item(ui.Button(style=discord.ButtonStyle.url, row=3, label="Video+Audio", url=video6.url))
      # youtube_view.add_item(ui.Button(style=discord.ButtonStyle.url, row=3, label="Video only", url=video7.url))
      # youtube_view.add_item(ui.Button(style=discord.ButtonStyle.url, row=3, label="Audio only", url=video8.url))
      # await ctx.reply(view=youtube_view)

def setup(bot):
  bot.add_command(definition)
  bot.add_command(error)
  bot.add_command(errorcat)
  bot.add_command(errordog)
  bot.add_command(forecast)
  bot.add_command(gender)
  bot.add_command(hk_forecast)
  bot.add_command(hk_weather)
  bot.add_command(minecraft)
  bot.add_command(redirect)
  bot.add_command(translate)
  bot.add_command(unscramble)
  bot.add_command(weather)
  bot.add_command(wiki)
  bot.add_command(youtube)
