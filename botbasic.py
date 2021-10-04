import discord as discord
from discord.ext import commands
from shared import *

@commands.command()
async def hello(ctx, *, text=None):
  embed = discord.Embed(title="Leaderboard", description="We upload the leaderboard to YouTube every week. You can find the leaderboard [here](https://youtu.be/4spCNEPawyQ).")
  await ctx.reply(embed=embed)

@commands.command(aliases=["commands"])
async def help(ctx, *, cat=None):
  await ctx.reply(embed=help_all)

@commands.command(aliases=["inter_help", "interactive"])
async def interactive_help(ctx, *, text=None):
  help_menu_view = ui.View(timeout=None)
  help_menu = ui.Select(options=help_menu_options(ctx), placeholder="Select a category…")
  help_menu_view.add_item(help_menu)
  await ctx.reply("Please select a category to continue.", view = help_menu_view)

@commands.command()
async def invite(ctx, *, text=None):
  await ctx.reply(embed=invite_embed)

@commands.command()
async def prefix(ctx, *, text=None):
  await ctx.reply("The prefix for SuperBot is `=` (an equal sign).")

@commands.command(aliases=['supportserver', 'supports', 'johann', 'johannlau', 'supporting', 'team', 'dev', 'developer'])
async def support(ctx, *, text=None):
  support_view = ui.View(timeout=0)
  for count in support_buttons:
    support_view.add_item(count)
  await ctx.reply(embed=support_embed, view=support_view)

def setup(bot):
  bot.add_command(hello)
  bot.add_command(help)
  bot.add_command(interactive_help)
  bot.add_command(invite)
  bot.add_command(prefix)
  bot.add_command(support)