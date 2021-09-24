import discord as discord
from discord.ext import commands
from shared import *

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
`react` `snipe` `clearsnipe` `pretend` `pretendembed` `embed` `editembed` `simpleembed` `quickembed` `ett` `tts`

**Moderation Commands**
`kick` `ban` `unban` `slowmode` `purge` `purgeuser` `purgeregex` `purgepy` `purgepygex` `purgereactions` `makeinvite`

**Text Manipulation Commands**
`poll` `insert` `spoiler` `rawspoiler` `rawrawspoiler` `reverse` `emoji` `encode` `decode`

**Information Commands**
`color` `simplecolor` `translate` `definition` `unix` `time` `rtimer` `ttimer` `terminate` `unscramble` `unicode` `random` `choice`

**Web Commands**
`redirect` `screenshot` `youtube` `wiki` `minecraft` `engrave` `covid` `population` `map`
`bunny` `cat` `dog` `duck` `fox` `koala` `lizard` `panda` `shiba` `error` `errorcat` `errordog`

**Plot/Drawing Commands**
`ascii` `table` `render` `captcha` `pie` `barh` `barv` `hist` `sankey` `snow` `mandelbrot`

**Developer Tools and Miscellaneous Commands**
`html` `md` `regex` `regsub` `button` `menu`

**Image Commands**
`analyse` `histogram` `resize` `rotate` `brightness` `contrast` `sharpen` `edge` `contour` `blur` `invert` `hue` `recolor`
To use the 13 commands above, type `=image ` first, then upload an image. Example: `=image analyse`. Supply a user name to work on his avatar, e.g. `=image SuperBot#4073 analyse`
`ocr` `qr` `qrmake` `transparent` `text`

`hello` leads you to death
Many slash commands are available as well
Need help? check the [documentation](https://superbot-discord.github.io/documentation)!"""
  embed=discord.Embed(title="SuperBot#4073 (ID:796686363604680755)", description=desc)
  await ctx.send(embed=embed)

@commands.command()
async def interactive_help(ctx, *, text=None):
  help_menu_view = ui.View(timeout=None)
  help_menu = ui.Select(options=help_menu_options(ctx), placeholder="Select a category…")
  help_menu_view.add_item(help_menu)
  await ctx.send("Please select a category to continue.", view = help_menu_view)

@commands.command()
async def invite(ctx, *, text=None):
  await ctx.send(embed=invite_embed)

@commands.command()
async def prefix(ctx, *, text=None):
  await ctx.send("The prefix for SuperBot is `=` (an equal sign).")

def setup(bot):
  bot.add_command(hello)
  bot.add_command(help)
  bot.add_command(interactive_help)
  bot.add_command(invite)
  bot.add_command(prefix)