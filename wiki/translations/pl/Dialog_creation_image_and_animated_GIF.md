# Dialog creation image and animated GIF/pl
## Wprowadzenie

To jest przykład [tworzenia dialogu](Dialog_creation/pl.md) z [PySide](PySide/pl.md).

W tym przykładzie cały interfejs jest zdefiniowany w środowisku [Python](Python/pl.md). Chociaż jest to możliwe w przypadku małych interfejsów, w przypadku większych interfejsów zaleca się tworzenie plików **.ui** za pomocą Qt Designer i ładowanie ich do programu.



## Okno dialogowe z obrazkiem *(QLabel)* i animowanym GIF-em *(QMovie)* 


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
*Przykład QLabel z obrazem i tekstem.*

![](images/Qlabel_Image_Animee00.gif ) 
*Przykład QLabel z animowanym GIF-em.*



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Dialog creation image and animated GIF/pl
