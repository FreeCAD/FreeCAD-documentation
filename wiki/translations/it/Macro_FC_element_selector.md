# Macro FC element selector/it

 {{Macro/it
|Name=Macro FC element selector
|Icon=Macro_FC_element_selector.png
|Translate=Macro FC element selector
|Description= Questa macro mostra tutti gli elementi di sotto il mouse.
|Author=HoWil
|Version=01.00
|Date=2016-12-26
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/0/07/Macro_FC_element_selector.png ToolBar Icon]
|SeeAlso=<img src=images/Macro_Mouse_over_cb.png style="width:Macro Mouse over cb](Macro_Mouse_over_cb.md) [24px">
}}

## Descrizione

Questa macro mostra tutti gli elementi sotto il mouse (verranno visualizzati anche tutti gli elementi coperti da altri elementi)


<div class="mw-translate-fuzzy">

## Utilizzo


</div>

Lanciare la macro

## Codice

ToolBar Icon ![](images/Macro_FC_element_selector.png )

**Macro FC element selector.FCMacro**


{{MacroCode|code=
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 22:29:29 2016

@author: HoWil
License: LGPL v 2.1

Concept:
 After starting the process by clicking on "Start here..." one can click into the 3D view to get all elements below the the cursor click.
 The found elements are then listed in a pulldown-menu.

Hint:
  Does not work with Part-Design-Next 'Part'-elements and childs of them in the tree.
"""

#==============================================================================
#
#==============================================================================
from PySide import QtGui, QtCore
import FreeCADGui
import FreeCAD
from pivy.coin import SoMouseButtonEvent


class element_selector():

# ========================================================
#  GUI
# ========================================================
    def __init__(self):

        self.dialog = None
        self.dialog = QtGui.QDialog()
        self.dialog.resize(500,150)
        self.dialog.setWindowTitle("Find all components and related objects below cursor click.")
 
        self.view = None
        self.root = None
        self.hm = None

        self.elements_list = []
        self.objects_list = []
        self.components_list = []
        self.element_selection_data = []

        self.element_selection = QtGui.QComboBox()
        self.element_selection.setToolTip("Lists all found components")
        self.element_selection.currentIndexChanged.connect(self.selection_manager)
        self.element_selection.setMinimumContentsLength = 40
        self.element_selection.setMinimumSize(300,30)
        self.element_selection.addItems(['Found elements will be listed here.'])
        self.element_selection.setEditable(False) # Set the combo-box not-editalbe
        
        self.get_click = QtGui.QPushButton("Start here before clicking on an object in the draw window.")
        self.get_click.clicked.connect(self.start_mouse_over_cb)
        
        cancle_button = QtGui.QDialogButtonBox(self.dialog)
        cancle_button.setOrientation(QtCore.Qt.Horizontal)
        cancle_button.setStandardButtons(QtGui.QDialogButtonBox.Close)

        
        grid = QtGui.QGridLayout()             #    rot, column, alignment
        grid.setSpacing(10)

        # Run
        grid.addWidget(self.get_click,              0, 0, 1, 1)
        # Elements
        grid.addWidget(self.element_selection,      1, 0, 1, 1)
        # Cancel
        grid.addWidget(cancle_button,                       2, 0, 1, 1)

        self.dialog.setLayout(grid)

        QtCore.QObject.connect(cancle_button, QtCore.SIGNAL("rejected()"), self.close)

        QtCore.QMetaObject.connectSlotsByName(self.dialog)
        self.dialog.show()
        self.dialog.exec_()
        
    def start_mouse_over_cb(self):
        self.element_selection.clear() # Clear all elements in the combo-box
        self.element_selection.setEditable(True) # Set the combo-box editalbe
        self.view = FreeCADGui.ActiveDocument.ActiveView

        view = FreeCADGui.ActiveDocument.ActiveView.getViewer()
        root = view.getSceneGraph()
        hm = root.highlightMode.getValue() # store the original highlightMode
        root.highlightMode.setValue(2) # switch highlightMode off
        self.root = root
        self.hm = hm
        
        self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.mouse_over_cb)
        
        
    def mouse_over_cb(self, event_callback):
        event = event_callback.getEvent()
        
        if event.getState() == SoMouseButtonEvent.DOWN:
            pos = event.getPosition().getValue()

            element_list = FreeCADGui.ActiveDocument.ActiveView.getObjectsInfo((int(pos[0]), int(pos[1])))
            FreeCADGui.Selection.clearSelection()
            
            self.element_selection.clear() # clear pull down dialog
            self.element_selection_data = []
        
            self.elements_list = element_list # store all elements found
            
            self.objects_list = [] # reset objects_list
            self.components_list = [] # restet components_list
            
            if element_list: # if there were elements found
            
                FreeCAD.Console.PrintMessage("\n *** Elements found under mouse pointer (Part-Desing-Next- 'Parts' do not work yet!) ***\n")
                
                for e in element_list:
                    label_object = str(e["Object"])
                    label_component = str(e["Component"])
                    label_object_plus_component = label_object + ' - ' + label_component

                    if label_object not in self.element_selection_data:
                        self.objects_list.append(e["Object"])
                        self.components_list.append(None)
                        
                        FreeCAD.Console.PrintMessage(" " + str(label_object) + "\n")
                        
                        self.element_selection.addItem(label_object)
                        self.element_selection_data.append(label_object)
                    
                    if label_object_plus_component not in self.element_selection_data:
                        self.objects_list.append(e["Object"])
                        self.components_list.append(e["Component"])
                            
                        FreeCAD.Console.PrintMessage(" " + str(label_object_plus_component) + "\n")
        
                        self.element_selection.addItem(label_object_plus_component)
                        self.element_selection_data.append(label_object_plus_component)
                        
        
        self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)    
        
        self.root.highlightMode.setValue(self.hm) # restore the original highlightMode
        FreeCADGui.Selection.clearSelection()

        self.element_selection.removeItem(self.element_selection.findText('tmp'))

#==============================================================================
# Highligthing the choice from GUI
#==============================================================================
    def selection_manager(self):
        try:
            FreeCADGui.Selection.clearSelection()
            if self.element_selection.isEditable():
                sel_index = self.element_selection.currentIndex()
                
                if self.components_list[sel_index] == None :
                    # An object was selected in combobox
                    FreeCADGui.Selection.addSelection(FreeCAD.ActiveDocument.getObject(self.objects_list[sel_index]))
                else:
                    # An element of an object was selected in combobox
                    FreeCADGui.Selection.addSelection(FreeCAD.ActiveDocument.getObject(self.objects_list[sel_index]), self.components_list[sel_index])

        except:
            FreeCAD.Console.PrintError("Unable to complete the element selection/highlighting.\n")
            self.close()

    def close(self):
        self.dialog.hide()

element_selector()
}}

## Vincolo

Discussione sul foro [Selecting internal faces of a pressure vessel](https://forum.freecadweb.org/viewtopic.php?f=18&t=12381&p=151950#p151950)

Altra similare macro [Macro Mouse over cb](Macro_Mouse_over_cb.md)
