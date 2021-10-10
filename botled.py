from shared import *

@commands.command()
async def lcd(ctx, *, text):
  sizes = font_lcd.getsize_multiline(text, spacing=20)
  image = Image.new("RGBA", (sizes[0], sizes[1]+15), color="#300000FF")
  draw = ImageDraw.Draw(image)
  draw.multiline_text((0, 3), text, font=font_lcd, fill="#D83030FF", spacing=20)
  image.save('output.png')
  await ctx.send(file=discord.File('output.png'))
  os.remove('output.png')

@commands.command()
async def led(ctx, mode: typing.Optional[typing.Literal['bold', 'regular', 'serif', 'mono']] = 'regular', *, text):
  if mode == 'bold':
    current_font = font_led_bold
  elif mode == 'serif':
    current_font = font_led_serif
  elif mode.startswith('mono'):
    current_font = font_led_mono
  else:
    current_font = font_led
  current_properties = led_font_dict[current_font]
  sizes = current_font.getsize_multiline(text, spacing=current_properties["spacing"])
  image = Image.new("RGBA", (sizes[0], sizes[1]+current_properties["height_plus"]), color="#300000FF")
  draw = ImageDraw.Draw(image)
  draw.multiline_text((0, current_properties["padding"]), text, font=current_font, fill="#D83030FF", spacing=current_properties["spacing"])
  image.save('output.png')
  await ctx.send(file=discord.File('output.png'))
  os.remove('output.png')

def setup(bot):
  bot.add_command(lcd)
  bot.add_command(led)