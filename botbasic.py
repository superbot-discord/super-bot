import discord

def bothelp(cat : str):
desc = """**Prefix: **`=`
**Basic Commands**
`help` `invite` `prefix` `ping` `speedtest` `invite`

**Discord Information Commands**
`server` `role` `channel` `voicechannel` `user` `uservoice` `avatar` `invitelink` `reactions` `template`

**Discord Commands**
`embed` `pretend` `pretendembed`

**Text Manipulation Commands**
`insert` `spoiler` `rawspoiler` `reverse` `emoji`

**Moderation**
`kick` `ban` `slowmode` `nick` `purgeregex` `purgepy` `purgepygex`

**Information Commands**
`color` `simpcolor` `translate` `calc` `define` `time` `rtimer` `terminate`

**Web Commands**
`screenshot` `youtube` `wiki` `engrave` `covid` `population`

**Plot commands**
`table` `pie` `barh` `barv` `hist` `snow`

**Developer Tools and Others**
`python` `transparent` `ocr` `text` `html` `md` `regex` `regsub`

Need help? check the [documentation](https://github.com/johann-lau/Bot#bot-documentation)!
  """
  embed=discord.Embed(title=ti, description=desc)
  if cat=="simpcolor" or cat=="simplecolor" or cat=="simpcolour" or cat=="simplecolour":
    embed.set_image(url="https://u.cubeupload.com/Johann/Colours001.jpeg")
  return embed

def botinvite():
  embed = discord.Embed(title="Invite", description = "Our bot could be invited [here](https://discord.com/oauth2/authorize?client_id=796686363604680755&permissions=805399670&scope=bot).")
  return embed
