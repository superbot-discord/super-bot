from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from PIL import Image
import emojis as em
import requests
import discord
import pytz
import re
set(pytz.all_timezones_set)
hexstring_pattern = re.compile(r'#?([0-9A-F]{2})([0-9A-F]{2})([0-9A-F]{2})', re.IGNORECASE)
rgbtoper = lambda input: str(round(input/0.0255)/100)+"%"

def botregex(regularexp, text):
  theregex = r"(?P<LargestCapturingGroup>"+regularexp+")"
  newtext = re.sub(theregex, "**\g<LargestCapturingGroup>**", text)
  matches = len(re.findall(theregex, text))
  if matches == 1:
    ti = "There was 1 occurrence."
  elif matches == 0:
    ti = "There was no occurrences."
  elif matches >= 2:
    ti = "There were "+str(matches)+" occurrences."
  embed = discord.Embed(title = ti, description = newtext.replace("****",""))
  embed.set_author(name="Match Results for "+regularexp)
  embed.set_footer(text="Match Results are highlighted in bold")
  return embed

def botregsub(regular1, regular2, text):
  newtext = re.sub(regular1, regular2, text)
  matches = len(re.findall(regular1, text))
  if matches == 1:
    ti = "There was 1 occurrence."
  elif matches == 0:
    ti = "There was no occurrences."
  elif matches >= 2:
    ti = "There were "+str(matches)+" occurrences."
  embed = discord.Embed(title = ti, description = "`"+newtext+"`")
  embed.set_author(name="Substitution Result for "+regular1)
  return embed

def botcolor(color):
  colors = re.split(',|\s|;|/|\||\\|&', color)
  match = hexstring_pattern.fullmatch(colors[0])
  if all(arg and arg.isdigit() and 0 <= int(arg) < 256 for arg in colors) and len(colors)>2:
    r, g, b = map(int, colors)
  elif colors[0].isdigit() and 0 <= int(colors[0]) < 2 ** 24:
    n = int(colors[0])
    r, g, b = n >> 16, (n >> 8) & 255, n & 255
  elif match:
    r, g, b = (int(val, 16) for val in match.groups())
  else:
    return "Please specify a correct colour value."
  r1, g1, b1 = (rgbtoper(r), rgbtoper(g), rgbtoper(b))
  deci = (r << 16) + (g << 8) + b
  hex_ = f'{deci:02x}'.upper()
  if len(hex_)!=6:
    while len(hex_)<6:
      hex_="0"+hex_
  page = requests.get('https://www.colorhexa.com/'+hex_)
  soup = BeautifulSoup(page.content, 'html.parser')
  result1 = soup.find(id='header-title')
  ti = re.sub(r'([\w]+?) \/ #[\da-f]{6} hex color',r'\1',result1.text)
  result2 = soup.find_all("strong")[2].text
  embed = discord.Embed(title='Colour information: '+ti, description=result2, color=deci)
  embed.add_field(name='RGB', value=f'{r}, {g}, {b}\n{r1}, {g1}, {b1}', inline=True)
  embed.add_field(name='Hex Code', value=f'#{hex_}', inline=True)
  embed.add_field(name='Decimal Value', value=deci, inline=True)
  embed.set_thumbnail(url='attachment://color.png')
  img = Image.new('RGB', (32, 32), (r, g, b))
  img.save('color.png')
  return embed

def botemoji(text):
  text = text.lower()
  text = text.replace(" ","   ")
  text = text.replace(" wc","🚾")
  text = text.replace(" ng","🆖")
  text = text.replace(" ok","🆗")
  text = text.replace(" up!","🆙")
  text = text.replace(" cool","🆒")
  text = text.replace(" new","🆕")
  text = text.replace(" free","🆓")
  text = text.replace(" tm","™️")
  text = text.replace(" id","🆔")
  text = text.replace(" vs","🆚")
  text = text.replace(" sos","🆘")
  text = text.replace(" (c)","©️")
  text = text.replace(" (r)","®️")
  text = text.replace("a","🇦 ").replace("b","🇧 ").replace("c","🇨 ").replace("d","🇩 ").replace("e","🇪 ")
  text = text.replace("f","🇫 ").replace("g","🇬 ").replace("h","🇭 ").replace("i","🇮 ").replace("j","🇯 ")
  text = text.replace("k","🇰 ").replace("l","🇱 ").replace("m","🇲 ").replace("n","🇳 ").replace("o","🇴 ")
  text = text.replace("p","🇵 ").replace("q","🇶 ").replace("r","🇷 ").replace("s","🇸 ").replace("t","🇹 ")
  text = text.replace("u","🇺 ").replace("v","🇻 ").replace("w","🇼 ").replace("x","🇽 ").replace("y","🇾 ").replace("z","🇿 ")
  text = text.replace(">||",":play_pause:")
  text = text.replace(">>|",":track_next:")
  text = text.replace("|<<",":track_previous:")
  text = text.replace("<->",":left_right_arrow:")
  text = text.replace("->",":arrow_right:")
  text = text.replace("<-",":arrow_left:")
  text = text.replace(">>",":fast_forward:")
  text = text.replace("<<",":rewind:")
  text = text.replace("||",":pause_button:")
  text = text.replace(">",":arrow_forward:")
  text = text.replace("<",":arrow_backward:")
  text = text.replace("!",":exclamation:")
  text = text.replace("?",":question:")
  text = text.replace("!!",":bangbang:")
  text = text.replace("!?",":interrobang:")
  text = text.replace("$",":heavy_dollar_sign:")
  text = text.replace("#",":hash:")
  text = text.replace("*",":asterisk:")
  text = text.replace("+",":heavy_plus_sign:")
  text = text.replace("-",":heavy_minus_sign:")
  text = text.replace("×",":heavy_multiplication_x:")
  text = text.replace("÷",":heavy_division_sign:")
  text = text.replace("1",":one:")
  text = text.replace("2",":two:")
  text = text.replace("3",":three:")
  text = text.replace("4",":four:")
  text = text.replace("5",":five:")
  text = text.replace("6",":six:")
  text = text.replace("7",":seven:")
  text = text.replace("8",":eight:")
  text = text.replace("9",":nine:")
  text = text.replace("0",":zero:")
  text = em.encode(text)
  return text

def bottime(timezoneinput):
  if timezoneinput.replace(".","").isnumeric():
    timezone=float(timezoneinput)
    if 15>timezone>-15 and timezone%0.25==0:
      tnow = datetime.now() + datetime.timedelta(minutes = int(timezoneinput*60))
      return "Time in UTC " + timezoneinput + " is " + tnow.strftime("%d %b, %Y (%a) %H:%M:%S")
    else:
      return "Invalid timezone! Timezone must be below 15, above -15 and divisible by 0.25."
  elif timezoneinput=="all":
    desc = f"**[ISO 3166 Country Codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements)**:\n```AD AE AF AG AI AL AM AO AQ AR AS AT AU AW AX AZ BA BB BD BE BF BG BH BI BJ BL BM BN BO BQ BR BS BT BV BW BY BZ CA CC CD CF CG CH CI CK CL CM CN CO CR CU CV CW CX CY CZ DE DJ DK DM DO DZ EC EE EG EH ER ES ET FI FJ FK FM FO FR GA GB GD GE GF GG GH GI GL GM GN GP GQ GR GS GT GU GW GY HK HM HN HR HT HU ID IE IL IM IN IO IQ IR IS IT JE JM JO JP KE KG KH KI KM KN KP KR KW KY KZ LA LB LC LI LK LR LS LT LU LV LY MA MC MD ME MF MG MH MK ML MM MN MO MP MQ MR MS MT MU MV MW MX MY MZ NA NC NE NF NG NI NL NO NP NR NU NZ OM PA PE PF PG PH PK PL PM PN PR PS PT PW PY QA RE RO RS RU RW SA SB SC SD SE SG SH SI SJ SK SL SM SN SO SR SS ST SV SX SY SZ TC TD TF TG TH TJ TK TL TM TN TO TR TT TV TW TZ UA UG UM US UY UZ VA VC VE VG VI VN VU WF WS YE YT ZA ZM ZW```\nIn addition, **[TZ Database Names](http://worldtimeapi.org/api/timezone.txt)** and **UTC Timezone Numbers** (between -15 and 15, divisible by 0.25) are supported."
    embed = discord.Embed(title="All Timezones", description=desc)
    return embed
  elif len(timezoneinput)==2 and timezoneinput.isalpha():
    try:
      tz = pytz.timezone(pytz.country_timezones[timezoneinput][0])
      return "Time in " + pytz.country_timezones(timezoneinput)[0] + " is " + datetime.now(tz=tz).strftime("%d %b, %Y (%a) %H:%M:%S")
    except:
      return "Timezone not found. Please use `=time all` for a list of all timezones."
  else:
    try:
      tz = pytz.timezone(timezoneinput)
      return "Time in " + timezoneinput + " is " + datetime.now(tz=tz).strftime("%d %b, %Y (%a) %H:%M:%S")
    except:
      return "Timezone not found. Please use `=time all` for a list of all timezones."
