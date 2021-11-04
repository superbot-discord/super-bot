import base64
import hashlib

import emojis as em
import pytz
from unicode_charnames import search_charnames, charname, codepoint
from spellwise import Typox
from shared import *

spell_checker = Typox()
spell_checker.add_from_path("fonts/dictionary.txt")

@commands.command(aliases=["lower", "upper", "capital", "capitalise", "capitalize", "lowercase", "lower_case", "uppercase", "upper_case"])
async def case(ctx, *, text):
  f = open("output.txt", "w")
  f.write(f"UPPERCASE\n{text.upper()}\n\nLOWERCASE\n{text.lower()}\n\nTITLE CASE\n{text.title()}")
  f.close()
  await ctx.reply(file=discord.File('output.txt'))
  try_delete('output.txt')

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
  elif SequenceMatcher(None, code, 'sha1').ratio()>0.6:
    coder = hashlib.sha1()
    coder.update(bytes(text, encoding='utf-8'))
    await ctx.reply(coder.hexdigest())
  elif SequenceMatcher(None, code, 'blake2b').ratio()>0.9:
    coder = hashlib.blake2b()
    coder.update(bytes(text, encoding='utf-8'))
    await ctx.reply(coder.hexdigest())
  elif SequenceMatcher(None, code, 'blakes2s').ratio()>0.9:
    coder = hashlib.blake2s()
    coder.update(bytes(text, encoding='utf-8'))
    await ctx.reply(coder.hexdigest())
  elif SequenceMatcher(None, code, 'base64').ratio()>0.8:
    coder = base64.b64encode(bytes(text, encoding='utf-8'))
    await ctx.reply(coder.decode("utf-8"))
  elif SequenceMatcher(None, code, 'base32').ratio()>0.8:
    coder = base64.b32encode(bytes(text, encoding='utf-8'))
    await ctx.reply(coder.decode("utf-8"))
  elif SequenceMatcher(None, code, 'base16').ratio()>0.8:
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
  f.flush()
  f.close()
  desc = f"The piece of text contains {len(text)} characters."
  length_msg = await ctx.reply(desc, file=discord.File('analysis.txt'))
  try_delete('analysis.txt')
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
async def spellcheck(ctx, text, distance : typing.Optional[int] = 3, *, disposed = None):
  results = spell_checker.get_suggestions(text, max_distance = distance)
  desc = f"QWERTY-spellchecking results for {text}"
  distances = {count["distance"] for count in results}
  for count in distances:
    desc += f"\n\nDISTANCE: {count+1}\n{', '.join([count3 for count3 in [count4['word'] for count4 in results if count4['distance'] == count]])}"
  f = open("output.txt", "w")
  f.write(desc)
  f.flush()
  f.close()
  await ctx.reply(file = discord.File("output.txt"))
  try_delete("output.txt")

@commands.command()
async def spoiler(ctx, *, text):
  text="||||".join(text)
  await ctx.reply(f"||{text}||")

@commands.command(aliases=['antispoiler', 'antispoilers', 'aspoiler', 'aspoilers', 'spoils'])
async def spoil(ctx, *, text):
  await ctx.reply(text.replace("||", ""))

@commands.command()
async def unicode(ctx, *query):
  embed = discord.Embed(title = f"Search results for: {' '.join(query)}")
  all_results = []
  for count in query:
    current_results = []
    for count in search_charnames(count):
      current_results.append(count)
    all_results.append(current_results)
  intersected_results = []
  x=sum(all_results, [])
  for count in x:
    if count not in intersected_results and all([count in y for y in all_results]):
      intersected_results.append(count)
  characters_added = int(len(query[0]) == 1)
  try:
    hex_character = chr(int(query[0], 16))
    characters_added += 1
    add_hex_character = True
  except:
    add_hex_character = False
  for count, count2 in zip(intersected_results, range(25-characters_added)):
    embed.add_field(name = count[1].title(), value = f"U+{count[0]} `"+eval(f'u\'\\u{count[0]}\'')+"`")
  desc = f"Code\tChar.\tName\n\n"
  for count in intersected_results:
    desc += f"U+{count[0]}\t" + eval(f'u\'\\u{count[0]}\'') + f"\t{count[1].title()}\n"
  if int(len(query[0]) == 1):
    embed.add_field(name = f"INPUT - {charname(query[0]).title()}", value = f"U+{codepoint(charname(query[0]))} `"+eval(f'u\'\\u{codepoint(charname(query[0]))}\'')+"`")
    desc += f"U+{codepoint(charname(query[0]))}\t" + eval(f'u\'\\u{codepoint(charname(query[0]))}\'') + f"\t{charname(query[0]).title()}"
  if add_hex_character:
    try:
      embed.add_field(name = f"HEX - {charname(hex_character).title()}", value = f"U+{codepoint(charname(hex_character))} `"+eval(f'u\'\\u{codepoint(charname(hex_character))}\'')+"`")
      desc += f"U+{codepoint(charname(hex_character))}\t" + eval(f'u\'\\u{codepoint(charname(hex_character))}\'') + f"\t{charname(hex_character).title()}"
    except:
      pass
  f = open("unicode.txt", 'w')
  f.write(desc)
  f.flush()
  f.close()
  await ctx.reply(embed=embed, file=discord.File("unicode.txt"))
  try_delete("unicode.txt")

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
  bot.add_command(spellcheck)
  bot.add_command(spoiler)
  bot.add_command(spoil)
  bot.add_command(unicode)
  bot.add_command(unix)
