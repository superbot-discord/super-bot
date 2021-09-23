
from shared import *
from discord.ext import commands

from shared import *

@commands.command(aliases=['buttons'])
async def button(ctx, *, text=None):
  await ctx.send(view = sample_buttons_view)

def setup(bot):
  bot.add_command(button)
