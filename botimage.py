import colorsys
import random as ra

import discord
import matplotlib.pyplot as plt
import pytesseract
from captcha.image import ImageCaptcha
from colorgram import extract
from colorthief import ColorThief
from discord.ext import commands
from pdf2image import convert_from_path
from pyzbar import pyzbar

import ascii2 as asc
import requests
from shared import *

cimage = ImageCaptcha()
@commands.command()
async def captcha(ctx, *, text = None):
  if text == None:
    text = ra.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") + ra.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") + ra.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") + ra.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
  data = cimage.generate(text)
  cimage.write(text, 'captcha.png')
  await ctx.reply(f"Captcha for {text}", file = discord.File('captcha.png'))
  try_delete('captcha.png')

@commands.command()
async def image(ctx, *, mode):
  try:
    await ctx.message.attachments[0].save('input.png')
  except:
    mode_split = mode.split(" ")
    user_input = mode_split[0]
    mode = " ".join(mode_split[1:])
    try:
      image_user = await commands.UserConverter().convert(ctx, user_input)
      downloaded_obj = requests.get(image_user.display_avatar.url.replace("?size=1024", "?size=4096"))
    except:
      downloaded_obj = requests.get(user_input)
    with open("input.png", "wb") as f:
      f.write(downloaded_obj.content)
  if mode.startswith("analyse") or mode.startswith("analyze"):
    try:
      scale = int(mode.split(" ")[1])
    except:
      scale = 1000
    try:
      colors = int(mode.split(" ")[2])
    except:
      colors = 5
    dominant = analyse(scale, colors)
    try:
      await ctx.reply(f"Images are sorted by amount, brightness and hue respectively.\nDominant color: {dominant}", files=[discord.File('output_amount.png'), discord.File('output_lightness.png'), discord.File('output_hue.png'), discord.File('analysis.txt')])
    except:
      await ctx.reply(f"Images are sorted by amount, brightness and hue respectively.\nDominant color: {dominant}", file=discord.File('output_amount.png'))
      await ctx.reply(file=discord.File('output_lightness.png'))
      await ctx.reply(file=discord.File('output_hue.png'))
      await ctx.reply(file=discord.File('analysis.txt'))
    try_delete('analysis.txt', 'output_hue.png', 'output_lightness.png')
  elif mode.startswith("blur"):
    try:
      blur(int(mode.split(" ")[1]))
    except:
      blur(2)
    await ctx.reply(files=[discord.File('output1.png'), discord.File('output2.png')])
    try_delete('output1.png', 'output2.png')
  elif mode.startswith("resize "):
    resize(int(mode.split(" ")[1]), int(mode.split(" ")[2]))
    try:
      await ctx.reply(files=[discord.File('output1.png'), discord.File('output2.png'), discord.File('output3.png'), discord.File('output4.png'), discord.File('output5.png'), discord.File('output6.png')])
    except:
      await ctx.reply(file=discord.File('output1.png'))
      await ctx.reply(file=discord.File('output2.png'))
      await ctx.reply(file=discord.File('output3.png'))
      await ctx.reply(file=discord.File('output4.png'))
      await ctx.reply(file=discord.File('output5.png'))
      await ctx.reply(file=discord.File('output6.png'))
      try_delete('output1.png', 'output2.png', 'output3.png', 'output4.png', 'output5.png', 'output6.png')
  elif mode.startswith("edge"):
    edge()
    try:
      await ctx.reply(files=[discord.File('output1.png'), discord.File('output2.png')])
    except:
      await ctx.reply(file=discord.File('output1.png'))
      await ctx.reply(file=discord.File('output2.png'))
      try_delete('output1.png', 'output2.png')
  elif mode.startswith("rotate "):
    rotate(float(mode.split(" ")[1]))
    await ctx.reply(files=[discord.File('output1.png'), discord.File('output2.png')])
    try_delete('output1.png', 'output2.png')
  else:
    if mode.startswith("invert"):
      invert()
    elif mode.startswith("hue") or mode.startswith("color"):
      try:
        addhue(int(mode.split(" ")[1]))
      except:
        addhue(180)
    elif mode.startswith("grey") or mode.startswith("gray"):
      try:
        greyscale(float(mode.split(" ")[1]))
      except:
        greyscale(0)
    elif mode.startswith("contrast"):
      try:
        contrast(float(mode.split(" ")[1]))
      except:
        contrast(50)
    elif mode.startswith("bright"):
      try:
        contrast(float(mode.split(" ")[1]))
      except:
        contrast(50)
    elif mode.startswith("sharp"):
      try:
        contrast(float(mode.split(" ")[1]))
      except:
        contrast(200)
    elif mode.startswith("hist"):
      hist()
    elif mode.startswith("contour"):
      contour()
    elif mode.startswith("recolo"):
      try:
        recolor(mode.split(" ")[1], mode.split(" ")[2])
      except:
        try:
          recolor(mode.split(" ")[1], (255,0,0))
        except:
          recolor((0,0,0), (255,0,0))
    await ctx.reply(file=discord.File('output.png'))
    try_delete('output.png')
  try_delete('input.png')

def addhue(degs):
  im = Image.open('input.png')
  pixels = im.load()
  for i in range(im.size[0]):
    for j in range(im.size[1]):
      a=pixels[i,j]
      b=colorsys.rgb_to_hsv(a[0]/255, a[1]/255, a[2]/255)
      c=colorsys.hsv_to_rgb(b[0]+degs/360,b[1],b[2])
      c1 = round(c[0]*255)
      c2 = round(c[1]*255)
      c3 = round(c[2]*255)
      try:
        d=(c1,c2,c3,a[3])
      except:
        d=(c1,c2,c3)
      pixels[i,j] = d
  im.save('output.png')

def analyse(scale, colors):
  if scale > 5000:
    scale = 1000
  palette = extract('input.png', colors)
  desc = f"Red\tGreen\tBlue\tHue\tSatur.\tLight.\tHex\tPercentage\n"

  palette.sort(key=lambda c: c.proportion)
  newimg = Image.new('RGB', (scale, round(scale/3)), (255, 255, 255))
  draw = ImageDraw.Draw(newimg)
  counter = 0
  r_total = g_total = b_total = h_total = s_total = l_total = 0
  for count in palette:
    rgb_tuple = count.rgb
    hsl_tuple = count.hsl
    r_total += rgb_tuple.r
    g_total += rgb_tuple.g
    b_total += rgb_tuple.b
    h_total += hsl_tuple.h
    s_total += hsl_tuple.s
    l_total += hsl_tuple.l
    draw.rectangle((counter, 0, counter+count.proportion*scale, round(scale/3)), (rgb_tuple.r, rgb_tuple.g, rgb_tuple.b))
    hexcode = f'{((rgb_tuple.r << 16) + (rgb_tuple.g << 8) + rgb_tuple.b):02x}'.upper().zfill(6)
    desc += f"{rgb_tuple.r}\t{rgb_tuple.g}\t{rgb_tuple.b}\t{hsl_tuple.h}\t{hsl_tuple.s}\t{hsl_tuple.l}\t{hexcode}\t{str(count.proportion*100)}%\n"
    counter += count.proportion*scale
  newimg.save('output_amount.png')
  avg_hexcode = f'#{((round(r_total/colors) << 16) + (round(g_total/colors) << 8) + round(b_total/colors)):02x}'.upper().zfill(6)
  desc += f"Average:\n{round(r_total/colors,2)}\t{round(g_total/colors,2)}\t{round(b_total/colors,2)}\t{round(h_total/colors,2)}\t{round(s_total/colors,2)}\t{round(l_total/colors,2)}\t{avg_hexcode}"
  
  palette.sort(key=lambda c: c.hsl.l)
  newimg = Image.new('RGB', (scale, round(scale/3)), (255, 255, 255))
  draw = ImageDraw.Draw(newimg)
  counter = 0
  for count in palette:
    rgb_tuple = count.rgb
    hsl_tuple = count.hsl
    draw.rectangle((counter, 0, counter+count.proportion*scale, round(scale/3)), (rgb_tuple.r, rgb_tuple.g, rgb_tuple.b))
    counter += count.proportion*scale
  newimg.save('output_lightness.png')
  
  palette.sort(key=lambda c: c.hsl.h)
  newimg = Image.new('RGB', (scale, round(scale/3)), (255, 255, 255))
  draw = ImageDraw.Draw(newimg)
  counter = 0
  for count in palette:
    rgb_tuple = count.rgb
    hsl_tuple = count.hsl
    draw.rectangle((counter, 0, counter+count.proportion*scale, round(scale/3)), (rgb_tuple.r, rgb_tuple.g, rgb_tuple.b))
    counter += count.proportion*scale
  newimg.save('output_hue.png')

  dominant = ColorThief('input.png').get_color(quality=1)
  hexcode = f'#{((dominant[0] << 16) + (dominant[1] << 8) + dominant[2]):02x}'.upper().zfill(6)

  f = open("analysis.txt", "a")
  f.write(desc)
  f.flush()
  f.close()
  return hexcode

def blur(distance):
  image = Image.open('input.png')
  newimg = image.filter(ImageFilter.BoxBlur(distance))
  newimg.save('output1.png')
  newimg = image.filter(ImageFilter.GaussianBlur(distance))
  newimg.save('output2.png')

def brightness(percent):
  image = Image.open('input.png')
  newimg = ImageEnhance.Brightness(image).enhance(percent/100)
  newimg.save('output.png')

def contour():
  image = Image.open('input.png')
  newimg = image.filter(ImageFilter.CONTOUR)
  newimg.save('output.png')

def contrast(percent):
  image = Image.open('input.png')
  newimg = ImageEnhance.Contrast(image).enhance(percent/100)
  newimg.save('output.png')

def edge():
  image = Image.open('input.png')
  newimg = image.filter(ImageFilter.EDGE_ENHANCE)
  newimg.save('output1.png')
  newimg = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
  newimg.save('output2.png')

def greyscale(percent):
  image = Image.open('input.png')
  newimg = ImageEnhance.Color(image).enhance(percent/100)
  newimg.save('output.png')

def hist():
  image = Image.open("input.png")
  split_image = image.split()
  plt.hist(split_image[0].histogram(), color="#FF000055")
  plt.hist(split_image[1].histogram(), color="#00FF0055")
  plt.hist(split_image[2].histogram(), color="#0000FF55")
  plt.title("Image histogram")
  plt.savefig("output.png", transparent=True)
  plt.clf()

def invert():
  image = Image.open('input.png')
  if image.mode == 'RGBA':
    r,g,b,a = image.split()
    rgb_image = Image.merge('RGB', (r,g,b))
    newimg = ImageOps.invert(rgb_image)
    r2,g2,b2 = newimg.split()
    newimg2 = Image.merge('RGBA', (r2,g2,b2,a))
    newimg2.save('output.png')
  else:
    newimg = ImageOps.invert(image)
    newimg.save('output.png')

def recolor(black_color, white_color):
  image = Image.open('input.png').convert('L')
  newimg = ImageOps.colorize(image, black_color, white_color)
  newimg.save('output.png')

def resize(x, y):
  image = Image.open('input.png')
  newimg = image.resize((x,y), Image.NEAREST)
  newimg.save('output1.png')
  newimg = image.resize((x,y), Image.BOX)
  newimg.save('output2.png')
  newimg = image.resize((x,y), Image.BILINEAR)
  newimg.save('output3.png')
  newimg = image.resize((x,y), Image.HAMMING)
  newimg.save('output4.png')
  newimg = image.resize((x,y), Image.BICUBIC)
  newimg.save('output5.png')
  newimg = image.resize((x,y), Image.LANCZOS)
  newimg.save('output6.png')

def rotate(degrees):
  image = Image.open('input.png')
  newimg = image.rotate(angle=degrees)
  newimg.save('output1.png')
  newimg = image.rotate(angle=degrees, expand=True)
  newimg.save('output2.png')

def sharpness(percent):
  image = Image.open('input.png')
  newimg = ImageEnhance.Sharpness(image).enhance(percent/100)
  newimg.save('output.png')

@commands.command()
async def mandelbrot(ctx, size:int = 1024):
  img = Image.effect_mandelbrot((size, size), (-1.5, -2.5, 3.5, 2.5), 95)
  img.save('mandelbrot.png')
  await ctx.reply(file = discord.File('mandelbrot.png'))
  try_delete('mandelbrot.png')

@commands.command()
async def ocr(ctx, lang="eng", *, disposed = None):
  images = ctx.message.attachments
  for count in images:
    await count.save('input.png')
    img = Image.open('input.png')
    desc=pytesseract.image_to_string(img, lang=lang)
    if not desc.replace(" ",""):
      desc="There was no text."
    await ctx.reply(desc)

@commands.command()
async def qr(ctx, *, disposed = None):
  for count in ctx.message.attachments:
    await count.save("input.png")
    image = Image.open("input.png").convert("RGBA")
    qr_code = pyzbar.decode(image)[0]
    poly = qr_code.polygon
    rectangle = qr_code.rect
    draw = ImageDraw.Draw(image)
    draw.rectangle([rectangle.left, rectangle.top, rectangle.left+rectangle.width, rectangle.top+rectangle.height], outline="#00FF00A0", width=8)
    points = [(i.x, i.y) for i in poly]
    for point in points:
      draw.ellipse((point[0] - 12, point[1] - 12, point[0]  + 12, point[1] + 12), fill="#FF5050A0")
    points.append((poly[0].x, poly[0].y))
    draw.line(points, fill="#FF0000A0", width=8)
    image.save('qrcode.png')
    await ctx.send(qr_code.data.decode("utf-8"), file=discord.File('qrcode.png'))
    try_delete('input.png', 'qrcode.png')

@commands.command()
async def render(ctx, width:float=1):
  att = ctx.message.attachments[0]
  att_width = att.width
  for count in range(100,0, -5):
    try:
      output = asc.loadFromUrl(att.url, columns=int(att_width*count/100*width), color=False)
      f = open('output.txt', 'w')
      f.write(output)
      f.flush()
      f.close()
      await ctx.reply(file = discord.File('output.txt'))
      try_delete('output.txt')
      break
    except:
      pass

@commands.command()
async def text(ctx, *, text = None):
  files = ctx.message.attachments
  for count in files:
    cname = count.filename
    await count.save(cname)
    if cname.endswith(".pdf"):
      images = convert_from_path(cname)
      for count in images:
        desc=pytesseract.image_to_string(count)
      try_delete(cname)
    elif cname.endswith(".txt"):
      f = open('data.txt', 'r')
      desc = f.read().replace('\n', '')
      f.close()
      try_delete(cname)
    else:
      desc = "Unsupported format. Please use .pdf or .txt."
    if desc=="":
      desc="There was no text."
    await ctx.reply(desc)

@commands.command()
async def transparent(ctx, alpha = 128):
  await ctx.message.attachments[0].save("Not_Transparent.png")
  img = Image.open("Not_Transparent.png")
  img2 = img.copy()
  img2.putalpha(int(alpha))
  img.paste(img2, img)
  img.save('Transparent.png')
  await ctx.reply(file = discord.File('Transparent.png'))
  try_delete('Transparent.png')

def setup(bot):
  bot.add_command(image)
  bot.add_command(mandelbrot)
  bot.add_command(ocr)
  bot.add_command(qr)
  bot.add_command(render)
  bot.add_command(text)
  bot.add_command(transparent)
