import colorsys
import os
import random as ra
import sys

import discord
import pytesseract
import qr_img
import requests
from discord.ext import commands
from pdf2image import convert_from_path
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageOps

import ascii2 as asc

@commands.command()
async def audio(ctx, mode, *, input=""):
  await ctx.message.attachments[0].save(ctx.message.attachments[0].filename)
  if mode.startswith("convert") or mode.startswith("convert"):
    

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
  f.close()
  return hexcode


def setup(bot):
  bot.add_command(audio)
