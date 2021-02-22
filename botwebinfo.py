import discord
from pygoogletranslation import Translator
from PyDictionary import PyDictionary
import wikipedia
from bs4 import BeautifulSoup
import requests
import re
dictionary=PyDictionary()
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

def botminecraft(item):
  r=requests.get('https://minecraft.gamepedia.com/'+item)
  soup=BeautifulSoup(r.content, features="html.parser")
  table = soup.findAll('table')[0].findAll('tbody')[0]
  renewable = table.findAll('tr')[0].findAll('td')[0].findAll('p')[0].string.replace(f"\n","")
  stackable = table.findAll('tr')[1].findAll('td')[0].findAll('p')[0].string.replace(f"\n","")
  blastr = table.findAll('tr')[3].findAll('td')[0].findAll('p')[0].string.replace(f"\n","")
  hardness = table.findAll('tr')[4].findAll('td')[0].findAll('p')[0].string.replace(f"\n","")
  luminant = table.findAll('tr')[5].findAll('td')[0].findAll('p')[0].string.replace(f"\n","")
  transparent = table.findAll('tr')[6].findAll('td')[0].findAll('p')[0].string.replace(f"\n","")
  flammable = table.findAll('tr')[7].findAll('td')[0].findAll('p')[0].string.replace(f"\n","")
  cffl = table.findAll('tr')[8].findAll('td')[0].findAll('p')[0].string.replace(f"\n","")
  desc=str(soup.findAll('p')[9])
  desc = re.sub(r'/<a href="\/([\s\S]*?)" title="([\s\S]*?)">([\w]*)<\/a>/g', r'[\3](https://minecraft.gamepedia.com/\1)', desc)
  desc = re.sub(r'/<b>([\s\S]*?)<\/b>/g', r'**\1**', desc)
  embed = discord.Embed(title = "Minecraft: "+item, desc=desc)
  embed.add_field(name="Renewable?", value=renewable)
  embed.add_field(name="Stackable?", value=stackable)
  embed.add_field(name="Luminant?", value=luminant)
  embed.add_field(name="Transparent?", value=transparent)
  embed.add_field(name="Flammable?", value=flammable)
  embed.add_field(name="Burns with lava?", value=cffl)
  embed.add_field(name="Blast Resistance", value=blastr)
  embed.add_field(name="Hardness", value=hardness)
  return embed

def bottranslate(langinput, text):
  if langinput == "list" or langinput == "all":
    embed1 = discord.Embed(description = f"**List of Language Input (Abbreviations)**\n`"+"  ".join(list(langdict.keys()))+f"`\n\n**List of Language Input (Full Names)**\n`"+"` `".join(list(langdict.values())))
    embed2 = discord.Embed(description = f"**List of Language Output (Abbreviations)**\n`"+"  ".join(list(srclangdict.keys()))+f"`\n\n**List of Language Output (Full Names)**\n`"+"` `".join(list(srclangdict.values()))+"`")
    return [embed1, embed2]
  else:
    if langinput.count(",")==1:
      lang = langinput.split(",")[0]
      fromlang = langinput.split(",")[1]
      if list(srclangdict.values()).count(fromlang) == 1:
        fromlang = list(srclangdict.keys())[list(srclangdict.values()).index(fromlang)]
    else:
      fromlang = "auto"
      lang = langinput
    if list(langdict.values()).count(lang) == 1:
      lang = list(langdict.keys())[list(langdict.values()).index(lang)]
    translation = translatorvar.translate(text, src=fromlang, dest=lang)
    try:
      return "**Translation from "+srclangdict[translatorvar.detect(text).lang]+" to "+langdict[lang]+f":**\n"+translation.text.replace("u003c", "<").replace("u003e", ">").replace("u0026", "&")
    except:
      return "Language not found! Please use `=translate list` to get a list of languages."

def botwiki(query):
  totallen = 0
  try:
    desc = wikipedia.summary(query)[:2047]
    totallen = totallen + len(wikipedia.summary(query)) + len(desc) + len(query)
    wpage = wikipedia.page(title=query, auto_suggest=True, redirect=True, preload=False)
    embed = discord.Embed(title=query, url="https://en.wikipedia.org/wiki/"+wpage.title.replace(" ","_"), description=desc)
    print(wpage.sections)
    counter = 0
    for count in wpage.sections:
      if counter >=4 or totallen + len(wpage.section(count)) >= 6000:
        break
      if len(wpage.section(count))!=0:
        embed.add_field(name=count, value=wpage.section(count)[:499], inline=False)
        totallen = totallen + len(wpage.section(count))
        counter = counter + 1
    if len(wpage.images)>=1:
      embed.set_thumbnail(url = wpage.images[0])
    if len(wpage.images)>=2:
      embed.set_image(url = wpage.images[1])
  except:
    results = wikipedia.search(query, results=20, suggestion=False)
    desc = "**Please make one of these searches:**"
    for count in results:
      desc = desc + "`"+str(count)+"` "
    embed = discord.Embed(title=query, description=desc)
  return embed

def botdefinition(word):
  try:
    ti = "Definition of "+word
    desc = ""
    definitions = dictionary.meaning(word)
    counter = 0
    for count in list(definitions.keys()):
      desc = desc + "**"+count+f"**\n"+definitions[count][counter]+f"\n"
      counter = counter + 1
    desc = desc + f"**Synonyms**\n"
    for count in dictionary.synonym(word):
      desc = desc + count + ", "
    desc = desc[:-2]
    desc = desc + f"\n**Antonyms**\n"
    for count in dictionary.antonym(word):
      desc = desc + count + ", "
    desc = desc[:-2]
    embed = discord.Embed(title=ti, description=desc)
    return embed
  except:
    return "Invalid word. Please try again."
