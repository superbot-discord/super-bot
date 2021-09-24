from discord.ext import commands
from shared import *

@commands.command(aliases=['buttons'])
async def button(ctx, *, text=None):
  sample_buttons_view = ui.View(timeout=None)
  for count in sample_buttons(ctx):
    sample_buttons_view.add_item(count)
  await ctx.send("All buttons will not timeout.", view = sample_buttons_view)

@commands.command()
@commands.cooldown(2, 10, commands.BucketType.user)
async def patience(ctx, *, text=None):
  await ctx.send("Success!")

@patience.error
async def patience_error(ctx, error):
  await ctx.send("This command is on cooldown! You can only use it twice per 10 seconds.")

@commands.command(aliases=['selectmenu', 'menu', 'option', 'options'])
async def select(ctx, *, text=None):
  sample_select_view = ui.View(timeout=None)
  for count in sample_menus():
    sample_select_view.add_item(count)
  await ctx.send("All menus will not timeout.", view = sample_select_view)

def setup(bot):
  bot.add_command(button)
  bot.add_command(patience)
  bot.add_command(select)