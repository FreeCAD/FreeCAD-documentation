# Dialog creation image and animated GIF/it
## Introduzione

Questo è un esempio di [creazione di dialoghi](Dialog_creation/it.md) con [PySide](PySide/it.md).

In questo esempio, l\'intera interfaccia è definita in [Python](Python/it.md). Sebbene ciò sia possibile per interfacce di piccole dimensioni, per le interfacce più grandi si raccomanda di creare i file **.ui** tramite Qt Designer e caricarli nel programma.

## Finestra di dialogo con immagine (QLabel) e GIF animate (QMovie) 


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
*Esempio di QLabel con immagine e testo.*

![](images/Qlabel_Image_Animee00.gif ) 
*Esempio di QLabel con GIF animate.*



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Dialog creation image and animated GIF/it
