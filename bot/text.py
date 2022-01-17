import base64
import collections
import hashlib

import bitarray
import emojis as em
import huffman
from spellwise import Typox
from unicode_charnames import charname, codepoint, search_charnames

from shared import *
from functions import *

spell_checker = Typox()
spell_checker.add_from_path("fonts/dictionary.txt")
allid=[]

@commands.command(aliases=["lower", "upper", "capital", "capitalise", "capitalize", "lowercase", "lower_case", "uppercase", "upper_case"])
async def case(ctx, *, text):
  f = open("output.txt", "w")
  f.write(f"UPPERCASE\n{text.upper()}\n\nLOWERCASE\n{text.lower()}\n\nTITLE CASE\n{text.title()}")
  f.close()
  await ctx.reply(file=discord.File('output.txt'))
  try_delete('output.txt')

@commands.command()
async def choice(ctx, *options): # T
  rand = ra.choice(options)
  desc = f"Your random option is {rand}"
  embed = discord.Embed(title= "Random choice", description= desc)
  await ctx.reply(embed= embed)

@commands.command()
async def compress(ctx, *, text):
  lengths = list(collections.Counter(text).items())
  huffman_encoder = huffman.codebook(lengths)
  compressed = ""
  for x in text:
    compressed += huffman_encoder[x]
  compressed_int = int(compressed, 2)
  compressed_bytes = compressed_int.to_bytes(len(compressed)//8+(len(compressed)%8>0), byteorder="big")
  f=open("compressed.txt", "wb")
  f.write(compressed_bytes)
  f.close()
  compress_key = ""
  for x, y in lengths:
    compress_key += x.replace("_", "UD")+f"{y}_"
  await ctx.reply(f"Estimated file size: {os.path.getsize('compressed.txt')} bytes\nKey:\n```\n{compress_key[:-1]}\n```", file = discord.File("compressed.txt"))
  try_delete("compressed.txt")

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
    for x in text:
      encrypted += chr(ord(x) - distance % 128)
    await ctx.reply(encrypted)
  else:
    await ctx.reply("Encoding not found!")

@commands.command()
async def decompress(ctx, *, key):
  if not ctx.message.attachments:
    await ctx.reply("The message does not include (that many) attachments.")
    return
  await ctx.message.attachments[0].save('decompress.txt')
  f=open("decompress.txt", "rb")
  decompress_bytes=f.read()
  f.close()
  try_delete("decompress.txt")
  lengths = []
  for x in key.split("_"):
    x=x.replace("UD", "_")
    lengths.append((x[0], int(x[1:])))
  huffman_encoder = huffman.codebook(lengths)
  for x, y in huffman_encoder.items():
    huffman_encoder[x] = bitarray.bitarray(y)
  x=bitarray.bitarray()
  x.frombytes(decompress_bytes)
  desc = ''.join(x.decode(huffman_encoder))
  await ctx.reply(f"```\n{desc}\n```")

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
    for x in text:
      encrypted += chr(ord(x) + distance % 128)
    await ctx.reply(encrypted)
  else:
    await ctx.reply("Encoding not found!")
  
@commands.command()
async def insert(ctx,emoji, *, text):
  text=text.replace(" "," "+emoji+" ")
  await ctx.reply(text)

@commands.command()
async def length(ctx, *, text):
  analysis = collections.Counter(text).items()
  desc = f"Freq.\tCharacter\n"+f"\n".join([f"{x[1]}\t{x[0]}" for x in analysis])
  f = open('analysis.txt', 'w')
  f.write(desc)
  f.flush()
  f.close()
  desc = f"The piece of text contains {len(text)} characters."
  length_msg = await ctx.reply(desc, file=discord.File('analysis.txt'))
  try_delete('analysis.txt')

@commands.command()
async def pick(ctx, lower: int, upper: int, times: int): # MS
  desc = ""
  if lower > upper:
    lower, upper = upper, lower
  upper_length = len(str(upper))
  if times <= (upper - lower + 1):
    rand = list(range(lower, upper + 1))
    ra.shuffle(rand)
    for x, y in zip(range(times), rand):
      desc += f"||`{str(y).zfill(upper_length)}`||  "
  else:
    for x in range(times):
      desc += f"||`{str(ra.randint(lower,upper)).zfill(upper_length)}`||  "
  embed=discord.Embed(title= f"{times} random number(s) between {lower} and {upper}", description= desc)
  await ctx.reply(embed= embed)

@commands.command()
async def quantum_random(ctx, size: typing.Literal['256', '65536'] = '256', amount: int = 1):
  api_size = {'256':8, '65536':16}[size]
  r=requests.get(f"https://qrng.anu.edu.au/API/jsonI.php?length={amount}&type=uint{api_size}").json()['data']
  r=[str(x) for x in r]
  desc=f"Your quantum random number(s) is/are:\n{', '.join(r)}"
  embed=discord.Embed(title=f"{amount} random number(s) between 0 and {int(size)-1}", description=desc)
  await ctx.reply(embed=embed)

# NON-QUANTUM RANDOM
# 7/12 migrated
# M: Multiple values   R: Can repeat   S: Spoilers   T: Text choices
#    One value            Cannot repeat   Unformatted   Integral choice(s)
# =random{_{m{r}}{s}{t}}

@commands.command()
async def random(ctx, lower: int, upper: int):
  await ctx.reply(f"Your random number is {ra.randint(lower,upper)}")

@commands.command()
async def random_m(ctx, times: int, lower: int, upper: int):
  if lower > upper:
    lower, upper = upper, lower
  if times <= (upper - lower + 1):
    desc = ""
    rand = list(range(lower, upper + 1))
    ra.shuffle(rand)
    for x, y in zip(range(times), rand):
      desc += f"{y}, "
  else:
    desc = ", ".join(ra.sample(range(lower, upper + 1), times))
  embed = discord.Embed(title= f"{times} random number(s) between {lower} and {upper}", description= desc)
  await ctx.reply(embed= embed)

@commands.command()
async def random_s(ctx, lower: int, upper: int):
  if lower > upper:
    lower, upper = upper, lower
  await ctx.reply(f"Your random number is ||`{x_fill(ra.randint(lower,upper), ' ', len(str(upper)))}`||.")

@commands.command()
async def random_t(ctx, *options):
  await ctx.reply(f"Your random choice is {ra.choice(options)}")

@commands.command()
async def random_mr(ctx, times: int, lower: int, upper: int):
  desc = ""
  if lower > upper:
    lower, upper = upper, lower
  zfill_length = len(str(upper))
  for x in range(times):
    desc += f"{ra.randint(lower,upper)}, "
  embed = discord.Embed(title= f"{times} random number(s) between {lower} and {upper}", description= desc)
  await ctx.reply(embed= embed)

@commands.command()
async def random_ms(ctx, times: int, lower: int, upper: int):
  desc = ""
  if lower > upper:
    lower, upper = upper, lower
  upper_length = len(str(upper))
  if times <= (upper - lower + 1):
    rand = list(range(lower, upper + 1))
    ra.shuffle(rand)
    for x, y in zip(range(times), rand):
      desc += f"||`{str(y).zfill(upper_length)}`||  "
  else:
    for x in range(times):
      desc += f"||`{str(ra.randint(lower,upper)).zfill(upper_length)}`||  "
  embed=discord.Embed(title=f"{times} random number(s) between {lower} and {upper}", description= desc)
  await ctx.reply(embed= embed)

@commands.command()
async def random_mt(ctx, times: int, *options):
  options = list(options) if isinstance(options, tuple) else [options]
  if times <= (len(options)):
    desc = ""
    ra.shuffle(options)
    for x, y in zip(range(times), options):
      desc += f"{y}, "
  else:
    desc = ", ".join(ra.sample(options, times))
  embed = discord.Embed(title= f"{times} random choice(s)", description= desc)
  await ctx.reply(embed= embed)

@commands.command()
async def raffle(ctx,lower: int, upper: int, amount: int): # MRS
  desc = ""
  if lower > upper:
    lower, upper = upper, lower
  upper_length = len(str(upper))
  for x in range(amount):
    rand = ra.randint(lower,upper)
    desc += f"||`{str(rand).zfill(upper_length)}`||  "
  embed=discord.Embed(title= f"{amount} random number(s) between {lower} and {upper}", description= desc)
  await ctx.reply(embed= embed)

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
async def rtimer(ctx, timetocount, *, Text = None):
  sec = int(timedelta(**{
    UNITS.get(m.group('unit').lower(), 'seconds'): int(m.group('val'))
    for m in re.finditer(r'(?P<val>\d+)(?P<unit>[smhdw]?)', timetocount, flags=re.I)
  }).total_seconds())
  end = datetime.now(timezone.utc) + timedelta(seconds = sec)
  seconds = int((end - datetime.now(timezone.utc)).total_seconds())
  idcode = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]
  exec(f"terminate{idcode.lower()}{ctx.guild.id}=0",globals())
  newidcode=idcode.lower()
  allid.append(idcode+str(ctx.guild.id))
  desc = "Initializing countdown…"
  message = await ctx.reply(desc)
  while seconds>=1 and eval("terminate"+idcode.lower()+str(ctx.guild.id))==0:
    seconds = int((end - datetime.now(timezone.utc)).total_seconds())
    newsec=str(seconds%60)
    newmin=str((seconds%3600)//60)
    newhrs=str(seconds%86400//3600)
    newday=str(seconds//86400)
    if int(newsec) <= 9:
      newsec = "0"+newsec
    if int(newmin) <= 9:
      newmin = "0"+newmin
    if int(newhrs) <= 9:
      newhrs = "0"+newhrs
    if int(newday) <= 9:
      newday = "0"+newday
    newsec=number_to_emoji(newsec)
    newmin=number_to_emoji(newmin)
    newhrs=number_to_emoji(newhrs)
    newday=number_to_emoji(newday)
    prevdesc = desc
    if seconds<0:
      break
    desc=newidcode+f"\n"+newday+":regional_indicator_d:   "+newhrs+":regional_indicator_h:   "+newmin+":regional_indicator_m:   "+newsec+":regional_indicator_s:"
    if desc != prevdesc:
      await message.edit(content = desc)
  desc = "Countdown for "
  if sec >= 604800:
    desc = desc + str(sec//604800) + " weeks "
    sec = sec%604800
  if sec >= 86400:
    desc = desc + str(sec//86400) + " days "
    sec = sec%86400
  if sec >= 3600:
    desc = desc + str(sec//3600) + " hours "
    sec = sec%3600
  if sec >= 60:
    desc = desc + str(sec//60) + " minutes "
    sec = sec%60
  if sec >= 1:
    desc = desc + str(sec//1) + " seconds "
  desc = desc + "completed!"
  await message.edit(content=desc)
  if Text==None:
    await message.reply("Countdown complete!")
  else:
    await message.reply(f"Countdown complete!\n"+Text)

@commands.command()
async def spellcheck(ctx, text, distance: typing.Optional[int] = 3, *, disposed= None):
  results = spell_checker.get_suggestions(text, max_distance = distance)
  desc = f"QWERTY-spellchecking results for {text}"
  distances = {x["distance"] for x in results}
  for x in distances:
    desc += f"\n\nDISTANCE: {x+1}\n{', '.join([y for y in [z['word'] for z in results if z['distance'] == x]])}"
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
async def spoil(ctx, msg: discord.Message = None, *, text="Reply to a message, add a message ID/link or add some text to remove the spoilers!"):
  potential_reference = ctx.message.reference
  if potential_reference and not msg:
    msg = await ctx.bot.get_channel(potential_reference.channel_id).fetch_message(potential_reference.message_id)
  if msg:
    text = msg.content
  await ctx.reply(text.replace("||", ""))

@commands.command()
async def terminate(ctx, *, idc):
  if id_pattern.fullmatch(idc) and len(idc)==5:
    if f"{idc.upper()}{ctx.guild.id}" in allid:
      exec(f"terminate{idc.lower()}{ctx.guild.id}=1",globals())
      allid.remove(idc.upper()+str(ctx.guild.id))
      await ctx.reply("Timer terminated!")
    else:
      await ctx.reply("Please provide a valid timer code. A timer code could be found at the beginning of a running timer.")
  else:
    await ctx.reply("Please provide an 5-alphabet ID code. Example: `ABCDE`")

@commands.command()
async def ttimer(ctx, timetocount, *, Text= None):
  sec = int(timedelta(**{
    UNITS.get(m.group('unit').lower(), 'seconds'): int(m.group('val'))
    for m in re.finditer(r'(?P<val>\d+)(?P<unit>[smhdw]?)', timetocount, flags=re.I)
  }).total_seconds())
  end = datetime.now(timezone.utc) + timedelta(seconds = sec)
  seconds = int((end - datetime.now(timezone.utc)).total_seconds())
  newidcode = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ra.randint(0, 25)]
  exec(f"terminate{newidcode.lower()}{ctx.guild.id}=0",globals())
  allid.append(newidcode+str(ctx.guild.id))
  desc = "Initializing countdown…"
  message = await ctx.reply(desc)
  while seconds>=1 and eval("terminate"+newidcode.lower()+str(ctx.guild.id))==0:
    seconds = int((end - datetime.now(timezone.utc)).total_seconds())
    newsec=str(seconds%60)
    newmin=str((seconds%3600)//60)
    newhrs=str(seconds%86400//3600)
    newday=str(seconds//86400)
    if int(newsec) <= 9:
      newsec = "0"+newsec
    if int(newmin) <= 9:
      newmin = "0"+newmin
    if int(newhrs) <= 9:
      newhrs = "0"+newhrs
    if int(newday) <= 9:
      newday = "0"+newday
    prevdesc = desc
    if seconds<0:
      break
    desc="Timer (Terminate with `=terminate "+newidcode+f"`)\n**"+newday+"** d   **"+newhrs+"** h   **"+newmin+"** m   **"+newsec+"**s"
    if desc != prevdesc:
      await message.edit(content = desc)
  desc = "Countdown for "
  if sec >= 604800:
    desc = desc + str(sec//604800) + " weeks "
    sec = sec%604800
  if sec >= 86400:
    desc = desc + str(sec//86400) + " days "
    sec = sec%86400
  if sec >= 3600:
    desc = desc + str(sec//3600) + " hours "
    sec = sec%3600
  if sec >= 60:
    desc = desc + str(sec//60) + " minutes "
    sec = sec%60
  if sec >= 1:
    desc = desc + str(sec//1) + " seconds "
  desc = desc + "completed!"
  await message.edit(content=desc)
  if Text==None:
    await message.reply("Countdown complete!")
  else:
    await message.reply(f"Countdown complete!\n"+Text)

@commands.command()
async def unicode(ctx, *query):
  embed = discord.Embed(title = f"Search results for: {' '.join(query)}")
  all_results = []
  for x in query:
    current_results = []
    for y in search_charnames(x):
      current_results.append(y)
    all_results.append(current_results)
  intersected_results = []
  x=sum(all_results, [])
  for y in x:
    if y not in intersected_results and all([y in y for y in all_results]):
      intersected_results.append(y)
  characters_added = int(len(query[0]) == 1)
  try:
    hex_character = chr(int(query[0], 16))
    characters_added += 1
    add_hex_character = True
  except:
    add_hex_character = False
  for x, y in zip(intersected_results, range(25-characters_added)):
    embed.add_field(name = x[1].title(), value = f"U+{x[0]} `"+eval(f'u\'\\u{x[0]}\'')+"`")
  desc = f"Code\tChar.\tName\n\n"
  for x in intersected_results:
    desc += f"U+{x[0]}\t" + eval(f'u\'\\u{x[0]}\'') + f"\t{x[1].title()}\n"
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
async def unix(ctx, *, text= "now"):
  now = datetime.now(tz=timezone.utc)
  dateParts = {
    m[-1]: int(m[:-1]) for m in re.findall(r'([\d]{1,4}[yMdhms])', text)
  }
  if text.startswith("now") or SequenceMatcher(None, text, "now").ratio()>0.66:
    dt2=now
  else:
    dt2 = datetime(dateParts.get('y', now.year), dateParts.get('M', now.month), dateParts.get('d', now.day), dateParts.get('h', now.hour), dateParts.get('m', now.minute), dateParts.get('s', now.second), tzinfo=timezone.utc)
  s = round(datetime.timestamp(dt2))
  await ctx.reply(f"`<t:{s}>`      | <t:{s}>\n`<t:{s}:F>` | <t:{s}:F>\n`<t:{s}:f>` | <t:{s}:f>\n`<t:{s}:D>` | <t:{s}:D>\n`<t:{s}:d>` | <t:{s}:d>\n`<t:{s}:T>` | <t:{s}:T>\n`<t:{s}:t>` | <t:{s}:t>\n`<t:{s}:R>` | <t:{s}:R>")

def setup(bot):
  bot.add_command(case)
  bot.add_command(choice)
  bot.add_command(compress)
  bot.add_command(decode)
  bot.add_command(decompress)
  bot.add_command(emoji)
  bot.add_command(encode)
  bot.add_command(insert)
  bot.add_command(length)
  bot.add_command(pick)
  bot.add_command(quantum_random)
  bot.add_command(raffle)
  bot.add_command(random)
  bot.add_command(rawspoiler)
  bot.add_command(rawrawspoiler)
  bot.add_command(reverse)
  bot.add_command(rtimer)
  bot.add_command(spellcheck)
  bot.add_command(spoiler)
  bot.add_command(spoil)
  bot.add_command(terminate)
  bot.add_command(ttimer)
  bot.add_command(unicode)
  bot.add_command(unix)
