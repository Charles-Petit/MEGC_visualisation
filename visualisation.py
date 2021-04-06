from PIL import Image, ImageDraw
import os.path
import os
import psutil

class Micro_xpr:
    def __init__(self,start,stop,path,points):
        self.start = start
        self.stop = stop
        self.path = path
        self.points = points #liste de couples, chaque couples = coords du point d'intieret de la frame i
 
    def rectangle(self,p):
        r = 50
        return [(p[0]+r,p[1]+r),(p[0]-r,p[1]+r),(p[0]-r,p[1]-r),(p[0]+r,p[1]-r),(p[0]+r,p[1]+r)]
    
    def show_one(self,image_file,rect):
        image = Image.open(self.path + '/' + image_file)
        draw = ImageDraw.Draw(image)
        if rect != []:
            draw.line(rect,fill = 'black', width=4)
        image.show()

    def file_to_int(self,file_name):
        l = (file_name.split('_'))[-1]
        s = (l.split('.'))[0]
        file_id = int(s)
        return file_id #le nom du fichier est prefixe + file_id


    def show_all(self):
        rectangles = [self.rectangle(point) for point in self.points]
        marge = 5 # nbre de frames supplémentaires visualisées
        for (path, dirs, files) in os.walk(self.path):
            file_list = files
        
        
        n = len(file_list)
        for i in range(len(file_list)):
            file_int = self.file_to_int(file_list[i])
            if file_int > self.start - marge and file_int < self.stop + marge: 
                if file_int >= self.start and file_int <= self.stop:
                    self.show_one(file_list[i],rectangles[file_int - self.start])
                else:
                    self.show_one(file_list[i],[]) #c'est pas une microxpr
                


micr = Micro_xpr(1917,1918,'1 ME',[(500,500),(550,500),(700,500)])

#micr.show_one('006_05582.jpg', [micr.rectangle(micr.points[0])])
micr.show_all()


