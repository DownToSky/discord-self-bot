import os
from PIL import ImageFont, ImageDraw, Image

def creat_text(image_folder_path, text):
    pass

image = Image.open('1.png')
draw = ImageDraw.Draw(image)
txt = "k\nk"
txt2 = "This is usually used to turn on optional font features that are not enabled by default, for example ‘dlig’ or ‘ss01’, but can be also used to turn off default font features for example ‘-liga’ to disable ligatures or ‘-kern’ to disable kerning. To get all supported features, see"
fontsize = 1

w1 = 48
h1 = 436
w2 = 633
h2 = 984
textbox_width = w2 - w1
textbox_height = h2 - h1

font = ImageFont.truetype("arial.ttf", fontsize)
while font.getsize(txt)[0] <= textbox_width \
    and font.getsize(txt)[1] <= textbox_height:
    fontsize += 1
    font = ImageFont.truetype("arial.ttf", fontsize)


font = ImageFont.truetype("arial.ttf", fontsize)

draw.text((w1, h1), txt, font=font)
image.save('tmp.png')