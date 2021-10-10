from shared import *

@commands.command()
async def lcd(ctx, mode: typing.Optional[typing.Literal['calc', 'regular']] = 'regular', color: typing.Optional[typing.Literal['cyan', 'red', 'green', 'blue', 'icyan', 'ired', 'igreen', 'iblue']] = 'red', alignment: typing.Optional[typing.Literal['left', 'center', 'right']] = 'left', *, text):
  if mode.startswith('calc'):
    current_font = font_lcd_calc
  else:
    current_font = font_lcd
  current_properties = led_font_dict[current_font]
  sizes = current_font.getsize_multiline(text, spacing=current_properties["spacing"])
  image = Image.new("RGBA", (sizes[0], sizes[1]+current_properties["height_plus"]), color=db["led_colors"][color]["bg"])
  draw = ImageDraw.Draw(image)
  draw.multiline_text((0, current_properties["padding"]), text, font=current_font, fill=db["led_colors"][color]["fg"], spacing=current_properties["spacing"], align=alignment)
  image.save('output.png')
  await ctx.send(file=discord.File('output.png'))
  os.remove('output.png')
#to_hex
@commands.command()
async def led(ctx, mode: typing.Optional[typing.Literal['bold', 'regular', 'serif', 'mono']] = 'regular', color: typing.Optional[typing.Literal['cyan', 'red', 'green', 'blue', 'icyan', 'ired', 'igreen', 'iblue']] = 'red', alignment: typing.Optional[typing.Literal['left', 'center', 'right']] = 'left', *, text):
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
  image = Image.new("RGBA", (sizes[0], sizes[1]+current_properties["height_plus"]), color=db["led_colors"][color]["bg"])
  draw = ImageDraw.Draw(image)
  draw.multiline_text((0, current_properties["padding"]), text, font=current_font, fill=db["led_colors"][color]["fg"], spacing=current_properties["spacing"], align=alignment)
  image.save('output.png')
  await ctx.send(file=discord.File('output.png'))
  os.remove('output.png')

def setup(bot):
  bot.add_command(lcd)
  bot.add_command(led)