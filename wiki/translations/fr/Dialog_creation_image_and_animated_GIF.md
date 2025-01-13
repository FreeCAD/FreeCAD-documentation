# Dialog creation image and animated GIF/fr
## Introduction

Exemple de [création de boîte de dialogue](Dialog_creation/fr.md) avec [PySide](PySide/fr.md).

Dans cet exemple, l\'interface entière est définie en [Python](Python/fr.md). Bien que cela soit possible pour les petites interfaces, pour les interfaces plus importantes, il est recommandé de créer des fichiers **.ui** via Qt Designer et de les charger dans le programme.



## Fenêtre de dialogue avec image (QLabel) et GIF animé (QMovie) 


```python
import PySide
from PySide import QtGui ,QtCore
from PySide.QtGui import QPixmap, QMovie, QLabel
from PySide.QtCore import *
class MyLabelPatience():
    label = QtGui.QLabel()
    label.setText("<img src=" + path_Name_Image + "><b><center>Wait please</center> \n\n<center>i search the fonts !\n\n</center></b>")
    # center screen
    ecran = FreeCADGui.getMainWindow().frameGeometry()
    xF = 250; yF = 120
    xW = (ecran.width()/2) - (xF/2)
    yW = (ecran.height()/2)- (yF/2)
    label.setGeometry(xW, yW, xF, yF)
    ####
    label.setStyleSheet("QLabel {background-color : #F0C300;font: 12pt; }");
    label.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint))        # pas de bords (not border)
    ### un-comment for use ###############
    movie = QtGui.QMovie(path_Name_Image)    # anime le fichier Gif anime (decommenter)
    label.setMovie(movie)
    movie.start()
    ##################

patience = MyLabelPatience().label
patience.show()                    #show the image
#patience.close()                   #close the Qlabel
#MyLabelPatience().movie.start()    #start the animation (after patience.show())
#MyLabelPatience().movie.stop()     #stop animation

```

![](images/Qlabel_Image00.png ) 
*Exemple QLabel avec image et texte.*

![](images/Qlabel_Image_Animee00.gif ) 
*Exemple QLabel avec GIF animé.*



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Dialog creation image and animated GIF/fr
