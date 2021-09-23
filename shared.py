import json

from discord import Embed, Permissions, ui
import discord

f = open('database.json', 'r')
db = json.loads(f.read())
f.close()

botadmin        =lambda context        : context.author.id in db["botadmins"]
number_to_emoji =lambda a              : a.replace("1",":one: ").replace("2",":two: ").replace("3",":three: ").replace("4",":four: ").replace("5",":five: ").replace("6",":six: ").replace("7",":seven: ").replace("8",":eight: ").replace("9",":nine: ").replace("0",":zero: ")
sizer           =lambda bytes          : f"{round(bytes/1024,4):,}KB" if bytes<1048576 else (f"{round(bytes/1048576,4):,}MB" if bytes<1073741824 else f"{round(bytes/1073741824,4):,}GB")
format_length   =lambda secs           : f"{str(secs//86400)} days plus {str(secs%21600//3600).zfill(2)}:{str(secs%3600//60).zfill(2)}:{str(secs%60).zfill(2)}" if secs >= 86400 else (f"{str(secs//3600).zfill(2)}:{str(secs%3600//60).zfill(2)}:{str(secs%60).zfill(2)}" if secs >= 3600 else f"{str(secs//60).zfill(2)}:{str(secs%60).zfill(2)}")
formabr         =lambda vid            : vid.__getattribute__("abr")+f"\t" if vid.__getattribute__("abr") else 'No audio'
specialbool     =lambda input          : input.lower() in ["1", "ok", "yes", "ye", "yeah", "enable", "on", "enabled", "tick", "true"]
has_perms       =lambda chn, memb, perm: (chn.permissions_for(memb).value  & 1 << perm) or (chn.permissions_for(memb).value  & 1 << 8) or memb.id in db["botadmins"]

def sample_buttons(ctx):
  return [
  ui.Button(style=discord.ButtonStyle.primary,   row=0, emoji="🟢", label="Primary (blurple)"),
  ui.Button(style=discord.ButtonStyle.secondary, row=0, emoji=ctx.bot.get_emoji(824680026858717234), label="Secondary (grey)"),
  ui.Button(style=discord.ButtonStyle.success,   row=0, label="Success (green)"),
  ui.Button(style=discord.ButtonStyle.danger,    row=0, label="Danger (red)"),
  ui.Button(style=discord.ButtonStyle.url,       row=0, label="URL (grey)", url=ctx.message.jump_url),
  ui.Button(style=discord.ButtonStyle.primary,   row=1, emoji="🟢", disabled=True, label="Primary (blurple)"),
  ui.Button(style=discord.ButtonStyle.secondary, row=1, emoji=ctx.bot.get_emoji(824680026858717234), disabled=True, label="Secondary (grey)"),
  ui.Button(style=discord.ButtonStyle.success,   row=1, disabled=True, label="Success (green)"),
  ui.Button(style=discord.ButtonStyle.danger,    row=1, disabled=True, label="Danger (red)"),
  ui.Button(style=discord.ButtonStyle.url,       row=1, disabled=True, label="URL (grey)", url=ctx.message.jump_url),
]

sample_options = [
  discord.SelectOption(label="Red"      , description="Roses are red"              , emoji="🔴"),
  discord.SelectOption(label="Orange"   , description="Oranges are orange"         , emoji="🟠"),
  discord.SelectOption(label="Yellow"   , description="Sunflowers are yellow"      , emoji="🟡"),
  discord.SelectOption(label="Green"    , description="Cabbages are green"         , emoji="🟢"),
  discord.SelectOption(label="Blue"     , description="Violets are blue (and cool)", emoji="🔵", default=True),
  discord.SelectOption(label="Purple"   , description="Discord is purple"          , emoji="🟣"),
  discord.SelectOption(label="Brown"    , description="Dry plants are brown"       , emoji="🟤"),
]

def sample_menus():
  return [
    ui.Select(placeholder="Select one option",          row=0, options=sample_options),
    ui.Select(placeholder="Select two to five options", row=1, min_values=2, max_values=5, options=sample_options),
    ui.Select(placeholder="Select one option",          row=2, disabled=True, options=sample_options),
    ui.Select(placeholder="Select two to five options", row=3, disabled=True, min_values=2, max_values=5, options=sample_options)
  ]

custom_permissions = {
  "admin"       : Permissions(8),
  "semiadmin"   : Permissions(536870911991),
  "mod"         : Permissions(536602476259),
  "manager"     : Permissions(466255085123),
  "speaker"     : Permissions(414598024897),
  "member"      : Permissions(414568664129),
  "semimember"  : Permissions(277129449025),
  "restrict"    : Permissions(274914675777),
  "mute"        : Permissions(67175425),
  "freeze"      : Permissions(66560),
  "none"        : Permissions(0),
}

server_permtext = """```
Index Permission
3     Administrator
5     Manage Server
28    Manage Roles
4     Manage Channels
1     Kick Members
2     Ban Members
0     Generate Invites
27    Manage Nicknames
26    Change Nickname
30    Manage Emojis and Stickers
29    Manage Webhooks
7     View Audit Logs
19    View Server Insights
10    View Channels
```"""

tc_permtext = """```
Index Permission
11    Send Messages
38    Send Messages in Threads
35    Create Public Threads
36    Create Private Threads
12    Send TTS Messages
13    Manage Messages
32    Manage Threads
14    Embed Links
15    Attach Files
16    Read Message History
17    Mention Everyone
6     Add Reactions
18    Use External Emojis
37    Use External Stickers
31    Use Slash Commands
```"""

vc_permtext = """```
Index Permission
20    Connect to Voice
21    Speak (Audio)
9     Stream (Video)
22    Mute Members
23    Deafen Members
24    Move Members
25    Use Voice Activity
8     Priority Speaker
```"""

perms_guide = Embed(title="Permission integers", description="""
Permission integers allow you to store permissions quickly. To represent some permissions, calculate the sum of 2 to the power of the permission index.
For example, to specify kick members, manage channels and stream, calculate `2^1+2^4+2^9`, which is 530.
Alternatively, if you know binary, put a `1` in the permission indices' places, which is `100001001`. Then run `=base 2 10 [Your binary]` to get the decimal equivalent.""")
perms_guide.add_field(name="Server permissions", value=server_permtext, inline=False)
perms_guide.add_field(name="Text channel permissions", value=tc_permtext, inline=False)
perms_guide.add_field(name="Voice channel permissions", value=vc_permtext, inline=False)

server_real = {
  3 : "Administrator",
  5 : "Manage Server",
  28: "Manage Roles",
  4 : "Manage Channels",
  1 : "Kick Members",
  2 : "Ban Members",
  0 : "Generate Invites",
  27: "Manage Nicknames",
  26: "Change Nickname",
  30: "Manage Emojis and Stickers",
  29: "Manage Webhooks",
  7 : "View Audit Logs",
  19: "View Server Insights",
  10: "View Channels"
}

text_channel_real = {
  11: "Send Messages",
  38: "Send Messages in Threads",
  35: "Create Public Threads",
  36: "Create Private Threads",
  12: "Send TTS Messages",
  13: "Manage Messages",
  32: "Manage Threads",
  14: "Embed Links",
  15: "Attach Files",
  16: "Read Message History",
  17: "Mention Everyone",
  6 : "Add Reactions",
  18: "Use External Emojis",
  37: "Use External Stickers",
  31: "Use Slash Commands"
}

voice_channel_real = {
  20: "Connect to Voice",
  21: "Speak (Audio)",
  9 : "Stream (Video)",
  22: "Mute Members",
  23: "Deafen Members",
  24: "Move Members",
  25: "Use Voice Activity",
  8 : "Priority Speaker"
}

def server_itop(integer):
  cache3 = ""
  for count, count2 in server_real.items():
    if integer & 1 << count:
      cache3 += count2 + ", "
  if len(cache3) > 2:
    return cache3[:-2]
  else:
    return "No server permissions"

def tc_itop(integer):
  cache3 = ""
  for count, count2 in text_channel_real.items():
    if integer & 1 << count:
      cache3 += count2 + ", "
  if len(cache3) > 2:
    return cache3[:-2]
  else:
    return "No text channel permissions"

def vc_itop(integer):
  cache3 = ""
  for count, count2 in voice_channel_real.items():
    if integer & 1 << count:
      cache3 += count2 + ", "
  if len(cache3) > 2:
    return cache3[:-2]
  else:
    return "No voice channel permissions"
