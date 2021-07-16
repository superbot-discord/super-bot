from bs4 import BeautifulSoup
import requests
import discord
import re

def botdog(number):
  if number == 1:
    r=requests.get(f"https://dog.ceo/api/breeds/image/random")
    link=re.sub('{"message":"([\s\S]*?)","status":"success"}', r'\1', r.content.decode("utf-8"))
    link=link.replace("\\", "")
    desc = link
  else:
    desc = ""
    for count in range(1, number+1):
      r=requests.get(f"https://dog.ceo/api/breeds/image/random")
      link=re.sub('{"message":"([\s\S]*?)","status":"success"}', r'\1', r.content.decode("utf-8"))
      desc += f"link\n"
  return desc
