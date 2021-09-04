import discord
from bot import bot_admins

async def botkick(ctx, user, reason):
  if ctx.author.permissions_in(ctx.channel).kick_members or bot_admins.count(ctx.author.id) != 0:
    try:
      await user.kick(reason=reason)
    except:
      await ctx.send("The bot doesn't have the required permission: Kick members.")
      return
    embed1 = discord.Embed(title=f"You were kicked from the server.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    embed2 = discord.Embed(title=f"{user.name} was kicked.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    try:
      await user.send(embed=embed1)
    except:
      pass
    await ctx.send(embed=embed2)
  else:
    await ctx.send("You don't have the required permission: Kick members.")


async def botunban(ctx, user, reason):
  if ctx.author.permissions_in(ctx.channel).ban_members or bot_admins.count(ctx.author.id) != 0:
    try:
      await ctx.guild.unban(user, reason=reason)
    except:
      await ctx.send("The bot doesn't have the required permission: Ban members.")
      return
    embed1 = discord.Embed(title=f"You were unbanned from the server.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    embed2 = discord.Embed(title=f"{user.name} was unbanned.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    try:
      await user.send(embed=embed1)
    except:
      pass
    await ctx.send(embed=embed2)
  else:
    await ctx.send("You don't have the required permission: Ban members.")


async def botban(ctx, user, delete, reason):
  if ctx.author.permissions_in(ctx.channel).ban_members or bot_admins.count(ctx.author.id) != 0:
    try:
      await ctx.guild.ban(user, delete_message_days=delete, reason=reason)
    except:
      await ctx.send("The bot doesn't have the required permission: Ban members.")
      return
    embed1 = discord.Embed(title=f"You were banned from the server.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    embed2 = discord.Embed(title=f"{user.name} was banned.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    try:
      await user.send(embed=embed1)
    except:
      1
    await ctx.send(embed=embed2)
  else:
    await ctx.send("You don't have the required permission: Ban members.")
