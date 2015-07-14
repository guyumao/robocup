#coding=utf-8
import os
from PIL import Image,ImageFont,ImageDraw
list_dir=os.listdir('./basic')
for i in list_dir:
    list_csv=os.listdir('./basic/'+i)
    for j in list_csv:
        print '\n',j,'\n'
        fileName=('./basic/'+i+'/'+j)
        print fileName
        f=file(fileName,'r')
        f_in=file("name.txt",'w')
        while True:
            line=f.readline()
            if len(line)==0:
                break
            print type(line),line,
            f_in.write(line[:-3]+'\n')
            name=line[:-3]
            fileN=name.replace(' ','_')+".jpg"
            os.system("cp 1.jpg "+fileN)
            print fileN
            image=Image.open(fileN)
            font=ImageFont.truetype("DroidSansFallbackFull.ttf",50)
            draw=ImageDraw.Draw(image)
            imagewidth,imageheight=image.size
            fontwidth,fontheight=draw.textsize(name,font)#-ImageFont.truetype().getoffset()
            draw.text(((imagewidth-fontwidth)/2,820),name,font=font,fill="#ffffff")
            image.save(fileN,"JPEG")
   #(imagewidth-fontwidth)/2 
        f.close()
        f_in.close()

        #os.system('./a.out')
        raw_input()
