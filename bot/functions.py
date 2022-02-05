import regex
from shared import re, SequenceMatcher, typing

def html_to_md(text: str):
  text = re.sub(r'<b>(.+?)</b>', r'**\1**', text)
  text = re.sub(r'<i>(.+?)</i>', r'*\1*', text)
  text = re.sub(r'<i>(.+?)</i>', r'*\1*', text)
  text = re.sub(r'<a href="([\w?:/\&%]+?)"( target="_[A-Za-z]+?")>(.+?)</a>', r'[\2](\1)', text)
  text = regex.sub(r'(?<=<ol>\n?(<li>[A-Za-z\s]+<\/li>\n?)*)(<li>([A-Za-z\s]+)<\/li>)(?=\n?(<li>[A-Za-z\s]+<\/li>\n?)*<\/ol>)', '• \3', text)
  text = regex.sub(r'(?<=<ul>\n?(<li>[A-Za-z\s]+<\/li>\n?)*)(<li>([A-Za-z\s]+)<\/li>)(?=\n?(<li>[A-Za-z\s]+<\/li>\n?)*<\/ul>)', '• \3', text)
  return text

def many_replace(text: str, replacer: dict[str: str]):
  for x, y in replacer.items():
    text = text.replace(x, y)
  return text

def xfill(text: str, chars: int, char: str = " "):
  """
  Pads a character to a `str` until it reaches a length.
  ```
  x_fill("123", "$", 7) # Returns "$$$$123"
  x_fill("123", "$", 2) # Returns "123" (Autofix too short strings)
  ```
  """
  return max(chars - len(text), 0) * char + text

def test_for(text: str, min_ratio: typing.Union[float, int], *choices: str):
  """
  Checks if a ``str`` is close enough to a list of strings, using `difflib.SequenceMatcher`.
  ```
  test_for("appel", 0.8, "apple", "banana", "cherry") # checks if "appel" is at least 80% close to\
  one of the listed fruits, returns True
  ```
  """
  choices = [choices[0]] if len(choices) == 1 else list(choices)
  raw_tested = {x:SequenceMatcher(None, x, text).ratio() for x in choices}
  tested = {x:y for x,y in sorted(raw_tested.items(), key=lambda item: item[1], reverse=True)}
  print(tested)
  if tested[list(tested)[0]] >= min_ratio:
    return list(tested)[0]

def trim(text: str, width: int):
  return text if len(text) <= width else text[:width - 1] + "…"