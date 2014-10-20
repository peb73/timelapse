from PIL import Image
import os
import sys
import time

#On determine le seuil
if len(sys.argv)<=1:
    seuil=15
else:
    seuil = int(sys.argv[1])

#On determine le path
if len(sys.argv)<=2:
    path="."
else:
    path = sys.argv[2]

for name in os.listdir(path):
    
    name = path+"/"+name
    if not (name.endswith(".jpg")):
        print "on ignore le ficher : "+name
        continue
    
    #On determine la luminosite
    my_liste = list(Image.open(name).convert("L").getdata())
    luminosite=0

    for elt in my_liste:
        luminosite+=elt

    luminosite = luminosite/len(my_liste)

    #On supprime le ficher
    if luminosite <= seuil :
        os.remove(name)
        print("On supprime le fichier : "+name+" avec la luminosite "+str(luminosite))
        continue
    else:
        print("On garde le fichier : "+name+" avec la luminosite "+str(luminosite))

