from shared import *

@commands.command()
async def teapot(ctx, *, disposed=None):
  await ctx.reply(f"This command doesn't exist, so here is a lovely…\nhttps://http.cat/418")

def setup(bot):
  bot.add_command(teapot)
