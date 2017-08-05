import os
import json
from PIL import ImageFont, ImageDraw, Image
import random

class elizabeth_cat():
    def __init__(self):
        self.folder_path = os.path.abspath("elizabeth_the_third/pictures/")
        self.font_path = os.path.abspath("elizabeth_the_third/fonts/")

        # making a list of all images paths
        self.pictures = list()
        directory = os.listdir(self.folder_path)
        for file in directory:
            if file.endswith(".png"):
                abs_file_path = os.path.join(self.folder_path, file)
                self.pictures.append( [file, abs_file_path, dict()] )

        # loading text box coordinate to a dictionary
        json_path = os.path.join(self.folder_path, "text_area.json")
        with open(json_path, "r") as jFile:
            self.coords = json.load(jFile)
        for p in self.pictures:
            p[2] = self.coords[p[0]]




    def create_text(self, image_number, text, rand = False):
        pic = self.pictures[random.randint(0, len(self.pictures)-1)]
        if rand == False:
            pic = self.pictures[image_number % len(self.pictures)]
        image = Image.open(pic[1])
        draw = ImageDraw.Draw(image)
        fontsize = 1

        # finding text box dimensions
        textbox_width = pic[2]["w2"] - pic[2]["w1"]
        textbox_height = pic[2]["h2"] - pic[2]["h1"]

        # picking the font and the best font size
        fontfile = os.path.join(self.font_path,"arial.ttf")
        font = ImageFont.truetype(fontfile, fontsize)
        while font.getsize(text)[0] <= textbox_width \
            and font.getsize(text)[1] <= textbox_height:
            fontsize += 1
            font = ImageFont.truetype(fontfile, fontsize)
        fontsize -= 1
        font = ImageFont.truetype(fontfile, fontsize)

        # forcing text to start in the middle of the box
        starting_height = (pic[2]["h2"]+ pic[2]["h1"]- font.getsize(text)[1])/2
        starting_width = (pic[2]["w2"]+ pic[2]["w1"]- font.getsize(text)[0])/2
        txt_colour = (77, 195, 255, 255)
        draw.text((starting_width, starting_height), text, font=font, fill = txt_colour)

        image.save(os.path.abspath('elizabeth_the_third/tmp.png'))




    def delete_tmp(self):
        tmp_path = os.path.join(os.path.abspath("elizabeth_the_third/tmp.png"))
        if os.path.isfile(tmp_path):
            os.remove(tmp_path)
