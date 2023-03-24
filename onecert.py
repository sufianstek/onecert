from PIL import Image, ImageDraw, ImageFont

# insert name string
namecert='NUR SYIFA SUFIAN'

# load template
image = Image.open('template.jpg')
draw = ImageDraw.Draw(image)
color = 'rgb(0, 0, 0)'

# load font and size of the font
font = ImageFont.truetype('Lucida_Calligraphy_Font.otf', 150)
# get length of text
w= draw.textlength(namecert, font=font)

#location of the name string on vertical axis in pixels
height=730 
# put the text on the horizontal center of image
draw.text(((image.width)/2, height), namecert, fill=color, font=font) 
# save image to folder
image.save(namecert + '.jpg') 
