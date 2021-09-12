from discord.ext import commands
from math import *
from cmath import *
import random as ra
import numpy as np
from math import *
import subprocess
import re
from bot import SY2VA

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
async def base(ctx, text, frombase, tobase):
  integer = 0
  for character in text:
    if character not in SY2VA:
      await ctx.send('Found unknown character!')
    value = SY2VA[character]
    if value >= frombase:
      await ctx.send('Found digit outside base!')
    integer *= frombase
    integer += value
  VA2SY = dict(map(reversed, SY2VA.items()))
  array = []
  while integer:
    integer, value = divmod(integer, tobase)
    array.append(VA2SY[value])
  answer = ''.join(reversed(array))
  await ctx.send(answer)

def botcalc(arg : str):
  if arg == "None":
    return "Invalid format! Please use the format `=calc [formula]`."
  else:
    arg=arg.replace("^","**").replace("÷","/").replace("×","*").replace("mod","%").replace("√(","sqrt(").replace("pi",str(pi)).replace(",","").replace("r","")
    if arg.count("=")==0 or arg.count("==")!=0 or arg.count("!=")!=0 or arg.count(">=")!=0 or arg.count("<=")!=0 or arg.count(">")!=0 or arg.count("<")!=0 or arg.count("and")!=0 or arg.count("or")!=0 or arg.count("not")!=0:
      lcls = locals()
      exec("result = "+arg, globals(), lcls)
      result = lcls["result"]
      if result.real==result:
        result=result.real
      if result<=1 and result>0:
        result=str(result)+f"\n"+str(round(result*100, 5))+"%"
      elif len(str(result))>100:
        result="{0:.3E}".format(float(result))
      else:
        if len(str(result))>400:
          number=result
          result=str(number)[0]+"."
          for count in range(1,60):
            result=result+str(number)[count]
          result=result+"e+"+str(len(str(number))-1)
      disp = "Result: "+str(result)
      return disp
    elif arg.count("=")!=0 and arg.count("==")==0 and arg.count("!=")==0 and arg.count(">=")==0 and arg.count("<=")==0 and arg.count(">")==0 and arg.count("<")==0 and arg.count("and")==0 and arg.count("or")==0 and arg.count("not")==0:
      #lcls = locals()
      exec(arg, globals(), globals())
      return "Add_Reaction"
    else:
      return "Invalid input, please try again."

def setup(bot):
  bot.add_command(base)