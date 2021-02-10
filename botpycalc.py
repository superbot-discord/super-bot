from discord import Webhook, RequestsWebhookAdapter
from discord_webhook import DiscordWebhook
from discord.ext.commands import *
from discord.ext import commands
import discord
from math import *
from cmath import *
import random as ra
import numpy as np
from math import *
import subprocess
import re

def botpython(script):
  python_pattern = re.compile(r'^\`\`\`(py|python)?\n[\s\S]*\`\`\`$')
  match = python_pattern.fullmatch(script)
  if match:
    script = script.replace("```py","", 1)
    script = script.replace("```","")
  file = open("program.py", "w")
  file.write(script)
  file.close()
  proc = subprocess.Popen(['python', 'program.py',  ''], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  try:
    output = str(await proc.communicate(timeout = 1)[0])
    output = output.lstrip("'b(").rstrip("\\n'").replace("\n", f"\n")
  except subprocess.TimeoutExpired:
    await proc.kill()
    output = await str(proc.communicate())
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

def botdefine(function, definition, argumentsraw):
  if argumentsraw == None:
    return "Not enough args"
  else:
    definition=definition.replace("^","**")
    definition=definition.replace("÷","/")
    definition=definition.replace("×","*")
    definition=definition.replace("mod","%")
    definition=definition.replace("√(","sqrt(")
    definition=definition.replace("pi",str(pi))
    definition=definition.replace("e",str(e))
    program="def "+function+"("
    if argumentsraw != "":
      arguments = argumentsraw.split(" ")
      for count in arguments:
        program = program + count + ","
    program = program[:-1]
    program = program + f"):\n  return "+definition
    exec(program, globals())
    return "Add_Reaction"

def botcalc(arg = None):
  if arg == None:
    return "Invalid format! Please use the format `=calc [formula]`."
  else:
    arg=arg.replace("^","**")
    arg=arg.replace("÷","/")
    arg=arg.replace("×","*")
    arg=arg.replace("mod","%")
    arg=arg.replace("√(","sqrt(")
    arg=arg.replace("pi",str(pi))
    arg=arg.replace("e",str(e))
    if arg.count("=")==0 or arg.count("==")!=0 or arg.count("!=")!=0 or arg.count(">=")!=0 or arg.count("<=")!=0 or arg.count(">")!=0 or arg.count("<")!=0 or arg.count("and")!=0 or arg.count("or")!=0 or arg.count("not")!=0:
      lcls = locals()
      exec("result = "+arg, globals(), lcls)
      result = lcls["result"]
      if result.real==result:
        result=result.real
      if len(str(result))>400:
        number=result
        result=str(number)[0]+"."
        for count in range(1,60):
          result=result+str(number)[count]
        result=result+"e+"+str(len(str(number))-1)
      elif len(str(result))>100:
        result="{0:.3E}".format(float(result))
      disp = "Result: "+str(result)
      return disp
    elif arg.count("=")!=0 and arg.count("==")==0 and arg.count("!=")==0 and arg.count(">=")==0 and arg.count("<=")==0 and arg.count(">")==0 and arg.count("<")==0 and arg.count("and")==0 and arg.count("or")==0 and arg.count("not")==0:
      lcls = locals()
      exec(arg, globals(), lcls)
      return "Add_Reaction"
    else:
      return "Invalid input, please try again."
