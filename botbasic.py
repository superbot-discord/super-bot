import discord

def bothelp(cat : str):
  desc = """**Prefix: **`=`
**Basic Commands**
`help` `invite` `prefix` `ping` `botpurge`

**Discord Information Commands**
`server` `invitelink` `role` `channel` `voicechannel` `autochannel` `user` `avatar` `status` `uservoice` `leftuser` `message` `raw` `reactions` `emojiinfo` `template`

**Discord Commands**
`react` `snipe` `clearsnipe` `pretend` `pretendembed` `embed` `editembed` `simpleembed` `ett`
**Coming soon: **quickembed which eliminates the use of `{{{newline}}}` entirely

**Text Manipulation Commands**
`poll` `insert` `spoiler` `rawspoiler` `rawrawspoiler` `reverse` `emoji`

**Moderation**
`kick` `ban` `unban` `slowmode` `purge` `purgeuser` `purgeregex` `purgepy` `purgepygex` `nick` `makeinvite`

**Information Commands**
`color` `simplecolor` `translate` `definition` `calc` `define` `time` `rtimer` `ttimer` `terminate` `minecraft`

**Web Commands**
`screenshot` `youtube` `wiki` `engrave` `covid` `population`

**Plot/Drawing commands**
`ascii` `table` `render` `captcha` `pie` `barh` `barv` `hist` `snow` `mandelbrot`

**Developer Tools and Miscellaneous commands**
`python` `transparent` `ocr` `text` `html` `md` `regex` `regsub`

`hello` leads you to death
Need help? check the [documentation](https://github.com/johann-lau/Bot#bot-documentation)!"""
  embed=discord.Embed(title="SuperBot#4073 (ID:796686363604680755)", description=desc)
  return embed

def botinvite():
  embed = discord.Embed(title="Invite", description = "The bot can be invited [here](https://discord.com/api/oauth2/authorize?client_id=796686363604680755&permissions=0&scope=bot%20applications.commands).")
  return embed
