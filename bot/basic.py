from shared import commands, Embed, ui

class InteractiveHelpL(ui.listener.Listener):
  @ui.Listener.select(custom_id= "interactive_help")
  async def interactive_help(self_, ctx: ui.SelectInteraction):
    await ctx.respond(embed= eval(ctx.selected_values[0]), hidden= True)

invite_embed = Embed(title= "Invite", description= "The bot can be invited [here](https://discord.com/api/oauth2/authorize?client_id=796686363604680755&permissions=8&scope=bot%20applications.commands).")
help_all = Embed(title= "SuperBot#4073 (ID:796686363604680755)", description= f"""**Prefix: **`=`
**Basic Commands**
`help` `inter_help` `support` `invite` `prefix` `ping` `botpurge`\n
**Discord Information Commands**
`server` `statuses` `invitelink` `role` `channel` `user` `avatar` `banner` `status` `leftuser` `message` `raw` `rawraw` `reactions` `emojiinfo` `sticker` `template`
`permissions` `badges` `stickers` `emojis` `led_server` `led2_server` `led3_server` `led4_server`\n
**Discord Commands**
`react` `snipe` `clearsnipe` `pretend` `pretendembed` `embed` `editembed` `simpleembed` `quickembed` `ett` `tts`\n
**Moderation Commands**
`kick` `ban` `unban` `slowmode` `purge` `purgeuser` `purgeregex` `purgepy` `purgepygex` `purgereactions` `makeinvite`\n
**Text Manipulation Commands**
`poll` `insert` `spoiler` `rawspoiler` `rawrawspoiler` `reverse` `emoji` `base` `encode` `decode` `length` `spellcheck` `case`\n
**Information Commands**
`color` `simplecolor` `translate` `definition` `unix` `time` `rtimer` `ttimer` `terminate` `unscramble` `unicode` `random` `choice` `raffle` `pick`\n
**Web Commands**
`redirect` `screenshot` `rss` `wiki` `wiki_search` `google` `youtube` `minecraft` `engrave` `covid` `population` `states` `map` `weather` `forecast` `gender`
`bird` `bunny` `cat` `dog` `duck` `fox` `kangaroo` `koala` `lizard` `panda` `raccoon`
Add `_fact` to each of the 11 animal commands above (e.g. `bird_fact`) to get a fun fact about the animal.
`dish` `nasa` `joke` `quote` `trivia` `shiba` `error` `errorcat` `errordog`\n
**Plot/Drawing Commands**
`ascii` `fonts` `table` `captcha` `graph` `bline` `bline2` `pie` `barh` `barv` `hist` `sankey` `snow` `mandelbrot`\n
**Developer Tools and Miscellaneous Commands**
`html` `md` `regex` `regsub` `button` `menu`\n
**Image Commands**
`analyse` `histogram` `resize` `rotate` `brightness` `contrast` `sharpen` `edge` `contour` `blur` `invert` `hue` `recolor`
To use the 13 commands above, type `=image ` first, then upload an image. Example: `=image analyse`. Supply a user name to work on his avatar, e.g. `=image SuperBot#4073 analyse`
`render` `lcd` `led` `led2` `led3` `led4` `led_bar` `ocr` `qr` `qrmake` `transparent` `text`\n
`hello` leads you to death\nNeed help? check the [documentation](https://superbot-website.vercel.app/Documentation)!""")

def help_menu_options(ctx):
  return [
    ui.SelectOption(label="All", description="Rough list of all commands",                                           value="help_all",    emoji=ctx.bot.get_emoji(891363286589780058)),
    ui.SelectOption(label="Basic", description="Fundamental commands, e.g. help, ping",                              value="help_basic",  emoji=ctx.bot.get_emoji(891363286661087272)),
    ui.SelectOption(label="Discord info", description="Discord information viewer, e.g. server. user",               value="help_dinfo",  emoji=ctx.bot.get_emoji(891363286656905246)),
    ui.SelectOption(label="Discord", description="Commands that interact with Discord, e.g. snipe",                  value="help_discord",emoji=ctx.bot.get_emoji(891363286761734264)),
    ui.SelectOption(label="Moderation", description="Commands to simplify server moderation, e.g. purge, makeinvite",value="help_mod",    emoji=ctx.bot.get_emoji(891363286786928650)),
    ui.SelectOption(label="Text", description="Have fun with your text, e.g. reverse, encode",                       value="help_text",   emoji=ctx.bot.get_emoji(891363286614949898)),
    ui.SelectOption(label="Information", description="Informative commands, e.g. color, unix",                       value="help_info",   emoji=ctx.bot.get_emoji(891363286694625342)),
    ui.SelectOption(label="Web", description="Commands that interact with the Internet, e.g. youtube, wiki",         value="help_web",    emoji=ctx.bot.get_emoji(891363286761734265)),
    ui.SelectOption(label="Plot", description="Commands to plot graphs, e.g. pie, bar",                              value="help_plot",   emoji=ctx.bot.get_emoji(891363286631743618)),
    ui.SelectOption(label="Developer", description="Developer-oriented commands, e.g. html, regex",                  value="help_dev",    emoji=ctx.bot.get_emoji(891363286665265183)),
    ui.SelectOption(label="Image", description="Image-editing or analysing commands, e.g. analyse, ocr",             value="help_img",    emoji=ctx.bot.get_emoji(891363286694625341)),
    ui.SelectOption(label="General Documentation", description="Quick links and documentation website",              value="help_general",emoji=ctx.bot.get_emoji(891363286078066749)),
  ]

help_basic = Embed(title="SuperBot Basic Commands", description=f"""
**help** Views a rough list of all commands.
**inter_help** Interactive version of `help` with fancy buttons.
**support** Shows you an invite to the support server.
**invite** Gets a link to invite the bot.
**prefix** Views the prefix of the bot (`=`).
**ping** Checks whether the bot is online and shows the latency.
**botpurge [Number]** Purges messages sent by the bot. Requires `Manage Messages`.
\nNeed help? check the [documentation](https://superbot-wevsite.vercel.app/Documentation/)!""")

help_dinfo = Embed(title="SuperBot Discord Information Commands", description=f"""
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
**rawraw** Views the escaped raw content of a message.
**reactions** Views information about the reactions of a message.
**emojiinfo** Views information about an emoji.
**template** Views information about a server template.\n
You need to supply arguments for most commands.
Need help? check the [documentation](https://superbot-wevsite.vercel.app/Documentation/)!""")

help_discord = Embed(title="SuperBot Discord Commands", description=f"""
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
Need help? check the [documentation](https://superbot-wevsite.vercel.app/Documentation/)!""")

help_mod = Embed(title="SuperBot Moderation Commands", description=f"""
**kick [User] {{Reason}}** Kicks a user. Bot and you need `Kick members`.
**ban [User] {{Days}} {{Reason}}** Bans a user and delete 0-7 (default: 0) days of messages. Bot and you need `Ban members`.
**unban [User] {{Reason}}** Unbans a user. Bot and you need `Ban members`.
**slowmode [Seconds] {{Channels}}** Sets the slowmode of several (default: current) channels.
**purge [No.]** Purges [No.] of the most recent message(s) in the same channel.¹
**purgeuser [No.] [User]** Purges [No.] of the most recent message(s) in the same channel.¹
**purgeregex [No.] [Regex]** Purges [No.] of the most recent message(s) based on a [regular expression](https://superbot-discord.github.io/Appendices/A2/).¹
**purgepy [No.] [Py. script]** Purges [No.] of the most recent message(s) based on a Python function.¹
**purgepygex** Purges [No.] of the most recent message(s) based on a regular expression and a Python function.¹
**purgereactions [No.]** Purges all reactions from [No.] of the most recent messages.¹
**makeinvite [Valid duration (secs)] {{Max. uses}}** Creates an invite link with a maximum number of uses (default: infinity). Bot and you need `Create invites`.\n
1: Bot and you need `Manage messages`.
Need help? check the [documentation](https://superbot-wevsite.vercel.app/Documentation/)!
""")

help_text = Embed(title="SuperBot Text Commands", description=f"""
**poll [Title] [Options]** Starts a poll. Example: `=poll Do you like pizza? Yes🍕 No😟`
**insert [Emoji] [Text]** Inserts an emoji. Example: `=insert 👏 This is a sentence.`
**spoiler [Text]** Turns each character of the text into a spoiler.
**rawspoiler [Text]** Copy-paste version of `=spoiler`.
**rawrawspoiler [Text]** Copy-paste version of `=rawspoiler`.
**reverse [Text]** Reverses a piece of text.
**emoji [Text]** Turns text into emojis. Supports alphabets and common symbols.
**base [x] [y] [Number]** Converts numbers from base-[x] to base-[y].
**encode [Algorithm] [Text]** Encodes the text in base-x, ascii caesar cipher and hashes.
**decode [Algorithm] [Text]** Encodes the text in base-x and ascii caesar cipher.
**length [Text]** Calculates the length of the text and analyses the most frequent characters.
**spellcheck [Word]** Spellchecks a word based on the QWERTY keyboard layout. 
**case [Text]** Converts the case (capitalization) of the text.
Need help? check the [documentation](https://superbot-wevsite.vercel.app/Documentation/)!
""")

help_info = Embed(title="SuperBot Information Commands", description=f"""
**color [Color]** Views information about a color. Supports Decimal, `R G B` and `#Hex`.
**simplecolor [Color]** Draws a color of gradient. Supports [these colors](https://raw.githubusercontent.com/johann-lau/Bot/main/Colours001.jpeg).
**translate [Language] [Text]** Translates the text into the [Language].
**definition [Word]** Looks up the word in a ditionary.
**unix [Time]** Converts the time into Discord timestamps.
**time {{Timezone}} Shows the time. Defaults to UTC+0.**
**rtimer [Duration] Starts a regional-indicator-based timer.**
**ttimer [Duration]** Starts a plain-text timer. Suitable for iOS devices.
**terminate [Timer ID]** Stops a timer.
**unscramble [Scrambled letters]** Unscrambles letters. Useful during a Scrabble game.
**unicode [Name/Hex/Char]** Searches for Unicode characters.
**random [L] [H]** Draws a random integer between [L] and [H].
**choice [Choices]** Draws an option out of choices. Example: `=choice Apple Banana Cherry`
**raffle [L] [H] [T]** Draws [T] random integer(s) betwene [L] and [H] in spoilers.
**pick [L] [H] [T]** Same as `=raffle`, but integers do not repeat.
Need help? check the [documentation](https://superbot-wevsite.vercel.app/Documentation/)!
""")

support_embed = Embed(title= "Support", description= f"""If you need support, please kindly 
join the support server or directly contact JohannLau#6541. Here are some links you might find useful:
""".replace(f"\n", " "))

support_buttons = [
  ui.LinkButton(label= "Support server", url= "https://discord.gg/RtRttctJYq"),
  ui.LinkButton(label= "Website", url= "https://superbot-website.vercel.app"),
  ui.LinkButton(label= "Documentation", url= "https://superbot-website.vercel.app/Documentation"),
]

@commands.command()
async def hello(ctx, *, disposed=None):
  embed = Embed(title= "Leaderboard", description= """We upload the leaderboard to YouTube
  every week. You can find the leaderboard [here](https://youtu.be/4spCNEPawyQ).""".replace(f"\n", ""))
  await ctx.reply(embed= embed)

@commands.command(aliases=["commands"])
async def help(ctx, *, cat= None):
  await ctx.reply(embed= help_all)

@commands.command(aliases=["inter_help", "interactive"])
async def interactive_help(ctx, *, disposed=None):
  await ctx.reply("Please select a category to continue.", components= [ui.SelectMenu(custom_id="interactive_help",
    options= help_menu_options(ctx), placeholder= "Select")], listener= InteractiveHelpL())

@commands.command()
async def invite(ctx, *, disposed=None):
  await ctx.reply(embed= invite_embed)

@commands.command()
async def prefix(ctx, *, disposed=None):
  await ctx.reply("The prefix for SuperBot is `=` (an equal sign).")

@commands.command(aliases=['supportserver', 'supports', 'johann', 'johannlau', 'supporting', 'team', 'dev', 'developer'])
async def support(ctx, *, disposed=None):
  await ctx.reply(embed= support_embed, components= support_buttons)

def setup(bot):
  bot.add_command(hello)
  bot.add_command(help)
  bot.add_command(interactive_help)
  bot.add_command(invite)
  bot.add_command(prefix)
  bot.add_command(support)