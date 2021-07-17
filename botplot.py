from table2ascii import table2ascii, PresetStyle
from ascii_canvas import canvas, item
import matplotlib.pyplot as plt
import numpy as np
from art import *
import qrcode
import re

cmaphsv = plt.cm.hsv
def func(pct, allvals):
  absolute = int(pct/100*np.sum(allvals))
  return "{:d} ({:.1f}%)".format(absolute, int(pct))

def botdraw(text):
  canvas_ = canvas.Canvas()
  splitted = text.split(f"\n")
  for count in splitted:
    if count.startswith("R|"):
      count = count.replace("R|", "", 1)
      pos_x = re.sub(r'(-?[\d]+?)\|(-?[\d]+?)\|(-?[\s\S]+)', r'\1', count)
      pos_y = re.sub(r'(-?[\d]+?)\|(-?[\d]+?)\|(-?[\s\S]+)', r'\2', count)
      rtext = re.sub(r'(-?[\d]+?)\|(-?[\d]+?)\|(-?[\s\S]+)', r'\3', count)
      canvas_.add_item(item.Item("+" + "-"*len(rtext) + f"+\n|" + rtext + f"|\n+" + "-"*len(rtext) + "+", position=[int(pos_x), int(pos_y)]))
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
  return output

def botqrencode(text):
  textlist = text.split("\n")
  try:
    textlist2 = textlist[1].split(" ")
    data = textlist[0].replace("{{{newline}}}", f"\n")
    fgc = textlist2[1]
    bgc = textlist2[2]
    tsize = textlist2[3]
    bsize = textlist2[4]
    version = textlist2[5]
  except:
    pass
  try:
    qr = qrcode.QRCode(version=version, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=tsize, border=bsize)
  except:
    try:
      qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=tsize, border=bsize)
    except:
      try:
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=tsize, border=4)
      except:
        try:
          qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
        except:
          return "Invalid input. Please try again."
  try:
    qr.add_data(data)
  except:
    return "Invalid input. Please try again."
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

def botascii(text):
  output = text2art(text,"cybermedium") + f"\n" + text2art(text,"big")+f"\n" + text2art(text,"future_1")
  file = open("ascii.txt", "w")
  file.write(output)
  file.close()
  return output

def bottable(text):
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
          output = "Invalid syntax, please try again."
  return output

def botsimpcolor(name):
  plt.clf()
  fig, ax = plt.subplots()
  ax.axes.get_xaxis().set_visible(False)
  ax.axes.get_yaxis().set_visible(False)
  try:
    cmapv = plt.get_cmap(name)
    plt.setp(ax.spines.values(), color="w")
    gradient = np.vstack((np.linspace(0, 1, 256), np.linspace(0, 1, 256)))
    fig.set_facecolor("w")
    ax.set_facecolor(cmapv)
    plt.savefig("color.png", transparent=True)
  except:
    try:
      bcs = plt.gca()
      plt.setp(ax.spines.values(), color=name)
      ax.set_facecolor(name)
      fig.set_facecolor(name)
      plt.savefig("color.png", transparent=False)
    except:
      plt.clf()

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

def botsnow(recursion):
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
  plt.clf()

def bothist(title, numbers):
  numlist = []
  for count in numbers.split(","):
    if float(count)%1 == 0:
      numlist.append(int(count))
    else:
      numlist.append(float(count))
  plt.hist(numlist)
  if title != "No_title_required":
    plt.title(title)
  plt.savefig("histogram.png", transparent=True)
  plt.clf()

def botpie(title, numbers, label):
  numlist = []
  for count in numbers.split(","):
    numlist.append(int(count))
  mycolors = []
  labels = label.split(",")
  if len(labels) > len(numlist):
    labels = labels[:len(numlist)-1]
  elif len(numlist) > len(labels):
    numlist = numlist[:len(labels)-1]
  y = np.array(numlist)
  for count in range(0, len(numlist)):
    mycolors.append(cmaphsv(count/len(numlist)))
  plt.pie(y, labels=labels, colors=mycolors, autopct=lambda pct: func(pct, y), textprops = {'color':"w"})
  plt.legend(loc="lower right")
  if title != "No_title_required":
    plt.title(title)
  plt.savefig("piechart.png", transparent=True)
  plt.clf()

def botbarh(title, numbers, label):
  numlist = []
  for count in numbers.split(","):
    numlist.append(int(count))
  mycolors = []
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
  if title != "No_title_required":
    plt.title(title)
  plt.savefig("horizontalbarchart.png", transparent=True)
  plt.clf()

def botbarv(title, numbers, label):
  numlist = []
  for count in numbers.split(","):
    numlist.append(int(count))
  mycolors = []
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
  if title != "No_title_required":
    plt.title(title)
  plt.savefig("verticalbarchart.png", transparent=True)
  plt.clf()
