from PIL import Image, ImageFilter, ImageOps, ImageDraw
from colorthief import ColorThief
from colorgram import extract
import colorsys

def addhue(degs):
  im = Image.open('input.png')
  pixels = im.load()
  for i in range(im.size[0]):
    for j in range(im.size[1]):
      a=pixels[i,j]
      b=colorsys.rgb_to_hsv(a[0]/255, a[1]/255, a[2]/255)
      c=colorsys.hsv_to_rgb(b[0]+degs/360,b[1],b[2])
      c1 = round(c[0]*255)
      c2 = round(c[1]*255)
      c3 = round(c[2]*255)
      d=(c1,c2,c3,a[3])
      pixels[i,j] = d
  im.save('output.png')

def invert():
  image = Image.open('input.png')
  if image.mode == 'RGBA':
    r,g,b,a = image.split()
    rgb_image = Image.merge('RGB', (r,g,b))
    inverted_image = ImageOps.invert(rgb_image)
    r2,g2,b2 = inverted_image.split()
    final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))
    final_transparent_image.save('output.png')
  else:
    inverted_image = ImageOps.invert(image)
    inverted_image.save('output.png')

def resize(x, y):
  image = Image.open('input.png')
  newimg = image.resize((x,y), Image.NEAREST)
  newimg.save('output1.png')
  newimg = image.resize((x,y), Image.BOX)
  newimg.save('output2.png')
  newimg = image.resize((x,y), Image.BILINEAR)
  newimg.save('output3.png')
  newimg = image.resize((x,y), Image.HAMMING)
  newimg.save('output4.png')
  newimg = image.resize((x,y), Image.BICUBIC)
  newimg.save('output5.png')
  newimg = image.resize((x,y), Image.LANCZOS)
  newimg.save('output6.png')

def blur(distance):
  image = Image.open('input.png')
  newimg = image.filter(ImageFilter.BoxBlur(distance))
  newimg.save('output1.png')
  newimg = image.filter(ImageFilter.GaussianBlur(distance))
  newimg.save('output2.png')

def rotate(degrees):
  image = Image.open('input.png')
  newimg = image.rotate(angle=degrees)
  newimg.save('output1.png')
  newimg = image.rotate(angle=degrees, expand=True)
  newimg.save('output2.png')

def analyse(scale):
  if scale > 5000:
    scale = 1000
  palette = extract('input.png', 15)
  palette.sort(key=lambda c: c.hsl.l)
  newimg = Image.new('RGB', (scale, round(scale/3)), (255, 255, 255))
  draw = ImageDraw.Draw(newimg)
  counter = 0
  for count in palette:
    draw.rectangle((counter, 0, counter+count.proportion*scale, round(scale/3)), (count.rgb.r, count.rgb.g, count.rgb.b))
    counter += count.proportion*scale
  newimg.save('output_lightness.png')

  palette.sort(key=lambda c: c.hsl.h)
  newimg = Image.new('RGB', (scale, round(scale/3)), (255, 255, 255))
  draw = ImageDraw.Draw(newimg)
  counter = 0
  for count in palette:
    draw.rectangle((counter, 0, counter+count.proportion*scale, round(scale/3)), (count.rgb.r, count.rgb.g, count.rgb.b))
    counter += count.proportion*scale
  newimg.save('output_hue.png')

  palette.sort(key=lambda c: c.proportion)
  newimg = Image.new('RGB', (scale, round(scale/3)), (255, 255, 255))
  draw = ImageDraw.Draw(newimg)
  counter = 0
  for count in palette:
    draw.rectangle((counter, 0, counter+count.proportion*scale, round(scale/3)), (count.rgb.r, count.rgb.g, count.rgb.b))
    counter += count.proportion*scale
  newimg.save('output_amount.png')

  dominant = ColorThief('input.png').get_color(quality=1)
  hexcode = f'#{((dominant[0] << 16) + (dominant[1] << 8) + dominant[2]):02x}'.upper()
  return hexcode