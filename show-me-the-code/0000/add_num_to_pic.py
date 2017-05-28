#!/usr/bin/env/python3
#coding:utf-8

from PIL import Image,ImageDraw,ImageFont

class Add_Num_to_Image(object) :
    def __init__(self,image_file):
        self.im=Image.open(image_file)
    def add_num(self):
        draw=ImageDraw.Draw(self.im)
        text_font=ImageFont.truetype('comsc.ttf',size=40)
        fill_color='#ff0000'
        im_width,im_height=self.im.size
        draw.text((im_width-160,0),'I love you',fill=fill_color,font=text_font)
        self.im.save('draw_done.jpg')

if __name__=='__main__' :
    Add_Num_to_Image('lutianaicai.jpg').add_num()

