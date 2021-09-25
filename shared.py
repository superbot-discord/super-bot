import json
import re
from datetime import datetime, timezone

import discord
from discord import Embed, Permissions, ui

f = open('database.json', 'r')
db = json.loads(f.read())
f.close()

botadmin        =lambda context        : context.author.id in db["botadmins"]
number_to_emoji =lambda a              : a.replace("1",":one: ").replace("2",":two: ").replace("3",":three: ").replace("4",":four: ").replace("5",":five: ").replace("6",":six: ").replace("7",":seven: ").replace("8",":eight: ").replace("9",":nine: ").replace("0",":zero: ")
sizer           =lambda bytes          : f"{round(bytes,4):,}Bytes" if bytes<1024 else (f"{round(bytes/1024,4):,}KB" if bytes<1048576 else (f"{round(bytes/1048576,4):,}MB" if bytes<1073741824 else f"{round(bytes/1073741824,4):,}GB"))
format_length   =lambda secs           : f"{str(secs//86400)} days plus {str(secs%21600//3600).zfill(2)}:{str(secs%3600//60).zfill(2)}:{str(secs%60).zfill(2)}" if secs >= 86400 else (f"{str(secs//3600).zfill(2)}:{str(secs%3600//60).zfill(2)}:{str(secs%60).zfill(2)}" if secs >= 3600 else f"{str(secs//60).zfill(2)}:{str(secs%60).zfill(2)}")
formabr         =lambda vid            : vid.__getattribute__("abr")+f"\t" if vid.__getattribute__("abr") else 'No audio'
specialbool     =lambda input          : input.lower() in ["1", "ok", "yes", "ye", "yeah", "enable", "on", "enabled", "tick", "true"]
has_perms       =lambda chn, memb, perm: (chn.permissions_for(memb).value  & 1 << perm) or (chn.permissions_for(memb).value  & 1 << 8) or memb.id in db["botadmins"]

verify_pattern = re.compile(r'[^ ⠀][\s\S]{0,30}?[^ ⠀]#?[\d]{4}(,|, | )?[\d+\-*/×÷%xyz()\[\]\{\}]{1,50}=[\d+\-*/×÷%xyz()\[\]\{\}]{1,50}(,|, | )?[\S ]{3,20}(,|, | )?(Red|Orange|Yellow|Green|Light( |_)?Green|Dark( |_)?Green|Cyan|Blue|Light( |_)?Blue|Dark( |_)?Blue|Purple|Pink|Brown)', re.IGNORECASE)
id_pattern = re.compile(r'([A-Z]{5})', re.IGNORECASE)
poll_pattern = re.compile(r'([\w]+?)(:\w{2,32}:|[\uD800-\uDBFF])')
UNITS = {'s':'seconds', 'm':'minutes', 'h':'hours', 'd':'days', 'w':'weeks'}
view_overwrite = discord.PermissionOverwrite()
view_overwrite.view_channel = True
clickers = {}
dt1 = datetime(1970,1,1,0,0,0,0,timezone.utc)

def sample_buttons(ctx):
  return [
  ui.Button(style=discord.ButtonStyle.primary,   row=0, custom_id="primary",   emoji="🟢", label="Primary (blurple)"),
  ui.Button(style=discord.ButtonStyle.secondary, row=0, custom_id="secondary", emoji=ctx.bot.get_emoji(824680026858717234), label="Secondary (grey)"),
  ui.Button(style=discord.ButtonStyle.success,   row=0, custom_id="green",     label="Success (green)"),
  ui.Button(style=discord.ButtonStyle.danger,    row=0, custom_id="red",       label="Danger (red)"),
  ui.Button(style=discord.ButtonStyle.url,       row=0,                        label="URL (grey)", url=ctx.message.jump_url),
  ui.Button(style=discord.ButtonStyle.primary,   row=1, emoji="🟢", disabled=True, label="Primary (blurple)"),
  ui.Button(style=discord.ButtonStyle.secondary, row=1, emoji=ctx.bot.get_emoji(824680026858717234), disabled=True, label="Secondary (grey)"),
  ui.Button(style=discord.ButtonStyle.success,   row=1, disabled=True, label="Success (green)"),
  ui.Button(style=discord.ButtonStyle.danger,    row=1, disabled=True, label="Danger (red)"),
  ui.Button(style=discord.ButtonStyle.url,       row=1, disabled=True, label="URL (grey)", url=ctx.message.jump_url),
]

#clicker_button = ui.Button(style=discord.ButtonStyle.primary, row=0, custom_id="clicker", label="Click me!")

sample_options = [
  discord.SelectOption(label="Red"   , description="Roses are red"              , emoji="🔴"),
  discord.SelectOption(label="Orange", description="Oranges are orange"         , emoji="🟠"),
  discord.SelectOption(label="Yellow", description="Sunflowers are yellow"      , emoji="🟡"),
  discord.SelectOption(label="Green" , description="Cabbages are green"         , emoji="🟢"),
  discord.SelectOption(label="Blue"  , description="Discord is blue (and cool)" , emoji="🔵", default=True),
  discord.SelectOption(label="Purple", description="Violets are blurple"        , emoji="🟣"),
  discord.SelectOption(label="Brown" , description="Dry plants are brown"       , emoji="🟤"),
]

def sample_menus():
  return [
    ui.Select(placeholder="Select one option",          custom_id="single-selection", row=0, options=sample_options),
    ui.Select(placeholder="Select two to five options", custom_id="multi-selection" ,row=1, min_values=2, max_values=5, options=sample_options),
    ui.Select(placeholder="Select one option",          row=2, disabled=True, options=sample_options),
    ui.Select(placeholder="Select two to five options", row=3, disabled=True, min_values=2, max_values=5, options=sample_options)
  ]

def help_menu_options(ctx):
  return [
    discord.SelectOption(label="All", description="Rough list of all commands",                                           value="help_all"), #emoji=ctx.bot.get_emoji(), 
    discord.SelectOption(label="Basic", description="Fundamental commands, e.g. help, ping",                              value="help_basic"), #emoji=ctx.bot.get_emoji(), 
    discord.SelectOption(label="Discord info", description="Discord information viewer, e.g. server. user",               value="help_dinfo"), #emoji=ctx.bot.get_emoji(), 
    discord.SelectOption(label="Discord", description="Commands that interact with Discord, e.g. snipe",                  value="help_discord"), #emoji=ctx.bot.get_emoji(), 
    discord.SelectOption(label="Moderation", description="Commands to simplify server moderation, e.g. purge, makeinvite",value="help_mod"), #emoji=ctx.bot.get_emoji(), 
    discord.SelectOption(label="Text", description="Have fun with your text, e.g. reverse, encode",                       value="help_text"), #emoji=ctx.bot.get_emoji(), 
    discord.SelectOption(label="Information", description="Informative commands, e.g. color, unix",                       value="help_info"), #emoji=ctx.bot.get_emoji(), 
    discord.SelectOption(label="Web", description="Commands that interact with the Internet, e.g. youtube, wiki",         value="help_web"), #emoji=ctx.bot.get_emoji(), 
    discord.SelectOption(label="Plot", description="Commands to draw graphs, e.g. pie, bar",                              value="help_plot"), #emoji=ctx.bot.get_emoji(), 
    discord.SelectOption(label="Developer", description="Developer-oriented commands, e.g. html, regex",                  value="help_dev"), #emoji=ctx.bot.get_emoji(), 
    discord.SelectOption(label="Image", description="Image-editing or analysing commands, e.g. analyse, ocr",             value="help_img"), #emoji=ctx.bot.get_emoji(), 
    discord.SelectOption(label="General Documentation", description="Quick links and documentation website",              value="help_general"), #emoji=ctx.bot.get_emoji(), 
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

invite_embed = discord.Embed(title="Invite", description = "The bot can be invited [here](https://discord.com/api/oauth2/authorize?client_id=796686363604680755&permissions=8&redirect_uri=https%3A%2F%2Fsuperbot-discord.github.io&scope=bot%20applications.commands).")
help_all = discord.Embed(title="SuperBot#4073 (ID:796686363604680755)", description=f"""**Prefix: **`=`
**Basic Commands**
`help` `interactive_help` `invite` `prefix` `ping` `botpurge`\n
**Discord Information Commands**
`server` `invitelink` `role` `channel` `user` `avatar` `status` `leftuser` `message` `raw` `reactions` `emojiinfo` `template`\n
**Discord Commands**
`react` `snipe` `clearsnipe` `pretend` `pretendembed` `embed` `editembed` `simpleembed` `quickembed` `ett` `tts`\n
**Moderation Commands**
`kick` `ban` `unban` `slowmode` `purge` `purgeuser` `purgeregex` `purgepy` `purgepygex` `purgereactions` `makeinvite`\n
**Text Manipulation Commands**
`poll` `insert` `spoiler` `rawspoiler` `rawrawspoiler` `reverse` `emoji` `encode` `decode`\n
**Information Commands**
`color` `simplecolor` `translate` `definition` `unix` `time` `rtimer` `ttimer` `terminate` `unscramble` `unicode` `random` `choice`\n
**Web Commands**
`redirect` `screenshot` `youtube` `wiki` `minecraft` `engrave` `covid` `population` `map`
`bunny` `cat` `dog` `duck` `fox` `koala` `lizard` `panda` `shiba` `error` `errorcat` `errordog`\n
**Plot/Drawing Commands**
`ascii` `table` `render` `captcha` `pie` `barh` `barv` `hist` `sankey` `snow` `mandelbrot`\n
**Developer Tools and Miscellaneous Commands**
`html` `md` `regex` `regsub` `button` `menu`\n
**Image Commands**
`analyse` `histogram` `resize` `rotate` `brightness` `contrast` `sharpen` `edge` `contour` `blur` `invert` `hue` `recolor`
To use the 13 commands above, type `=image ` first, then upload an image. Example: `=image analyse`. Supply a user name to work on his avatar, e.g. `=image SuperBot#4073 analyse`
`ocr` `qr` `qrmake` `transparent` `text`\n
`hello` leads you to death\nNeed help? check the [documentation](https://superbot-discord.github.io/documentation)!""")

help_basic = discord.Embed(title="SuperBot Basic Commands", description=f"""
**help** Views a rough list of all commands.
**interactive_help** Interactive version of `help` with fancy buttons.
**invite** Gets a link to invite the bot.
**prefix** Views the prefix of the bot (`=`).
**ping** Checks whether the bot is online and shows the latency.
**botpurge [Number]** Purges messages sent by the bot. Requires `Manage Messages`.
\nNeed help? check the [documentation](https://superbot-discord.github.io/documentation)!""")

help_dinfo = discord.Embed(title="SuperBot Discord Information Commands", description=f"""
**Discord Information Commands**
**server** Views information about the current server.
**server mod** Views banned members and invite links of the current server.
**invitelink** Views information about an invite link.
**role** Views information about a role.
**channel** Views information about a text, voice or stage channel.
**user** Views information about a user.
**avatar** Views the avatar of a user.
**status** Views the status of a user.
**leftuser** Views limited information about a user not in the current server.
**message** Views information about a message.
**raw** Views the content of a message.
**reactions** Views information about the reactions of a message.
**emojiinfo** Views information about an emoji.
**template** Views information about a server template.\n
You need to supply arguments for most commands.
Need help? check the [documentation](https://superbot-discord.github.io/documentation)!""")

help_discord = discord.Embed(title="SuperBot Discord Commands", description=f"""
**react [Message] [Emoji ID]** Temporarily reacts with an emoji. Replaces Nitro.
**snipe** Snipes the 5 most recently deleted messages.
**snipe [0/1]** Enables or disables sniping in the current channel. Requires `Manage Messages`.
**clearsnipe** Enables or disables sniping in the current channel. Requires `Manage Channels`.
**pretend [User] [Content]** Pretends as a user and sends something. Bot needs `Manage Webhooks`.
**pretendembed [User] [Embed]** Pretends as a user and sends an embed. Bot needs `Manage Webhooks`.
**embed [Embed]** Sends an embed.
**editembed [Message] [Embed]** Edits an embed.
**simpleembed [Simple Embed]** Sends an embed with a simpler interface.
**quickembed [Quick Embeds]** Sends an embed with an extremely intuitive interface.
**ett [Message]** Converts an embed into `=embed`-compatible format.
**tts [Content]** Sends a message with TTS. Bot and you need `Send TTS Messages`.\n
Check [how to supply embeds](https://superbot-discord.github.io/Appendices/A1/). `=pretendembed` and `=editembed` takes the same arguments as `=embed`.
Need help? check the [documentation](https://superbot-discord.github.io/documentation)!""")
