from _bot import bs
import html
from shared import ra, requests, ui

# Q1 Q2 Q3    Code   Category
# 00 10 20       9   General Knowledge
# 01 11 21      12   Entertainment: Music
# 02 12 22      13   Entertainment: Musicals & Theatres
# 03 13 23      31   Entertainment: Japanese Anime & Manga 
# 04 14 24      32   Entertainment: Cartoon & Animations
# 05 15 25      15   Entertainment: Video Games
# 06 16 26      29   Entertainment: Comics
# 07 17 27      30   Science: Gadgets
# 08 18 28      25   Art
# 09 19 29      27   Animals
trivia_qs = [None] * 30
trivia_cats = [9, 12, 13, 31, 32, 15, 29, 30, 25, 27]

# @bs.command(name="trivnight", description="Trivia night", guild_ids=[867705331413155861, 841330908560228412],
#             default_permission=False, guild_permissions={867705331413155861: ui.SlashPermission(
#             allowed={1: [867705331739525125]}), 841330908560228412: ui.SlashPermission( # 1 represent role in both cases
#             allowed={1: [883803366692638762]})}, options=[ui.SlashOption(name="Number", type=int,
#             description="The question number (between 1 and 30 inclusive).", required=True, min_value=1, max_value=30)])
@bs.command(name="trivnight", description="Trivia night", guild_ids=[841330908560228412],
            default_permission=False, guild_permissions={841330908560228412: ui.SlashPermission(
            allowed={1: [883803366692638762]})}, options=[ui.SlashOption(name="Number", type=int,
            description="The question number (between 1 and 30 inclusive).", required=True, min_value=1, max_value=30)])
async def trivnight(ctx: ui.SlashInteraction, *, number: int):
  await ctx.defer(hidden=True)
  # if ctx.guild.id != 867705331413155861:
  #   return
  # if 867705331739525125 not in [x.id for x in ctx.author.roles]:
  #   return # Further actions - as required by Murvon
  if trivia_qs == [None] * 30:
    for x in range(10):
      r = requests.get(f"https://opentdb.com/api.php?amount=3&category={trivia_cats[x]}&difficulty=easy&type=multiple&encoding=base64").json()['results']
      for y in range(3):
        trivia_qs[int(f"{y}{x}")] = r[y]
  q = trivia_qs[number - 1]
  opts = q['incorrect_answers']
  opts.append(q['correct_answer'])
  ra.shuffle(opts)
  ordered_opts = [f"{y}. {html.unescape(x)}" for x, y in zip(opts, "ABCD")]
  opts_joined = "\n".join(ordered_opts)
  desc = f"{q['category']}: {html.unescape(q['question'])}\n{opts_joined}"
  await ctx.respond(f"Correct option:\n{list(filter(lambda x: html.unescape(q['correct_answer']) == x[3:], ordered_opts))[0]}", hidden=True)
  await ctx.channel.send(desc)


def setup(bot):
  pass