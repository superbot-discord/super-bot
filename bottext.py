import base64
import hashlib
import random as ra
import re
from datetime import datetime
from difflib import SequenceMatcher

import discord as discord
import emojis as em
import pytz
from discord.ext import commands
from unicode_charnames import search_charnames, charname, codepoint

from shared import *

@commands.command(aliases=["lower", "upper", "capital", "capitalise", "capitalize", "lowercase", "lower_case", "uppercase", "upper_case"])
async def case(ctx, *, text):
  f = open("output.txt", "w")
  f.write(f"UPPERCASE\n{text.upper()}\n\nLOWERCASE\n{text.lower()}\n\nTITLE CASE\n{text.title()}")
  f.close()
  await ctx.send(file=discord.File('output.txt'))
  os.remove('output.txt')

@commands.command()
async def choice(ctx,*options):
  ti="Random choice"
  rand=ra.choice(options)
  desc="Your random option is "+rand
  embed=discord.Embed(title=ti, description=desc)
  await ctx.reply(embed=embed)

@commands.command()
async def decode(ctx, code, *, text):
  if SequenceMatcher(None, code, 'base64').ratio()>0.6:
    coder = base64.b64decode(bytes(text, encoding='utf-8'))
    await ctx.reply(coder.decode("utf-8"))
  elif SequenceMatcher(None, code, 'base32').ratio()>0.6:
    coder = base64.b32decode(bytes(text, encoding='utf-8'))
    await ctx.reply(coder.decode("utf-8"))
  elif SequenceMatcher(None, code, 'base16').ratio()>0.6:
    coder = base64.b16decode(bytes(text, encoding='utf-8'))
    await ctx.reply(coder.decode("utf-8"))
  elif SequenceMatcher(None, code, 'caesar').ratio()>0.6 or code.startswith("caesar"):
    encrypted = ""
    distance = int(code.replace("caesar", "", 1))
    for count in text:
      encrypted += chr(ord(count) - distance % 128)
    await ctx.reply(encrypted)
  else:
    await ctx.reply("Encoding not found!")

@commands.command()
async def emoji(ctx, *, text):
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
  await ctx.reply(text)

@commands.command()
async def encode(ctx, code, *, text):
  if SequenceMatcher(None, code, 'sha512').ratio()>0.6:
    coder = hashlib.sha512()
    coder.update(bytes(text, encoding='utf-8'))
    await ctx.reply(coder.hexdigest())
  elif SequenceMatcher(None, code, 'sha384').ratio()>0.6:
    coder = hashlib.sha384()
    coder.update(bytes(text, encoding='utf-8'))
    await ctx.reply(coder.hexdigest())
  elif SequenceMatcher(None, code, 'sha256').ratio()>0.6:
    coder = hashlib.sha256()
    coder.update(bytes(text, encoding='utf-8'))
    await ctx.reply(coder.hexdigest())
  elif SequenceMatcher(None, code, 'sha224').ratio()>0.6:
    coder = hashlib.sha224()
    coder.update(bytes(text, encoding='utf-8'))
    await ctx.reply(coder.hexdigest())
  elif SequenceMatcher(None, code, 'sha128').ratio()>0.6:
    coder = hashlib.sha1()
    coder.update(bytes(text, encoding='utf-8'))
    await ctx.reply(coder.hexdigest())
  elif SequenceMatcher(None, code, 'base64').ratio()>0.6:
    coder = base64.b64encode(bytes(text, encoding='utf-8'))
    await ctx.reply(coder.decode("utf-8"))
  elif SequenceMatcher(None, code, 'base32').ratio()>0.6:
    coder = base64.b32encode(bytes(text, encoding='utf-8'))
    await ctx.reply(coder.decode("utf-8"))
  elif SequenceMatcher(None, code, 'base16').ratio()>0.6:
    coder = base64.b16encode(bytes(text, encoding='utf-8'))
    await ctx.reply(coder.decode("utf-8"))
  elif SequenceMatcher(None, code, 'caesar').ratio()>0.6 or code.startswith("caesar"):
    encrypted = ""
    distance = int(code.replace("caesar", "", 1))
    for count in text:
      encrypted += chr(ord(count) + distance % 128)
    await ctx.reply(encrypted)
  else:
    await ctx.reply("Encoding not found!")
  
@commands.command()
async def insert(ctx,emoji, *, text):
  text=text.replace(" "," "+emoji+" ")
  await ctx.reply(text)

@commands.command()
async def length(ctx, *, text):
  full_analysis = f"Freq.\tCharacter\n"
  length_analysis = {}
  for count in text:
    length_analysis[count] = length_analysis.get(count, 0) + 1
  length_analysis = {count1: count2 for count1, count2 in sorted(length_analysis.items(), key=lambda item: item[1], reverse=True)}
  for count1, count2 in length_analysis.items():
    full_analysis += f"{count2}\t{count1}\n"
  f = open('analysis.txt', 'a')
  f.write(full_analysis)
  f.close()
  desc = f"The piece of text contains {len(text)} characters."
  length_msg = await ctx.reply(desc, file=discord.File('analysis.txt'))
  os.remove('analysis.txt')
  desc += f"\n**Most common characters:**\n"
  for (count1, count2),count3 in zip(length_analysis.items(), range(5)):
    desc += f"`{count1}` ({count2})\n"
  desc += f"\n**Least common characters:**\n"
  for count1, count2,count3 in zip(reversed(length_analysis.keys()), reversed(length_analysis.values()), range(5)):
    desc += f"`{count1}` ({count2})\n"
  await length_msg.edit(desc)

@commands.command()
async def pick(ctx, lower:int, upper:int, times:int):
  ti=f"{times} random number(s) between {lower} and {upper}"
  desc=f"Your random number(s) is/are:\n"
  if lower > upper:
    lower, upper = upper, lower
  upper_length = len(str(upper))
  if times <= (upper-lower+1):
    rand = list(range(lower, upper+1))
    ra.shuffle(rand)
    for count,count2 in zip(range(times), rand):
      desc += f"||`{str(count2).zfill(upper_length)}`||  "
  else:
    for count in range(times):
      desc += f"||`{str(ra.randint(lower,upper)).zfill(upper_length)}`||  "
  embed=discord.Embed(title=ti, description=desc)
  await ctx.reply(embed=embed)

@commands.command()
async def random(ctx,lower:int,upper:int):
  ti=f"Random number between {lower} and {upper}"
  rand=ra.randint(lower,upper)
  rand=str(rand)
  desc="Your random number is "+rand
  embed=discord.Embed(title=ti, description=desc)
  await ctx.reply(embed=embed)

@commands.command()
async def raffle(ctx,lower:int,upper:int,times:int):
  ti=f"{times} random number(s) between {lower} and {upper}"
  desc=f"Your random number(s) is/are:\n"
  for count in range(times):
    rand=ra.randint(lower,upper)
    desc += f"||`{str(rand).zfill(len(str(upper)))}`||  "
  embed=discord.Embed(title=ti, description=desc)
  await ctx.reply(embed=embed)

@commands.command()
async def rawspoiler(ctx, *, text):
  text="\|\|\|\|".join(text)
  text="\|\|"+text+"\|\|"
  await ctx.reply(text)

@commands.command()
async def rawrawspoiler(ctx, *, text):
  text="\\\|\\\|\\\|\\\|".join(text)
  text="\\\|\\\|"+text+"\\\|\\\|"
  await ctx.reply(text)

@commands.command()
async def reverse(ctx, *, text):
  await ctx.reply(text[::-1])

@commands.command()
async def spoiler(ctx,*,text):
  text="||||".join(text)
  await ctx.reply(f"||{text}||")

@commands.command(aliases=['antispoiler', 'antispoilers', 'aspoiler', 'aspoilers', 'spoils'])
async def spoil(ctx, *, text):
  await ctx.reply(text.replace("||", ""))

@commands.command()
async def unicode(ctx, *, query):
  allchars = search_charnames(query)
  embed = discord.Embed(title = f"Search results for: {query}")
  should_add_character = len(query) == 1
  for count, count2 in zip(allchars, range(24 if should_add_character else 25)):
    embed.add_field(name = count[1].title(), value = f"U+{count[0]} `{eval(f'u\' \\u{count[0]}\'')}`")
  if should_add_character:
    embed.add_field(name = charname(query), value = f"U+{codepoint(query)} `{eval(f'u\' \\u{codepoint(query)}\'')}`")
  await ctx.reply(embed=embed)

@commands.command(aliases=["timestamp", "posix"])
async def unix(ctx, *, text = "now"):
  now = datetime.now()
  dateParts = {
    m[-1]: int(m[:-1])
    for m in re.findall(r'([\d]{1,4}[yMdhms]{1})', text)
  }
  if text.startswith("now") or SequenceMatcher(None, text, "now").ratio()>0.65:
    dt2=now
  else:
    dt2 = datetime(
      dateParts.get('y', now.year),   dateParts.get('M', now.month),
      dateParts.get('d', now.day),    dateParts.get('h', now.hour),
      dateParts.get('m', now.minute), dateParts.get('s', now.second))
  dt2 = pytz.timezone('UTC').localize(dt2)
  seconds = round((dt2-dt1).total_seconds())
  await ctx.reply(f"`<t:{seconds}>` | <t:{seconds}>\n`<t:{seconds}:F>` | <t:{seconds}:F>\n`<t:{seconds}:f>` | <t:{seconds}:f>\n`<t:{seconds}:D>` | <t:{seconds}:D>\n`<t:{seconds}:d>` | <t:{seconds}:d>\n`<t:{seconds}:T>` | <t:{seconds}:T>\n`<t:{seconds}:t>` | <t:{seconds}:t>\n`<t:{seconds}:R>` | <t:{seconds}:R>")

def setup(bot):
  bot.add_command(case)
  bot.add_command(choice)
  bot.add_command(decode)
  bot.add_command(emoji)
  bot.add_command(encode)
  bot.add_command(insert)
  bot.add_command(length)
  bot.add_command(pick)
  bot.add_command(raffle)
  bot.add_command(random)
  bot.add_command(rawspoiler)
  bot.add_command(rawrawspoiler)
  bot.add_command(reverse)
  bot.add_command(spoiler)
  bot.add_command(spoil)
  bot.add_command(unicode)
  bot.add_command(unix)
