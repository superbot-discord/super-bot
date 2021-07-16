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
        desc = desc + eauthor['name']
      desc = desc + f"\n"
      if authorkeys.count('url') == 1:
        desc = desc + eauthor['url']
      desc = desc + f"\n"
      if authorkeys.count('icon_url') == 1:
        desc = desc + eauthor['icon_url']
      desc = desc + f"\n"
    else:
      desc = desc + f"\n"
      desc = desc + f"\n"
      desc = desc + f"\n"
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
      desc = desc + f"\n"
      desc = desc + f"\n"
    if ekeys.count('thumbnail') == 1:
      desc = desc + (edict['thumbnail'])['url']
    desc = desc + f"\n"
    if ekeys.count('image') == 1:
      desc = desc + (edict['image'])['url']
    desc = desc + f"\n"
    if ekeys.count('fields') == 1:
      for count in edict['fields']:
        desc = desc + count['name']
        desc = desc + f"\n"
        desc = desc + count['value'].replace(f"\n", "{{{newline}}}")
        desc = desc + f"\n"
        desc = desc + str(count['inline'])
        desc = desc + f"\n"
    return desc

def botquickembed(text):
  textlist=text.splitlines()
  try:
    embed=discord.Embed(title=textlist[0], description="\n".join(textlist[2:]), color = int(textlist[1]))
  except:
    try:
      embed=discord.Embed(title=textlist[0], color = int(textlist[1]))
    except:
      embed=discord.Embed(title=textlist[0])
  
  return embed

def botsimpembed(text):
  textlist=text.splitlines()
  if len(textlist) == 1:
    embed=discord.Embed(title=textlist[0])
  elif len(textlist) >= 2:
    try:
      embed=discord.Embed(title=textlist[0], description=textlist[1].replace("{{{newline}}}",f"\n"))
    except:
      embed=discord.Embed(description=textlist[1].replace("{{{newline}}}",f"\n"))
    textlist = textlist[1:]
  textlist = textlist[1:]
  if len(textlist) >= 1:
    embed.set_image(url=textlist[0])
    textlist = textlist[1:]
  for count in range(0,len(textlist)//3):
    if textlist[2].lower()=="y" or textlist[2].lower()=="yes" or textlist[2].lower()=="true" or textlist[2].lower()=="1":
      inl=True
    else:
      inl=False
    embed.add_field(name=textlist[0], value=textlist[1].replace("{{{newline}}}",f"\n"), inline=inl)
    textlist = textlist[3:]
  return embed

def botembed(text):
  textlist=text.splitlines()
  if len(textlist) == 1:# and len(textlist[0].replace(" ", ""))!=0:
    embed=discord.Embed(title=textlist[0])
    textlist = textlist[1:]
  elif len(textlist) == 2:# and len(textlist[0].replace(" ", ""))!=0 and len(textlist[1].replace(" ", ""))!=0:
    embed=discord.Embed(title=textlist[0], url=textlist[1])
    textlist = textlist[2:]
  elif len(textlist) == 3:# or (len(textlist) == 4 and len(textlist[3].replace(" ", ""))==0)):# and len(textlist[0].replace(" ", ""))!=0 and len(textlist[1].replace(" ", ""))!=0 and len(textlist[2].replace(" ", ""))!=0:
    embed=discord.Embed(title=textlist[0], url=textlist[1], description=textlist[2].replace("{{{newline}}}","\n"))
    textlist = textlist[3:]
  elif len(textlist) >= 4:# and len(textlist[0].replace(" ", ""))!=0:# and len(textlist[3].replace(" ", ""))!=0:# and len(textlist[2].replace(" ", ""))!=0 and len(textlist[3].replace(" ", ""))!=0:
    try:
      embed=discord.Embed(title=textlist[0], url=textlist[1], description=textlist[2].replace("{{{newline}}}","\n"), color=int(textlist[3]))
      textlist = textlist[4:]
    except:
      embed=discord.Embed(title=textlist[0], url=textlist[1], description=textlist[2].replace("{{{newline}}}","\n"))
      textlist = textlist[3:]
  if len(textlist) == 1 and len(textlist[0].replace(" ", ""))!=0:
    embed.set_author(name=textlist[0])
    textlist = textlist[1:]
  elif len(textlist) == 2 and len(textlist[0].replace(" ", ""))!=0 and len(textlist[1].replace(" ", ""))!=0:
    embed.set_author(name=textlist[0], url=textlist[1])
    textlist = textlist[2:]
  elif len(textlist) >= 3 and len(textlist[0].replace(" ", ""))!=0 and len(textlist[2].replace(" ", ""))!=0:# and len(textlist[2].replace(" ", ""))!=0:
    embed.set_author(name=textlist[0], url=textlist[1], icon_url=textlist[2])
    textlist = textlist[3:]
  else:
    textlist = textlist[3:]
  if len(textlist) >= 2 and len(textlist[0].replace(" ", ""))!=0:# and len(textlist[1].replace(" ", ""))!=0:
    embed.set_footer(text=textlist[0], icon_url=textlist[1])
  elif len(textlist[0].replace(" ", ""))!=0:
    embed.set_footer(text=textlist[0])
  textlist = textlist[2:]
  if len(textlist) == 1 and len(textlist[0].replace(" ", ""))!=0:
    embed.set_thumbnail(url=textlist[0])
  textlist = textlist[1:]
  if len(textlist) == 1 and len(textlist[0].replace(" ", ""))!=0:
    embed.set_image(url=textlist[0])
  textlist = textlist[1:]
  for count in range(0, len(textlist)//3):
    if textlist[2].lower()=="y" or textlist[2].lower()=="yes" or textlist[2].lower()=="true" or textlist[2].lower()=="1":
      inl=True
    else:
      inl=False
    embed.add_field(name=textlist[0], value=textlist[1].replace("{{{newline}}}",f"\n"), inline=inl)
    textlist = textlist[3:]
  return embed
