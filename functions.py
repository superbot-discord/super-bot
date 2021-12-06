from difflib import SequenceMatcher
import typing

def test_for(text : str, min_ratio : typing.Union[float, int], *choices : list[str]):
  choices = [choices[0]] if len(choices) == 1 else list(choices)
  raw_tested = {x:SequenceMatcher(None, x, text).ratio() for x in choices}
  tested = {x:y for x,y in sorted(raw_tested.items(), key=lambda item: item[1], reverse=True)}
  print(tested)
  if tested[list(tested)[0]] >= min_ratio:
    return list(tested)[0]

def many_replace(text : str, replacer : dict[str : str]):
  for x, y in replacer.items():
    text = text.replace(x, y)
  return text