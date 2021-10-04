import os
import re
from datetime import datetime, timedelta

import pytz
from bs4 import BeautifulSoup
from PIL import Image

import discord as discord
import requests as requests
from discord.ext import commands

set(pytz.all_timezones_set)
hexstring_pattern = re.compile(r'#?([0-9A-F]{2})([0-9A-F]{2})([0-9A-F]{2})', re.IGNORECASE)
rgbtoper = lambda input: str(round(input/0.0255)/100)+"%"

@commands.command(aliases=["colour"])
async def color(ctx, *, name):
  colors = re.split(',|\s|;|/|\||\\|&', name)
  match = hexstring_pattern.fullmatch(colors[0])
  if all(arg and arg.isdigit() and 0 <= int(arg) < 256 for arg in colors) and len(colors)>2:
    r, g, b = map(int, colors)
  elif colors[0].isdigit() and 0 <= int(colors[0]) < 2 ** 24:
    n = int(colors[0])
    r, g, b = n >> 16, (n >> 8) & 255, n & 255
  elif match:
    r, g, b = (int(val, 16) for val in match.groups())
  else:
    await ctx.reply("Please specify a correct colour value.")
    return
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
  img = Image.new('RGB', (64, 64), (r, g, b))
  img.save('color.png')
  await ctx.reply(embed=embed, file=discord.File('color.png'))
  os.remove('color.png')

@commands.command()
async def regex(ctx, regularexp, *, text):
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
  await ctx.reply(embed=embed)

@commands.command()
async def regsub(ctx, regular1, regular2, *, text):
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
  await ctx.reply(embed=embed)

@commands.command()
async def time(ctx, *, timezoneinput="0"):
  if timezoneinput.replace(".","").isnumeric():
    timezone=float(timezoneinput)
    if 15>timezone>-15 and timezone%0.25==0:
      tnow = datetime.now() + timedelta(minutes = int(timezone*60))
      await ctx.reply(f"Time in UTC {timezoneinput} is {tnow.strftime('%d %B %Y (%A), %H:%M:%S')}")
    else:
      return "Invalid timezone! Timezone must be below 15, above -15 and divisible by 0.25."
  elif timezoneinput=="all":
    desc = f"**[ISO 3166 Country Codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements)**:\n```AD AE AF AG AI AL AM AO AQ AR AS AT AU AW AX AZ BA BB BD BE BF BG BH BI BJ BL BM BN BO BQ BR BS BT BV BW BY BZ CA CC CD CF CG CH CI CK CL CM CN CO CR CU CV CW CX CY CZ DE DJ DK DM DO DZ EC EE EG EH ER ES ET FI FJ FK FM FO FR GA GB GD GE GF GG GH GI GL GM GN GP GQ GR GS GT GU GW GY HK HM HN HR HT HU ID IE IL IM IN IO IQ IR IS IT JE JM JO JP KE KG KH KI KM KN KP KR KW KY KZ LA LB LC LI LK LR LS LT LU LV LY MA MC MD ME MF MG MH MK ML MM MN MO MP MQ MR MS MT MU MV MW MX MY MZ NA NC NE NF NG NI NL NO NP NR NU NZ OM PA PE PF PG PH PK PL PM PN PR PS PT PW PY QA RE RO RS RU RW SA SB SC SD SE SG SH SI SJ SK SL SM SN SO SR SS ST SV SX SY SZ TC TD TF TG TH TJ TK TL TM TN TO TR TT TV TW TZ UA UG UM US UY UZ VA VC VE VG VI VN VU WF WS YE YT ZA ZM ZW```\nIn addition, **[TZ Database Names](http://worldtimeapi.org/api/timezone.txt)** and **UTC Timezone Numbers** (between -15 and 15, divisible by 0.25) are supported."
    embed = discord.Embed(title="All Timezones", description=desc)
    await ctx.reply(embed=embed)
  elif len(timezoneinput)==2 and timezoneinput.isalpha():
    try:
      tz = pytz.timezone(pytz.country_timezones[timezoneinput][0])
      await ctx.reply(f"Time in {pytz.country_timezones(timezoneinput)[0]} is {datetime.now(tz=tz).strftime('%d %B %Y (%A), %H:%M:%S')}")
    except:
      await ctx.reply("Timezone not found. Please use `=time all` for a list of all timezones.")
  else:
    try:
      tz = pytz.timezone(timezoneinput)
      await ctx.reply(f"Time in {timezoneinput} is {datetime.now(tz=tz).strftime('%d %B %Y (%A), %H:%M:%S')}")
    except:
      await ctx.reply("Timezone not found. Please use `=time all` for a list of all timezones.")

def setup(bot):
  bot.add_command(color)
  bot.add_command(regex)
  bot.add_command(regsub)
  bot.add_command(time)
