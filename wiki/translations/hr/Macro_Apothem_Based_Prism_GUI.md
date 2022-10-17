# Macro Apothem Based Prism GUI/hr
{{Macro
|Name=Apothem Based Prism
|Translate=Prizma utemeljena na apotemu
|Icon=Part Prism Apothem.svg
|Description=GUI dijalog koji stvara Apothem, (inradius) bazirani prizma od korisničkog unosa.
|Author=Quick61
|Version=1.0
|Date=2014-12-31
|Download=[https   *//www.freecadweb.org/wiki/images/4/4e/Part_Prism_Apothem.svg ToolBar Icon]
|FCVersion=All
}}

## Opis

Ova makronaredba će korisniku pružiti dijalog koji će pružiti udaljenost između centara, broj strana i visinu i stvorit će prizmu temeljenu na apothemu ili inradiusu poligona. To može biti vrlo zgodno kada se zna samo udaljenost između stanova. Primjer za to bi bila šesterokutna zaliha plastike ili metala koju pružaju dobavljači. Većina dobavljača takve dionice definiraju prema udaljenosti između stanova. Ako netko koristi takve zalihe u svojim projektima, ovaj makro može uštedjeti u stvarnom vremenu.

## Kako koristiti 

Kopirajte Makro u svoj FreeCAD Makro direktorij. Zatim pokrenite makronaredbu iz dijaloškog okvira Izvrši makronaredbu ili stvorite prečac za upotrebu s prilagođene alatne trake.

Kada se pokrene, Macro će korisniku predstaviti dijalog kao što je prikazano u nastavku. Najprije unesite željenu udaljenost između stanova. To može biti bilo koji broj i može sadržavati decimalnu vrijednost, neće uzeti djelomični unos. Zatim unesite broj strana. Ovaj broj je cijeli broj i trebao bi biti paran broj za odgovarajuće rezultate. Na kraju unesite visinu za koju želite da bude prizma. Opet, to može biti bilo koji broj i može sadržavati decimalnu vrijednost. Kliknite U redu i prizma će biti izrađena u vašem dokumentu. ![](images/ABP_Screenshot.png )

## Skripta

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
 
class p()   *
 
 
    def priSm(self)   *
 
        try   *
            dbf = float(self.d1.text())
            nos = int(self.d2.text())
            hth = float(self.d3.text())
            aR = dbf / 2
            op1 = 180/float(nos)
            coS = cos(math.radians(op1))
            cR = aR / coS
            prism=App.ActiveDocument.addObject("Part   *   *Prism","Prism")
            prism.Polygon=nos
            prism.Circumradius=cR
            prism.Height=hth
            prism.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))
            prism.Label='Prism'
            App.ActiveDocument.recompute()
            Gui.SendMsgToActiveView("ViewFit")
        except   *
            FreeCAD.Console.PrintError("Unable to complete task")
 
            self.close()
 
    def close(self)   *
        self.dialog.hide()
 
 
#
# Make dialog box and get input for distance between flats, number of sides, and height
#
 
    def __init__(self)   *
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

## Dodaci

SVG ikona za korištenje u prečacima prilagođene alatne trake.

<img alt="" src=images/Part_Prism_Apothem.svg  style="width   *128px;">

## Zahvale

Zahvaljujući glavnom programeru FreeCAD-a [shoogen](http   *//forum.freecadweb.org/memberlist.php?mode=viewprofile&u=765) and FreeCAD programmer [wandererfan](http   *//forum.freecadweb.org/memberlist.php?mode=viewprofile&u=1375) za njihovu neprocjenjivu pomoć i savjete u izradi ovog makroa.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Apothem Based Prism GUI/hr
