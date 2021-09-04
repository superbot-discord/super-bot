from discord.ext.commands import *
import discord

def botengrave(product : str, text : str):
  product = product.lower()
  product = product.replace(" ","")
  product = product.replace("-","")
  product = product.replace("_","")
  product = product.replace(".","")
  product = product.replace(",","")
  text = text.replace("%","%25")
  text = text.replace(" ","%20")
  text = text.replace("+","%2B")
  text = text.replace("/","%2F")
  text = text.replace(":","%3A")
  text = text.replace(";","%3B")
  text = text.replace("[","%5B")
  text = text.replace("]","%5D")
  text = text.replace("{","%7B")
  text = text.replace("}","%7D")
  text = text.replace("=","%3D")
  text = text.replace("|","%7C")
  text = text.replace("#","%23")
  text = text.replace("$","%24")
  text = text.replace("&","%26")
  text = text.replace("?","%3F")
  text = text.replace("@","%40")
  text = text.replace("^","%5E")
  text = text.replace("`","%60")
  if product == "airtag" or product == "airtags":
    embed = discord.Embed(title="Engrave on AirTags")
    embed.set_image(url="https://www.apple.com/hk/shop/preview/engrave/PX532AM/A?th=" + text + "&s=2&f=mixed")
  elif product == "airpodspro" or product == "airpodpro":
    embed = discord.Embed(title="Engrave on AirPods Pro")
    embed.set_image(url="https://www.apple.com/shop/preview/engrave/PWP22AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "airpodson" or product == "airpodon":
    embed = discord.Embed(title="Engrave on AirPods (On)")
    embed.set_image(url="https://www.apple.com/shop/preview/engrave/PRXJ2AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "airpods" or product == "airpod" or product == "airpodsoff" or product == "airpodoff":
    embed = discord.Embed(title="Engrave on AirPods")
    embed.set_image(url="https://www.apple.com/shop/preview/engrave/PV7N2AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "airpodsmaxgray" or product == "airpodmaxgray" or product == "airpodsmaxgrey" or product == "airpodmaxgrey" or product == "airpodsmaxspacegray" or product == "airpodmaxspacegray" or product == "airpodsmaxspacegrey" or product == "airpodmaxspacegrey" or product == "airpodsmax" or product == "airpodmax":
    embed = discord.Embed(title="Engrave on AirPods Max (Space Gray)")
    embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PGYH3AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "airpodsmaxsilver" or product == "airpodmaxsilver":
    embed = discord.Embed(title="Engrave on AirPods Max (Silver)")
    embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PGYJ3AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "airpodsmaxgreen" or product == "airpodmaxgreen":
    embed = discord.Embed(title="Engrave on AirPods Max (Green)")
    embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PGYN3AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "airpodsmaxblue" or product == "airpodmaxblue" or product == "airpodsmaxskyblue" or product == "airpodmaxskyblue":
    embed = discord.Embed(title="Engrave on AirPods Max (Sky blue)")
    embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PGYL3AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "airpodsmaxpink" or product == "airpodmaxpink":
    embed = discord.Embed(title="Engrave on AirPods Max (Pink)")
    embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PGYM3AM/A?th="+text+"&s=2&tl=&f=mixed")
  elif product == "ipadprogray" or product == "ipadprogrey" or product == "ipadpro" or product == "padpro":
    embed = discord.Embed(title="Engrave on iPad Pro (Space Gray)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PHP43LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PHP43LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadprosilver":
    embed = discord.Embed(title="Engrave on iPad Pro (Silver)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PHP53LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PHP53LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadgray" or product == "ipadgrey" or product == "padgray" or product == "padgrey" or product == "ipadspacegray" or product == "ipadspacegrey" or product == "padspacegray" or product == "padspacegrey" or product == "ipad" or product == "pad":
    embed = discord.Embed(title="Engrave on iPad (Space Gray)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYN72LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYN72LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadsilver" or product == "padsilver":
    embed = discord.Embed(title="Engrave on iPad (Silver)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYN82LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYN82LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadgold" or product == "ipadgolden" or product == "padgold" or product == "ipadgolden":
    embed = discord.Embed(title="Engrave on iPad (Gold)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYN92LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYN92LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadairgray" or product == "ipadairgrey" or product == "padairgray" or product == "padairgrey" or product == "ipadairspacegray" or product == "ipadairspacegrey" or product == "padairspacegray" or product == "padairspacegrey" or product == "ipadair" or product == "padair":
    embed = discord.Embed(title="Engrave on iPad Air (Space Gray)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYFM2LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYFM2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadairsilver" or product == "padairsilver":
    embed = discord.Embed(title="Engrave on iPad Air (Silver)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYFN2LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYFN2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadairrose" or product == "ipadairrosegold" or product == "padairrose" or product == "padairrosegold":
    embed = discord.Embed(title="Engrave on iPad Air (Rose Gold)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYFP2LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYFP2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadairgreen" or product == "padairgreen":
    embed = discord.Embed(title="Engrave on iPad Air (Green)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYFR2LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYFR2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadairblue" or product == "ipadairskyblue" or product == "padairblue" or product == "padairskyblue":
    embed = discord.Embed(title="Engrave on iPad Air (Sky Blue)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYFQ2LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PYFQ2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadminigray" or product == "ipadminigrey" or product == "padminigray" or product == "padminigrey" or product == "ipadminispacegray" or product == "ipadminispacegrey" or product == "padminispacegray" or product == "padminispacegrey" or product == "ipadmini" or product == "padmini":
    embed = discord.Embed(title="Engrave on iPad Mini (Space Gray)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PUQW2LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PUQW2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadminisilver" or product == "padminisilver":
    embed = discord.Embed(title="Engrave on iPad Mini (Silver)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PUQX2LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PUQX2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipadminigold" or product == "ipadminigolden" or product == "padminigold" or product == "padminigolden":
    embed = discord.Embed(title="Engrave on iPad Mini (Gold)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PUQY2LL/A?th="+text+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/engrave/PUQY2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipodgray" or product == "ipodgrey" or product == "podgray" or product == "podgrey" or product == "ipodspacegray" or product == "ipodspacegrey" or product == "podspacegray" or product == "podspacegrey" or product == "ipodtouchgray" or product == "ipodtouchgrey" or product == "podtouchgray" or product == "podtouchgrey" or product == "ipodtouchspacegray" or product == "ipodtouchspacegrey" or product == "podtouchspacegray" or product == "podtouchspacegrey" or product == "ipod" or product == "pod" or product == "ipodtouch" or product == "podtouch" :
    embed = discord.Embed(title="Engrave on iPod Touch (Space Gray)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHW2LL/A?th="+split[0]+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHW2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipodsilver" or product == "podsilver" or product == "ipodtouchsilver" or product == "podtouchsilver":
    embed = discord.Embed(title="Engrave on iPod Touch (Silver)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHV2LL/A?th="+split[0]+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHV2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipodgold" or product == "ipodgolden" or product == "podgold" or product == "podgolden" or product == "ipodtouchgold" or product == "ipodtouchgolden" or product == "podtouchgold" or product == "podtouchgolden":
    embed = discord.Embed(title="Engrave on iPod Touch (Gold)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHT2LL/A?th="+split[0]+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHT2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipodblue" or product == "podblue" or product == "ipodtouchblue" or product == "podtouchblue":
    embed = discord.Embed(title="Engrave on iPod Touch (Blue)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHU2LL/A?th="+split[0]+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHU2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipodpink" or product == "podpink" or product == "ipodtouchpink" or product == "podtouchpink":
    embed = discord.Embed(title="Engrave on iPod Touch (Pink)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHY2LL/A?th="+split[0]+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHY2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "ipodred" or product == "podred" or product == "ipodtouchred" or product == "podtouchred":
    embed = discord.Embed(title="Engrave on iPod Touch (Red)")
    split = text.splitlines()
    if len(split) == 1:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHX2LL/A?th="+split[0]+"&tl=&s=2")
    else:
      embed.set_image(url="https://www.apple.com/shop/preview/v2/engrave/PVHX2LL/A?th="+split[0]+"&tl="+split[1]+"&s=2")
  elif product == "pencil" or product == "pencil2":
    embed = discord.Embed(title="Engrave on Apple Pencil (2nd generation)")
    embed.set_image(url="https://www.apple.com/shop/preview/engrave/PU8F2AM/A?th="+text+"&s=2&tl=")
  elif product == "list" or product == "product" or product == "help" or product == "products":
    embed = discord.Embed(title="List of products")
    embed.add_field(name="AirPods/Accesories", value="`airpods` `airpodson` `airpodspro` `pencil` `airtag`", inline=False)
    embed.add_field(name="AirPods Max", value="`airpodsmax` `airpodsmaxgray` `airpodsmaxsilver` `airpodsmaxpink` `airpodsmaxgreen` `airpodsmaxblue`", inline=False)
    embed.add_field(name="iPad/iPad Mini", value="`ipadmini` `ipadminigray` `ipadminisilver` `ipadminigold`", inline=False)
    embed.add_field(name="iPad Pro", value="`ipadpro` `ipadprogray` `ipadprosilver`", inline=False)
    embed.add_field(name="iPad Air", value="`ipadair` `ipadairgray` `ipadairsilver` `ipadairrose` `ipadairgreen` `ipadairblue`", inline=False)
    embed.add_field(name="iPod Touch", value="`ipod` `ipodgray` `ipodsilver` `ipodgold` `ipodred` `ipodpink` `ipodblue`", inline=False)
    
  else:
    embed = discord.Embed(title="Invalid product", description="")
  return embed
