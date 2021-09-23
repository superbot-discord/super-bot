from discord.ext import commands
from shared import *


@commands.command(aliases=['buttons'])
async def button(ctx, *, text=None):
  sample_buttons_view = ui.View()
  for count in sample_buttons(ctx):
    sample_buttons_view.add_item(count)
  await ctx.send("All buttons are automatically timed-out and they will not work.", view = sample_buttons_view)
  sample_buttons_view.stop()

@commands.command(aliases=['selectmenu', 'menu', 'option', 'options'])
async def select(ctx, *, text=None):
  sample_select_view = ui.View()
  for count in sample_menus():
    sample_select_view.add_item(count)
  await ctx.send("All buttons are automatically timed-out and they will not work.", view = sample_select_view)
  sample_select_view.stop()

def setup(bot):
  bot.add_command(button)
  bot.add_command(select)
