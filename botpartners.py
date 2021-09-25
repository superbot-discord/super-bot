from discord.ext import commands

from shared import *

UNITS = {'s':'seconds', 'm':'minutes', 'h':'hours', 'd':'days', 'w':'weeks'}

@commands.command()
async def craftbot(ctx, *, text=None):
  craftbot_view = ui.View(timeout=0)
  craftbot_view.add_item(craftbot_buttons(ctx))
  await ctx.send(embed = craftbot_embed, view = craftbot_view)

def setup(bot):
  bot.add_command(craftbot)