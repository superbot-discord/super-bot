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

def botunscramble(text, ilength):
  try:
    ilength = int(ilength)
  except:
    ilength = 0
  if ilength != 0 and ilength > len(text):
    ilength = 0
  r=requests.get(f"https://wordunscrambler.me/unscramble/{text}")
  soup=BeautifulSoup(r.content, features="html.parser")
  raw_everything = soup.findAll('a', target="_blank")[:-7]
  everything = []
  for count in raw_everything:
    everything.append(count.text)
  output = discord.Embed(title=f"Unscrambled results for {text}")
  _sorted = {}
  for count in everything:
    _sorted.setdefault(len(count), []).append(count)
  print(_sorted)
  everything = list(_sorted.values())
  print(everything)
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
      
  file = open("output.txt", "w")
  file.write(text)
  file.close()
  return output

def botminecraft(item):
  r=requests.get('https://minecraft.fandom.com/wiki/'+item)
  soup=BeautifulSoup(r.content, features="html.parser")
  table = soup.findAll('table')[0].findAll('tbody')[0]
  results = soup.findAll("p")
  for count in results:
    if len(count.findAll('b')) != 0:
      desc = str(count)
      break
  try:
    print(desc)
    desc = re.sub(r'<a (class=".+?" )?href="\/([\w/]+?)" title="([\s\S]+?)">([\s\S]+?)<\/a>', r'[\4](https://minecraft.fandom.com/\2)', desc)
    desc = re.sub(r'<b>([\s\S]*?)<\/b>', r'**\1**', desc)
    desc = re.sub(r'<i>([\s\S]*?)<\/i>', r'*\1*', desc)
    desc = desc.replace("<p>", "").replace("</p>", "")
    desc = re.sub(r'<([a-z]+?)( ([a-z]+?)=".*?")*?>(.*?)<\/\1>', '', desc)
    embed = discord.Embed(title = "Minecraft: "+item, description=desc, url='https://minecraft.fandom.com/wiki/'+item)
    try:
      for count in table.findAll('tr'):
        if count.findAll('td')[0].text.replace("<p>", "").replace("</p>", "").replace(" ", "").replace("\n", "") != "":
          embed.add_field(name=count.findAll('th')[0].text.replace("<p>", "").replace("</p>", ""), value=count.findAll('td')[0].text.replace("<p>", "").replace("</p>", ""))
    except:
      1
    """for count in soup.findAll("h3"):
      if ["ID", "Metadata", "Share", "Views", "More", "Search", "Minecraft Wiki", "Games", "Useful pages", "Minecraft links", "Gamepedia", "Tools", "In other languages", "Namespaces", "Variants"].count(count.text.replace("[edit]", "")) == 0:
        desc = str(count.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element).replace("<p>", "").replace("</p>", "")
        desc = re.sub(r'<a (class=".+?" )?href="\/([\w/]+?)"( title="([\s\S]+?))?">([\s\S]+?)<\/a>', r'[\5](https://minecraft.fandom.com/\4)', desc)
        desc = re.sub(r'<b>([\s\S]*?)<\/b>', r'**\1**', desc)
        desc = re.sub(r'<i>([\s\S]*?)<\/i>', r'*\1*', desc)
        desc = re.sub(r'<([a-z]+?)( ([a-z]+?)=".*?")*?>([\s\S]*?)<\/\1>', '', desc)
        desc = re.sub(r'\s', '', desc)
        try:
          print(desc)
          if len(desc.replace(" ", "").replace(f"\n", "").replace("[edit]", "")) != 0:
            print("Check")
            embed.add_field(name=count.text.replace("[edit]", ""), value=desc, inline=False)
        except:
          1
    """
    results = soup.findAll("img")
    image = str(results[1])
    image = re.sub(r'<img alt=".*?"( class="thumbimage")? decoding="async" height="[\d]*?" src="([\s\S]*?)" width="[\d]*?"/>', r'\2', image)
    image = re.sub(r'(https:\/\/static.wikia.nocookie.net\/minecraft_gamepedia\/images\/[\S]*?\/[\S]*?\/[\w]*?\.[\w]{2,5}\/revision\/latest)\/scale-to-width-down\/\d{1,4}\?cb=(\d{5,30})', r'\1?cb=\2&format=original', image)
    embed.set_image(url = image)
    return embed
  except:
    desc = "No Wiki page with that name found."
    return desc

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
    #try:
    return "**Translation from "+srclangdict[fromlang]+" to "+langdict[lang]+f":**\n"+translation.text.replace("u003c", "<").replace("u003e", ">").replace("u0026", "&")
    #except:
    #  return "Language not found! Please use `=translate list` to get a list of languages."

def botwiki(query):
  totallen = 0
  try:
    desc = wikipedia.summary(query)[:2047]
    totallen = totallen + len(wikipedia.summary(query)) + len(desc) + len(query)
    wpage = wikipedia.page(title=query, auto_suggest=True, redirect=True, preload=False)
    embed = discord.Embed(title=query, url="https://en.wikipedia.org/wiki/"+wpage.title.replace(" ","_"), description=desc)
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
