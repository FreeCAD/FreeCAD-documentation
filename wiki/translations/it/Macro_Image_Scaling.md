# Macro Image Scaling/it
{{Macro/it
|Name=Image Scaling
|Icon=Image_Scaling.svg
|Translate=Scala immagine
|Description=Scala i disegni
|Author=JAndersM
|Version=1.0
|Date=2016-01-19
|FCVersion=0.17 and below
|Download=[https://www.freecadweb.org/wiki/images/0/05/Image_Scaling.svg ToolBar Icon]
}}

## Descrizione

Macro per scalare disegni, grafici, schemi, modelli e immagini 2D simili nell\'ambiente Immagine. Funziona per figure importate come immagini planari nello spazio 3D.

Notare: Per le foto di oggetti o immagini coinvolgenti oggetti giacenti a distanze diverse dal punto di vista,, si deve tenere presente l\'effetto di [Parallasse](https://en.wikipedia.org/wiki/Parallax) (distorsione dovuta a \"differenza nella posizione apparente di un oggetto osservato lungo due diverse linee di vista\"). Nello schema seguente i 2 oggetti blu sono complanari con il piano perpendicolare al punto di vista dell\'utente e possono essere scalati:

![](images/Perspective.png )

Nella seconda figura, gli oggetti rossi e verdi non sono complanari con i 2 oggetti blu e quindi non possono essere scalati. Inoltre, con un solo punto di vista dell\'utente non si può stabilire con certezza che l\'oggetto rosso è complanare con 1 oggetto blu:

![](images/Parallax.jpg )

## Utilizzo

-   avviare la Macro - appare un dialogo
-   cliccare nell\'immagine sui due punti di cui si conosce la vera distanza
-   Selezionare il piano dell\'immagine nella vista ad albero
-   Inserire in mm la vera distanza tra i punti nel campo di testo del dialogo e fare clic su OK
-   L\'immagine viene ridimensionata e il dialogo si chiude.

## Script

ToolBar Icon ![](images/Image_Scaling.svg )

**Macro_Image_Scaling.FCMacro**


{{MacroCode|code=

import FreeCADGui, FreeCAD, Part
import math
import pivy.coin as pvy
from PySide import QtCore, QtGui
import DraftTrackers, Draft

__title__   = "Macro Image Scaling"
__author__  = "JAndersM"
__url__     = "http://www.freecadweb.org/index-fr.html"
__version__ = "00.01"
__date__    = "19/01/2016"

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

def distance(p1,p2):
    dx=p2[0]-p1[0]
    dy=p2[1]-p1[1]
    dz=p2[2]-p1[2]
    return math.sqrt(dx*dx+dy*dy+dz*dz)
    
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.stack = []
        self.callback = self.view.addEventCallbackPivy(pvy.SoMouseButtonEvent.getClassTypeId(),self.getpoint)
        self.callmouse=self.view.addEventCallbackPivy(pvy.SoLocation2Event.getClassTypeId(),self.getmousepoint)
        self.distance=0
        self.dialog=Dialog
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        Dialog.resize(300, 102)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 70, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel.__or__(QtGui.QDialogButtonBox.Ok))
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.buttonBox.button(QtGui.QDialogButtonBox.Ok).setEnabled(False)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 10, 113, 29))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label1 = QtGui.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(20, 45, 260, 17))
        self.label1.setObjectName(_fromUtf8("label1"))
        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.tracker = DraftTrackers.lineTracker(scolor=(1,0,0))
        self.tracker.raiseTracker()
        self.tracker.on()
        self.dialog.show()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Distance", None))
        self.label1.setText(_translate("Dialog", "Select first point", None))
        
    def accept(self):
        sel = FreeCADGui.Selection.getSelection()
        try:
            locale=QtCore.QLocale.system()
            d, ok = locale.toFloat(self.lineEdit.text())
            if not ok:
                raise ValueError
            s=d/self.distance
            sel[0].XSize.Value=sel[0].XSize.Value*s
            sel[0].YSize.Value=sel[0].YSize.Value*s
            FreeCAD.Console.PrintMessage("Scale="+str(s))
            self.tracker.off()
            self.tracker.finalize()
            self.dialog.hide()
        except (ValueError, ZeroDivisionError) as e:
            self.label1.setText(_translate("Dialog", "<font color='red'>Enter distance</font>", None))
            return
        except (IndexError, AttributeError) as e:
            self.label1.setText(_translate("Dialog", "<font color='red'>Select ImagePlane</font>", None))
            return
        
    def reject(self):
        self.stack=[]
        self.view.removeEventCallbackPivy(pvy.SoMouseButtonEvent.getClassTypeId(),self.callback)
        self.view.removeEventCallbackPivy(pvy.SoLocation2Event.getClassTypeId(),self.callmouse)
        self.tracker.off()
        self.tracker.finalize()
        self.dialog.hide()def getmousepoint(self, event_cb):
        event = event_cb.getEvent()
        if len(self.stack)==1:
            pos = event.getPosition()
            point = self.view.getPoint(pos[0],pos[1])
            self.tracker.p2(point)
               
    def getpoint(self,event_cb):
        event = event_cb.getEvent()           
        if event.getState() == pvy.SoMouseButtonEvent.DOWN:
            pos = event.getPosition()
            point = self.view.getPoint(pos[0],pos[1])
            self.stack.append(point)
            self.label1.setText(_translate("Dialog", "Select second point", None))
            if len(self.stack)==1:
                self.tracker.p1(point)
            elif len(self.stack) == 2:
                self.distance=distance(self.stack[0], self.stack[1])
                self.tracker.p2(point)
                self.view.removeEventCallbackPivy(pvy.SoMouseButtonEvent.getClassTypeId(),self.callback)
                self.view.removeEventCallbackPivy(pvy.SoLocation2Event.getClassTypeId(),self.callmouse)
                self.buttonBox.button(QtGui.QDialogButtonBox.Ok).setEnabled(True)
                self.label1.setText(_translate("Dialog", "Select Image Plane and type distance", None))
                
#Init               
d = QtGui.QWidget()
ui = Ui_Dialog()
ui.setupUi(d)
        
}}

## Link

-   [La discussione nel forum](http://forum.freecadweb.org/viewtopic.php?f=22&t=13877)
-   [Download zip](http://forum.freecadweb.org/download/file.php?id=19542)
-   [Movie created by microelly2](https://youtu.be/2iFE40uHrA8)



---
⏵ [documentation index](../README.md) > Macro Image Scaling/it
