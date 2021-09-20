import discord
from discord.ext import commands

@commands.command()
async def hello(ctx, *, text=None):
  embed = discord.Embed(title="Leaderboard", description="We upload the leaderboard to YouTube every week. You can find the leaderboard [here](https://youtu.be/4spCNEPawyQ).")
  await ctx.send(embed=embed)

@commands.command(aliases=["commands"])
async def help(ctx, *, cat=None):
  desc = """**Prefix: **`=`
**Basic Commands**
`help` `invite` `prefix` `ping` `botpurge`

**Discord Information Commands**
`server` `invitelink` `role` `channel` `user` `avatar` `status` `leftuser` `message` `raw` `reactions` `emojiinfo` `template`

**Discord Commands**
`react` `snipe` `clearsnipe` `pretend` `pretendembed` `embed` `editembed` `simpleembed` `ett` `tts`
**Coming soon: **quickembed which eliminates the use of `{{{newline}}}` entirely

**Moderation Commands**
`kick` `ban` `unban` `slowmode` `purge` `purgeuser` `purgeregex` `purgepy` `purgepygex` `makeinvite`

**Text Manipulation Commands**
`poll` `insert` `spoiler` `rawspoiler` `rawrawspoiler` `reverse` `emoji`

**Information Commands**
`color` `simplecolor` `translate` `definition` `calc` `define` `time` `rtimer` `ttimer` `terminate` `unscramble` `unicode` `random` `choice`

**Web Commands**
`screenshot` `youtube` `wiki` `minecraft` `engrave` `covid` `population` `cat` `dog`

**Plot/Drawing Commands**
`ascii` `table` `render` `captcha` `pie` `barh` `barv` `hist` `sankey` `snow` `mandelbrot`

**Developer Tools and Miscellaneous Commands**
`python` `transparent` `ocr` `text` `html` `md` `regex` `regsub`

`hello` leads you to death
Many slash commands are available as well
Need help? check the [documentation](https://superbot-discord.github.io/documentation)!"""
  embed=discord.Embed(title="SuperBot#4073 (ID:796686363604680755)", description=desc)
  await ctx.send(embed=embed)

@commands.command()
async def invite(ctx, *, text=None):
  embed = discord.Embed(title="Invite", description = "The bot can be invited [here](https://discord.com/api/oauth2/authorize?client_id=796686363604680755&permissions=8&redirect_uri=https%3A%2F%2Fsuperbot-discord.github.io&scope=bot%20applications.commands).")
  await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(hello)
  bot.add_command(help)
  bot.add_command(invite)