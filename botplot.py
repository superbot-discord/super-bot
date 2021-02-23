import matplotlib.pyplot as plt
import numpy as np

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
    if count%1 == 0:
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
