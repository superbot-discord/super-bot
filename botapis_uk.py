from shared import *

@commands.command()
async def uk_extremes(ctx, *, disposed=None):
  r=requests.get("http://datapoint.metoffice.gov.uk/public/data/txt/wxobs/ukextremes/json/latest?key=69eba5b0-9c89-4198-b973-b4576f60f0f5").json()

def setup(bot):
  bot.add_command(uk_extremes)