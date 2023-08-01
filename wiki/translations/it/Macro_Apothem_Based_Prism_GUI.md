# Macro Apothem Based Prism GUI/it
{{Macro/it
|Name=Apothem Based Prism
|Translate=Prisma da apotema
|Icon=Part Prism Apothem.svg
|Description=Interfaccia grafica per creare un prisma basato sull'apotema (inraggio) inserita dall'utente.
|Author=Quick61
|Version=1.0
|Date=2014-12-31
|Download=[https://www.freecadweb.org/wiki/images/4/4e/Part_Prism_Apothem.svg ToolBar Icon]
|FCVersion=All
}}

## Descrizione

Questa macro apre una finestra di dialogo per fornire la distanza tra i centri, il numero di lati, altezza e crea un prisma basato sull\'apotema o raggio del cerchio inscritto in un poligono regolare. Essa può essere estremamente utile quando si conosce solo la distanza tra le facce. Per esempio, questi oggetti possono essere i contenitori esagonali di plastica o di metallo offerti dai fornitori. La maggior parte dei fornitori definisce le caratteristiche di questi prodotti indicando la distanza tra le facce. Se questi contenitori sono usati nei progetti, la macro può consentire un notevole risparmio di tempo.

## Utilizzo

Copiare la macro nella propria directory delle Macro di FreeCAD. Poi eseguire la macro dalla finestra di dialogo Esegui macro oppure creare un collegamento per utilizzarla dalla barra degli strumenti personalizzata.

Quando viene eseguita, la Macro presenta all\'utente la finestra di dialogo che si vede nella figura sottostante. Per prima cosa inserire la distanza che si vuole avere tra le facce. Per la distanza si può usare qualsiasi valore, anche decimale, ma non una frazione. Dopo, inserire il numero di lati. Questo numero deve essere un numero intero e deve essere un numero pari e per ottenere dei risultati soddisfacenti. Infine, inserire l\'altezza del prisma. Di nuovo, si può usare qualsiasi valore, anche decimale. Fare clic su OK per creare il prisma nel documento. ![](images/ABP_Screenshot.png )

## La Macro 

ToolBar Icon ![](images/Part_Prism_Apothem.svg )

**Macro_Apothem_Based_Prism_GUI.FCMacro**


{{MacroCode|code=
# # # # # # # # # # #
#
# Apothem Based Prism
#
# This script will take the input of the distance between flats, (apothem, aka inradius), 
# and the number of sidesfor a regular polygon along with a height and produce a 
# correctly sized prism derived from the circumradius.
#
# # # # # # # # # # #
 
import FreeCAD, FreeCADGui, Part, PartGui, math
from FreeCAD import Base
from PySide import QtGui, QtCore
from math import cos, radians
App = FreeCAD
Gui = FreeCADGui
 
class p():
 
 
    def priSm(self):
 
        try:
            dbf = float(self.d1.text())
            nos = int(self.d2.text())
            hth = float(self.d3.text())
            aR = dbf / 2
            op1 = 180/float(nos)
            coS = cos(math.radians(op1))
            cR = aR / coS
            prism=App.ActiveDocument.addObject("Part::Prism","Prism")
            prism.Polygon=nos
            prism.Circumradius=cR
            prism.Height=hth
            prism.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))
            prism.Label='Prism'
            App.ActiveDocument.recompute()
            Gui.SendMsgToActiveView("ViewFit")
        except:
            FreeCAD.Console.PrintError("Unable to complete task")
 
            self.close()
 
    def close(self):
        self.dialog.hide()
 
 
#
# Make dialog box and get input for distance between flats, number of sides, and height
#
 
    def __init__(self):
        self.dialog = None
 
        self.dialog = QtGui.QDialog()
        self.dialog.resize(280,110)
 
        self.dialog.setWindowTitle("Apothem Based Prism")
        la = QtGui.QVBoxLayout(self.dialog)
 
        iN1 = QtGui.QLabel("Distance Between Flats")
        la.addWidget(iN1)
        self.d1 = QtGui.QLineEdit()
        la.addWidget(self.d1)
 
        iN2 = QtGui.QLabel("Number Of Sides (Best results - use even numbers)")
        la.addWidget(iN2)
        self.d2 = QtGui.QLineEdit()
        la.addWidget(self.d2)
 
        iN3 = QtGui.QLabel("Prism Height")
        la.addWidget(iN3)
        self.d3 = QtGui.QLineEdit()
        la.addWidget(self.d3)
 
        okbox = QtGui.QDialogButtonBox(self.dialog)
        okbox.setOrientation(QtCore.Qt.Horizontal)
        okbox.setStandardButtons(QtGui.QDialogButtonBox.Cancel{{!}}

QtGui.QDialogButtonBox.Ok)

       la.addWidget(okbox)
       QtCore.QObject.connect(okbox, QtCore.SIGNAL("accepted()"), self.priSm)
       QtCore.QObject.connect(okbox, QtCore.SIGNAL("rejected()"), self.close)
       QtCore.QMetaObject.connectSlotsByName(self.dialog)
       self.dialog.show()
       self.dialog.exec_()

p() }}

## Altro

L\'icona SVG da usare per il collegamento nella barra degli strumenti personalizzata.

<img alt="" src=images/Part_Prism_Apothem.svg  style="width:128px;">

## Ringraziamenti

Un grazie al principale sviluppatore di FreeCAD [shoogen](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=765) e al programmatore di FreeCAD [wandererfan](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=1375) per il loro prezioso aiuto e consulenza nella costruzione di questo Macro.



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro Apothem Based Prism GUI/it
