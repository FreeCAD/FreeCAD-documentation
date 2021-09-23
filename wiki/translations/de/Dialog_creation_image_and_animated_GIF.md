# Dialog creation image and animated GIF/de


## Einführung

Dies ist ein Beispiel für [Dialogerstellung](Dialog_creation/de.md) mit [PySide](PySide/de.md).

In diesem Beispiel ist die gesamte Oberfläche in [Python](Python/de.md) definiert. Obwohl dies für kleine Oberflächen möglich ist, wird für größere Oberflächen empfohlen, {{FileName|.ui}} Dateien mit Qt Designer zu erstellen und diese in das Programm zu laden. Siehe [Oberflächenerstellung mit UI Dateien](Interface_creation_with_UI_files.md).

## Dialog mit Bild (QLabel) und animiertem GIF (QMovie) 


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

![](images/Qlabel_Image00.png ) *Beispiel QLabel mit Bild und Text*

![](images/Qlabel_Image_Animee00.gif ) *Beispiel QLabel mit animiertem GIF*


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
