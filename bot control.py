from discord import Webhook, RequestsWebhookAdapter
from discord_webhook import DiscordWebhook
from discord.ext.commands import *
from discord.ext import commands

@bot.event
async def on_message(message):
  if banned_ids.count(message.author.id)==0 and message.content.startswith("=") and message.content.startswith("==")==False:
    await bot.process_commands(message)
  elif message.content.startswith("="):
    await message.channel.send("You are banned from the bot. Reason: "+banned_text[banned_ids.index(message.author.id)])

@bot.command()
async def botban(ctx, user : discord.User, *, text="No reason was provided"):
  if ctx.author.id == 687474789342117900 and banned_ids.cound(user.id) == 0:
    banned_ids.append(user.id)
    banned_text.append(text)
    await ctx.send("Banned user from using the bot.")

@bot.command()
async def botunban(ctx, user : discord.User):
  if ctx.author.id == 687474789342117900 and banned_ids.cound(user.id) == 1:
    banned_text.remove(banned_text[banned_ids.index(user.id)])
    banned_ids.remove(user.id)
    await ctx.send("Unbanned user from using the bot.")

@bot.command()
async def botadmin(ctx, user : discord.User):
  if ctx.author.id == 687474789342117900:
    bot_admins.append(user.id)
    await ctx.send("Added user as bot admin.")
