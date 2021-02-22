import matplotlib.pyplot as plt
import numpy as np

cmaphsv = plt.cm.hsv
def func(pct, allvals):
  absolute = int(pct/100*np.sum(allvals))
  return "{:d} ({:.1f}%)".format(absolute, int(pct))

def bothist(title, numbers):
  numlist = []
  for count in numbers.split(","):
    numlist.append(float(count))
  plt.hist(numlist)
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
  plt.savefig("verticalbarchart.png", transparent=True)
  plt.clf()
