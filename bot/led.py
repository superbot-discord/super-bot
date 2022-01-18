from shared import commands, db, discord, Image, ImageDraw, ImageFont, try_delete, typing
#"icyan" : {"fg":"#87B33FFF", "bg":"#131402FF"}

font_led      = ImageFont.truetype("fonts/led.ttf", 50)
font_led_bold = ImageFont.truetype("fonts/led_bold.ttf", 50)
font_led_caps = ImageFont.truetype("fonts/led_caps.ttf", 50)
font_led_mono = ImageFont.truetype("fonts/led_mono.ttf", 50)
font_led_serif= ImageFont.truetype("fonts/led_serif.ttf", 50)

font_led2      = ImageFont.truetype("fonts/led2.ttf", 50)
font_led2_bold = ImageFont.truetype("fonts/led2_bold.ttf", 50)
font_led2_caps = ImageFont.truetype("fonts/led2_caps.ttf", 50)
font_led2_fat  = ImageFont.truetype("fonts/led2_fat.ttf", 50)
font_led2_modern=ImageFont.truetype("fonts/led2_modern.ttf", 50)
font_led2_serif= ImageFont.truetype("fonts/led2_serif.ttf", 50)

font_led3_1   = ImageFont.truetype("fonts/led3_1.ttf", 50)
font_led3_1i  = ImageFont.truetype("fonts/led3_1i.ttf", 50)
font_led3_2   = ImageFont.truetype("fonts/led3_2.ttf", 50)
font_led3_2i  = ImageFont.truetype("fonts/led3_2i.ttf", 50)
font_led3_3   = ImageFont.truetype("fonts/led3_3.ttf", 50)
font_led3_3i  = ImageFont.truetype("fonts/led3_3i.ttf", 50)

font_led4_1   = ImageFont.truetype("fonts/led4_1.ttf", 50)
font_led4_1i  = ImageFont.truetype("fonts/led4_1i.ttf", 50)
font_led4_2   = ImageFont.truetype("fonts/led4_2.ttf", 50)
font_led4_2i  = ImageFont.truetype("fonts/led4_2i.ttf", 50)
font_led4_3   = ImageFont.truetype("fonts/led4_3.ttf", 50)
font_led4_3i  = ImageFont.truetype("fonts/led4_3i.ttf", 50)

font_lcd      = ImageFont.truetype("fonts/lcd.ttf", 50)
font_lcd_calc = ImageFont.truetype("fonts/lcd_calc.ttf", 50)
font_lcd_dense= ImageFont.truetype("fonts/lcd_dense.otf", 50)
font_lcd_mono = ImageFont.truetype("fonts/lcd_mono.otf", 50)

font_lcd2_1   = ImageFont.truetype("fonts/lcd2_1.ttf", 50)
font_lcd2_1i  = ImageFont.truetype("fonts/lcd2_1i.ttf", 50)
font_lcd2_2   = ImageFont.truetype("fonts/lcd2_2.ttf", 50)
font_lcd2_2i  = ImageFont.truetype("fonts/lcd2_2i.ttf", 50)
font_lcd2_3   = ImageFont.truetype("fonts/lcd2_3.ttf", 50)
font_lcd2_3i  = ImageFont.truetype("fonts/lcd2_3i.ttf", 50)

font_lcd3_1   = ImageFont.truetype("fonts/lcd3_1.ttf", 50)
font_lcd3_1i  = ImageFont.truetype("fonts/lcd3_1i.ttf", 50)
font_lcd3_2   = ImageFont.truetype("fonts/lcd3_2.ttf", 50)
font_lcd3_2i  = ImageFont.truetype("fonts/lcd3_2i.ttf", 50)
font_lcd3_3   = ImageFont.truetype("fonts/lcd3_3.ttf", 50)
font_lcd3_3i  = ImageFont.truetype("fonts/lcd3_3i.ttf", 50)

whitney       = ImageFont.truetype("fonts/whitney.otf", 34)

led_font_dict = {
  font_led      :  {"spacing" : 20, "padding" : 3  , "height_plus" : 15 , "required_height_plus" : 3  , "unneeded_width" : 8 , "unneeded_padding" : 12},
  font_led_bold :  {"spacing" : 20, "padding" : 3  , "height_plus" : 15 , "required_height_plus" : 3  , "unneeded_width" : 6 , "unneeded_padding" : 12},
  font_led_caps :  {"spacing" : 10, "padding" : -10, "height_plus" : -10, "required_height_plus" : -10, "unneeded_width" : 7 , "unneeded_padding" : 0},
  font_led_mono :  {"spacing" : 10, "padding" : -12, "height_plus" : -13, "required_height_plus" : -13, "unneeded_width" : 7 , "unneeded_padding" : 14},
  font_led_serif:  {"spacing" : 25, "padding" : 9  , "height_plus" : 22 , "required_height_plus" : 8  , "unneeded_width" : 6 , "unneeded_padding" : 12},

  font_led2       :{"spacing" : 10, "padding" : -5 , "height_plus" : 5  , "required_height_plus" : -5 , "unneeded_width" : 5 , "unneeded_padding" : 10},
  font_led2_bold  :{"spacing" : 50, "padding" : 20 , "height_plus" : 40 , "required_height_plus" : 20 , "unneeded_width" : 8 , "unneeded_padding" : 20},
  font_led2_caps  :{"spacing" : 10, "padding" : -15, "height_plus" : -15, "required_height_plus" : -15, "unneeded_width" : 5 , "unneeded_padding" : 0},
  font_led2_fat   :{"spacing" : 10, "padding" : -15, "height_plus" : -15, "required_height_plus" : -15, "unneeded_width" : 5 , "unneeded_padding" : 0},
  font_led2_modern:{"spacing" : 20, "padding" : 0  , "height_plus" : 10 , "required_height_plus" : -10, "unneeded_width" : 5 , "unneeded_padding" : 4},
  font_led2_serif :{"spacing" : 25, "padding" : 5  , "height_plus" : 15 , "required_height_plus" : 5  , "unneeded_width" : 5 , "unneeded_padding" : 10},

  font_led3_1    : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 11 },
  font_led3_1i   : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 11 },
  font_led3_2    : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 10 },
  font_led3_2i   : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 10 },
  font_led3_3    : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 9  },
  font_led3_3i   : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 9  },

  font_led4_1    : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 11 },
  font_led4_1i   : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 11 },
  font_led4_2    : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 10 },
  font_led4_2i   : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 10 },
  font_led4_3    : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 9  },
  font_led4_3i   : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 9  },

  font_lcd       : {"spacing" : 20, "padding" : 3,  "height_plus" : 15},
  font_lcd_calc  : {"spacing" : 20, "padding" : 3,  "height_plus" : 15},
  font_lcd_dense : {"spacing" : 20, "padding" : 3,  "height_plus" : 15},
  font_lcd_mono  : {"spacing" : 20, "padding" : 3,  "height_plus" : 15},

  font_lcd2_1    : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 11 },
  font_lcd2_1i   : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 11 },
  font_lcd2_2    : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 10 },
  font_lcd2_2i   : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 10 },
  font_lcd2_3    : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 9  },
  font_lcd2_3i   : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 9  },

  font_lcd3_1    : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 11 },
  font_lcd3_1i   : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 11 },
  font_lcd3_2    : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 10 },
  font_lcd3_2i   : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 10 },
  font_lcd3_3    : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 9  },
  font_lcd3_3i   : {"spacing" : 20, "padding" : 3 , "height_plus" : 3 , "unneeded_width" : 9  }
}

led_colors = typing.Optional[typing.Literal["cyan", "icyan", "crystal", "icrystal", "amber", "iamber", "red", "ired", "green", "igreen", "blue", "iblue", "purple", "ipurple", "yellow", "iyellow",
                                            "teal", "iteal", "black", "white", "tblack", "twhite", "dark", "light", "tdark", "tlight", "wdark", "wlight", "twdark", "twlight"]]
led_alignment = typing.Optional[typing.Literal['left', 'center', 'right']]
led_34_modes = typing.Optional[typing.Literal['1', '1i', '2', '2i', '3', '3i']]
# S: Getsize sizes   C: Current properties   M: Minus padding   L: Logest text line
led_sizer      = lambda s, c, m, l: (s[0]-c["unneeded_width"], s[1]-m+(c["height_plus"] if any(check in l for check in "gjpqy,;") else c["required_height_plus"]))
led34_sizer    = lambda s, c, m, l: (s[0]-c["unneeded_width"], s[1]-m+c["height_plus"])
led_positioner = lambda    c, m   : (0, c["padding"] - m)
led34_positioner=lambda    c, m   : (-4, c["padding"] - m)
all_halfheight = lambda       t   : all(check in "acegmnopqrsuvwxyz., " for check in t.splitlines()[0])
channel_sort   = lambda    c      : 1 if c.type in [discord.ChannelType.voice, discord.ChannelType.stage_voice] else 0

def autowrap(needed_width, font, text):
  output = ""
  cache_text = ""
  for x in text.split(' '):
    width = font.getsize_multiline(f"{cache_text}{x}")[0]
    if width < needed_width or cache_text == "":
      cache_text += f"{x} "
    else:
      output += f"{cache_text}\n"
      cache_text = ""
  output += f"{cache_text}"
  return output

def led_server_info(server: discord.Guild):
  desc = server.name
  def desc_add(ch):
    if ch.type == discord.ChannelType.category:
      return f"\n {ch.name}"
    elif ch.type == discord.ChannelType.text:
      cache = f"\n   #{ch.name}"
      for x in ch.threads:
        cache += f"\n     -{x.name}"
      return cache
    elif ch.type == discord.ChannelType.voice:
      return f"\n   !{ch.name}"
    elif ch.type == discord.ChannelType.stage_voice:
      return f"\n   %{ch.name}"
    elif ch.type == discord.ChannelType.store:
      return f"\n   ${ch.name}"
    elif ch.type == discord.ChannelType.news:
      return f"\n   >{ch.name}"
    #elif ch.type in [discord.ChannelType.news_thread, discord.ChannelType.private_thread, discord.ChannelType.public_thread]:
    #  return f"\n     -{ch.name}"
    else:
      return ""
  led_server_channels = list(filter(lambda i: i.type != discord.ChannelType.category, server.channels))
  led_server_channels.sort(key=channel_sort)
  for x in led_server_channels:
    if not x.category:
      desc += desc_add(x)
  led_server_categories = server.categories
  led_server_categories.sort(key=lambda i: i.position)
  for x in led_server_categories:
    desc += desc_add(x)
    led_in_category_channels = x.channels
    #led_in_category_channels.sort(key=lambda i: i.position)
    led_in_category_channels.sort(key=channel_sort)
    for y in led_in_category_channels:
      desc += desc_add(y)
  return desc

@commands.command()
async def fakemsg(ctx, size: typing.Optional[typing.Literal['mobile', 'tablet', 'laptop']] = 'mobile', theme: typing.Optional[typing.Literal['white', 'dark', 'black']] = 'dark', *, text_input):
  true_size = db["fakemsg_size"][size]
  text = autowrap(true_size, whitney, text_input)
  image = Image.new("RGBA", (true_size, whitney.getsize_multiline(text)[1]+8), color=db["led_colors"][theme]["bg"])
  draw = ImageDraw.Draw(image)
  draw.multiline_text((-1, 0), text, font=whitney, fill=db["led_colors"][theme]["fg"], spacing=0, align="left")
  image.save('output.png')
  await ctx.reply(file=discord.File('output.png'))
  try_delete('output.png')

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
  await ctx.reply(file=discord.File('output.png'))
  try_delete('output.png')

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
  minus_padding = current_properties["unneeded_padding"] if all_halfheight(text) else 0
  image = Image.new("RGBA", led_sizer(sizes, current_properties, minus_padding, text.splitlines()[len(text.splitlines())-1]), color=db["led_colors"][color]["bg"])
  draw = ImageDraw.Draw(image)
  draw.multiline_text(led_positioner(current_properties, minus_padding), text, font=current_font, fill=db["led_colors"][color]["fg"], spacing=current_properties["spacing"], align=alignment)
  image.save('output.png')
  await ctx.reply(file=discord.File('output.png'))
  try_delete('output.png')

@commands.command()
async def led_server(ctx, mode: typing.Optional[typing.Literal['regular', 'bold', 'caps', 'mono', 'serif']] = 'regular', color: led_colors = 'red', alignment: led_alignment = 'left'):
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
  text = led_server_info(ctx.guild)
  sizes = current_font.getsize_multiline(text, spacing=current_properties["spacing"])
  minus_padding = current_properties["unneeded_padding"] if all_halfheight(text) else 0
  image = Image.new("RGBA", led_sizer(sizes, current_properties, minus_padding, text.splitlines()[len(text.splitlines())-1]), color=db["led_colors"][color]["bg"])
  draw = ImageDraw.Draw(image)
  draw.multiline_text(led_positioner(current_properties, minus_padding), text, font=current_font, fill=db["led_colors"][color]["fg"], spacing=current_properties["spacing"], align=alignment)
  image.save('output.png')
  await ctx.reply(file=discord.File('output.png'))
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
  minus_padding = current_properties["unneeded_padding"] if all_halfheight(text) else 0
  image = Image.new("RGBA", led_sizer(sizes, current_properties, minus_padding, text.splitlines()[len(text.splitlines())-1]), color=db["led_colors"][color]["bg"])
  draw = ImageDraw.Draw(image)
  draw.multiline_text(led_positioner(current_properties, minus_padding), text, font=current_font, fill=db["led_colors"][color]["fg"], spacing=current_properties["spacing"], align=alignment)
  image.save('output.png')
  await ctx.reply(file=discord.File('output.png'))
  try_delete('output.png')

@commands.command()
async def led2_server(ctx, mode: typing.Optional[typing.Literal['regular', 'bold', 'caps', 'fat', 'modern', 'serif']] = 'regular', color: led_colors = 'red', alignment: led_alignment = 'left'):
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
  text = led_server_info(ctx.guild)
  sizes = current_font.getsize_multiline(text, spacing=current_properties["spacing"])
  minus_padding = current_properties["unneeded_padding"] if all_halfheight(text) else 0
  image = Image.new("RGBA", led_sizer(sizes, current_properties, minus_padding, text.splitlines()[len(text.splitlines())-1]), color=db["led_colors"][color]["bg"])
  draw = ImageDraw.Draw(image)
  draw.multiline_text(led_positioner(current_properties, minus_padding), text, font=current_font, fill=db["led_colors"][color]["fg"], spacing=current_properties["spacing"], align=alignment)
  image.save('output.png')
  await ctx.reply(file=discord.File('output.png'))
  try_delete('output.png')

@commands.command()
async def led3(ctx, mode: led_34_modes = '2', color: led_colors = 'red', alignment: led_alignment = 'left', *, text):
  if mode == '1':
    current_font = font_led3_1
  elif mode == '1i':
    current_font = font_led3_1i
  elif mode == '2i':
    current_font = font_led3_2i
  elif mode == '3':
    current_font = font_led3_3
  elif mode == '3i':
    current_font = font_led3_3i
  else:
    current_font = font_led3_2
  current_properties = led_font_dict[current_font]
  sizes = current_font.getsize_multiline(text, spacing=current_properties["spacing"])
  minus_padding = 3
  image = Image.new("RGBA", led34_sizer(sizes, current_properties, minus_padding, text.splitlines()[len(text.splitlines())-1]), color=db["led_colors"][color]["bg"])
  draw = ImageDraw.Draw(image)
  draw.multiline_text(led34_positioner(current_properties, minus_padding), text, font=current_font, fill=db["led_colors"][color]["fg"], spacing=current_properties["spacing"], align=alignment)
  image.save('output.png')
  await ctx.reply(file=discord.File('output.png'))
  try_delete('output.png')

@commands.command()
async def led3_server(ctx, mode: led_34_modes = '1', color: led_colors = 'red', alignment: led_alignment = 'left'):
  if mode == '1':
    current_font = font_led3_1
  elif mode == '1i':
    current_font = font_led3_1i
  elif mode == '2i':
    current_font = font_led3_2i
  elif mode == '3':
    current_font = font_led3_3
  elif mode == '3i':
    current_font = font_led3_3i
  else:
    current_font = font_led3_2
  text = led_server_info(ctx.guild)
  current_properties = led_font_dict[current_font]
  sizes = current_font.getsize_multiline(text, spacing=current_properties["spacing"])
  minus_padding = 3
  image = Image.new("RGBA", led34_sizer(sizes, current_properties, minus_padding, text.splitlines()[len(text.splitlines())-1]), color=db["led_colors"][color]["bg"])
  draw = ImageDraw.Draw(image)
  draw.multiline_text(led34_positioner(current_properties, minus_padding), text, font=current_font, fill=db["led_colors"][color]["fg"], spacing=current_properties["spacing"], align=alignment)
  image.save('output.png')
  await ctx.reply(file=discord.File('output.png'))
  try_delete('output.png')

@commands.command()
async def led4(ctx, mode: led_34_modes = '2', color: led_colors = 'red', alignment: led_alignment = 'left', *, text):
  if mode == '1':
    current_font = font_led4_1
  elif mode == '1i':
    current_font = font_led4_1i
  elif mode == '2i':
    current_font = font_led4_2i
  elif mode == '3':
    current_font = font_led4_3
  elif mode == '3i':
    current_font = font_led4_3i
  else:
    current_font = font_led4_2
  current_properties = led_font_dict[current_font]
  sizes = current_font.getsize_multiline(text, spacing=current_properties["spacing"])
  minus_padding = 3
  image = Image.new("RGBA", led34_sizer(sizes, current_properties, minus_padding, text.splitlines()[len(text.splitlines())-1]), color=db["led_colors"][color]["bg"])
  draw = ImageDraw.Draw(image)
  draw.multiline_text(led34_positioner(current_properties, minus_padding), text, font=current_font, fill=db["led_colors"][color]["fg"], spacing=current_properties["spacing"], align=alignment)
  image.save('output.png')
  await ctx.reply(file=discord.File('output.png'))
  try_delete('output.png')

@commands.command()
async def led4_server(ctx, mode: led_34_modes = '1', color: led_colors = 'red', alignment: led_alignment = 'left'):
  if mode == '1':
    current_font = font_led4_1
  elif mode == '1i':
    current_font = font_led4_1i
  elif mode == '2i':
    current_font = font_led4_2i
  elif mode == '3':
    current_font = font_led4_3
  elif mode == '3i':
    current_font = font_led4_3i
  else:
    current_font = font_led4_2
  text = led_server_info(ctx.guild)
  current_properties = led_font_dict[current_font]
  sizes = current_font.getsize_multiline(text, spacing=current_properties["spacing"])
  minus_padding = 3
  image = Image.new("RGBA", led34_sizer(sizes, current_properties, minus_padding, text.splitlines()[len(text.splitlines())-1]), color=db["led_colors"][color]["bg"])
  draw = ImageDraw.Draw(image)
  draw.multiline_text(led34_positioner(current_properties, minus_padding), text, font=current_font, fill=db["led_colors"][color]["fg"], spacing=current_properties["spacing"], align=alignment)
  image.save('output.png')
  await ctx.reply(file=discord.File('output.png'))
  try_delete('output.png')

@commands.command()
async def led_bar(ctx, total : int, step : int, color: led_colors = 'red', width : int = 5):
  #width = width if width else round(total/66.0555)
  image = Image.new("RGBA", (total*20, width*20), color=db["led_colors"][color]["bg"])
  draw = ImageDraw.Draw(image)
  for x in range(step):
    for y in range(width):
      draw.rectangle([x*20, y*20+1, x*20+17, y*20+18], fill=db["led_colors"][color]["fg"])
  image.save('output.png')
  await ctx.reply(file=discord.File('output.png'))
  try_delete('output.png')

def setup(bot):
  bot.add_command(fakemsg)
  bot.add_command(lcd)
  bot.add_command(led)
  bot.add_command(led_server)
  bot.add_command(led2)
  bot.add_command(led2_server)
  bot.add_command(led3)
  bot.add_command(led3_server)
  bot.add_command(led4)
  bot.add_command(led4_server)
  bot.add_command(led_bar)