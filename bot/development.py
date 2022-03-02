from _bot import bs
from shared import commands, discord, ra, SequenceMatcher, typing, ui

vclients = {}

class SampleButtonL(ui.listener.Listener):
  @ui.Listener.button()
  async def sample_button(self_, ctx: ui.ButtonInteraction):
    await ctx.respond(f"You pressed on the {ctx.component.label} button.", hidden= True)


class SampleSelectL(ui.listener.Listener):
  @ui.Listener.select(custom_id="single-selection")
  async def sample_single_select(self_, ctx: ui.SelectInteraction):
    await ctx.respond(f"You selected {ctx.selected_options[0].label} in the single-selection menu.", hidden= True)

  @ui.Listener.select(custom_id="multi-selection")
  async def sample_multi_select(self_, ctx: ui.SelectInteraction):
    await ctx.respond(f"You selected {', '.join([x.label for x in ctx.selected_options])} in the multi-selection menu.", hidden= True)


class ThinkForeverL(ui.listener.Listener):
  @ui.Listener.button(custom_id= "think")
  async def think(self_, ctx: ui.ButtonInteraction):
    await ctx.message.edit("I will now think forever. Have fun waiting!", components=[think_buttons[1]])
    await ctx.defer()


def sample_buttons(ctx):
  return [
  ui.Button(color='primary', custom_id="p", label="Primary (blurple)", emoji="🟢"),
  ui.Button(color='secondary', custom_id="s", label="Secondary (grey)", emoji=ctx.bot.get_emoji(824680026858717234)),
  ui.Button(color='green',  custom_id="g", label="Success (green)"),
  ui.Button(color='red', custom_id="r", label="Danger (red)"),
  ui.LinkButton(url="https://example.com", label="URL (grey)"),
  ui.Button(color='primary', disabled=True, label="Primary (blurple)", emoji="🟢", new_line=True),
  ui.Button(color='secondary', disabled=True, label="Secondary (grey)", emoji=ctx.bot.get_emoji(824680026858717234)),
  ui.Button(color='green', disabled=True, label="Success (green)"),
  ui.Button(color='red', disabled=True, label="Danger (red)"),
  ui.LinkButton(url="https://example.com", disabled=True, label="URL (grey)")]

sample_options = [
  ui.SelectOption(value="Red"   , label="Red"   , description="Roses are red"              , emoji="🔴"),
  ui.SelectOption(value="Orange", label="Orange", description="Oranges are orange"         , emoji="🟠"),
  ui.SelectOption(value="Yellow", label="Yellow", description="Sunflowers are yellow"      , emoji="🟡"),
  ui.SelectOption(value="Green" , label="Green" , description="Cabbages are green"         , emoji="🟢"),
  ui.SelectOption(value="Blue"  , label="Blue"  , description="Discord is blue"            , emoji="🔵", default=True),
  ui.SelectOption(value="Purple", label="Purple", description="Violets are blurple"        , emoji="🟣"),
  ui.SelectOption(value="Brown" , label="Brown" , description="Dry plants are brown"       , emoji="🟤")]

sample_menus = [
  ui.SelectMenu(placeholder="Select one option",          custom_id="single-selection", options=sample_options),
  ui.SelectMenu(placeholder="Select two to five options", custom_id="multi-selection" , min_values=2, max_values=5, options=sample_options),
  ui.SelectMenu(placeholder="Select one option",          disabled=True, options=sample_options),
  ui.SelectMenu(placeholder="Select two to five options", disabled=True, min_values=2, max_values=5, options=sample_options)]

think_buttons = [
  ui.Button(label="Think", custom_id="think", color='primary', emoji="🧠"),
  ui.Button(label="Think", custom_id="think", color='primary', emoji="🧠", disabled=True)
]


@commands.command(aliases=['buttons'])
async def button(ctx, *, disposed=None):
  await ctx.reply("All buttons will not timeout.", components=sample_buttons(ctx), listener=SampleButtonL())

@bs.command(name="buttons", description="Generates all kinds of buttons. Mainly for development purposes.")
async def buttons(ctx):
  await ctx.respond("All buttons will not timeout.", components=sample_buttons(ctx), listener=SampleButtonL())

@commands.command()
async def join(ctx, vc: discord.VoiceChannel = None, *, disposed=None):
  if not vc:
    vc = ctx.author.voice.channel
  vclients[ctx.guild] = await vc.connect()
  await ctx.reply("Joined the channel.")

@commands.command()
async def leave(ctx, *, disposed=None):
  await ctx.guild.voice_client.disconnect()
  del vclients[ctx.guild]
  await ctx.reply("Left the channel.")

@commands.command()
async def loop(ctx, *, disposed=None):
  if vclients.get(ctx.guild, None).loop:
    vclients.get(ctx.guild, None).loop = False
    await ctx.reply('Disabled loop.')
  elif not vclients.get(ctx.guild, None).loop:
    vclients.get(ctx.guild, None).loop = True
    await ctx.reply('Enabled loop.')

@commands.command()
@commands.cooldown(2, 10, commands.BucketType.user)
async def patience(ctx, *, disposed=None):
  await ctx.reply("Success!")

@patience.error
async def patience_error(ctx, error):
  await ctx.reply("This command is on cooldown! You can only use it twice per 10 seconds.")

@commands.command(aliases=['continue', 'resume', 'paused'])
async def pause(ctx, *, disposed=None):
  if vclients.get(ctx.guild, None).is_playing():
    vclients.get(ctx.guild, None).pause()
    await ctx.reply("Paused the song.")
  else:
    vclients.get(ctx.guild, None).resume()
    await ctx.reply("Resumed the song.")

@commands.command()
async def play(ctx, volume: typing.Optional[int] = 100, *, song="rickroll"):
  vc = vclients.get(ctx.guild, None)
  if not vc:
    vc = await ctx.author.voice.channel.connect()
    vclients[ctx.guild] = vc
  if len(ctx.message.attachments):
    random_play_id = ra.randint(1000000,9999999)
    await ctx.message.attachments[0].save(f'music_{random_play_id}.mp3')
    audio_source = discord.FFmpegPCMAudio(f'music_{random_play_id}.mp3')
  elif SequenceMatcher(None, song, "rickroll").ratio() > 0.7:
    audio_source = discord.FFmpegPCMAudio('songs/rickroll.mp3', options=f'-filter:a "volume={volume/100}"')
  elif SequenceMatcher(None, song, "stickbug").ratio() > 0.7:
    audio_source = discord.FFmpegPCMAudio('songs/stickbug.mp3')
  vc.play(audio_source)
  await ctx.reply("Playing the song.")

@commands.command(aliases=['selectmenu', 'menu', 'option', 'options'])
async def select(ctx, *, disposed=None):
  await ctx.reply("All menus will not timeout.", components= sample_menus, listener=SampleSelectL())

@commands.command(aliases=['think'])
async def think_forever(ctx, *, disposed=None):
  await ctx.reply("It is easy to make me think forever. Just click on the button!", components=[think_buttons[0]], listener= ThinkForeverL())

def setup(bot):
  bot.add_command(button)
  bot.add_command(join)
  bot.add_command(leave)
  bot.add_command(loop)
  bot.add_command(patience)
  bot.add_command(pause)
  bot.add_command(play)
  bot.add_command(select)
  bot.add_command(think_forever)
