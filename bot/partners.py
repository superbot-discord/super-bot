from shared import commands, Embed, ui, UNITS

craftbot_embed = Embed(title= "CraftBot", description= f"""
CraftBot is a fun-oriented bot developed by me (Johann, developer of SuperBot) and Murvon (my real-life friend).
Its commands are highly related to Minecraft; though non-players will be entertained by the bot as well.
The most important fact is that it does not have "votewalls" (vote-for-rewards) or excessive "paywalls" (pay-for-features).
Note: The button allows you to invite CraftBot without opening a browser.
""".replace(f"\n", " "))

def craftbot_buttons(ctx):
  return ui.LinkButton(label= "Invite!", url= "https://discord.com/api/oauth2/authorize?client_id=814444200946434069&permissions=909631057&scope=bot", emoji=ctx.bot.get_emoji(891265683801923604))

partners_embed = Embed(title= "SuperBot Partners")
partners_embed.add_field(name= "CraftBot", value= "Minecraft-oriented bot with rock-paper-scissors and a lyrics index.", inline= False)
def partners_buttons(ctx):
  return [
    ui.LinkButton(label= "CraftBot", url= "https://discord.com/api/oauth2/authorize?client_id=814444200946434069&permissions=909631057&scope=bot", emoji=ctx.bot.get_emoji(891265683801923604))
  ]

@commands.command(aliases=['cb', 'craftbots', 'minecraftbot', 'minecraftbots', 'mcbot', 'mcbots'])
async def craftbot(ctx, *, disposed=None):
  craftbot_view = ui.View(timeout=0)
  craftbot_view.add_item(craftbot_buttons(ctx))
  await ctx.reply(embed=craftbot_embed, view=craftbot_view)

@commands.command(aliases=['partners', 'otherbots', 'otherbot', 'bots'])
async def partner(ctx, *, disposed=None):
  partners_view = ui.View(timeout=0)
  for x in partners_buttons(ctx):
    partners_view.add_item(x)
  await ctx.reply(embed=partners_embed, view=partners_view)

def setup(bot):
  bot.add_command(craftbot)
  bot.add_command(partner)