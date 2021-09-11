import discord

def botett(msg):
  #for count in msg.embeds:
  count = msg.embeds[0]
  edict = count.to_dict()
  ekeys = list(edict)
  desc = "=embed "
  if ekeys.count('title') == 1:
    desc = desc + edict['title']
  desc = desc + f"\n"
  if ekeys.count('url') == 1:
    desc = desc + edict['url']
  desc = desc + f"\n"
  if ekeys.count('description') == 1:
    desc = desc + edict['description'].replace(f"\n", "{{{newline}}}")
  desc = desc + f"\n"
  if ekeys.count('color') == 1:
    desc = desc + str(edict['color'])
  desc = desc + f"\n"
  if ekeys.count('author') == 1:
    eauthor = edict['author']
    authorkeys = list(eauthor)
    if authorkeys.count('name') == 1:
      desc = desc + eauthor['name'] + f"\n"
    if authorkeys.count('url') == 1:
      desc = desc + eauthor['url'] + f"\n"
    if authorkeys.count('icon_url') == 1:
      desc = desc + eauthor['icon_url'] + f"\n"
  else:
    desc = desc + f"\n" + f"\n" + f"\n"
  if ekeys.count('footer') == 1:
    efooter = edict['footer']
    footerkeys = list(efooter)
    if footerkeys.count('text') == 1:
      desc = desc + efooter['text']
    desc = desc + f"\n"
    if footerkeys.count('icon_url') == 1:
      desc = desc + efooter['icon_url']
    desc = desc + f"\n"
  else:
    desc = desc + f"\n" + f"\n"
  if ekeys.count('thumbnail') == 1:
    desc = desc + (edict['thumbnail'])['url'] + f"\n"
  if ekeys.count('image') == 1:
    desc = desc + (edict['image'])['url'] + f"\n"
  if ekeys.count('fields') == 1:
    for count in edict['fields']:
      desc = desc + count['name'] + f"\n" + count['value'].replace(f"\n", "{{{newline}}}") + f"\n" + str(count['inline']) + f"\n"
  return desc

def botquickembed(text):
  textlist=text.splitlines()
  embed = discord.Embed()
  try:
    embed.title            = textlist[0]
  except:
    pass
  try:
    embed.color          = int(textlist[1])
  except:
    pass
  try:
    embed.set_image    (url =textlist[2])
  except:
    pass
  try:
    embed.description      = textlist[3:]
  except:
    pass
  
  return embed

def botsimpembed(text):
  textlist=text.splitlines()
  embed = discord.Embed()
  try:
    embed.title            = textlist[0]
  except:
    pass
  try:
    embed.description      = textlist[1].replace("{{{newline}}}", f"\n")
  except:
    pass
  try:
    embed.color          = int(textlist[2])
  except:
    pass
  try:
    embed.set_image    (url =textlist[3])
  except:
    pass
  for count in range(0, (len(textlist)-11)//3):
    inline = textlist[3*count+11].lower()
    inline = inline.startswith("y") or inline.startswith("1") or inline.startswith("e") or inline.startswith("on")
    embed.add_field(name=textlist[3*count+12], value=textlist[3*count+13], inline=inline)
  return embed

def botembed(text):
  textlist=text.splitlines()
  embed = discord.Embed()
  try:
    embed.title            = textlist[0]
  except:
    pass
  try:
    embed.description      = textlist[1].replace("{{{newline}}}", f"\n")
  except:
    pass
  try:
    embed.color          = int(textlist[2])
  except:
    pass
  try:
    embed.url              = textlist[3]
  except:
    pass
  try:
    embed.set_author   (name=textlist[4])
  except:
    pass
  try:
    embed.set_footer   (text=textlist[5])
  except:
    pass
  try:
    embed.set_author   (name=textlist[4], url=textlist[6])
  except:
    pass
  try:
    embed.set_image    (url =textlist[7])
  except:
    pass
  try:
    embed.set_thumbnail(url =textlist[8])
  except:
    pass
  try:
    embed.set_author   (name=textlist[4], url=textlist[6], icon_url=textlist[9])
  except:
    pass
  try:
    embed.set_footer   (text=textlist[5], icon_url=textlist[10])
  except:
    pass
  for count in range(0, (len(textlist)-11)//3):
    inline = textlist[3*count+11].lower()
    inline = inline.startswith("y") or inline.startswith("1") or inline.startswith("e") or inline.startswith("on")
    embed.add_field(name=textlist[3*count+12], value=textlist[3*count+13], inline=inline)
  return embed
