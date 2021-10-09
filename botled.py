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
async def led(ctx, *, text):
  sizes = font_led.getsize_multiline(text, spacing=20)
  image = Image.new("RGBA", (sizes[0], sizes[1]+15), color="#300000FF")
  draw = ImageDraw.Draw(image)
  draw.multiline_text((0, 3), text, font=font_led, fill="#D83030FF", spacing=20)
  image.save('output.png')
  await ctx.send(file=discord.File('output.png'))
  os.remove('output.png')

def setup(bot):
  bot.add_command(lcd)
  bot.add_command(led)