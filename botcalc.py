from discord.ext import commands

from shared import db

SY2VA = db["decoder"]
ASCII = db["encoder"]

@commands.command()
async def ascii(ctx, *, text):
  answer = ""
  for character in text:
    answer = answer + ASCII[character]
  await ctx.reply(answer)

@commands.command()
async def base(ctx, frombase : int, tobase : int, *, text):
  integer = 0
  for character in text:
    if character not in SY2VA:
      await ctx.reply('Found unknown character!')
      return
    value = SY2VA[character]
    if value >= frombase:
      await ctx.reply(f'Found digit outside base! {value} is greater than {frombase}.')
      return
    integer *= frombase
    integer += value
  VA2SY = dict(map(reversed, SY2VA.items()))
  array = []
  while integer:
    integer, value = divmod(integer, tobase)
    array.append(VA2SY[value])
  answer = ''.join(reversed(array))
  await ctx.reply(answer)

def setup(bot):
  #bot.add_command(ascii)
  bot.add_command(base)
