import re
import typing
from difflib import SequenceMatcher

def html_to_md(text : str):
  text = re.sub(r'<b>(.+?)</b>', r'**\1**', text)
  text = re.sub(r'<i>(.+?)</i>', r'*\1*', text)
  return text

def many_replace(text : str, replacer : dict[str : str]):
  for x, y in replacer.items():
    text = text.replace(x, y)
  return text

def test_for(text : str, min_ratio : typing.Union[float, int], *choices : list[str]):
  choices = [choices[0]] if len(choices) == 1 else list(choices)
  raw_tested = {x:SequenceMatcher(None, x, text).ratio() for x in choices}
  tested = {x:y for x,y in sorted(raw_tested.items(), key=lambda item: item[1], reverse=True)}
  print(tested)
  if tested[list(tested)[0]] >= min_ratio:
    return list(tested)[0]
