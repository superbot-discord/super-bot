import random
from difflib import SequenceMatcher
import typing

from discord.ext import commands

from shared import *


@commands.command(aliases=['buttons'])
async def button(ctx, *, text=None):
  sample_buttons_view = ui.View(timeout=None)
  for count in sample_buttons(ctx):
    sample_buttons_view.add_item(count)
  await ctx.send("All buttons will not timeout.", view = sample_buttons_view)

@commands.command()
async def join(ctx, vc:discord.VoiceChannel = None, *, text=None):
  if not vc:
    vc = ctx.author.voice.channel
  vclients[ctx.guild] = await vc.connect()
  await ctx.send("Joined the channel.")

@commands.command()
async def leave(ctx, *, text=None):
  await ctx.guild.voice_client.disconnect()
  del vclients[ctx.guild]
  await ctx.send("Left the channel.")

@commands.command()
async def loop(ctx, *, text=None):
  if ctx.voice_state.loop:
    ctx.voice_state.loop = False
    await ctx.send('Disabled loop.')
  elif not ctx.voice_state.loop:
    ctx.voice_state.loop = True
    await ctx.send('Enabled loop.')

@commands.command()
@commands.cooldown(2, 10, commands.BucketType.user)
async def patience(ctx, *, text=None):
  await ctx.send("Success!")

@patience.error
async def patience_error(ctx, error):
  await ctx.send("This command is on cooldown! You can only use it twice per 10 seconds.")

@commands.command(aliases=['continue', 'resume', 'paused'])
async def pause(ctx, *, text=None):
  if ctx.voice_state.is_playing and ctx.voice_state.voice.is_playing():
    ctx.voice_state.voice.pause()
    await ctx.send("Paused the song.")
  else:
    ctx.voice_state.voice.resume()
    await ctx.send("Resumed the song.")

@commands.command()
async def play(ctx, volume: typing.Optional[int]=100, *, song="rickroll"):
  vc = vclients.get(ctx.guild, None)
  if not vc:
    vc = await ctx.author.voice.channel.connect()
    vclients[ctx.guild] = vc
  if SequenceMatcher(None, song, "rickroll").ratio() > 0.7:
    audio_source = discord.FFmpegPCMAudio('songs/rickroll.mp3', options=f'-filter:a "volume={volume/100}"')
  elif SequenceMatcher(None, song, "stickbug").ratio() > 0.7:
    audio_source = discord.FFmpegPCMAudio('songs/stickbug.mp3')
  elif len(ctx.message.attachments):
    random_play_id = random.randint(1000000,9999999)
    await ctx.message.attachments[0].save(f'music_{random_play_id}.mp3')
    audio_source = discord.FFmpegPCMAudio(f'music_{random_play_id}.mp3')
  vc.play(audio_source)
  await ctx.send("Playing the song.")

@commands.command(aliases=['selectmenu', 'menu', 'option', 'options'])
async def select(ctx, *, text=None):
  sample_select_view = ui.View(timeout=None)
  for count in sample_menus():
    sample_select_view.add_item(count)
  await ctx.send("All menus will not timeout.", view = sample_select_view)
def setup(bot):
  bot.add_command(button)
  bot.add_command(join)
  bot.add_command(leave)
  bot.add_command(patience)
  bot.add_command(play)
  bot.add_command(select)
