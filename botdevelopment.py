
from shared import *
from discord.ext import commands

from shared import *

@commands.command(aliases=['buttons'])
async def button(ctx, *, text=None):
  sample_buttons_view = ui.View()
  for count in sample_buttons:
    sample_buttons_view.add_item(count)
  await ctx.send("All buttons are automatically timed-out and they will not work.", view = sample_buttons_view)
  sample_buttons_view.stop()

def setup(bot):
  bot.add_command(button)
