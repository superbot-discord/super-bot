from bs4 import BeautifulSoup
import requests
import discord
import re

def botdog(number):
  if number == 1:
    r=requests.get(f"https://dog.ceo/api/breeds/image/random")
    link=re.sub('{"message":"([\s\S]*?)","status":"success"}', r'\1', r.content.decode("utf-8"))
    open('dog.jpg', 'w').write(requests.get(link).content)
    desc = [discord.File('dog.jpg')]
  else:
    desc = []
    for count in range(1, number+1):
      r=requests.get(f"https://dog.ceo/api/breeds/image/random")
      link=re.sub('{"message":"([\s\S]*?)","status":"success"}', r'\1', r.content.decode("utf-8"))
      fname = 'dog' + str(count) + '.jpg'
      open(fname, 'w').write(requests.get(link).content)
      desc.append(discord.File(fname))
  return desc
