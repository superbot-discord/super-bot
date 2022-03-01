from _bot import bs
from shared import asyncio, discord, ra, typing, ui


rps_dict = {0: "Rock", 1: "Paper", 2: "Scissors"}
rps_status_dict = {0: "Chosen", 1: "Chosen", 2: "Chosen", None: "Pending"}
rps_buttons = [
  ui.Button(color='green', custom_id="0", label="Rock", emoji="✊"),
  ui.Button(color='blurple', custom_id="1", label="Paper", emoji="✋"),
  ui.Button(color='red', custom_id="2", label="Scissors", emoji="✌️")
]

class Rps_1pL(ui.listener.Listener):
  def __init__(self, bot_selection):
    self.selection = bot_selection

  async def rps_1p_handle(self, ctx: ui.ButtonInteraction):
    await ctx.message.disable_components()
    status = (int(ctx.custom_id) - self.selection) % 3
    desc = "You won!" if status == 1 else ("You lost." if status == 2 else "It was a tie.")
    desc += f"\nYou chose **{rps_dict[int(ctx.custom_id)]}**\nThe bot chose **{rps_dict[self.selection]}**"
    await ctx.respond(desc)

  @ui.Listener.button(custom_id="0")
  async def r(self, ctx: ui.ButtonInteraction):
    await self.rps_1p_handle(ctx)

  @ui.Listener.button(custom_id="1")
  async def p(self, ctx: ui.ButtonInteraction):
    await self.rps_1p_handle(ctx)

  @ui.Listener.button(custom_id="2")
  async def s(self, ctx: ui.ButtonInteraction):
    await self.rps_1p_handle(ctx)


class Rps_2pL(ui.listener.Listener):
  def __init__(self, p1, p2):
    self.p1: discord.Member = p1 # P1: Person who invoked command
    self.p2: discord.Member = p2 # P2: Person invited to play
    self.p1_choice: typing.Literal[0, 1, 2, None] = None
    self.p2_choice: typing.Literal[0, 1, 2, None] = None

  async def rps_2p_handle(self, ctx: ui.ButtonInteraction):
    if ctx.author not in [self.p1, self.p2]:
      await ctx.respond("You are not a player!", hidden=True)
      return
    if ctx.author == self.p1:
      if self.p1_choice != None:
        await ctx.respond(f"You have already chosen {rps_dict[self.p1_choice]}!", hidden=True)
        return
      else:
        self.p1_choice = int(ctx.custom_id)
        await ctx.respond(f"Successfully chosen {rps_dict[self.p1_choice]}.", hidden=True)
    elif ctx.author == self.p2:
      if self.p2_choice != None:
        await ctx.respond(f"You have already chosen {rps_dict[self.p2_choice]}!", hidden=True)
        return
      else:
        self.p2_choice = int(ctx.custom_id)
        await ctx.respond(f"Successfully chosen {rps_dict[self.p2_choice]}.", hidden=True)
    desc = f"{self.p1.name} | {rps_status_dict[self.p1_choice]}\n{self.p2.name} | {rps_status_dict[self.p2_choice]}"
    if self.p1_choice != None and self.p2_choice != None:
      desc += "\nResults coming…"
    await ctx.message.edit(desc)
    if self.p1_choice != None and self.p2_choice != None:
      await ctx.message.disable_components()
      status = (self.p1_choice - self.p2_choice) % 3
      desc = f"{self.p1.name} won!" if status == 1 else (f"{self.p2.name} won!" if status == 2 else "It was a tie.")
      desc += f"\n{self.p1.name} chose **{rps_dict[self.p1_choice]}**"
      desc += f"\n{self.p2.name} chose **{rps_dict[self.p2_choice]}**"
      await asyncio.sleep(2)
      await ctx.message.edit(desc)

  @ui.Listener.button(custom_id="0")
  async def r(self, ctx: ui.ButtonInteraction):
    await self.rps_2p_handle(ctx)

  @ui.Listener.button(custom_id="1")
  async def p(self, ctx: ui.ButtonInteraction):
    await self.rps_2p_handle(ctx)

  @ui.Listener.button(custom_id="2")
  async def s(self, ctx: ui.ButtonInteraction):
    await self.rps_2p_handle(ctx)


@bs.command(name="game_rps_1p", description="Starts a solo game of Rock-Paper-Scissors.")
async def game_rps_1p(ctx: ui.SlashInteraction):
  await ctx.respond(components=rps_buttons, listener=Rps_1pL(ra.randint(0, 2)))


@bs.command(name="game_rps_2p", description="Starts a game of Rock-Paper-Scissors with another user.",
            options=[ui.SlashOption(name="User", description="The user to play with.",
            type=discord.Member, required=True)])
async def game_rps_2p(ctx: ui.SlashInteraction, user: discord.Member):
  await ctx.respond(f"{ctx.author.name} | Pending\n{user.name} | Pending", components=rps_buttons,
                    listener=Rps_2pL(ctx.author, user))


def setup(bot):
  pass