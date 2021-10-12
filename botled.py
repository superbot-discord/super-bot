from shared import *
#"icyan" : {"fg":"#87B33FFF", "bg":"#131402FF"}
led_colors = typing.Optional[typing.Literal["cyan", "icyan", "crystal", "icrystal" "red", "ired", "green", "igreen", "blue", "iblue", "purple", "ipurple", "yellow", "iyellow",
                                            "teal", "iteal", "black", "white", "tblack", "twhite", "dark", "light", "tdark", "tlight"]]
led_alignment = typing.Optional[typing.Literal['left', 'center', 'right']]

@commands.command()
async def lcd(ctx, mode: typing.Optional[typing.Literal['regular', 'calc', 'dense', 'mono']] = 'regular', color: led_colors = 'red', alignment: led_alignment = 'left', *, text):
  if mode == 'calc':
    current_font = font_lcd_calc
  elif mode == 'dense':
    current_font = font_lcd_dense
  elif mode == 'mono':
    current_font = font_lcd_mono
  else:
    current_font = font_lcd
  current_properties = led_font_dict[current_font]
  sizes = current_font.getsize_multiline(text, spacing=current_properties["spacing"])
  image = Image.new("RGBA", (sizes[0], sizes[1]+current_properties["height_plus"]), color=db["led_colors"][color]["bg"])
  draw = ImageDraw.Draw(image)
  draw.multiline_text((0, current_properties["padding"]), text, font=current_font, fill=db["led_colors"][color]["fg"], spacing=current_properties["spacing"], align=alignment)
  image.save('output.png')
  await ctx.send(file=discord.File('output.png'))
  try_delete('output.png')
#to_hex

@commands.command()
async def led(ctx, mode: typing.Optional[typing.Literal['regular', 'bold', 'caps', 'mono', 'serif']] = 'regular', color: led_colors = 'red', alignment: led_alignment = 'left', *, text):
  if mode == 'bold':
    current_font = font_led_bold
  elif mode == 'caps':
    current_font = font_led_caps
  elif mode == 'mono':
    current_font = font_led_mono
  elif mode == 'serif':
    current_font = font_led_serif
  else:
    current_font = font_led
  current_properties = led_font_dict[current_font]
  sizes = current_font.getsize_multiline(text, spacing=current_properties["spacing"])
  image = Image.new("RGBA", (sizes[0], sizes[1]+current_properties["height_plus"]), color=db["led_colors"][color]["bg"])
  draw = ImageDraw.Draw(image)
  draw.multiline_text((0, current_properties["padding"]), text, font=current_font, fill=db["led_colors"][color]["fg"], spacing=current_properties["spacing"], align=alignment)
  image.save('output.png')
  await ctx.send(file=discord.File('output.png'))
  try_delete('output.png')

@commands.command()
async def led2(ctx, mode: typing.Optional[typing.Literal['regular', 'bold', 'caps', 'fat', 'modern', 'serif']] = 'regular', color: led_colors = 'red', alignment: led_alignment = 'left', *, text):
  if mode == 'bold':
    current_font = font_led2_bold
  elif mode == 'caps':
    current_font = font_led2_caps
  elif mode == 'fat':
    current_font = font_led2_fat
  elif mode == 'mono':
    current_font = font_led2_modern
  elif mode == 'serif':
    current_font = font_led2_serif
  else:
    current_font = font_led2
  current_properties = led_font_dict[current_font]
  sizes = current_font.getsize_multiline(text, spacing=current_properties["spacing"])
  image = Image.new("RGBA", (sizes[0], sizes[1]+current_properties["height_plus"]), color=db["led_colors"][color]["bg"])
  draw = ImageDraw.Draw(image)
  draw.multiline_text((0, current_properties["padding"]), text, font=current_font, fill=db["led_colors"][color]["fg"], spacing=current_properties["spacing"], align=alignment)
  image.save('output.png')
  await ctx.send(file=discord.File('output.png'))
  try_delete('output.png')

def setup(bot):
  bot.add_command(lcd)
  bot.add_command(led)
  bot.add_command(led2)