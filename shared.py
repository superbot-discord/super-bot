import json

from discord import Permissions, channel, threads
from discord.types.member import Nickname

f = open('database.json', 'r')
db = json.loads(f.read())
f.close()

botadmin = lambda context : context.author.id == 687474789342117900
number_to_emoji = lambda a: a.replace("1",":one: ").replace("2",":two: ").replace("3",":three: ").replace("4",":four: ").replace("5",":five: ").replace("6",":six: ").replace("7",":seven: ").replace("8",":eight: ").replace("9",":nine: ").replace("0",":zero: ")
sizer = lambda bytes: f"{round(bytes/1024,4):,}KB" if bytes<1048576 else (f"{round(bytes/1048576,4):,}MB" if bytes<1073741824 else f"{round(bytes/1073741824,4):,}GB")
format_length=lambda secs: f"{str(secs//86400)} days plus {str(secs%21600//3600).zfill(2)}:{str(secs%3600//60).zfill(2)}:{str(secs%60).zfill(2)}" if secs >= 86400 else (f"{str(secs//3600).zfill(2)}:{str(secs%3600//60).zfill(2)}:{str(secs%60).zfill(2)}" if secs >= 3600 else f"{str(secs//60).zfill(2)}:{str(secs%60).zfill(2)}")
formabr = lambda vid: vid.__getattribute__("abr")+f"\t" if vid.__getattribute__("abr") else 'No audio'
specialbool = lambda input: True if input.lower() in ["1","yes", "enable", "on", "enabled", "tick", "true"] else False


custom_permissions = {
  "admin"       : Permissions(8),
  "semiadmin"   : Permissions(536870911991),
  "mod"         : Permissions(467882999523),
  "manager"     : Permissions(534974561879),
  "member"      : Permissions(414568664129),
  "semimember"  : Permissions(277129449025),
  "restrict"    : Permissions(274914675777),
  "mute"        : Permissions(67175425),
  "freeze"      : Permissions(66560),
  "none"        : Permissions(0),
}

server_permissions = {
  8:            "Administrator",
  32:           "Manage Server",
  16:           "Manage Channels",
  268435456:    "Manage Roles",
  128:          "View Audit Logs",
  524288:       "View Server Insights",
  2:            "Kick Members", 
  4:            "Ban Members",
  134217728:    "Manage Nicknames",
  536870912:    "Manage Webhooks",
  1073741824:   "Manage Emojis and Stickers",
  67108864:     "Change Nickname",
  1:            "Generate Invites",
  1024:         "View Channels",
}

tc_permissions = {
  8192:         "Manage Messages",
  65536:        "Read Message History",
  2048:         "Send Messages",
  4096:         "Send TTS Messages",
  131072:       "Mention Everyone",
  64:           "Add Reactions",
  262144:       "Use External Emojis",
  137438953472: "Use External Stickers",
  16384:        "Embed Links",
  32768:        "Attach Files",
  2147483648:   "Use Slash Commands",
  17179869184:  "Manage threads",
  34359738368:  "Create Public Threads",
  68719476736:  "Create Private Threads",
  274877906944: "Send Messages in Threads",
}

vc_permissions = {
  1048576:      "Connect to Voice",
  2097152:      "Speak (Audio)",
  512:          "Stream (Video)",
  4194304:      "Mute Members",
  8388608:      "Deafen Members",
  16777216:     "Move Members",
  33554432:     "Use Voice Activity",
  256:          "Priority Speaker"
}

all_permissions = server_permissions
all_permissions.update(tc_permissions)
all_permissions.update(vc_permissions)

{
  1:            "Generate Invites",
  2:            "Kick Members", 
  4:            "Ban Members",
  8:            "Administrator",
  16:           "Manage Channels",
  32:           "Manage Server",
  64:           "Add Reactions",
  128:          "View Audit Logs",
  256:          "Priority Speaker",
  512:          "Stream (Video)",
  1024:         "View Channels",
  2048:         "Send Messages",
  4096:         "Send TTS Messages",
  8192:         "Manage Messages",
  16384:        "Embed Links",
  32768:        "Attach Files",
  65536:        "Read Message History",
  131072:       "Mention Everyone",
  262144:       "Use External Emojis",
  524288:       "View Server Insights",
  1048576:      "Connect to Voice",
  2097152:      "Speak (Audio)",
  4194304:      "Mute Members",
  8388608:      "Deafen Members",
  16777216:     "Move Members",
  33554432:     "Use Voice Activity",
  67108864:     "Change Nickname",
  134217728:    "Manage Nicknames",
  268435456:    "Manage Roles",
  536870912:    "Manage Webhooks",
  1073741824:   "Manage Emojis and Stickers",
  2147483648:   "Use Slash Commands",
  17179869184:  "Manage threads",
  34359738368:  "Create Public Threads",
  68719476736:  "Create Private Threads",
  137438953472: "Use External Stickers",
  274877906944: "Send Messages in Threads"
}