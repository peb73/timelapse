#import picamera
from PIL import Image
import os
import sys
import time

#on determine le seuil
if len(sys.argv)<=1:
    seuil=15
else:
    seuil = sys.argv[1]

#on determine le path
if len(sys.argv)<=2:
    path="."
else:
    path = sys.argv[2]

#on initialise la camera
camera = picamera.PiCamera()
camera.hflip = True
camera.vflip = True
camera.resolution(2592, 1944)

#on determine le nom du fichier
name = path+"/"+time.strftime('%y_%m_%d_%H_%M',time.localtime())+".jpg"

#on prend la photo
camera.capture(name)

#on determine la luminosite
my_liste = list(Image.open(name).convert("L").getdata())
i=0
luminosite=0

while i < len(my_liste):
    luminosite+=my_liste[i]
    i += 1

luminosite = luminosite/len(my_liste)

#on supprime le ficher
if luminosite<=seuil :
    os.remove(name)

