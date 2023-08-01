# Macro ArrayCopy/cs
{{Macro/cs
|Name=ArrayCopy
|Icon=Macro_ArrayCopy.png
|Translate=ArrayCopy
|Description=Toto makro několikrát zkopíruje vybraný objekt do mřížkového pole
|Author=Yorik
|Version=1.0
|Date=2014-05-04
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/9/9d/Macro_ArrayCopy.png ToolBar Icon]
}}

## Deskriptivní

Toto makro několikrát zkopíruje vybraný objekt do mřížkového pole. Můžete definovat počet řádků a sloupců a vzdálenosti mezi nimi.

## Skript

ToolBar Icon ![](images/Macro_ArrayCopy.png )

**Macro_ArrayCopy.FCMacro**


{{MacroCode|code=

import FreeCAD, FreeCADGui, Part
from PySide import QtGui,QtCore
 
def proceed():
    try:
        u = (int(l1.text()),float(l2.text()))   
        v = (int(l3.text()),float(l4.text()))
    except:
        FreeCAD.Console.PrintError("Wrong input! Only numbers allowed...\n")
    sel = FreeCADGui.Selection.getSelection()
    if sel:
        sel = sel[0]
        name = sel.Name   
        shape = sel.Shape
        for column in range(u[0]):
            for row in range(v[0]):
                if (column != 0) or (row != 0):
                    delta = FreeCAD.Vector(column*u[1],row*v[1],0)   
                    newshape = sel.Shape.copy()
                    newshape.translate(delta)
                    newobject = FreeCAD.ActiveDocument.addObject("Part::Feature",name)
                    newobject.Shape = newshape
    else:
        FreeCAD.Console.PrintError("Error: One object must be selected")
    hide()
 
def hide():
    dialog.hide()
 
dialog = QtGui.QDialog()
dialog.resize(200,300)
dialog.setWindowTitle("Array")
la = QtGui.QVBoxLayout(dialog)
t1 = QtGui.QLabel("number of columns")
la.addWidget(t1)
l1 = QtGui.QLineEdit()
la.addWidget(l1)
t2 = QtGui.QLabel("distance between columns")
la.addWidget(t2)
l2 = QtGui.QLineEdit()
la.addWidget(l2)
t3 = QtGui.QLabel("number of rows")
la.addWidget(t3)
l3 = QtGui.QLineEdit()
la.addWidget(l3)
t4 = QtGui.QLabel("distance between rows")   
la.addWidget(t4)
l4 = QtGui.QLineEdit()
la.addWidget(l4)
okbox = QtGui.QDialogButtonBox(dialog)
okbox.setOrientation(QtCore.Qt.Horizontal)
okbox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
la.addWidget(okbox)
QtCore.QObject.connect(okbox, QtCore.SIGNAL("accepted()"), proceed)
QtCore.QObject.connect(okbox, QtCore.SIGNAL("rejected()"), hide)
QtCore.QMetaObject.connectSlotsByName(dialog)
dialog.show()

}}



---
⏵ [documentation index](../README.md) > Macro ArrayCopy/cs
