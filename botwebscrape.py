from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from discord import Webhook, RequestsWebhookAdapter
from selenium.webdriver.common.by import By
from discord_webhook import DiscordWebhook
from discord.ext.commands import *
from discord.ext import commands
import matplotlib.pyplot as plt
from markdown2 import Markdown
from selenium import webdriver
from bs4 import BeautifulSoup
import numpy as np
import requests
import discord
import re
markdowner = Markdown(extras=["strike", "footnotes"])
html_pattern = re.compile(r'^\`\`\`(html)?\n[\s\S]*\`\`\`$')
md_pattern = re.compile(r'^\`\`\`(md|markdown)?\n[\s\S]*\`\`\`$')

def func(pct, allvals):
  absolute = int(pct/100*np.sum(allvals))
  return "{:d} ({:.1f}%)".format(absolute, pct)

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

def botmd(mdcode):
  match = md_pattern.fullmatch(mdcode)
  if match:
    mdcode = mdcode.replace("```md","", 1)
    code = mdcode.replace("```","")
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
  driver.quit()

def bothtml(code):
  match = html_pattern.fullmatch(code)
  if match:
    code = code.replace("```html","", 1)
    code = code.replace("```","")
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
  driver.quit()

def botscreenshot(url, form):
  driver = webdriver.Chrome(options=options)
  if url == None:
    return "Invalid format! Please use the format `=screenshot [url]`."
  else:
    driver.get(url)
    if form == "short" or form == "first" or form == "normal" or form == "regular" or form == "basic" or form == "general" or form == "all":
      driver.set_window_size(1440,900)
      driver.get_screenshot_as_file('web_screenshot1.png')
    if form == "everything" or form == "full" or form == "entire" or form == "whole" or form == "all":
      S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
      driver.set_window_size(S('Width'),S('Height'))
      driver.get_screenshot_as_file('web_screenshot2.png')
    driver.quit()

def botcovid(country : str):
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
    plt.pie(y, labels = mylabels, colors = mycolors, autopct=lambda pct: func(pct, y), textprops = {'color':"#707070"}, pctdistance=0.7)
    plt.legend(loc="lower right")
    plt.savefig("pc1.png", transparent=True)
    plt.clf()
    mylabels = ["Non-infected", "Infected"]
    mycolors = ["#A0A0A0", "#FF5252"]
    y = np.array([int(tpopulation.replace(",",""))-int(tcases.replace(",","")), int(tcases.replace(",",""))])
    plt.pie(y, labels = mylabels, colors = mycolors, autopct=lambda pct: func(pct, y), textprops = {'color':"#707070"}, pctdistance=0.5)
    plt.legend(loc="lower right")
    plt.savefig("pc2.png", transparent=True)
    plt.clf()
    filelist = [discord.File("pc1.png"), discord.File("pc2.png")]
    embed.set_thumbnail(url="attachment://pc2.png")
    embed.set_image(url="attachment://pc1.png")
    return [filelist, embed]
    os.remove('pc1.png')
    os.remove('pc2.png')
  else:
    return "Invalid country. Please try again."

def botpopulation(country : str):
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
    return embed
  except selenium.common.exceptions.TimeoutException:
    return "Invalid country. Please try again."
