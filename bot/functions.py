import regex
from shared import re, SequenceMatcher, typing

def enum_mentionables(mentionables, max_length: int, delimiter1: str, delimiter2: str, no_text: str):
  """
  Enumerates a list of instances with properties `mention` and `name`.

  To enumerate through `roles` with up to 1024 length, separating role mentions with spaces if\
  possible, otherwise separating names with commas, returning "No roles" if `roles` is empty:
  ```
  enum_mentionables(roles, 1024, " ", ", ", "No roles")
  ```
  """
  if not mentionables:
    return no_text
  result = delimiter1.join([x.mention for x in mentionables])
  if len(result) > max_length:
    result = delimiter2.join([x.name for x in mentionables])
    if len(result) > max_length:
      pass
      # Comma-separate until length too high, then add ellipses
  return result

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
  test_for("appel", 0.8, "apple", "banana", "cherry") # Checks if "appel" is at least 80% close to\
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
  """
  Trims a ``str`` if it is longer than ``width``.
  ```
  trim("Lorem Ipsum", 11) # Returns "Lorem Ipsum" because it is not longer than 11 characters
  trim("Lorem Ipsum", 9) # Returns "Lorem Ip…"
  ```
  """
  return text if len(text) <= width else text[:width - 1] + "…"