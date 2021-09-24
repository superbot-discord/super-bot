from datetime import time
from discord.ext import commands
from shared import *


@commands.command(aliases=['buttons'])
async def button(ctx, *, text=None):
  sample_buttons_view = ui.View(timeout=300)
  for count in sample_buttons(ctx):
    sample_buttons_view.add_item(count)
  await ctx.send("All buttons will automatically timeout in 5 minutes.", view = sample_buttons_view)

# @commands.command()
# async def clicker(ctx, *, text = None):
#   clicker_view = ui.View(timeout=5)
#   clicker_view.add_item(clicker_button)
#   msg = await ctx.send("Click the button for as many times as possible! Anyone in the server can participate.", view=clicker_view)
#   clickers[msg.id] = {}
#   @clicker_view.on_timeout
#   async def clicker_timeout():
#     await ctx.send('Test')

@commands.command(aliases=['selectmenu', 'menu', 'option', 'options'])
async def select(ctx, *, text=None):
  sample_select_view = ui.View(timeout=300)
  for count in sample_menus():
    sample_select_view.add_item(count)
  await ctx.send("All menus will automatically timeout in 5 minutes.", view = sample_select_view)

def setup(bot):
  bot.add_command(button)
  #bot.add_command(clicker)
  bot.add_command(select)
