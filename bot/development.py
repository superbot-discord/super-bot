from shared import *


class SampleButtonL(ui.listener.Listener):
  @ui.Listener.button()
  async def sample_button(self_, ctx: ui.ButtonInteraction):
    await ctx.respond(f"You pressed on the {ctx.component.label} button.", hidden= True)


class SampleSelectL(ui.listener.Listener):
  @ui.Listener.select(custom_id= "single-selection")
  async def sample_single_select(self_, ctx: ui.SelectInteraction):
    await ctx.respond(f"You selected {ctx.selected_options[0].label} in the single-selection menu.", hidden= True)

  @ui.Listener.select(custom_id= "multi-selection")
  async def sample_multi_select(self_, ctx: ui.SelectInteraction):
    await ctx.respond(f"You selected {', '.join([x.label for x in ctx.selected_options])} in the multi-selection menu.", hidden= True)

def sample_buttons(ctx):
  return [
  ui.Button(color='primary',   custom_id="primary", emoji="🟢",                                 label="Primary (blurple)"),
  ui.Button(color='secondary',custom_id="secondary",emoji=ctx.bot.get_emoji(824680026858717234),label="Secondary (grey)"),
  ui.Button(color='success',   custom_id="green",                                               label="Success (green)"),
  ui.Button(color='danger',    custom_id="red",                                                 label="Danger (red)"),
  ui.LinkButton(url=ctx.message.jump_url,                                                       label="URL (grey)"),
  ui.Button(color='primary',  emoji="🟢",                                 disabled=True, label="Primary (blurple)", new_line=True),
  ui.Button(color='secondary',emoji=ctx.bot.get_emoji(824680026858717234),disabled=True, label="Secondary (grey)"),
  ui.Button(color='success',                                              disabled=True, label="Success (green)"),
  ui.Button(color='danger',                                               disabled=True, label="Danger (red)"),
  ui.LinkButton(url=ctx.message.jump_url,                                 disabled=True, label="URL (grey)")]

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

@commands.command(aliases=['buttons'])
async def button(ctx, *, disposed = None):
  await ctx.reply("All buttons will not timeout.", components = sample_buttons(ctx))

@commands.command()
async def join(ctx, vc:discord.VoiceChannel = None, *, disposed = None):
  if not vc:
    vc = ctx.author.voice.channel
  vclients[ctx.guild] = await vc.connect()
  await ctx.reply("Joined the channel.")

@commands.command()
async def leave(ctx, *, disposed = None):
  await ctx.guild.voice_client.disconnect()
  del vclients[ctx.guild]
  await ctx.reply("Left the channel.")

@commands.command()
async def loop(ctx, *, disposed = None):
  if vclients.get(ctx.guild, None).loop:
    vclients.get(ctx.guild, None).loop = False
    await ctx.reply('Disabled loop.')
  elif not vclients.get(ctx.guild, None).loop:
    vclients.get(ctx.guild, None).loop = True
    await ctx.reply('Enabled loop.')

@commands.command()
@commands.cooldown(2, 10, commands.BucketType.user)
async def patience(ctx, *, disposed = None):
  await ctx.reply("Success!")

@patience.error
async def patience_error(ctx, error):
  await ctx.reply("This command is on cooldown! You can only use it twice per 10 seconds.")

@commands.command(aliases=['continue', 'resume', 'paused'])
async def pause(ctx, *, disposed = None):
  if vclients.get(ctx.guild, None).is_playing():
    vclients.get(ctx.guild, None).pause()
    await ctx.reply("Paused the song.")
  else:
    vclients.get(ctx.guild, None).resume()
    await ctx.reply("Resumed the song.")

@commands.command()
async def play(ctx, volume: typing.Optional[int]=100, *, song="rickroll"):
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
async def select(ctx, *, disposed = None):
  await ctx.reply("All menus will not timeout.", components = sample_menus, listener=SampleSelectL())

def setup(bot):
  bot.add_command(button)
  bot.add_command(join)
  bot.add_command(leave)
  bot.add_command(loop)
  bot.add_command(patience)
  bot.add_command(pause)
  bot.add_command(play)
  bot.add_command(select)
