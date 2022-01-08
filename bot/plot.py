import matplotlib.pyplot as plt
import qrcode
from art import text2art
from ascii_canvas import canvas, item
from table2ascii import PresetStyle, table2ascii

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
  output = f'''{text2art(text,"cybermedium")}
{text2art(text,"cyberlarge")}
{text2art(text,"big")}
{text2art(text,"arrows")}
{text2art(text,"keyboard")}
{text2art(text,"smkeyboard")}
{text2art(text,"asc")}
{text2art(text,"ascii")}
{text2art(text,"banner")}
{text2art(text,"banner3")}
{text2art(text,"banner3-d")}
{text2art(text,"banner4")}
{text2art(text,"block")}
{text2art(text,"appha")}
{text2art(text,"xcour")}
{text2art(text,"xcourb")}
{text2art(text,"xcouri")}
{text2art(text,"xcourbi")}
{text2art(text,"xhelv")}
{text2art(text,"xhelvb")}
{text2art(text,"xhelvi")}
{text2art(text,"xhelvbi")}
{text2art(text,"xsans")}
{text2art(text,"xsansb")}
{text2art(text,"xsansi")}
{text2art(text,"xsansbi")}
{text2art(text,"isometric1")}
{text2art(text,"isometric2")}
{text2art(text,"isometric3")}
{text2art(text,"isometric4")}
'''
  f = open("ascii.txt", "w")
  f.write(output)
  f.flush()
  f.close()
  await ctx.reply(file=discord.File('ascii.txt'))
  try_delete('ascii.txt')

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
    for x in ['top', 'bottom', 'left', 'right']:
      ax.spines[x].set_color("w")
    ax.tick_params(axis='both', colors='w')
    if title != "No_title_required":
      plt.title(title, fontdict=db["font_dicts"]["title"])
    plt.savefig("horizontalbarchart.png", transparent=True)
    plt.savefig("horizontalbarchart.svg", transparent=True)
    plt.clf()
    await ctx.reply(files=[discord.File("horizontalbarchart.png"), discord.File("horizontalbarchart.svg")])
    try_delete('horizontalbarchart.png')
    try_delete('horizontalbarchart.svg')
  except:
    await ctx.reply("Invalid input. Please try again.")

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
    for x in ['top', 'bottom', 'left', 'right']:
      ax.spines[x].set_color("w")
    ax.tick_params(axis='both', colors='w')
    if title != "No_title_required":
      plt.title(title, fontdict=db["font_dicts"]["title"])
    plt.savefig("verticalbarchart.png", transparent=True)
    plt.savefig("verticalbarchart.svg", transparent=True)
    plt.clf()
    await ctx.reply(files=[discord.File("verticalbarchart.png"), discord.File("verticalbarchart.svg")])
    try_delete('verticalbarchart.png')
    try_delete('verticalbarchart.svg')
  except:
    await ctx.reply("Invalid input. Please try again.")

@commands.command(aliases=["brokenl", "brokel", "breakl", "brokenline"])
async def bline(ctx, numbers, *, title="No_title_required"):
  try:
    numlist = numbers.split(",")
    numlist = list(map(float, numlist))
    plt.rcdefaults()
    fig, ax = plt.subplots()
    ax.plot(numlist)
    for x in ['top', 'bottom', 'left', 'right']:
      ax.spines[x].set_color("w")
    ax.tick_params(axis='both', colors='w')
    if title != "No_title_required":
      plt.title(title, fontdict=db["font_dicts"]["title"])
    plt.savefig("brokenline.png", transparent=True)
    plt.savefig("brokenline.svg", transparent=True)
    plt.clf()
    await ctx.reply(files=[discord.File("brokenline.png"), discord.File("brokenline.svg")])
    try_delete('brokenline.png')
    try_delete('brokenline.svg')
  except:
    await ctx.reply("Invalid input. Please try again.")

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
    for x in ['top', 'bottom', 'left', 'right']:
      ax.spines[x].set_color("w")
    ax.tick_params(axis='both', colors='w')
    if title != "No_title_required":
      plt.title(title, fontdict=db["font_dicts"]["title"])
    plt.savefig("brokenline.png", transparent=True)
    plt.savefig("brokenline.svg", transparent=True)
    plt.clf()
    await ctx.reply(files=[discord.File("brokenline.png"), discord.File("brokenline.svg")])
    try_delete('brokenline.png')
    try_delete('brokenline.svg')
  except:
    await ctx.reply("Invalid input. Please try again.")

@commands.command()
async def draw(ctx, *, text):
  canvas_ = canvas.Canvas()
  splitted = text.split(f"\n")
  for x in splitted:
    if x.startswith("R|"):
      x = x.replace("R|", "", 1)
      pos_x = re.sub(r'(-?[\d]+?)\|(-?[\d]+?)\|(-?[\s\S]+)', r'\1', x)
      pos_y = re.sub(r'(-?[\d]+?)\|(-?[\d]+?)\|(-?[\s\S]+)', r'\2', x)
      rtext = re.sub(r'(-?[\d]+?)\|(-?[\d]+?)\|(-?[\s\S]+)', r'\3', x)
      canvas_.add_item(item.Item(f"+{'-'*len(rtext)}+\n|{rtext}|\n+{'-'*len(rtext)}+", position=[int(pos_x), int(pos_y)]))
    elif x.startswith("L|"):
      x = x.replace("L|", "", 1)
      x1 = re.sub(r'(-?[\d]+?)\|(-?[\d]+?)\|(-?[\d]+?)\|(-?[\d]+?)', r'\1', x)
      y1 = re.sub(r'(-?[\d]+?)\|(-?[\d]+?)\|(-?[\d]+?)\|(-?[\d]+?)', r'\2', x)
      x2 = re.sub(r'(-?[\d]+?)\|(-?[\d]+?)\|(-?[\d]+?)\|(-?[\d]+?)', r'\3', x)
      y2 = re.sub(r'(-?[\d]+?)\|(-?[\d]+?)\|(-?[\d]+?)\|(-?[\d]+?)', r'\4', x)
      canvas_.add_item(item.Line(start=[int(x1), int(y1)], end=[int(x2), int(y2)]))
  output = canvas_.render()
  f = open("drawing.txt", "w")
  f.write(output)
  f.flush()
  f.close()
  if len(output) > 1994:
    await ctx.reply(file=discord.File('drawing.txt'))
  else:
    await ctx.reply(f"```{output}```", file=discord.File('drawing.txt'))
  try_delete('drawing.txt')

@commands.command()
async def fonts(ctx, *, text):
  output = f'''{text2art(text,"antrophobia")}
{text2art(text,"awesome")}
{text2art(text,"carrier1")}
{text2art(text,"carrier2")}
{text2art(text,"cranky")}
{text2art(text,"cute1")}
{text2art(text,"drako")}
{text2art(text,"strange")}

{text2art(text,"monospace")}
{text2art(text,"fancy57")}

{text2art(text,"thin2")}
{text2art(text,"thin3")}
{text2art(text,"tiny")}
{text2art(text,"tiny2")}
{text2art(text,"wiggly")}
{text2art(text,"smallcaps2")}
{text2art(text,"smallcaps3")}

{text2art(text,"fancy60")}
{text2art(text,"fancy62")}
{text2art(text,"fancy64")}

{text2art(text,"fancy56")}
{text2art(text,"fancy61")}
{text2art(text,"fancy63")}

{text2art(text,"fancy65")}
{text2art(text,"fancy66")}
{text2art(text,"fancy58")}

{text2art(text,"handwriting1")}
{text2art(text,"handwriting2")}
{text2art(text,"handwriting3")}

{text2art(text,"black_bubble")}
{text2art(text,"black_square")}
{text2art(text,"white_bubble")}
{text2art(text,"white_square")}
{text2art(text,"contouring3")}
{text2art(text,"contouring4")}
'''
  f = open("fonts.txt", "w")
  f.write(output)
  f.flush()
  f.close()
  await ctx.reply(file=discord.File('fonts.txt'))
  try_delete('fonts.txt')

@commands.command(aliases=["mathplot", "mathgraph"])
async def graph(ctx, func, range_low:float=-10.0, range_high:float=10.0, equalize:specialbool=False, *, title="No_title_required"):
  try:
    x_ = np.linspace(range_low, range_high, 200)
    y_axis = eval(func)
    fig, ax = plt.subplots()
    plt.plot(x_, y_axis)
    if equalize:
      ax.set_aspect(1, adjustable='datalim')
    for x in ['top', 'bottom', 'left', 'right']:
      ax.spines[x].set_color("w")
    ax.tick_params(axis='both', colors='w')
    if title != "No_title_required":
      plt.title(title, fontdict=db["font_dicts"]["title"])
    plt.savefig("graph.png", transparent=True)
    plt.savefig("graph.svg", transparent=True)
    plt.clf()
    await ctx.reply(files=[discord.File("graph.png"), discord.File("graph.svg")])
    try_delete('graph.png')
    try_delete('graph.svg')
  except:
    await ctx.reply("Invalid input. Please try again.")

@commands.command(aliases=["histogram", "histograms"])
async def hist(ctx, numbers, *, title="No_title_required"):
  try:
    numlist = numbers.split(",")
    numlist = list(map(float, numlist))
    fig, ax = plt.subplots()
    plt.hist(numlist)
    for x in ['top', 'bottom', 'left', 'right']:
      ax.spines[x].set_color("w")
    ax.tick_params(axis='both', colors='w')
    if title != "No_title_required":
      plt.title(title, fontdict=db["font_dicts"]["title"])
    plt.savefig("histogram.png", transparent=True)
    plt.savefig("histogram.svg", transparent=True)
    plt.clf()
    await ctx.reply(files=[discord.File("histogram.png"), discord.File("histogram.svg")])
    try_delete('histogram.png')
    try_delete('histogram.svg')
  except:
    await ctx.reply("Invalid input. Please try again.")

@commands.command(aliases=["multibrokenl", "multibrokel", "multibreakl", "multibrokenline"])
async def multibline(ctx, numbers, labels, *, title="No_title_required"):
  try:
    lines = numbers.split(";")
    plt.rcdefaults()
    fig, ax = plt.subplots()
    labels = labels.split(",")
    for x in range(len(lines)):
      numlist = lines[x].split(",")
      numlist = list(map(float, numlist))
      ax.plot(numlist, label=labels[x])
    for x in ['top', 'bottom', 'left', 'right']:
      ax.spines[x].set_color("w")
    ax.tick_params(axis='both', colors='w')
    ax.legend()
    if title != "No_title_required":
      plt.title(title, fontdict=db["font_dicts"]["title"])
    plt.savefig("brokenline.png", transparent=True)
    plt.savefig("brokenline.svg", transparent=True)
    plt.clf()
    await ctx.reply(files=[discord.File("brokenline.png"), discord.File("brokenline.svg")])
    try_delete('brokenline.png')
    try_delete('brokenline.svg')
  except:
    await ctx.reply("Invalid input. Please try again.")

@commands.command(aliases=["multimathplot", "multimathgraph"])
async def multigraph(ctx, func, range_low:float=-10.0, range_high:float=10.0, equalize:specialbool=False, *, title="No_title_required"):
  try:
    x_ = np.linspace(range_low, range_high, 200)
    fig, ax = plt.subplots()
    for x in func.split(";"):
      y_axis = eval(x)
      plt.plot(x_, y_axis)
    for x in ['top', 'bottom', 'left', 'right']:
      ax.spines[x].set_color("w")
    ax.tick_params(axis='both', colors='w')
    if title != "No_title_required":
      plt.title(title, fontdict=db["font_dicts"]["title"])
    plt.savefig("graph.png", transparent=True)
    plt.savefig("graph.svg", transparent=True)
    plt.clf()
    await ctx.reply(files=[discord.File("graph.png"), discord.File("graph.svg")])
    try_delete('graph.png')
    try_delete('graph.svg')
  except:
    await ctx.reply("Invalid input. Please try again.")

@commands.command(aliases=["piechart", "circlechart"])
async def pie(ctx, numbers, label="", *, title="No_title_required"):
  #try:
  numlist = numbers.split(",")
  numlist = list(map(float, numlist))
  mycolors = []
  y = np.array(numlist)
  for x in range(len(numlist)):
    mycolors.append(cmaphsv(x/len(numlist)))
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
  plt.legend(prop = db["font_dicts"]["legend"])
  if title != "No_title_required":
    plt.title(title, fontdict=db["font_dicts"]["title"])
  plt.savefig("piechart.png", transparent=True)
  plt.savefig("piechart.svg", transparent=True)
  plt.clf()
  await ctx.reply(files=[discord.File("piechart.png"), discord.File("piechart.svg")])
  try_delete('piechart.png')
  try_delete('piechart.svg')
  #except:
  #  await ctx.reply("Invalid input. Please try again.")

@commands.command()
async def qrmake(ctx, *, text):
  textlist = text.split("\n")
  data = textlist[0].replace("{{{newline}}}", f"\n")
  textlist2 = textlist[1].split(" ") if len(textlist) > 1 else []
  fgc       = textlist2[0] if len(textlist2) > 0 else "#000000"
  bgc       = textlist2[1] if len(textlist2) > 1 else "#FFFFFF"
  tsize     = textlist2[2] if len(textlist2) > 2 else "10"
  bsize     = textlist2[3] if len(textlist2) > 3 else "4"
  iecorr    = textlist2[4] if len(textlist2) > 4 else "4"
  version   = textlist2[5] if len(textlist2) > 5 else "1"
  if iecorr == "4":
    ecorr = qrcode.constants.ERROR_CORRECT_H
  elif iecorr == "3":
    ecorr = qrcode.cNonstants.ERROR_CORRECT_Q
  elif iecorr == "2":
    ecorr = qrcode.constants.ERROR_CORRECT_M
  else:
    ecorr = qrcode.constants.ERROR_CORRECT_L
  qr = qrcode.QRCode(version=version, error_correction=ecorr, box_size=tsize, border=bsize)
  try:
    qr.add_data(data)
  except:
    await ctx.reply("Invalid input. Please try again.")
  img = qr.make_image(fill_color=fgc, back_color=bgc)
  img.save('QRCode.png')
  await ctx.reply(file=discord.File("QRCode.png"))
  try_delete('QRCode.png')

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
  await ctx.reply(files=[discord.File("color.png"), discord.File("color.svg")])
  try_delete('color.png')
  try_delete('color.svg')

@commands.command(alias=["snowgraph", "snowflake"])
async def snow(ctx, recursion = 7):  
  try:
    if float(recursion) > 11:
      await ctx.reply("We are sorry, the maximum recursion we can process is 11.")
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
        await ctx.reply(file=discord.File("snow.svg"))
        try_delete('snow.svg')
      await ctx.reply(file=discord.File("snow.png"))
      plt.clf()
      try_delete('snow.png')
  except:
    await ctx.reply("Invalid input. Please try again.")

@commands.command()
async def table(ctx, *, text):
  splitted = text.split(f"\n")
  if len(splitted) == 1:
    splitted.insert(0, "")
    splitted.insert(0, "")
  header = splitted[0]
  footer = splitted[1]
  everythingelse = splitted[2:]
  if "|||" in header:
    rawstyle = re.sub(r"([\w]*?)\|\|\|([\s\S]*)", r"\1", header)
    header = re.sub(r"([\w]*?)\|\|\|([\s\S]*)", r"\2", header)
  else:
    rawstyle = ""
  fch = False
  lch = False
  if header.startswith("$F$"):
    fch = True
    header = header.replace("$F$", "", 1)
  if header.startswith("$L$"):
    lch = True
    header = header.replace("$L$", "", 1)
  if rawstyle.replace(" ", "") == "":
    style = PresetStyle.double_thin_compact
  else:
    try:
      style = eval(f"PresetStyle.{rawstyle}")
    except:
      style = PresetStyle.double_thin_compact
  try:
    headers = header.split(",") if header else []
    footers = footer.split(",") if footer else []
  except:
    pass
  rawbodies = everythingelse#.split(f"\n")
  bodies = []
  for x in rawbodies:
    bodies.append(x.split(","))
  output = table2ascii(header=headers, footer=footers, body=bodies, style=style, first_col_heading=fch, last_col_heading=lch)
  f = open("table.txt", "w")
  f.write(output)
  f.close()
  await ctx.reply(f"```{output}```", file=discord.File('table.txt'))
  try_delete('table.txt')

@commands.command()
async def table_plain(ctx, *, text):
  contents = text.split(f"\n")
  if "|||" in contents[0]:
    rawstyle = re.sub(r"([\w]*?)\|\|\|([\s\S]*)", r"\1", contents[0])
    contents[0] = re.sub(r"([\w]*?)\|\|\|([\s\S]*)", r"\2", contents[0])
  else:
    rawstyle = ""
  fch = False
  lch = False
  if contents[0].startswith("$F$"):
    fch = True
    contents[0] = contents[0].replace("$F$", "", 1)
  if contents[0].startswith("$L$"):
    lch = True
    contents[0] = contents[0].replace("$L$", "", 1)
  if rawstyle.replace(" ", "") == "":
    style = PresetStyle.double_thin_compact
  else:
    try:
      style = eval(f"PresetStyle.{rawstyle}")
    except:
      style = PresetStyle.double_thin_compact
  bodies = []
  for x in contents:
    bodies.append(x.split(","))
  output = table2ascii(body=bodies, style=style, first_col_heading=fch, last_col_heading=lch)
  f = open("table.txt", "w")
  f.write(output)
  f.close()
  await ctx.reply(f"```{output}```", file=discord.File('table.txt'))
  try_delete('table.txt')

def setup(bot):
  bot.add_command(ascii)
  bot.add_command(barh)
  bot.add_command(barv)
  bot.add_command(bline)
  bot.add_command(bline2)
  bot.add_command(fonts)
  bot.add_command(graph)
  bot.add_command(hist)
  bot.add_command(multibline)
  bot.add_command(multigraph)
  bot.add_command(pie)
  bot.add_command(qrmake)
  bot.add_command(simpcolor)
  bot.add_command(snow)
  bot.add_command(table)
  bot.add_command(table_plain)
  print("Midway through loading modules")