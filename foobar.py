#coding=utf-8
from PIL import Image
import os
#python 2.7
#using Pillow
#End
path = "."
dirs = os.listdir(path)

for i in dirs:
    if os.path.splitext(i)[1] == ".jpg":
        imload = Image.open(i);
        im = imload.convert("RGB")
        
        width = im.size[0] / 4
        height = im.size[1] / 4
        demo = open('Output.txt','a');

        for y in range(height):
            for x in range(width):
                r,g,b = im.getpixel((4*x,4*y))
                rgb =hex(r)+''+hex(g)+''+hex(b)
                demo.write('\t' + str(rgb))
            demo.write("\n")
        demo.write("End\n")
        demo.close()
