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
  "none"        : Permissions(0),
}