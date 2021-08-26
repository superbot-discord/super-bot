import discord

def botrole(ctx, role):
  if role==None:
    role=ctx.author.top_role
  ti="Role Information: "+role.name
  desc=role.mention + " created at " + role.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  embed=discord.Embed(title=ti,color=role.color, description=desc)
  memberlist=role.members
  if len(memberlist) == 0:
    f0v = "No members assigned with this role."
  else:
    f0v = ""
    for count in memberlist:
      f0v = f0v + count.mention + " "
    f0v = f0v[:-1]
  mention=role.mentionable
  if mention:
    f1v="Mentionable"
  else:
    f1v="Not mentionable"
  f1v=f1v+"""
  Mention: `<&"""+str(role.id)+">`"
  hoisted=role.hoist
  if hoisted:
    f2v="Yes"
  else:
    f2v="No"
  f4v=role.id
  f5v=role.position
  f6v=role.color
  embed.add_field(name="Mentions", value=f1v, inline=True)
  embed.add_field(name="Displayed separately?", value=f2v, inline=True)
  embed.add_field(name="Role ID", value=f4v, inline=True)
  embed.add_field(name="Position in hierarchy", value=f5v, inline=True)
  embed.add_field(name="Color", value=f6v, inline=True)
  if role.is_integration():
    f7v="This role is managed by an integration, such as a bot."
    embed.add_field(name="Integration", value=f7v, inline=False)
  embed.add_field(name="Members ("+str(len(memberlist))+")", value=f0v, inline=False)
  #embed.add_field(name="Channel Permissions", value=f3vb, inline=False)
  return embed

async def bottchannel(ctx, channel):
  if channel==None:
    channel=ctx.channel
  ti="Channel Information: "+channel.name
  desc=channel.mention
  embed=discord.Embed(title=ti, description=desc)
  f0v=channel.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  f3v=str(channel.topic)
  f4v=str(channel.category)
  f5vlist=await channel.invites()
  f5v=f8v=""
  for count in f5vlist:
    f5v=f5v+count.url+"  "
  f5v=f5v[:-2]
  for count in channel.members:
    f8v=f8v+count.mention+" "
  f8v=f8v[:-1]
  if len(f8v) > 500:
    f8v = ""
    for count in channel.members:
      if len(f8v + count.name) > 500:
        break
      f8v = f8v+count.name+", "
    f8v = f8v [:-2] + "…"
  embed.add_field(name="Created", value=f0v, inline=True)
  if channel.is_nsfw()==True:
    embed.add_field(name="NSFW", value="This is an NSFW channel.", inline=True)
  if channel.is_news()==True:
    embed.add_field(name="News", value="This is a news channel.", inline=True)
  embed.add_field(name="Topic", value=f3v, inline=True)
  embed.add_field(name="Category", value=f4v, inline=True)
  embed.add_field(name="Members", value=f8v, inline=False)
  if len(f5vlist)!=0:
    embed.add_field(name="Invites", value=f5v, inline=True)
  embed.add_field(name="ID", value=channel.id, inline=True)