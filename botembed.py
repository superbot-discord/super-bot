import discord

def botsimpembed(text):
  textlist=text.splitlines()
  if len(textlist) == 1:
    embed=discord.Embed(title=textlist[0])
  elif len(textlist) == 2:
    embed=discord.Embed(title=textlist[0], description=textlist[1].replace("{{{newline}}}",f"\n"))
    textlist.remove(textlist[0])
  textlist.remove(textlist[0])
  for count in range(0,len(textlist)//3):
    if textlist[2].lower()=="y" or textlist[2].lower()=="yes" or textlist[2].lower()=="true" or textlist[2].lower()=="1":
      inl=True
    else:
      inl=False
    embed.add_field(name=textlist[0], value=textlist[1].replace("{{{newline}}}",f"\n"), inline=inl)
    textlist.remove(textlist[0])
    textlist.remove(textlist[0])
    textlist.remove(textlist[0])
  return embed

def botembed(text):
  textlist=text.splitlines()
  if len(textlist) == 1:
    embed=discord.Embed(title=textlist[0])
    textlist.remove(textlist[0])
  elif len(textlist) == 2:
    embed=discord.Embed(title=textlist[0], url=textlist[1])
    textlist.remove(textlist[0])
    textlist.remove(textlist[0])
  elif len(textlist) == 3 or (len(textlist) == 4 and (textlist[3] == "" or textlist[3] == " ")):
    embed=discord.Embed(title=textlist[0], url=textlist[1], description=textlist[2].replace("{{{newline}}}","\n"))
    textlist.remove(textlist[0])
    textlist.remove(textlist[0])
    textlist.remove(textlist[0])
  elif len(textlist) >= 4:
    embed=discord.Embed(title=textlist[0], url=textlist[1], description=textlist[2].replace("{{{newline}}}","\n"), color=int(textlist[3]))
    textlist.remove(textlist[0])
    textlist.remove(textlist[0])
    textlist.remove(textlist[0])
    textlist.remove(textlist[0])
  if len(textlist) == 1:
    embed.set_author(name=textlist[0])
    textlist.remove(textlist[0])
  elif len(textlist) == 2:
    embed.set_author(name=textlist[0], url=textlist[1])
    textlist.remove(textlist[0])
    textlist.remove(textlist[0])
  elif len(textlist) == 3:
    embed.set_author(name=textlist[0], url=textlist[1], icon_url=textlist[2])
    textlist.remove(textlist[0])
    textlist.remove(textlist[0])
    textlist.remove(textlist[0])
  if len(textlist) == 1:
    embed.set_footer(text=textlist[0])
    textlist.remove(textlist[0])
  if len(textlist) == 1:
    embed.set_thumbnail(url=textlist[0])
    textlist.remove(textlist[0])
  if len(textlist) == 1:
    embed.set_image(url=textlist[0])
    textlist.remove(textlist[0])
  for count in range(0,len(textlist)//3):
    if textlist[2].lower()=="y" or textlist[2].lower()=="yes" or textlist[2].lower()=="true" or textlist[2].lower()=="1":
      inl=True
    else:
      inl=False
    embed.add_field(name=textlist[0], value=textlist[1].replace("{{{newline}}}",f"\n"), inline=inl)
    textlist.remove(textlist[0])
    textlist.remove(textlist[0])
    textlist.remove(textlist[0])
  return embed
