# Macro Duplicate Selection/fr

 {{Macro/fr
|Name=Macro_Duplicate_Selection
|Description= Cette macro change le curseur de la souris en "ForbiddenCursor" si une sélection est dupliquée.
|Author=Mario52
|Version=00.00
|Date=2016-06-06
|FCVersion=0.16
|Download= [https://www.freecadweb.org/wiki/images/5/54/Macro_Duplicate_Selection.png Icon ToolBar]
}}

## Description

Cette macro change le curseur de la souris si une sélection est dupliquée. Sélectionnez vos objets dans la vue 3D , si une sélection est dupliquée le curseur de la souris change en \"ForbiddenCursor\" et reste dans cet état tan que la sélection est dupliquée.

Cette macro reste résidente.

## Utilisation

Lancez la macro , elle reste résidente en mémoire et active.

Sélectionnez vos objets dans la vue 3D , si une sélection est dupliquée le curseur de la souris change en \"ForbiddenCursor\" et reste dans cet état tan que la sélection est dupliquée.

## Script

**Macro\_Duplicate\_Selection.FCMacro**

Icon for the toolBar ![](images/Macro_Duplicate_Selection.png )

**Macro\_Duplicate\_Selection.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
import FreeCADGui
import PySide
from PySide import QtGui ,QtCore
from PySide.QtGui import *
from PySide.QtCore import *

__title__   = "Macro_Duplicate_Selection"
__author__  = "Mario52"
__url__     = "http://www.freecadweb.org/index-fr.html"
__version__ = "00.00"
__date__    = "06/06/2016"

__Help__    = "Start the macro select the object IN THE 3D VIEW the ForbiddenCursor stay if the selection is duplicate"

def selectionObject():
    sel = FreeCADGui.Selection.getSelection() 
    x  = []
    del x[:]
    for a in range(len(sel)):
       x.append(sel[a].Name)
    doublet = 0
    for i in range(len(sel)):
        for ii in range((i+1),len(sel)):
            if x[i] == x[ii]:
                doublet = 1
                break
    if doublet == 1:
        QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
#        FreeCAD.Console.PrintError("HELP "+sel[-1].Name+" duplicate selection"+"\n")
    else:
        QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

class SelObserver:
    def addSelection(self,doc,obj,sub,pnt):   # Selection
        selectionObject()
    def removeSelection(self,doc,obj,sub):    # Effacer l'objet salectionne
        selectionObject()
    def setPreselection(self, doc, obj, sub):
        selectionObject()
    def clearSelection(self,doc):             # Si clic sur l'ecran, effacer la selection
        selectionObject()
#    def setSelection(self,doc):               # Selection dans Combo View pour quitter la fonction
#        App.Console.PrintMessage("Fin Macro_Duplicate"+"\n")
#        QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
#        FreeCADGui.Selection.removeObserver(s)# desinstalle la fonction residente

s=SelObserver()
FreeCADGui.Selection.addObserver(s)    # installe la fonction en mode resident

}}

## Liens

La discussion sur le forum [Duplicate Objects when more than one face selected](http://forum.freecadweb.org/viewtopic.php?f=3&t=15994)




