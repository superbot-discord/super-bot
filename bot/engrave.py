from shared import commands, Embed, SequenceMatcher
from urllib.parse import quote as urlescape


@commands.command() # Migrated, see apis__int.py
async def engrave(ctx, product = "list", *, text = "Your text goes here."):
  product = product.lower()
  text = urlescape(text, safe='')
  if product == "airtag" or product == "airtags":
    embed = Embed(title="Engrave on AirTags")
    embed.set_image(url="https://www.apple.com/shop/preview/engrave/PX532AM/A?th=" + text[:4] + "&s=2&f=mixed")
  elif product == "airpodspro" or product == "airpodpro":
    embed = Embed(title="Engrave on AirPods Pro")
    embed.set_image(url="https://www.apple.com/shop/preview/engrave/PLWK3AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "airpodson" or product == "airpodon":
    embed = Embed(title="Engrave on AirPods (2nd Gen)")
    embed.set_image(url="https://www.apple.com/shop/preview/engrave/PV7N2AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "airpods" or product == "airpod" or product == "airpodsoff" or product == "airpodoff":
    embed = Embed(title="Engrave on AirPods (3rd Gen)")
    embed.set_image(url="https://www.apple.com/shop/preview/engrave/PMTC3AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "airpodsmaxgray" or product == "airpodmaxgray" or product == "airpodsmaxgrey" or product == "airpodmaxgrey" or product == "airpodsmaxspacegray" or product == "airpodmaxspacegray" or product == "airpodsmaxspacegrey" or product == "airpodmaxspacegrey" or product == "airpodsmax" or product == "airpodmax":
    embed = Embed(title="Engrave on AirPods Max (Space Gray)")
    embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PGYH3AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "airpodsmaxsilver" or product == "airpodmaxsilver":
    embed = Embed(title="Engrave on AirPods Max (Silver)")
    embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PGYJ3AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "airpodsmaxgreen" or product == "airpodmaxgreen":
    embed = Embed(title="Engrave on AirPods Max (Green)")
    embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PGYN3AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "airpodsmaxblue" or product == "airpodmaxblue" or product == "airpodsmaxskyblue" or product == "airpodmaxskyblue":
    embed = Embed(title="Engrave on AirPods Max (Sky blue)")
    embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PGYL3AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "airpodsmaxpink" or product == "airpodmaxpink":
    embed = Embed(title="Engrave on AirPods Max (Pink)")
    embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PGYM3AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "ipadprogray" or product == "ipadprogrey" or product == "ipadpro" or product == "padpro":
    embed = Embed(title="Engrave on iPad Pro (Space Gray)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PHNF3LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PHNF3LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadprosilver":
    embed = Embed(title="Engrave on iPad Pro (Silver)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PHNG3LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PHNG3LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadgray" or product == "ipadgrey" or product == "padgray" or product == "padgrey" or product == "ipadspacegray" or product == "ipadspacegrey" or product == "padspacegray" or product == "padspacegrey" or product == "ipad" or product == "pad":
    embed = Embed(title="Engrave on iPad (Space Gray)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PK2K3LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PK2K3LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadsilver" or product == "padsilver":
    embed = Embed(title="Engrave on iPad (Silver)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PK2L3LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PK2L3LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadairgray" or product == "ipadairgrey" or product == "padairgray" or product == "padairgrey" or product == "ipadairspacegray" or product == "ipadairspacegrey" or product == "padairspacegray" or product == "padairspacegrey" or product == "ipadair" or product == "padair":
    embed = Embed(title="Engrave on iPad Air (Space Gray)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYFM2LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYFM2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadairsilver" or product == "padairsilver":
    embed = Embed(title="Engrave on iPad Air (Silver)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYFN2LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYFN2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadairrose" or product == "ipadairgold" or product == "ipadairrosegold" or product == "padairrose" or product == "padairrosegold":
    embed = Embed(title="Engrave on iPad Air (Rose Gold)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYFP2LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYFP2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadairgreen" or product == "padairgreen":
    embed = Embed(title="Engrave on iPad Air (Green)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYFR2LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYFR2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadairblue" or product == "ipadairskyblue" or product == "padairblue" or product == "padairskyblue":
    embed = Embed(title="Engrave on iPad Air (Sky Blue)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYFQ2LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYFQ2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif SequenceMatcher(None, product, 'ipadmini').ratio()>0.77 or SequenceMatcher(None, product, 'ipadminispace').ratio()>0.77 or SequenceMatcher(None, product, 'ipadminigray').ratio()>0.77:
    embed = Embed(title="Engrave on iPad Mini (Space Gray)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PK7T3LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PK7T3LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif SequenceMatcher(None, product, 'ipadministar').ratio()>0.77 or SequenceMatcher(None, product, 'ipadminiyellow').ratio()>0.77:
    embed = Embed(title="Engrave on iPad Mini (Starlight/Yellow)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PK7V3LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PK7V3LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif SequenceMatcher(None, product, 'ipadminipurple').ratio()>0.77:
    embed = Embed(title="Engrave on iPad Mini (Purple)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PK7X3LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PK7X3LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif SequenceMatcher(None, product, 'ipadminipink').ratio()>0.77:
    embed = Embed(title="Engrave on iPad Mini (Pink)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PLWR3LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PLWR3LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif SequenceMatcher(None, product, 'ipod').ratio()>0.75 or SequenceMatcher(None, product, 'ipodtouch').ratio()>0.75 or SequenceMatcher(None, product, 'ipodspace').ratio()>0.75 or SequenceMatcher(None, product, 'ipodgray').ratio()>0.75:
    embed = Embed(title="Engrave on iPod Touch (Space Gray)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHW2LL/A?th="+split[0]+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHW2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif SequenceMatcher(None, product, 'ipodsilver').ratio()>0.77 or SequenceMatcher(None, product, 'ipodtouchsilver').ratio()>0.77:
    embed = Embed(title="Engrave on iPod Touch (Silver)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHV2LL/A?th="+split[0]+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHV2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif SequenceMatcher(None, product, 'ipodgold').ratio()>0.77 or SequenceMatcher(None, product, 'ipodtouchgold').ratio()>0.77:
    embed = Embed(title="Engrave on iPod Touch (Gold)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHT2LL/A?th="+split[0]+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHT2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif SequenceMatcher(None, product, 'ipodblue').ratio()>0.77 or SequenceMatcher(None, product, 'ipodtouchblue').ratio()>0.77:
    embed = Embed(title="Engrave on iPod Touch (Blue)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHU2LL/A?th="+split[0]+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHU2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif SequenceMatcher(None, product, 'ipodpink').ratio()>0.77 or SequenceMatcher(None, product, 'ipodtouchpink').ratio()>0.77:
    embed = Embed(title="Engrave on iPod Touch (Pink)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHY2LL/A?th="+split[0]+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHY2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif SequenceMatcher(None, product, 'ipodred').ratio()>0.77 or SequenceMatcher(None, product, 'ipodtouchred').ratio()>0.77:
    embed = Embed(title="Engrave on iPod Touch (Red)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHX2LL/A?th="+split[0]+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHX2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "pencil" or product == "pencil2":
    embed = Embed(title="Engrave on Apple Pencil (2nd generation)")
    embed.set_image(url="https://www.apple.com/shop/preview/engrave/PU8F2AM/A?th="+text+"&s=2&tl=")
  elif product == "list" or product == "product" or product == "help" or product == "products":
    embed = Embed(title="List of products")
    embed.add_field(name="AirPods/Accesories", value="`airpods` `airpodson` `airpodspro` `pencil` `airtag`", inline= False)
    embed.add_field(name="AirPods Max", value="`airpodsmax` `airpodsmaxgray` `airpodsmaxsilver` `airpodsmaxpink` `airpodsmaxgreen` `airpodsmaxblue`", inline= False)
    embed.add_field(name="iPad/iPad Mini", value="`ipad` `ipadsilver` `ipadmini` `ipadminiyellow` `ipadminipurple` `ipadminipink`", inline= False)
    embed.add_field(name="iPad Pro", value="`ipadpro` `ipadprosilver`", inline= False)
    embed.add_field(name="iPad Air", value="`ipadair` `ipadairsilver` `ipadairrose` `ipadairgreen` `ipadairblue`", inline= False)
    embed.add_field(name="iPod Touch", value="`ipod` `ipodgray` `ipodsilver` `ipodgold` `ipodred` `ipodpink` `ipodblue`", inline= False)
  else:
    embed = Embed(title="Invalid product", description="")
  await ctx.reply(embed=embed)

def setup(bot):
  bot.add_command(engrave)