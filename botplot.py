import os
import re

import matplotlib.pyplot as plt
import qrcode
from art import *
from ascii_canvas import canvas, item
from table2ascii import PresetStyle, table2ascii

import discord as discord
import numpy as np
from discord.ext import commands
from shared import *
cmaphsv = plt.cm.hsv
def func(pct, allvals):
  absolute = int(pct/100*np.sum(allvals))
  return "{:d} ({:.1f}%)".format(absolute, int(pct))

def koch_snowflake(order):
  def _koch_snowflake_complex(order):
    if order == 0:
      angles = np.array([0, 120, 240]) + 90
      return (10 / np.sqrt(3) * np.exp(np.deg2rad(angles) * 1j))
    else:
      ZR = 0.5 - 0.5j * np.sqrt(3) / 3
      p1 = _koch_snowflake_complex(order - 1)
      p2 = np.roll(p1, shift=-1)
      dp = p2 - p1
      new_points = np.empty(len(p1) * 4, dtype=np.complex128)
      new_points[::4] = p1
      new_points[1::4] = p1 + dp / 3
      new_points[2::4] = p1 + dp * ZR
      new_points[3::4] = p1 + dp / 3 * 2
      return new_points

  points = _koch_snowflake_complex(order)
  x, y = points.real, points.imag
  return x, y


@commands.command()
async def ascii(ctx, *, text):
  output = text2art(text,"cybermedium") + f"\n" + text2art(text,"big")+f"\n" + text2art(text,"future_1")
  file = open("ascii.txt", "w")
  file.write(output)
  file.close()
  if len(output) > 1994 or len(text) > 11:
    await ctx.send(file=discord.File('ascii.txt'))
  else:
    await ctx.send(f"```{output}```", file=discord.File('ascii.txt'))
  os.remove('ascii.txt')


@commands.command()
async def barh(ctx, numbers, label, *, title="No_title_required"):
  try:
    numlist = numbers.split(",")
    numlist = list(map(float, numlist))
    labels = tuple(label.split(","))
    if len(labels) > len(numlist):
      labels = labels[:len(numlist)-1]
    elif len(numlist) > len(labels):
      numlist = numlist[:len(labels)-1]
    y_pos = np.arange(len(labels))
    plt.rcdefaults()
    fig, ax = plt.subplots()
    ax.barh(np.arange(len(labels)), numlist, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    for count in ['top', 'bottom', 'left', 'right']:
      ax.spines[count].set_color("w")
    ax.tick_params(axis='both', colors='w')
    if title != "No_title_required":
      plt.title(title, fontdict=db["font_dicts"]["title"])
    plt.savefig("horizontalbarchart.png", transparent=True)
    plt.savefig("horizontalbarchart.svg", transparent=True)
    plt.clf()
    await ctx.send(files=[discord.File("horizontalbarchart.png"), discord.File("horizontalbarchart.svg")])
    os.remove('horizontalbarchart.png')
    os.remove('horizontalbarchart.svg')
  except:
    await ctx.send("Invalid input. Please try again.")

@commands.command(aliases=["bar", "barchart"])
async def barv(ctx, numbers, label, *, title="No_title_required"):
  try:
    numlist = numbers.split(",")
    numlist = list(map(float, numlist))
    labels = tuple(label.split(","))
    if len(labels) > len(numlist):
      labels = labels[:len(numlist)-1]
    elif len(numlist) > len(labels):
      numlist = numlist[:len(labels)-1]
    x_pos = np.arange(len(labels))
    plt.rcdefaults()
    fig, ax = plt.subplots()
    ax.bar(np.arange(len(labels)), numlist, align='center')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(labels)
    for count in ['top', 'bottom', 'left', 'right']:
      ax.spines[count].set_color("w")
    ax.tick_params(axis='both', colors='w')
    if title != "No_title_required":
      plt.title(title, fontdict=db["font_dicts"]["title"])
    plt.savefig("verticalbarchart.png", transparent=True)
    plt.savefig("verticalbarchart.svg", transparent=True)
    plt.clf()
    await ctx.send(files=[discord.File("verticalbarchart.png"), discord.File("verticalbarchart.svg")])
    os.remove('verticalbarchart.png')
    os.remove('verticalbarchart.svg')
  except:
    await ctx.send("Invalid input. Please try again.")

@commands.command(aliases=["brokenl", "brokel", "breakl", "brokenline"])
async def bline(ctx, numbers, *, title="No_title_required"):
  try:
    numlist = numbers.split(",")
    numlist = list(map(float, numlist))
    plt.rcdefaults()
    fig, ax = plt.subplots()
    ax.plot(numlist)
    for count in ['top', 'bottom', 'left', 'right']:
      ax.spines[count].set_color("w")
    ax.tick_params(axis='both', colors='w')
    if title != "No_title_required":
      plt.title(title, fontdict=db["font_dicts"]["title"])
    plt.savefig("brokenline.png", transparent=True)
    plt.savefig("brokenline.svg", transparent=True)
    plt.clf()
    await ctx.send(files=[discord.File("brokenline.png"), discord.File("brokenline.svg")])
    os.remove('brokenline.png')
    os.remove('brokenline.svg')
  except:
    await ctx.send("Invalid input. Please try again.")

@commands.command(aliases=["brokenl2", "brokel2", "breakl2", "brokenline2"])
async def bline2(ctx, numbers, xnumbers, *, title="No_title_required"):
  try:
    numlist = numbers.split(",")
    numlist = list(map(float, numlist))
    xnumlist = xnumbers.split(",")
    xnumlist = list(map(float, xnumlist))
    plt.rcdefaults()
    fig, ax = plt.subplots()
    ax.plot(xnumlist, numlist)
    for count in ['top', 'bottom', 'left', 'right']:
      ax.spines[count].set_color("w")
    ax.tick_params(axis='both', colors='w')
    if title != "No_title_required":
      plt.title(title, fontdict=db["font_dicts"]["title"])
    plt.savefig("brokenline.png", transparent=True)
    plt.savefig("brokenline.svg", transparent=True)
    plt.clf()
    await ctx.send(files=[discord.File("brokenline.png"), discord.File("brokenline.svg")])
    os.remove('brokenline.png')
    os.remove('brokenline.svg')
  except:
    await ctx.send("Invalid input. Please try again.")

@commands.command()
async def draw(ctx, *, text):
  canvas_ = canvas.Canvas()
  splitted = text.split(f"\n")
  for count in splitted:
    if count.startswith("R|"):
      count = count.replace("R|", "", 1)
      pos_x = re.sub(r'(-?[\d]+?)\|(-?[\d]+?)\|(-?[\s\S]+)', r'\1', count)
      pos_y = re.sub(r'(-?[\d]+?)\|(-?[\d]+?)\|(-?[\s\S]+)', r'\2', count)
      rtext = re.sub(r'(-?[\d]+?)\|(-?[\d]+?)\|(-?[\s\S]+)', r'\3', count)
      canvas_.add_item(item.Item(f"+{'-'*len(rtext)}+\n|{rtext}|\n+{'-'*len(rtext)}+", position=[int(pos_x), int(pos_y)]))
    elif count.startswith("L|"):
      count = count.replace("L|", "", 1)
      x1 = re.sub(r'(-?[\d]+?)\|(-?[\d]+?)\|(-?[\d]+?)\|(-?[\d]+?)', r'\1', count)
      y1 = re.sub(r'(-?[\d]+?)\|(-?[\d]+?)\|(-?[\d]+?)\|(-?[\d]+?)', r'\2', count)
      x2 = re.sub(r'(-?[\d]+?)\|(-?[\d]+?)\|(-?[\d]+?)\|(-?[\d]+?)', r'\3', count)
      y2 = re.sub(r'(-?[\d]+?)\|(-?[\d]+?)\|(-?[\d]+?)\|(-?[\d]+?)', r'\4', count)
      canvas_.add_item(item.Line(start=[int(x1), int(y1)], end=[int(x2), int(y2)]))
  output = canvas_.render()
  file = open("drawing.txt", "w")
  file.write(output)
  file.close()
  if len(output) > 1994:
    await ctx.send(file=discord.File('drawing.txt'))
  else:
    await ctx.send(f"```{output}```", file=discord.File('drawing.txt'))
  os.remove('drawing.txt')

@commands.command(aliases=["mathplot", "mathgraph"])
async def graph(ctx, func, range_low:float=-10.0, range_high:float=10.0, equalize:specialbool=False,*, title="No_title_required"):
  try:
    x_ = np.linspace(range_low, range_high, 200)
    y_axis = eval(func)
    fig, ax = plt.subplots()
    plt.plot(x_, y_axis)
    for count in ['top', 'bottom', 'left', 'right']:
      ax.spines[count].set_color("w")
    ax.tick_params(axis='both', colors='w')
    if title != "No_title_required":
      plt.title(title, fontdict=db["font_dicts"]["title"])
    plt.savefig("graph.png", transparent=True)
    plt.savefig("graph.svg", transparent=True)
    plt.clf()
    await ctx.send(files=[discord.File("graph.png"), discord.File("graph.svg")])
    os.remove('graph.png')
    os.remove('graph.svg')
  except:
    await ctx.send("Invalid input. Please try again.")

@commands.command(aliases=["histogram", "histograms"])
async def hist(ctx, numbers, *, title="No_title_required"):
  try:
    numlist = numbers.split(",")
    numlist = list(map(float, numlist))
    fig, ax = plt.subplots()
    plt.hist(numlist)
    for count in ['top', 'bottom', 'left', 'right']:
      ax.spines[count].set_color("w")
    ax.tick_params(axis='both', colors='w')
    if title != "No_title_required":
      plt.title(title, fontdict=db["font_dicts"]["title"])
    plt.savefig("histogram.png", transparent=True)
    plt.savefig("histogram.svg", transparent=True)
    plt.clf()
    await ctx.send(files=[discord.File("histogram.png"), discord.File("histogram.svg")])
    os.remove('histogram.png')
    os.remove('histogram.svg')
  except:
    await ctx.send("Invalid input. Please try again.")

@commands.command(aliases=["multibrokenl", "multibrokel", "multibreakl", "multibrokenline"])
async def multibline(ctx, numbers, labels, *, title="No_title_required"):
  try:
    lines = numbers.split(";")
    plt.rcdefaults()
    fig, ax = plt.subplots()
    labels = labels.split(",")
    for count1 in range(len(lines)):
      numlist = lines[count1].split(",")
      numlist = list(map(float, numlist))
      ax.plot(numlist, label=labels[count1])
    for count in ['top', 'bottom', 'left', 'right']:
      ax.spines[count].set_color("w")
    ax.tick_params(axis='both', colors='w')
    ax.legend()
    if title != "No_title_required":
      plt.title(title, fontdict=db["font_dicts"]["title"])
    plt.savefig("brokenline.png", transparent=True)
    plt.savefig("brokenline.svg", transparent=True)
    plt.clf()
    await ctx.send(files=[discord.File("brokenline.png"), discord.File("brokenline.svg")])
    os.remove('brokenline.png')
    os.remove('brokenline.svg')
  except:
    await ctx.send("Invalid input. Please try again.")

@commands.command(aliases=["multimathplot", "multimathgraph"])
async def multigraph(ctx, func, range_low:float=-10.0, range_high:float=10.0, *, title="No_title_required"):
  try:
    x_ = np.linspace(range_low, range_high, 200)
    fig, ax = plt.subplots()
    for count in func.split(";"):
      y_axis = eval(count)
      plt.plot(x_, y_axis)
    for count in ['top', 'bottom', 'left', 'right']:
      ax.spines[count].set_color("w")
    ax.tick_params(axis='both', colors='w')
    if title != "No_title_required":
      plt.title(title, fontdict=db["font_dicts"]["title"])
    plt.savefig("graph.png", transparent=True)
    plt.savefig("graph.svg", transparent=True)
    plt.clf()
    await ctx.send(files=[discord.File("graph.png"), discord.File("graph.svg")])
    os.remove('graph.png')
    os.remove('graph.svg')
  except:
    await ctx.send("Invalid input. Please try again.")

@commands.command(aliases=["piechart", "circlechart"])
async def pie(ctx, numbers, label="", *, title="No_title_required"):
  try:
    numlist = numbers.split(",")
    numlist = list(map(float, numlist))
    mycolors = []
    y = np.array(numlist)
    for count in range(0, len(numlist)):
      mycolors.append(cmaphsv(count/len(numlist)))
    if label:
      labels = label.split(",")
      if len(labels) > len(numlist):
        labels = labels[:len(numlist)-1]
      elif len(numlist) > len(labels):
        numlist = numlist[:len(labels)-1]
      patches, labels, pct_texts = plt.pie(y, labels=labels, colors=mycolors, autopct=lambda pct: func(pct, y),
      rotatelabels=True, pctdistance=0.6, textprops = db["font_dicts"]["label"])
    else:
      patches, labels, pct_texts = plt.pie(y, colors=mycolors, autopct=lambda pct: func(pct, y),
      rotatelabels=True, pctdistance=0.6, textprops = db["font_dicts"]["label"])
    for label, pct_text in zip(labels, pct_texts):
      pct_text.set_rotation(label.get_rotation())
      pct_text.update(db["font_dicts"]["light_label"])
    plt.legend(prop=db["font_dicts"]["legend"])
    if title != "No_title_required":
      plt.title(title, fontdict=db["font_dicts"]["title"])
    plt.savefig("piechart.png", transparent=True)
    plt.savefig("piechart.svg", transparent=True)
    plt.clf()
    await ctx.send(files=[discord.File("piechart.png"), discord.File("piechart.svg")])
    os.remove('piechart.png')
    os.remove('piechart.svg')
  except:
    await ctx.send("Invalid input. Please try again.")

@commands.command()
async def qrmake(ctx, *, text):
  textlist = text.split("\n")
  try:
    data = textlist[0].replace("{{{newline}}}", f"\n")
    textlist2 = textlist[1].split(" ")
    fgc = textlist2[0]
    bgc = textlist2[1]
    tsize = textlist2[2]
    bsize = textlist2[3]
    iecorr = textlist2[4]
    if iecorr == "4":
      ecorr = qrcode.constants.ERROR_CORRECT_H
    elif iecorr == "3":
      ecorr = qrcode.constants.ERROR_CORRECT_Q
    elif iecorr == "2":
      ecorr = qrcode.constants.ERROR_CORRECT_M
    else:
      ecorr = qrcode.constants.ERROR_CORRECT_L
    version = textlist2[5]
  except:
    pass
  try:
    qr = qrcode.QRCode(version=version, error_correction=ecorr, box_size=tsize, border=bsize)
  except:
    try:
      qr = qrcode.QRCode(version=1, error_correction=ecorr, box_size=tsize, border=bsize)
    except:
      try:
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=tsize, border=bsize)
      except:
        try:
          qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=tsize, border=4)
        except:
          try:
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
          except:
            await ctx.send("Invalid input. Please try again.")
  try:
    qr.add_data(data)
  except:
    await ctx.send("Invalid input. Please try again.")
  try:
    img = qr.make_image(fill_color=fgc, back_color=bgc)
  except:
    try:
      img = qr.make_image(fill_color=fgc, back_color="black")
    except:
      try:
        img = qr.make_image(fill_color="white", back_color=bgc)
      except:
        img = qr.make_image(fill_color="black", back_color="white")
  img.save('QRCode.png')
  await ctx.send(file=discord.File("QRCode.png"))
  os.remove("QRCode.png")

@commands.command(aliases=["simpcolour", "simplecolor", "simplecolour"])
async def simpcolor(ctx, *, name):
  plt.clf()
  fig, ax = plt.subplots()
  ax.axes.get_xaxis().set_visible(False)
  ax.axes.get_yaxis().set_visible(False)
  try:
    cmapv = plt.get_cmap(name)
    plt.setp(ax.spines.values(), color="w")
    gradient = np.vstack((np.linspace(0, 1, 256), np.linspace(0, 1, 256)))
    plt.imshow(gradient, aspect='auto', cmap=cmapv)
    plt.axis('off')
    plt.subplots_adjust(top = 1, right = 1, bottom = 0, left = 0)
    plt.savefig("color.png", transparent=True)
    plt.savefig("color.svg", transparent=True)
  except:
    bcs = plt.gca()
    plt.setp(ax.spines.values(), color=name)
    ax.set_facecolor(name)
    fig.set_facecolor(name)
    plt.savefig("color.png", transparent=True)
    plt.savefig("color.svg", transparent=True)
  await ctx.send(files=[discord.File("color.png"), discord.File("color.svg")])
  os.remove('color.png')
  os.remove('color.svg')

@commands.command(alias=["snowgraph", "snowflake"])
async def snow(ctx, recursion = 7):  
  try:
    if float(recursion) > 11:
      await ctx.send("We are sorry, the maximum recursion we can process is 11.")
    else:
      x, y = koch_snowflake(recursion)
      plt.figure(figsize=(8, 8))
      plt.axis('equal')
      plt.fill(x, y)
      ax = plt.subplot(111)
      ax.get_xaxis().set_visible(False)
      ax.get_yaxis().set_visible(False)
      ax.spines['top'].set_visible(False)
      ax.spines['bottom'].set_visible(False)
      ax.spines['left'].set_visible(False)
      ax.spines['right'].set_visible(False)
      plt.savefig("snow.png", transparent=True)
      if float(recursion) < 8:
        plt.savefig("snow.svg", transparent=True)
        await ctx.send(file=discord.File("snow.svg"))
        os.remove('snow.svg')
      await ctx.send(file=discord.File("snow.png"))
      plt.clf()
      os.remove('snow.png')
  except:
    await ctx.send("Invalid input. Please try again.")

@commands.command()
async def table(ctx, *, text):
  splitted = text.split(f"\n")
  if len(splitted) == 1:
    splitted.insert(0, "")
    splitted.insert(0, "")
  header = splitted[0]
  footer = splitted[1]
  everythingelse = splitted[2:len(splitted)]
  if "|||" in header:
    rawstyle = re.sub(r"([\w]*?)\|\|\|([\s\S]*)", r"\1", header)
    header = re.sub(r"([\w]*?)\|\|\|([\s\S]*)", r"\2", header)
  else:
    rawstyle = ""
  if header.startswith("$F$"):
    first_col_heading = True
    header = header.replace("$F$", "", 1)
  else:
    first_col_heading = False
  if header.startswith("$L$"):
    last_col_heading = True
    header = header.replace("$L$", "", 1)
  else:
    last_col_heading = False
  if rawstyle.replace(" ", "") == "":
    style = PresetStyle.double_thin_compact
  else:
    try:
      style = eval("PresetStyle."+rawstyle)
    except:
      style = PresetStyle.double_thin_compact
  try:
    headers = header.split(",")
    footers = footer.split(",")
  except:
    pass
  rawbodies = everythingelse#.split(f"\n")
  bodies = []
  for count in rawbodies:
    bodies.append(count.split(","))
  try:
    output = table2ascii(header=headers, footer=footers, body=bodies, style=style, first_col_heading=first_col_heading,  last_col_heading=last_col_heading)
  except:
    try:
      output = table2ascii(footer=footers, body=bodies, style=style)
    except:
      try:
        output = table2ascii(header=headers, body=bodies, style=style)
      except:
        try:
          output = table2ascii(body=bodies, style=style)
        except:
          await ctx.send("Invalid syntax, please try again.")
          return
  file = open("table.txt", "w")
  file.write(output)
  file.close()
  await ctx.send(f"```{output}```", file=discord.File('table.txt'))
  os.remove('table.txt')

def setup(bot):
  bot.add_command(ascii)
  bot.add_command(barh)
  bot.add_command(barv)
  bot.add_command(bline)
  bot.add_command(bline2)
  bot.add_command(graph)
  bot.add_command(hist)
  bot.add_command(multibline)
  bot.add_command(multigraph)
  bot.add_command(pie)
  bot.add_command(qrmake)
  bot.add_command(simpcolor)
  bot.add_command(snow)
  bot.add_command(table)
