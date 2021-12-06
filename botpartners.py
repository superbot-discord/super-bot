from discord.ext import commands

from shared import *

UNITS = {'s':'seconds', 'm':'minutes', 'h':'hours', 'd':'days', 'w':'weeks'}

@commands.command(aliases=['cb', 'craftbots', 'minecraftbot', 'minecraftbots', 'mcbot', 'mcbots'])
async def craftbot(ctx, *, disposed = None):
  craftbot_view = ui.View(timeout=0)
  craftbot_view.add_item(craftbot_buttons(ctx))
  await ctx.reply(embed=craftbot_embed, view=craftbot_view)

@commands.command(aliases=['partners', 'otherbots', 'otherbot', 'bots'])
async def partner(ctx, *, disposed = None):
  partners_view = ui.View(timeout=0)
  for x in partners_buttons(ctx):
    partners_view.add_item(x)
  await ctx.reply(embed=partners_embed, view=partners_view)

def setup(bot):
  bot.add_command(craftbot)
  bot.add_command(partner)