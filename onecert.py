from PIL import Image, ImageDraw, ImageFont

# insert name string
namecert='ABDUL RAHMAN'

# load template
image = Image.open('template.jpg')
draw = ImageDraw.Draw(image)
color = 'rgb(0, 0, 0)'

# load font and size of the font
font = ImageFont.truetype('Lucida_Calligraphy_Font.otf', 150)
w, h = draw.textsize(namecert, font=font)

height=730 #location of the name string on vertical axis in pixels
draw.text(((image.width - w)/2, height), namecert, fill=color, font=font) # put the text on the image
image.save(namecert + '.jpg') # save it