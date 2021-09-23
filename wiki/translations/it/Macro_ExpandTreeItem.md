# Macro ExpandTreeItem/it
 {{Macro/it
|Name=Macro ExpandTreeItem
|Translate=Macro ExpandTreeItem
|Description=Nella vista della struttura espande l'albero selezionato e tutti gli alberi secondari.
|Author=wmayer, UR_
|Version=00.00
|Date=2018-07-11
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/9/94/Macro_ExpandTreeItem.svg ToolBar Icon]
}}

## Descrizione

Espande l\'albero selezionato e tutti i sottoalberi nella vista ad albero.

se l\'albero selezionato è già espanso, questo albero e tutti gli alberi secondari vengono compressi

se non ci sono selezioni vengono compressi

![](images/Collapsed00.gif )


<div class="mw-translate-fuzzy">

## Uso


</div>

Copiare la macro nella directory macro, creare la barra degli strumenti e avviare la macro.

## Script

ToolBar Icon .PNG ![](images/Macro_ExpandTreeItem.png ) and the .SVG ![](images/Macro_ExpandTreeItem.svg )

**Macro\_ExpandTreeItem.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
#
# Expands selected tree and all sub trees in the tree view.
# if selected tree is already expanded this tree and all sub trees are collapsed True/False
# if there is no selection all trees are collapse False
#
__Title__    = "Macro ExpandTreeItem"
__Author__   = "wmayer, UR_"
__Version__  = "00.02"
__Date__     = "2019-07-25"

import PySide
from PySide import QtGui ,QtCore
from PySide.QtGui import *
from PySide.QtCore import *

def toggleAll(tree, item, collapse):
    if collapse == False:
        tree.expandItem(item)
    elif collapse == True:  
        tree.collapseItem(item)

    for i in range(item.childCount()):
        toggleAll(tree, item.child(i), collapse)

mw = Gui.getMainWindow()
trees = mw.findChildren(QtGui.QTreeWidget)

for tree in trees:
    items = tree.selectedItems()

    try:
        if items == []:
            #tree.selectAll()                          # select all object
            for obj in FreeCAD.ActiveDocument.Objects: # select obj.OutList
                if len(obj.OutList) != 0:
                    Gui.Selection.addSelection(obj)
                    items = tree.selectedItems()
            for item in items:
                toggleAll(tree, item, False)
    except Exception:
        None

    for item in items:
            if item.isExpanded() == True:
                toggleAll(tree, item, True)
        #            print ("collapsing")
            else:
                toggleAll(tree, item, False)
        #            print ("expanding")

}}

## Link

[Objektbaum mit einem Klick komplett aufklappen?](https://forum.freecadweb.org/viewtopic.php?f=13&t=29406)
