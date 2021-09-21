import random as ra
import re
import subprocess
from cmath import *
from math import *

import numpy as np
from discord.ext import commands

from shared import db

SY2VA = db["decoder"]
ASCII = db["encoder"]

def botpython(script : str):
  python_pattern = re.compile(r'^\`\`\`(py|python)?\n[\s\S]*\`\`\`$')
  match = python_pattern.fullmatch(script)
  if match:
    script = script.replace("```py","", 1).replace("```","")
  file = open("program.py", "w")
  file.write(str(script))
  file.close()
  proc = subprocess.Popen(['python', 'program.py',  ''], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  try:
    output = str(proc.communicate(timeout = 1)[0])
    output = output.lstrip("'b(").rstrip("\\n'").replace("\n", f"\n")
  except subprocess.TimeoutExpired:
    proc.kill()
    output = str(proc.communicate())
  output = output.lstrip("'b(").rstrip("\\n'").replace("\n", f"\n")
  outputlist = output.split("\\n")
  if len(outputlist)<=11:
    formatoutput = ""
    for count in range(0, len(outputlist)):
      if count+1<=9:
        formatoutput = formatoutput + "0" + str(count+1) + " | " + outputlist[count] + f"\n"
      else:
        formatoutput = formatoutput + str(count+1) + " | " + outputlist[count] + f"\n"
    
    if formatoutput == f"01 | \n":
      return "There was no result to be shown."
    else:
      return f"```\n"+formatoutput+f"\n```"
  else:
    truncatedoutput = ""
    for count in range(0,11):
      if count+1<=9:
        truncatedoutput = truncatedoutput + "0" + str(count+1) + " | " + outputlist[count] + f"\n"
      else:
        truncatedoutput = truncatedoutput + str(count+1) + " | " + outputlist[count] + f"\n"
    return f"The result was truncated due to the length of the result. It had probably timed out.\n```\n"+truncatedoutput+f"\n```"

def botdefine(function : str, definition : str, argumentsraw : str):
  if argumentsraw == None:
    return "Not enough args"
  else:
    definition=definition.replace("^","**").replace("÷","/").replace("×","*").replace("mod","%").replace("√(","sqrt(").replace("pi",str(pi)).replace("e",str(e))
    program="def "+function+"("
    if argumentsraw != "":
      program = program + argumentsraw.replace(" ",",")
    program = program + f"):\n  return "+definition
    exec(program, globals(), globals())
    return "Add_Reaction"

@commands.command()
async def base(ctx, frombase : int, tobase : int, *, text):
  integer = 0
  for character in text:
    if character not in SY2VA:
      await ctx.send('Found unknown character!')
      return
    value = SY2VA[character]
    if value >= frombase:
      await ctx.send(f'Found digit outside base! {value} is greater than {frombase}.')
      return
    integer *= frombase
    integer += value
  VA2SY = dict(map(reversed, SY2VA.items()))
  array = []
  while integer:
    integer, value = divmod(integer, tobase)
    array.append(VA2SY[value])
  answer = ''.join(reversed(array))
  await ctx.send(answer)

@commands.command()
async def ascii(ctx, *, text):
  answer = ""
  for character in text:
    answer = answer + ASCII[character]
  await ctx.send(answer)

def botcalc(arg):
  if arg == "None":
    return "Invalid format! Please use the format `=calc [formula]`."
  else:
    try:
      arg=arg.replace("^","**").replace("÷","/").replace("×","*").replace("mod","%").replace("√(","sqrt(").replace("pi",str(pi)).replace(",","").replace("a","")
      return f"Result: {str(eval(arg))}"
    except:
      return "Invalid formula!"

def setup(bot):
  bot.add_command(base)
