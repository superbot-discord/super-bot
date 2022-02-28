from _bot import bs
from shared import Embed, ra, ui


rps_dict = {0: "Rock", 1: "Paper", 2: "Scissors"}
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
  async def r(self_, ctx: ui.ButtonInteraction):
    await self_.rps_1p_handle(ctx)

  @ui.Listener.button(custom_id="1")
  async def p(self_, ctx: ui.ButtonInteraction):
    await self_.rps_1p_handle(ctx)

  @ui.Listener.button(custom_id="2")
  async def s(self_, ctx: ui.ButtonInteraction):
    await self_.rps_1p_handle(ctx)


@bs.command(name="game_rps_1p", description="Starts a solo game of Rock-Paper-Scissors.")
async def game_rps_1p(ctx: ui.SlashInteraction):
  await ctx.respond(components=rps_buttons, listener=Rps_1pL(ra.randint(0, 2)))


def setup(bot):
  pass