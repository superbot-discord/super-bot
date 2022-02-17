import base64
import collections
import hashlib

import bitarray
import huffman
from spellwise import Typox
from unicode_charnames import charname, codepoint, search_charnames

from _bot import bs
from shared import (commands, datetime, discord, Embed, ems, os, ra, re, requests, SequenceMatcher,
                    timedelta, timezone, try_delete, typing, ui, UNITS)
from functions import many_replace, xfill

spell_checker = Typox()
spell_checker.add_from_path("fonts/dictionary.txt")
id_pattern = re.compile(r'([A-Z]{5})', re.IGNORECASE)
allid = []
number_to_emoji = lambda x: many_replace(x, {'1': ":one: ", '2': ":two: ", '3': ":three: ", '4': ":four: ", '5': ":five: ", '6': ":six: ", '7': ":seven: ", '8': ":eight: ", '9': ":nine: ", '0': ":zero: "})

direction_choices = [
  {'name': "Encrypt", 'value': "encrypt"},
  {'name': "Decrypt", 'value': "decrypt"}
]

qrng_choices = [
  {'name': "Integer 0~255", 'value': "256"},
  {'name': "Integer 0~65535", 'value': "65536"},
  {'name': "ASCII Characters", 'value': "ascii"},
  {'name': "Unicode Characters", 'value': "unicode"}
]

encode_base_choices = [
  {'name': "Base 16", 'value': "16"},
  {'name': "Base 32", 'value': "32"},
  {'name': "Base 64", 'value': "64"},
  {'name': "Base 85", 'value': "85"}
]

@bs.command(name="ascii_caesar", description="Encrypts or decrypts a piece of text with an extended version of Caesar Cipher.",
           options=[ui.SlashOption(name="Direction", description="Whether you are encrypting or decrypting.",
           type=str, required=True, choices=direction_choices), ui.SlashOption(name="Distance",
           description= "The no. of positions to shift, between 1 and 128 inclusive.",
           type=int, required=True, min_value=1, max_value=128), ui.SlashOption(name="Text",
           description="The text to encrypt or decrypt.", type= str, required=True)])
async def ascii_caesar(ctx: ui.SlashInteraction, direction, distance, text):
  if not text.isascii():
    await ctx.respond("The string contains non-ASCII characters!")
    return
  if direction == "encrypt":
    await ctx.respond("".join([chr(ord(x) + distance % 128) for x in text]))
  else:
    await ctx.respond("".join([chr(ord(x) - distance % 128) for x in text]))

@commands.command() # Migrated
async def ascii_caesar_decode(ctx, distance: int, *, text):
  if not text.isascii():
    await ctx.reply("The string contains non-ASCII characters!")
    return
  await ctx.reply("".join([chr(ord(x) - distance % 128) for x in text]))

@commands.command() # Migrated
async def ascii_caesar_encode(ctx, distance: int, *, text):
  if not text.isascii():
    await ctx.reply("The string contains non-ASCII characters!")
    return
  await ctx.reply("".join([chr(ord(x) + distance % 128) for x in text]))

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
  embed = Embed(title= "Random choice", description= desc)
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

@bs.command(name="base_n", description="Encodes or decodes a piece of text with base-16, 32, 64 or 85.",
           options=[ui.SlashOption(name="Direction", description="Whether you are encoding or decoding.",
           type=str, required=True, choices=direction_choices), ui.SlashOption(name="Method",
           description= "The encoding method.", type=str, required=True,
           choices=encode_base_choices), ui.SlashOption(name="Text",
           description="The text to encode or decode.", type= str, required=True)])
async def base_n(ctx: ui.SlashInteraction, direction, method, text):
  coder = eval(f"base64.b{method}{direction[:2]}code(bytes(text, encoding='utf-8'))")
  await ctx.respond(coder.decode("utf-8"))

@commands.command() # Migrated
async def decrypt(ctx, code, *, text):
  if SequenceMatcher(None, code, 'base85').ratio()>0.6:
    coder = base64.b85decode(bytes(text, encoding='utf-8'))
  if SequenceMatcher(None, code, 'base64').ratio()>0.6:
    coder = base64.b64decode(bytes(text, encoding='utf-8'))
  elif SequenceMatcher(None, code, 'base32').ratio()>0.6:
    coder = base64.b32decode(bytes(text, encoding='utf-8'))
  elif SequenceMatcher(None, code, 'base16').ratio()>0.6:
    coder = base64.b16decode(bytes(text, encoding='utf-8'))
  else:
    await ctx.reply("Decryption method not found!")
    return
  await ctx.reply(coder.decode("utf-8"))

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
  text = ems.encode(text)
  await ctx.reply(text)

@commands.command() # Migrated
async def encrypt(ctx, code, *, text):
  if SequenceMatcher(None, code, 'base85').ratio()>0.8:
    coder = base64.b85encode(bytes(text, encoding='utf-8'))
  elif SequenceMatcher(None, code, 'base64').ratio()>0.8:
    coder = base64.b64encode(bytes(text, encoding='utf-8'))
  elif SequenceMatcher(None, code, 'base32').ratio()>0.8:
    coder = base64.b32encode(bytes(text, encoding='utf-8'))
  elif SequenceMatcher(None, code, 'base16').ratio()>0.8:
    coder = base64.b16encode(bytes(text, encoding='utf-8'))
  else:
    await ctx.reply("Encryption method not found!")
    return
  await ctx.reply(coder.decode("utf-8"))

@commands.command()
async def hash(ctx, code, *, text):
  if SequenceMatcher(None, code, 'sha512').ratio()>0.6:
    coder = hashlib.sha512()
  elif SequenceMatcher(None, code, 'sha384').ratio()>0.6:
    coder = hashlib.sha384()
  elif SequenceMatcher(None, code, 'sha256').ratio()>0.6:
    coder = hashlib.sha256()
  elif SequenceMatcher(None, code, 'sha224').ratio()>0.6:
    coder = hashlib.sha224()
  elif SequenceMatcher(None, code, 'sha1').ratio()>0.6:
    coder = hashlib.sha1()
  elif SequenceMatcher(None, code, 'blake2b').ratio()>0.9:
    coder = hashlib.blake2b()
  elif SequenceMatcher(None, code, 'blakes2s').ratio()>0.9:
    coder = hashlib.blake2s()
  else:
    await ctx.reply("Hash not found! The available hashes are `sha1` `sha224` `sha256` `sha384` `sha512` `blake2b` `blake2s`")
    return
  coder.update(bytes(text, encoding='utf-8'))
  await ctx.reply(coder.hexdigest())

@commands.command()
async def insert(ctx, emoji, *, text):
  text=text.replace(" "," "+emoji+" ")
  await ctx.reply(text)

@bs.command(name= "length", description= "Analyses the frequency of characters and counts the length of a piece of text.",
           options=[ui.SlashOption(name= "Text", description= "The text to analyse.", type= str,
           required= True)])
async def length(ctx, *, text):
  analysis = collections.Counter(text).items()
  analysis = sorted(analysis, key= lambda x: x[1], reverse= True)
  desc = f"Freq.\tCharacter\n"+f"\n".join([f"{x[1]}\t{x[0]}" for x in analysis])
  f = open('analysis.txt', 'w')
  f.write(desc)
  f.close()
  desc = f"The piece of text contains {len(text)} characters."
  msg = await ctx.respond(desc + " Full analysis coming shortly…")
  await ctx.send(file= discord.File('analysis.txt'))
  await msg.edit(desc)
  try_delete('analysis.txt')

@commands.command() # Migrated
async def length(ctx, *, text):
  analysis = collections.Counter(text).items()
  analysis = sorted(analysis, key= lambda x: x[1], reverse= True)
  desc = f"Freq.\tCharacter\n"+f"\n".join([f"{x[1]}\t{x[0]}" for x in analysis])
  f = open('analysis.txt', 'w')
  f.write(desc)
  f.close()
  desc = f"The piece of text contains {len(text)} characters."
  await ctx.reply(desc, file=discord.File('analysis.txt'))
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
  embed = Embed(title= f"{times} random number(s) between {lower} and {upper}", description= desc)
  await ctx.reply(embed= embed)

@bs.command(name="quantum_random", description="Generates random number(s) or character(s) using quantum fluctuations.",
           options=[ui.SlashOption(name="Type", description="The type of output to generate.",
           type=str, required=True, choices=qrng_choices), ui.SlashOption(name="Number",
           description="The no. of numbers/characters to generate, between 1 and 1024 inclusive. Defaults to 1.",
           type=int, required=False, min_value=1, max_value=1024)])
async def quantum_random_(ctx, type, number: int = 1):
  api_size = {'256': 8, '65536': 16, 'ascii': 8, 'unicode': 16}[type]
  r = requests.get(f"https://qrng.anu.edu.au/API/jsonI.php?length={number}&type=uint{api_size}").json()['data']
  if not type.isdigit():
    r = [chr(x) for x in r]
    await ctx.respond(f"Your quantum random {type.upper()} string is ```{''.join(r)}.```")
    return
  range_text = f" quantum random number{'' if number == 1 else 's'} between 0 and {int(type) - 1}"
  r = [str(x) for x in r]
  if number == 1:
    await ctx.respond(f"Your{range_text} is **{r[0]}**.")
    return
  embed = Embed(title=f"{number}{range_text}", description=", ".join(r))
  await ctx.respond(embed=embed)

@commands.command(aliases= ['qrng']) # Migrated
async def quantum_random(ctx, size: typing.Literal['256', '65536', 'alpha', 'ascii', 'unicode', 'ASCII', 'UNICODE'] = '256', times: int = 1):
  if times >= 1024:
    await ctx.reply(f"There are too many numbers/characters to generate! I can only generate 1024 numbers/characters at a time.")
    return
  api_size = {'256': 8, '65536': 16, 'ascii': 8, 'unicode': 16}[size]
  r = requests.get(f"https://qrng.anu.edu.au/API/jsonI.php?length={times}&type=uint{api_size}").json()['data']
  if not size.isdigit():
    r = [chr(x) for x in r]
    await ctx.reply(f"Your quantum random {size.upper()} string is {''.join(r)}.")
    return
  range_text = f"number{'' if times == 1 else 's'} between 0 and {int(size) - 1}"
  r = [str(x) for x in r]
  if times == 1:
    await ctx.reply(f"Your quantum random {range_text} is **{r[0]}**.")
    return
  desc = ", ".join(r)
  embed = Embed(title= f"{times} quantum random {range_text}", description= desc)
  await ctx.reply(embed= embed)

# NON-QUANTUM RANDOM
# M: Multiple values   R: Can repeat   S: Spoilers   T: Text choices
#    One value            Cannot repeat   Unformatted   Integral choice(s)
# =random{_{m{r}}{s}{t}}

@commands.command(aliases= ['rng'])
async def random(ctx, lower: int, upper: int):
  await ctx.reply(f"Your random number is **{ra.randint(lower,upper)}**")

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
  embed = Embed(title= f"{times} random number(s) between {lower} and {upper}", description= desc)
  await ctx.reply(embed= embed)

@commands.command()
async def random_mr(ctx, times: int, lower: int, upper: int):
  desc = ""
  if lower > upper:
    lower, upper = upper, lower
  for x in range(times):
    desc += f"{ra.randint(lower,upper)}, "
  embed = Embed(title= f"{times} random number(s) between {lower} and {upper}", description= desc)
  await ctx.reply(embed= embed)

@commands.command()
async def random_mrs(ctx, times: int, lower: int, upper: int):
  desc = ""
  if lower > upper:
    lower, upper = upper, lower
  upper_length = len(str(upper))
  for x in range(times):
    desc += f"||`{xfill(ra.randint(lower,upper), upper_length)}`||  "
  embed = Embed(title=f"{times} random number(s) between {lower} and {upper}", description= desc)
  await ctx.reply(embed= embed)

@commands.command()
async def random_mrst(ctx, times: int, *options):
  options = list(options) if isinstance(options, tuple) else [options]
  upper_length = max([len(x) for x in options])
  desc = ""
  for x in range(times):
    desc += f"||`{xfill(ra.choice(upper_length), upper_length)}`||  "
  embed = Embed(title= f"{times} random choice(s)", description= desc)
  await ctx.reply(embed= embed)

@commands.command()
async def random_mrt(ctx, times: int, *options):
  options = list(options) if isinstance(options, tuple) else [options]
  desc = ""
  for x in range(times):
    desc += f"{ra.choice(options)}, "
  embed = Embed(title= f"{times} random choice(s)", description= desc)
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
      desc += f"||`{xfill(ra.randint(lower,upper), upper_length)}`||  "
  embed = Embed(title=f"{times} random number(s) between {lower} and {upper}", description= desc)
  await ctx.reply(embed= embed)

@commands.command()
async def random_mst(ctx, times: int, *options):
  options = list(options) if isinstance(options, tuple) else [options]
  upper_length = max([len(x) for x in options])
  desc = ""
  if times <= (len(options)):
    ra.shuffle(options)
    for x, y in zip(range(times), options):
      desc += f"||`{y}`||  "
  else:
    for x in range(times):
      desc += f"||`{xfill(ra.choice(upper_length), upper_length)}`||  "
  embed = Embed(title= f"{times} random choice(s)", description= desc)
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
  embed = Embed(title= f"{times} random choice(s)", description= desc)
  await ctx.reply(embed= embed)

@commands.command()
async def random_s(ctx, lower: int, upper: int):
  if lower > upper:
    lower, upper = upper, lower
  await ctx.reply(f"Your random number is ||`{xfill(ra.randint(lower,upper), len(str(upper)))}`||.")

@commands.command()
async def random_st(ctx, *options):
  options = list(options) if isinstance(options, tuple) else [options]
  await ctx.reply(f"Your random choice is ||`{xfill(ra.choice(options), max([len(x) for x in options]))}`||.")

@commands.command()
async def random_t(ctx, *options):
  await ctx.reply(f"Your random choice is {ra.choice(options)}")

@commands.command()
async def raffle(ctx, lower: int, upper: int, amount: int): # MRS
  desc = ""
  if lower > upper:
    lower, upper = upper, lower
  upper_length = len(str(upper))
  for x in range(amount):
    rand = ra.randint(lower,upper)
    desc += f"||`{str(rand).zfill(upper_length)}`||  "
  embed = Embed(title= f"{amount} random number(s) between {lower} and {upper}", description= desc)
  await ctx.reply(embed= embed)

@commands.command()
async def rawspoiler(ctx, *, text):
  await ctx.reply(r"\|\|" + r"\|\|\|\|".join(text) + r"\|\|")

@commands.command()
async def rawrawspoiler(ctx, *, text):
  await ctx.reply(r"\\|\\|" + r"\\|\\|\\|\\|".join(text) + r"\\|\\|")

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
  f.close()
  await ctx.reply(file = discord.File("output.txt"))
  try_delete("output.txt")

@commands.command()
async def spoiler(ctx, *, text):
  text="||||".join(text)
  await ctx.reply(f"||{text}||")

@commands.command(aliases=['antispoiler', 'antispoilers', 'aspoiler', 'aspoilers', 'spoils']) # Migrated
async def spoil(ctx, msg: discord.Message = None, *, text= "Reply to a message, add a message ID/link or add some text to remove the spoilers!"):
  potential_reference = ctx.message.reference
  if potential_reference and not msg:
    msg = await ctx.bot.get_channel(potential_reference.channel_id).fetch_message(potential_reference.message_id)
  if msg:
    text = msg.content
  await ctx.reply(text.replace("||", ""))

@commands.command(aliases=['sub']) # Migrated
async def subscript(ctx, *, text):
  await ctx.send(many_replace(text, {'0': "₀", '1': "₁", '2': "₂", '3': "₃", '4': "₄", '5': "₅",
                                     '6': "₆", '7': "₇", '8': "₈", '9': "₉", '+': "₊", '-': "₋",
                                     '=': "₌", '(': "₍", ')': "₎", 'a': "ₐ", 'e': "ₑ", 'o': "ₒ",
                                     'x': "ₓ", 'h': "ₕ", 'k': "ₖ", 'l': "ₗ", 'm': "ₘ", 'n': "ₙ",
                                     'p': "ₚ", 's': "ₛ", 't': "ₜ"}))

@bs.command(name= "subscript", description= "Makes a piece of text subscript. Works on numbers and some other characters only.",
           options= [ui.SlashOption(name= "Text", type= str, required= True,
           description= "The text to make subscript.")])
async def subscript_(ctx, text):
  await ctx.respond(many_replace(text, {'0': "₀", '1': "₁", '2': "₂", '3': "₃", '4': "₄", '5': "₅",
                                     '6': "₆", '7': "₇", '8': "₈", '9': "₉", '+': "₊", '-': "₋",
                                     '=': "₌", '(': "₍", ')': "₎", 'a': "ₐ", 'e': "ₑ", 'o': "ₒ",
                                     'x': "ₓ", 'h': "ₕ", 'k': "ₖ", 'l': "ₗ", 'm': "ₘ", 'n': "ₙ",
                                     'p': "ₚ", 's': "ₛ", 't': "ₜ"}))

@commands.command(aliases=['sup', 'super']) # Migrated
async def superscript(ctx, text):
  await ctx.send(many_replace(text, {'0': "⁰", '1': "¹", '2': "²", '3': "³", '4': "⁴", '5': "⁵",
                                     '6': "⁶", '7': "⁷", '8': "⁸", '9': "⁹", '+': "⁺", '-': "⁻",
                                     '=': "⁼", '(': "⁽", ')': "⁾", 'i': "ⁱ", 'n': "ⁿ"}))

@bs.command(name= "superscript", description= "Makes a piece of text superscript. Works on numbers and some other characters only.",
           options= [ui.SlashOption(name= "Text", type= str, required= True,
           description= "The text to make superscript.")])
async def superscript_(ctx, *, text):
  await ctx.respond(many_replace(text, {'0': "⁰", '1': "¹", '2': "²", '3': "³", '4': "⁴", '5': "⁵",
                                     '6': "⁶", '7': "⁷", '8': "⁸", '9': "⁹", '+': "⁺", '-': "⁻",
                                     '=': "⁼", '(': "⁽", ')': "⁾", 'i': "ⁱ", 'n': "ⁿ"}))

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
  embed = Embed(title = f"Search results for: {' '.join(query)}")
  raw_results = [list(search_charnames(x)) for x in query]
  intersected_results = set.intersection(*map(set, raw_results))
  characters_added = int(len(query[0]) == 1)
  try:
    hex_character = chr(int(query[0], 16))
    characters_added += 1
    add_hex_character = True
  except:
    add_hex_character = False
  for x, y in zip(intersected_results, range(25 - characters_added)):
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
  f.close()
  await ctx.reply(embed= embed, file=discord.File("unicode.txt"))
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
  bot.add_command(ascii_caesar_decode)
  bot.add_command(ascii_caesar_encode)
  bot.add_command(case)
  bot.add_command(choice)
  bot.add_command(compress)
  bot.add_command(decrypt)
  bot.add_command(decompress)
  bot.add_command(emoji)
  bot.add_command(encrypt)
  bot.add_command(hash)
  bot.add_command(insert)
  bot.add_command(length)
  bot.add_command(pick)
  bot.add_command(quantum_random)
  bot.add_command(raffle)
  bot.add_command(random)
  bot.add_command(random_m)
  bot.add_command(random_mr)
  bot.add_command(random_mrs)
  bot.add_command(random_mrst)
  bot.add_command(random_mrt)
  bot.add_command(random_ms)
  bot.add_command(random_mst)
  bot.add_command(random_mt)
  bot.add_command(random_s)
  bot.add_command(random_st)
  bot.add_command(random_t)
  bot.add_command(rawspoiler)
  bot.add_command(rawrawspoiler)
  bot.add_command(reverse)
  bot.add_command(rtimer)
  bot.add_command(spellcheck)
  bot.add_command(spoiler)
  bot.add_command(spoil)
  bot.add_command(subscript)
  bot.add_command(superscript)
  bot.add_command(terminate)
  bot.add_command(ttimer)
  bot.add_command(unicode)
  bot.add_command(unix)
  print("Midway through loading modules")