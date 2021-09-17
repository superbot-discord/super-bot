from PIL import Image, ImageOps
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