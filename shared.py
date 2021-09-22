import json

from discord import Permissions

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

server_permissions_raw = {
  1073741824: 8,
  536870912:  16,
  268435456:  1024,
  134217728:  32,
  67108864:   4,
  524288:     256,
  1024:       1,
  128:        512,
  32:         4096,
  16:         2048,
  8:          8192,
  4:          64,
  2:          128,
  1:          2
}

tc_permissions_raw = {
  274877906944: 268435456,
  137438953472: 2097152,
  68719476736:  134217728,
  34359738368:  67108864,
  17179869184:  33554432,
  2147483648:   16777216,
  262144:       1048576,
  131072:       262144,
  65536:        32768,
  32768:        8388608,
  16384:        4194304,
  8192:         16384,
  4096:         131072,
  2048:         65536,
  64:           524288
}

vc_permissions_raw = {
  33554432: 1073741824,
  16777216: 2147483648,
  8388608:  4294967296,
  4194304:  8589934592,
  2097152:  34359738368,
  1048576:  68719476736,
  512:      17179869184,
  256:      536870912
}

server_permissions = {
  8192: "Administrator",
  4096: "Manage Server",
  2048: "Manage Channels",
  1024: "Manage Roles",
  512:  "View Audit Logs",
  256:  "View Server Insights",
  128:  "Kick Members",
  64:   "Ban Members",
  32:   "Manage Nicknames",
  16:   "Manage Webhooks",
  8:    "Manage Emojis and Stickers",
  4:    "Change Nickname",
  2:    "Generate Invites",
  1:    "View Channels"
}

tc_permissions = {
  268435456: "Manage threads",
  134217728: "Embed Links",
  67108864 : "Create Private Threads",
  33554432 : "Create Public Threads",
  16777216 : "Use External Stickers",
  8388608  : "Send Messages in Threads",
  4194304  : "Use External Emojis",
  2097152  : "Read Message History",
  1048576  : "Use Slash Commands",
  524288   : "Attach Files",
  262144   : "Add Reactions",
  131072   : "Mention Everyone",
  65536    : "Send TTS Messages",
  32768    : "Send Messages",
  16384    : "Manage Messages",
}

vc_permissions = {
  68719476736: "Connect to Voice",
  34359738368: "Speak (Audio)",
  17179869184: "Stream (Video)",
  8589934592:  "Mute Members",
  4294967296:  "Deafen Members",
  2147483648:  "Move Members",
  1073741824:  "Use Voice Activity",
  536870912:   "Priority Speaker"
}

all_permissions = server_permissions
all_permissions.update(tc_permissions)
all_permissions.update(vc_permissions)

def trysubtract(original, *subtractors):
  for count in subtractors:
    cache = original - count
    if cache >= 0:
      original = cache
  return original

def server_itop(integer):
  cache1 = trysubtract(integer, 274877906944, 137438953472, 68719476736, 34359738368, 17179869184, 8589934592, 4294967296, 2147483648, 1073741824, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 512, 256, 64)
  cache2 = 0
  for count, count2 in server_permissions_raw.items():
    if cache1 > count:
      cache1 -= count
      cache2 += count2
  cache3 = ""
  for count, count2 in server_permissions.items():
    if cache2 > count:
      cache2 -= count
      cache3 += count2 + ", "
  if len(cache3) > 2:
    return cache3[:-2]
  else:
    return "No server permissions"

def vc_itop(integer):
  cache1 = trysubtract(integer, 274877906944, 137438953472, 68719476736, 34359738368, 17179869184, 8589934592, 4294967296, 2147483648, 1073741824, 536870912, 268435456, 134217728, 67108864, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 128, 64, 32, 16, 8, 4, 2, 1)
  cache2 = 0
  for count, count2 in vc_permissions_raw.items():
    if cache1 > count:
      cache1 -= count
      cache2 += count2
  cache3 = ""
  for count, count2 in vc_permissions.items():
    if cache2 > count:
      cache2 -= count
      cache3 += count2 + ", "
  if len(cache3) > 2:
    return cache3[:-2]
  else:
    return "No voice channel permissions"

def tc_itop(integer):
  cache1 = trysubtract(integer, 8589934592, 4294967296, 1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 1024, 512, 256, 128, 32, 16, 8, 4, 2, 1)
  cache2 = 0
  for count, count2 in tc_permissions_raw.items():
    if cache1 > count:
      cache1 -= count
      cache2 += count2
  cache3 = ""
  for count, count2 in tc_permissions.items():
    if cache2 > count:
      cache2 -= count
      cache3 += count2 + ", "
  if len(cache3) > 2:
    return cache3[:-2]
  else:
    return "No text channel permissions"



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
