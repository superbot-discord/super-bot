from bs4 import BeautifulSoup
import requests
import re

def botcat(number):
  desc = ""
  for count in range(0, number):
    r=requests.get(f"https://dog.ceo/api/breeds/image/random")
    link=re.sub('{"message":"([\s\S]*?)","status":"success"}', r'\1', r.content.decode("utf-8"))
    desc += link + "\n"
  return desc
