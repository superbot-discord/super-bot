from shared import *

# INDEX
# 8    Bot

# bot

@ui_.slash.command(name="ping", description="Check whether the bot is online or not and see the latency & response time.")
async def ping_(ctx):
  now1 = datetime.now(timezone.utc)
  message = await ctx.send("Pong!")
  response_time = datetime.now(timezone.utc) - now1
  mcs = str(int(response_time.microseconds)+int((response_time.total_seconds())%60))
  await message.edit(content=f"Pong! 🏓\n```Message delay: {mcs:<10}microseconds\nBot latency  : {round(bot_.latency*1000000,2):<10}microseconds```")