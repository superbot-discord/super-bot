from shared import commands, db, discord, ui
from _bot import bs

bot_admin_guilds = []#[805441351033552916]
bot_admin_slash = {x: ui.SlashPermission(allowed= {2: db['botadmins']}) for x in bot_admin_guilds}
#bot_admin_slash = {x: ui.SlashPermission(allowed= {x: ui.SlashPermission.User for x in db['botadmins']}) for x in bot_admin_guilds}
banned_ids = []
banned_text = []

@commands.command()
@commands.is_owner()
async def purgeserver(ctx, text, condition= "True", *, disposed=None):
  text = text.lower()
  if text.startswith("role"):
    all_objects = ctx.guild.roles
    msg = await ctx.reply("Role purging started.")
  elif text.startswith("emoji"):
    all_objects = ctx.guild.emojis
    msg = await ctx.reply("Emoji purging started.")
  elif text.startswith("event"):
    all_objects = ctx.guild.scheduled_events
    msg = await ctx.reply("Event purging started.")
  else:
    await ctx.reply("Please use `role` or `emoji` to purge the respective items.")
    return
  for x in all_objects:
    if eval(condition):
      await x.delete()
  await msg.edit(msg.content.replace("started.", "completed!"))

@bs.command(name="bot_ban", description= "Bans a user from using the bot.", options=[ui.SlashOption
           (name= "User", type= discord.User, description="The user to ban from using the bot.",
           required= True), ui.SlashOption(name= "Reason", type= str, description=
           "The reason to ban the user for.", required= False)], default_permission= False,
           guild_ids= bot_admin_guilds, guild_permissions= bot_admin_slash)
async def bot_ban(ctx, user: discord.User, *, reason: str = "No reason was provided"):
  banned_ids.append(user.id)
  banned_text.append(reason)
  await ctx.respond("Banned user from using the bot.", hidden= True)
  owner = await ctx.bot.fetch_user(687474789342117900)
  await owner.send(f"{user.name}#{user.discriminator} (ID: {user.id}) has been bot-banned by {ctx.author.name}#{ctx.author.discriminator}.")

@bs.command(name= "bot_unban", description= "Unbans a user from using the bot.", options=[
                  ui.SlashOption(name= "User", type= discord.User, description=
                  "The user to remove the ban of.", required= True)], default_permission= False,
                  guild_ids= bot_admin_guilds, guild_permissions= bot_admin_slash)
async def bot_unban(ctx, user: discord.User):
  if user.id in banned_ids:
    banned_text.remove(banned_text[banned_ids.index(user.id)])
    banned_ids.remove(user.id)
    await ctx.respond("Unbanned user from using the bot.", hidden= True)
    owner = await ctx.bot.fetch_user(687474789342117900)
    await owner.send(f"{user.name}#{user.discriminator} (ID: {user.id}) has been bot-unbanned.")
  else:
    await ctx.respond("The user is not banned.", hidden= True)

@bs.command(name="bot_admin", description="Temporarily adds a user as a bot admin.",
                  options= [ui.SlashOption(name= "User", type= discord.User, description=
                  "The user to add to the list of bot admins.", required= True)],
                  default_permission= False, guild_ids= bot_admin_guilds,
                  guild_permissions= bot_admin_slash)
async def botadmin(ctx, user: discord.User):
  db['botadmins'].append(user.id)
  await ctx.respond("Added user as bot admin.")
  owner = await ctx.bot.fetch_user(687474789342117900)
  await owner.send(f"{user.name}#{user.discriminator} (ID: {user.id}) has been added as a bot-admin.")

def setup(bot):
  bot.add_command(purgeserver)