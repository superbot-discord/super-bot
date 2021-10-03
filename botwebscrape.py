from shared import *

markdowner = Markdown(extras=["strike", "footnotes"])
html_pattern = re.compile(r'^\`\`\`(html)?\n([\s\S]*)\`\`\`$')
md_pattern = re.compile(r'^\`\`\`(md|markdown)?\n([\s\S]*)\`\`\`$')
country_pattern = ""
specialbool = lambda input: True if input.lower() in ["1","yes", "enable", "on", "enabled", "tick", "true"] else False

def func(pct, allvals):
  absolute = int(pct/100*np.sum(allvals))
  return "{:d} ({:.1f}%)".format(absolute, pct)

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("–lang=zh-TW")

@commands.command()
async def covid(ctx, *, country="world"):
  await ctx.channel.trigger_typing()
  driver = webdriver.Chrome(options=options)
  if country.lower() == "world" or country.lower() == "global" or country.lower() == "worldwide" or country.lower() == "everywhere" or country.lower() == "anywhere" or country.lower() == "international" or country.lower() == "internationally" or country.lower() == "globally" or country.lower() == "current":
    country = "world"
  r=requests.get('https://www.worldometers.info/coronavirus/')
  soup=BeautifulSoup(r.content, features="html.parser")
  exec("country_pattern = re.compile(r'"+country+"', re.IGNORECASE)", globals())
  covidtable = soup.findAll('table')[0].findAll('tbody')[0]
  found = 0
  for count in covidtable.findAll('tr'):
    try:
      match = country_pattern.fullmatch(count.findAll('td')[1].string)
      if match:
        needrow = count
        found = 1
        break
    except:
      1
  if found == 1:
    if country == "world":
      embed = discord.Embed(title="Coronavirus statistics worldwide")
    else:
      embed = discord.Embed(title="Coronavirus statistics in "+country)
    tcases = needrow.findAll('td')[2].string
    trecovered = needrow.findAll('td')[6].string
    ttest = needrow.findAll('td')[12].string
    tactive = needrow.findAll('td')[8].string
    tserious = needrow.findAll('td')[9].string
    tdeath = needrow.findAll('td')[4].string
    try:
      tpopulation = needrow.findAll('td')[14].findAll('a')[0].string
    except:
      driver = webdriver.Chrome(options=options)
      driver.get("https://www.worldometers.info/world-population/")
      wait = WebDriverWait(driver,2)
      while True:
        tpopulation = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span[rel='current_population']"))).text
        if "retrieving data" not in tpopulation:
          break
    embed.add_field(name="Total Cases", value=tcases, inline=True)
    embed.add_field(name="Total Deaths", value=tdeath, inline=True)
    embed.add_field(name="Total Recovered", value=trecovered, inline=True)
    embed.add_field(name="New Cases", value=needrow.findAll('td')[3].string, inline=True)
    embed.add_field(name="New Deaths", value=needrow.findAll('td')[5].string, inline=True)
    embed.add_field(name="New Recovered", value=needrow.findAll('td')[7].string, inline=True)
    embed.add_field(name="Active Cases", value=tactive, inline=True)
    embed.add_field(name="Serious Cases", value=tserious, inline=True)
    if country != "world":
      embed.add_field(name="Cases/Tests", value=str(int(tcases.replace(",",""))/int(ttest.replace(",",""))), inline=True)
    embed.add_field(name="Cases/1M", value=needrow.findAll('td')[10].string, inline=True)
    embed.add_field(name="Deaths/1M", value=needrow.findAll('td')[11].string, inline=True)
    if country != "world":
      embed.add_field(name="Recovered/1M", value=str(int(trecovered.replace(",",""))/int(tpopulation.replace(",",""))*1000000), inline=True)
      embed.add_field(name="Total Tests", value=ttest, inline=True)
      embed.add_field(name="Tests/1M", value=needrow.findAll('td')[13].string, inline=True)
    mylabels = ["Active (Mild)", "Active (Serious)", "Recovered", "Died"]
    mycolors = ["#4287F5", "#FF5252", "#CAFF99", "#A1A1A1"]
    y = np.array([int(tactive.replace(",",""))-int(tserious.replace(",","")), int(tserious.replace(",","")), int(trecovered.replace(",","")), int(tdeath.replace(",",""))])
    patches, labels, pct_texts = plt.pie(y, labels = mylabels, colors = mycolors, autopct=lambda pct: func(pct, y), rotatelabels=True, pctdistance=0.5, textprops = db["font_dicts"]["label"])
    for label, pct_text in zip(labels, pct_texts):
      pct_text.set_rotation(label.get_rotation())
      pct_text.update(db["font_dicts"]["light_label"])
    plt.legend(loc="lower right")
    plt.savefig("pc1.png", transparent=True)
    plt.clf()
    mylabels = ["Non-infected", "Infected"]
    mycolors = ["#A0A0A0", "#FF5252"]
    y = np.array([int(tpopulation.replace(",",""))-int(tcases.replace(",","")), int(tcases.replace(",",""))])
    plt.pie(y, labels = mylabels, colors = mycolors, autopct=lambda pct: func(pct, y), textprops = db["font_dicts"]["light_tiny"], pctdistance=0.5)
    plt.legend(loc="lower right")
    plt.savefig("pc2.png", transparent=True)
    plt.clf()
    filelist = [discord.File("pc1.png"), discord.File("pc2.png")]
    embed.set_thumbnail(url="attachment://pc2.png")
    embed.set_image(url="attachment://pc1.png")
    await ctx.send(files=filelist, embed=embed)
  else:
    await ctx.send("Invalid country. Please try again.")

@commands.command()
async def html(ctx, *, htmlcode = None):
  await ctx.channel.trigger_typing()
  match = html_pattern.fullmatch(htmlcode)
  if match:
    code = re.sub(html_pattern, r"\2", htmlcode)
  else:
    code = htmlcode
  if code == None:
    r = requests.get(ctx.message.attachments[0].url, stream=True)
    r.raise_for_status()
    r.raw.decode_content = True
    code = r.content
  driver = webdriver.Chrome(options=options)
  driver.get(f"data:text/html;charset=utf-8,{code}")
  S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
  driver.set_window_size(S('Width'),S('Height'))
  driver.save_screenshot('html_screenshot.png')
  await ctx.send(file=discord.File('html_screenshot.png'))
  os.remove('html_screenshot.png')
  driver.quit()

@commands.command()
async def map(ctx, long:float, lati:float, zoom:int=10, antizoom = ""):
  await ctx.channel.trigger_typing()
  antizoom = specialbool(antizoom)
  if antizoom:
    m = folium.Map(location=[long, lati], zoom_start=zoom, min_zoom=zoom, max_zoom=zoom)
  else:
    m = folium.Map(location=[long, lati], zoom_start=zoom)
  m.save('map.html')
  await ctx.send(file=discord.File('map.html'))
  driver = webdriver.Chrome(options=options)
  driver.get("file:///map.html")
  await ctx.channel.trigger_typing()
  await asyncio.sleep(5)
  driver.get_screenshot_as_file('map.png')
  await ctx.send(file=discord.File('map.png'))
  driver.quit()

@commands.command(aliases=['md'])
async def markdown(ctx, *, mdcode = None):
  await ctx.channel.trigger_typing()
  match = md_pattern.fullmatch(mdcode)
  if match:
    code = re.sub(md_pattern, r"\2", mdcode)
  else:
    code = mdcode
  if code == None:
    r = requests.get(ctx.message.attachments[0].url, stream=True)
    r.raise_for_status()
    r.raw.decode_content = True
    mdcode = r.content
  code = str(markdowner.convert(mdcode)).lstrip("'u").rstrip("'")
  driver = webdriver.Chrome(options=options)
  driver.get(f"data:text/html;charset=utf-8,{code}")
  S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
  driver.set_window_size(S('Width'),S('Height'))
  driver.save_screenshot('md_screenshot.png')
  await ctx.send(file=discord.File('md_screenshot.png'))
  os.remove('md_screenshot.png')
  driver.quit()

@commands.command()
async def population(ctx, country="current"):
  await ctx.channel.trigger_typing()
  driver = webdriver.Chrome(options=options)
  if country.lower() == "world" or country.lower() == "global" or country.lower() == "worldwide" or country.lower() == "everywhere" or country.lower() == "anywhere" or country.lower() == "international" or country.lower() == "internationally" or country.lower() == "globally" or country.lower() == "current":
    country = "current_"
  else:
    country = country + "-"
  driver.get("https://www.worldometers.info/world-population/")
  wait = WebDriverWait(driver,1)
  try:
    while True:
      item = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span[rel='"+country.lower()+"population']"))).text
      if "retrieving data" not in item:
        break
    embed = discord.Embed(title="Population statistics of "+country.rstrip("-"))
    embed.add_field(name="Population", value=item, inline=False)
    if country == "current_":
      embed = discord.Embed(title="Population statistics worldwide", description="Total Population: "+item)
      while True:
        item = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span[rel='births_today']"))).text
        if "retrieving data" not in item:
          break
      embed.add_field(name="DAILY: Births", value=item, inline=True)
      while True:
        item = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span[rel='dth1s_today']"))).text
        if "retrieving data" not in item:
          break
      embed.add_field(name="Deaths", value=item, inline=True)
      while True:
        item = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span[rel='absolute_growth']"))).text
        if "retrieving data" not in item:
          break
      embed.add_field(name="Net growth", value=item, inline=True)
      while True:
        item = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span[rel='births_this_year']"))).text
        if "retrieving data" not in item:
          break
      embed.add_field(name="ANNUALLY: Births", value=item, inline=True)
      while True:
        item = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span[rel='dth1s_this_year']"))).text
        if "retrieving data" not in item:
          break
      embed.add_field(name="Deaths", value=item, inline=True)
      while True:
        item = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span[rel='absolute_growth_year']"))).text
        if "retrieving data" not in item:
          break
      embed.add_field(name="Net Growth", value=item, inline=True)
    await ctx.send(embed=embed)
  except selenium.common.exceptions.TimeoutException:
    await ctx.send("Invalid country. Please try again.")

@commands.command()
async def screenshot(ctx, url = None, form = "all"):
  await ctx.channel.trigger_typing()
  driver = webdriver.Chrome(options=options)
  if url == None:
    await ctx.send("Invalid format! Please use the format `=screenshot [url]`.")
  else:
    driver.get(url)
    if form == "short" or form == "first" or form == "normal" or form == "regular" or form == "basic" or form == "general" or form == "all":
      driver.set_window_size(1440,900)
      driver.get_screenshot_as_file('web_screenshot1.png')
      await ctx.send(file=discord.File('web_screenshot1.png'))
      os.remove('web_screenshot1.png')
    if form == "everything" or form == "full" or form == "entire" or form == "whole" or form == "all":
      S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
      driver.set_window_size(S('Width'),S('Height'))
      driver.get_screenshot_as_file('web_screenshot2.png')
      await ctx.send(file=discord.File('web_screenshot2.png'))
      os.remove('web_screenshot2.png')
    driver.quit()

def setup(bot):
  bot.add_command(covid)
  bot.add_command(html)
  bot.add_command(map)
  bot.add_command(markdown)
  bot.add_command(population)
  bot.add_command(screenshot)
