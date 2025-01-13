# Macro ExpandTreeItem/it
{{Macro/it
|Name=Macro ExpandTreeItem
|Icon=Macro_ExpandTreeItem.svg
|Description=Questa macro espande l'albero selezionato e tutti i sottoalberi nella visualizzazione ad albero.<br/>Se non c'è alcuna selezione, tutti gli alberi vengono espansi.
|Author=wmayer, UR_
|Version=00.02
|Date=2019-07-25
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/9/94/Macro_ExpandTreeItem.svg ToolBar Icon]
}}



## Descrizione

Espande l\'albero selezionato e tutti i sottoalberi nella vista ad albero.

se l\'albero selezionato è già espanso, questo albero e tutti gli alberi secondari verranno compressi.

se non ci sono selezioni, tutti gli alberi vengono espansi.

![](images/Collapsed00.gif )



## Utilizzo

Copiare la macro nella directory macro, creare la barra degli strumenti e avviare la macro.

## Script

Icona della barra degli strumenti .PNG ![](images/Macro_ExpandTreeItem.png ) e .SVG ![](images/Macro_ExpandTreeItem.svg )

**Macro_ExpandTreeItem.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
#
# Expands selected tree and all sub trees in the tree view.
# if selected tree is already expanded this tree and all sub trees are collapsed True/False
# if there is no selection all trees are expanded
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



---
⏵ [documentation index](../README.md) > Macro ExpandTreeItem/it
