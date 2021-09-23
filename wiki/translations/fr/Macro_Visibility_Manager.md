# Macro Visibility Manager/fr
{{Macro/fr
|Name=Visibility_Manager
|Icon=Macro_Visibility_Manager.png
|Description=Utilisez-le pour gérer la visibilité des objets de document.<br/>Il existe 2 modes de fonctionnement: Afficher tout et Afficher les types.<br/>En mode Afficher les types (par défaut), vous ne voyez qu'une liste des types d'objets, par exemple Corps, Sketch, Pad, Extrude.<br/>Activer/désactiver l’un des types permet de définir la visibilité de tous les documents.
objets de ce type dans le document actif.<br/>En mode Afficher tout (appuyez sur la touche Maj tout en exécutant la macro), une case à cocher différente apparaît pour chaque objet de document, triés par ordre alphabétique.<br/>Vous pouvez activer ou désactiver l’affichage de chaque objet. visibilité individuelle.
|Author=TheMarkster
|Version=1.06
|Date=2020-06-18
|FCVersion=Tous
|Download=[https://www.freecadweb.org/wiki/images/c/c8/Macro_Visibility_Manager.png ToolBar Icon]
}}

## Description

Utilisez cette macro pour gérer la visibilité des objets de document par type ou individuellement.

## Script

Icône de la toolBar ![](images/Macro_Visibility_Manager.png )

**Macro\_Visibility\_Manager.FCMacro**


```python
# -*- coding: utf-8 -*-
"""
***************************************************************************
*   Copyright (c) 2019 <TheMarkster>                                 *
*                                                                         *
*   This file is a supplement to the FreeCAD CAx development system.      *
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU Lesser General Public License (LGPL)    *
*   as published by the Free Software Foundation; either version 2 of     *
*   the License, or (at your option) any later version.                   *
*                                                                         *
*   This software is distributed in the hope that it will be useful,      *
*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
*   GNU Library General Public License at http://www.gnu.org/licenses     *
*   for more details.                                                     *
*                                                                         *
*   For more information about the GNU Library General Public License     *
*   write to the Free Software Foundation, Inc., 59 Temple Place,         *
*   Suite 330, Boston, MA  02111-1307 USA                                 *
*                                                                         *
***************************************************************************
"""

"""
Visibility_Manager Macro

Use this to manage the visibility of document objects.

There are 2 modes of operation: Show All and Show Types.

In Show Types mode (the default) you only see a list of the types
of objects, e.g. Body, Sketch, Pad, Extrude.

Toggling one of the types off/on will set the visibility of all document
objects of that type in the active document.

In Show All mode (Press Shift key while executing the macro) you see 
a different checkbox for each and every document object, sorted
alphabetically.  You can toggle each object's visibility individually.

"""

__title__ = "Visibility_Manager"
__author__ = "TheMarkster"
__url__ = ""
__Wiki__ = "https://www.freecadweb.org/wiki/Macro_Visibility_Manager"
__date__ = "2020.06.18"
__version__ = 1.06

import FreeCAD
from PySide import QtCore, QtGui
import time

class Dlg(QtGui.QDialog):
    def __init__(self, bShowAll=False):
        QtGui.QDialog.__init__(self)
        self.types={} #dict of types
        self.showAll = bShowAll
        self.reload = False
        self.infoLabel = QtGui.QLabel()
        self.infoLabel.mousePressEvent = self.label_clicked
        if self.showAll:
            self.infoLabel.setText("Show All mode")
        else:
            self.infoLabel.setText("Show by Type mode")
        checkboxLayout = QtGui.QVBoxLayout()
        self.checkboxes = []
        widget = QtGui.QWidget() #will hold scroll area
        checkboxLayout = QtGui.QVBoxLayout()
        self.addCheckboxes(checkboxLayout)  
        widget.setLayout(checkboxLayout)

        #Scroll Area Properties
        scroll = QtGui.QScrollArea()
        scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setWidget(widget)
        vLayout = QtGui.QVBoxLayout()
        vLayout.addWidget(scroll)

        #buttons = QtGui.QDialogButtonBox(
        #    QtGui.QDialogButtonBox.Ok.__or__(QtGui.QDialogButtonBox.Cancel),
        #    QtCore.Qt.Horizontal, self)
        buttons = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok, QtCore.Qt.Horizontal,self)
        buttons.addButton(QtGui.QDialogButtonBox.Cancel)
        mode_button = buttons.addButton('Switch Mode', QtGui.QDialogButtonBox.ActionRole)
        mode_button.clicked.connect(self.label_clicked)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        buttons.setCenterButtons(True)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.infoLabel)
        layout.addLayout(vLayout)
        layout.addWidget(buttons)
        self.setLayout(layout)

    def label_clicked(self, event):
        self.reload = True
        self.close()
        QtGui.QApplication.processEvents()
        time.sleep(0.1)

    def addCheckboxes (self, cbLayout):
        objectList = FreeCAD.ActiveDocument.findObjects()
        objectList.sort(key=lambda x: x.Name, reverse=False)
        nameList = []
        for obj in objectList:
            if not self.nameInList(obj.Name, nameList):
                nameList.append(obj.Name)
                self.newType(obj.Name)

        all = QtGui.QCheckBox("All", self)
        all.setObjectName("all")
        all.toggled.connect(self.allToggled)
        cbLayout.addWidget(all)
        self.checkboxes = [all]
        for name in nameList:
            for nn in range(0,len(self.types[name])):
                objLabel = getattr(FreeCAD.ActiveDocument,self.types[name][nn]).Label
                objName = self.types[name][nn]
                if objLabel != objName and self.showAll:
                    ck = QtGui.QCheckBox(self.types[name][nn]+" ("+objLabel+")", self)
                else:
                    ck = QtGui.QCheckBox(objName,self)
                ck.setObjectName(objName)

                if getattr(FreeCAD.ActiveDocument,self.types[name][nn]).ViewObject.Visibility:
                    ck.setCheckState(QtCore.Qt.Checked)
                else:
                    ck.setCheckState(QtCore.Qt.Unchecked)
                if nn != 0 and not self.showAll:
                    ck.hide()
                cbLayout.addWidget(ck)
                self.checkboxes.append(ck)def addToTypes(self, typeName, name):
        self.types[typeName].append(name)

    def newType(self, typeName):
        self.types[typeName] = [typeName]def nameInList(self, name, nameList):
        """ check if name is in nameList
            e.g. name = "Extrude002"
            nameList = ["Extrude", "Extrude001", "Extrude002"...]
        """
        for nl in nameList:
            if nl in name and nl[:3] == name[:3]:
                self.addToTypes(nl,name)
                return True
        return False

    def allToggled(self):
        """all checkbox was toggled"""
        allState = self.checkboxes[0].checkState()
        for ii in range(1,len(self.checkboxes)):
            self.checkboxes[ii].setCheckState(allState)

    def accept(self):
        """user clicked Ok"""
        self.setWindowOpacity(0.85)
        self.infoLabel.setText("Working...")
        if self.showAll:
            for ii in range(1, len(self.checkboxes)):
                name = self.checkboxes[ii].objectName()
                state = self.checkboxes[ii].checkState()
            
                if state == QtCore.Qt.Checked:
                    obj = getattr(FreeCAD.ActiveDocument, name)
                    if not obj.ViewObject.Visibility:
                        obj.ViewObject.Visibility = True
                else:
                    obj = getattr(FreeCAD.ActiveDocument, name)
                    if obj.ViewObject.Visibility:
                        obj.ViewObject.Visibility = False
                QtGui.QApplication.processEvents()
                time.sleep(0.01)
        else: #show type mode
            for ii in range(1, len(self.checkboxes)):
                if not self.checkboxes[ii].isVisible():
                    continue
                name = self.checkboxes[ii].objectName()
                state = self.checkboxes[ii].checkState()
            
                if state == QtCore.Qt.Checked:
                    for n in self.types[name]:
                        obj = getattr(FreeCAD.ActiveDocument, n)
                        obj.ViewObject.Visibility = True
                else:
                    for n in self.types[name]:
                        obj = getattr(FreeCAD.ActiveDocument, n)
                        obj.ViewObject.Visibility = False
                QtGui.QApplication.processEvents()
                time.sleep(0.01)
        self.close()


showAll = False
modifiers = QtGui.QApplication.keyboardModifiers()
if modifiers == QtCore.Qt.ShiftModifier:
    showAll = True
if FreeCAD.ActiveDocument:
    dlg = Dlg(showAll)
    dlg.setWindowTitle("Visibility Manager v"+str(__version__))
    result = dlg.exec_()
    while dlg.reload:
        showAll = not dlg.showAll
        dlg = Dlg(showAll)
        dlg.setWindowTitle("Visibility Manager v"+str(__version__))
        result = dlg.exec_()
else:
    FreeCAD.Console.PrintWarning("Visibility Manager v"+str(__version__)+": no active document\n")
```

---
[documentation index](../README.md) > Macro Visibility Manager/fr
