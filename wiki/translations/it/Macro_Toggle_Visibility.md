# Macro Toggle Visibility/it
<div class="mw-translate-fuzzy">


{{Macro/it
|Name=Toggle Visibility
|Translate=Visibilità oggetti
|Icon=Macro SelectVisible.png
|Description=Nasconde gli oggetti non selezionati e piu.
|Author=Mario52
|Version=00.02
|Date=2015-11-12|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/4/42/Macro_SelectVisible.png ToolBar Icon]
|SeeAlso=[Macro Toggle Visibility2 1-2](Macro_Toggle_Visibility2_1-2/it.md)<br>[Macro Toggle Visibility2 2-2](Macro_Toggle_Visibility2_2-2/it.md)<br>[Macro VisibleAlls](Macro_VisibleAlls/it.md)<br>[Macro HiddenAlls](Macro_HiddenAlls/it.md)<br>[Macro If Selected Stay If Not Then Delete](Macro_If_Selected_Stay_If_Not_Then_Delete/it.md)
}}


</div>


<div class="mw-translate-fuzzy">

## Descrizione

Questo è un insieme di tre macro correlate che servono per gestire la visibilità degli oggetti nella scheda Modello:

1.  gli oggetti selezionati in un documento sono resi visibili, mentre gli oggetti che non sono stati selezionati vengono resi invisibili
    -   se non ci sono oggetti selezionati allora tutti gli oggetti sono nascosti
    -   se vengono selezionati tutti gli oggetti allora tutti gli oggetti vengono resi visibili


</div>

Objects that are selected in a document are made visible while objects that are not selected are made invisible.

-   if no objects are selected then all objects are hidden
-   if all objects are selected then all objects are made visible


<div class="mw-translate-fuzzy">

## Uso

Copiare la macro e l\'icona nella cartella delle macro ed eseguirle (vedere [Come installare le macro](How_to_install_macros/it.md))


</div>

Copy the macro and the icon in your folder macros and run (see [How to install macros](How_to_install_macros.md))


<div class="mw-translate-fuzzy">

## ToggleVisibility

Selezionare gli oggetti in una delle viste di FreeCAD. Questa macro rende visibili tutti gli oggetti selezionati e nasconde tutti gli oggetti non selezionati.


</div>

Using the selection of objects in the one of the FreeCAD views, this macro makes all selected objects visible and hides all objects which are not selected.


<div class="mw-translate-fuzzy">

Se non ci sono oggetti selezionati tutti gli oggetti vengono nascosti


</div>


<div class="mw-translate-fuzzy">

Se tutti gli oggetti sono nascosti e nella Vista Combinata non ci sono oggetti selezionati, rende visibili tutti gli oggetti


</div>


<div class="mw-translate-fuzzy">

La nuova versione (00.02) comprende le tre macro in una


</div>

## Script

L\'icona per la vostra toolBar <img alt="" src=images/Macro_SelectVisible.png  style="width:48px;">

**Macro_ToggleSelectedObjectVisibility.FCMacro**


{{MacroCode|code=

import FreeCAD
# Macro_ToggleSelectedObjectVisibility
__title__="Macro_ToggleSelectedObjectVisibility"
__author__ = "Mario52"
__url__     = "http://www.freecadweb.org/index-fr.html"
__version__ = "00.02"
__date__    = "12/11/2015"

try:
    compt = 0
    for ShapeNameObj in FreeCAD.ActiveDocument.Objects:                                   # list alls objet for test if alls hidden
        if (FreeCADGui.ActiveDocument.getObject(ShapeNameObj.Name).Visibility == False) and (Gui.Selection.isSelected(ShapeNameObj) == False):
            compt += 1                                                                    # if hidden : compt += 1
            #print "False : ",ShapeNameObj.Name
    if compt == len(FreeCAD.ActiveDocument.Objects):                                      # if (compt = Alls objects hidden) then Visibility = True
        for ShapeNameObj in FreeCAD.ActiveDocument.Objects:
            FreeCADGui.ActiveDocument.getObject(ShapeNameObj.Name).Visibility = True      # Visibility = True
            #print "True  : ",ShapeNameObj.Name
        compt = 0
    else :
        for ShapeNameObj in FreeCAD.ActiveDocument.Objects:                               # hidde objects not selecteds
            if Gui.Selection.isSelected(ShapeNameObj) == False:
                FreeCADGui.ActiveDocument.getObject(ShapeNameObj.Name).Visibility = False # if objects is not selected then Visibility = False (Hidden)
                #print "False : ",ShapeNameObj.Name
            else:
                FreeCADGui.ActiveDocument.getObject(ShapeNameObj.Name).Visibility = True  # if objects are hidden and selected then Visibility = True and hidden alls objects visibles
                #print "True  : ",ShapeNameObj.Name
except Exception:
    None
}}


<div class="mw-translate-fuzzy">

## Link

La discussione nel forum [Proposal: select one or more pieces, hide the others.](http://forum.freecadweb.org/viewtopic.php?f=8&t=13152)


</div>

The discussion on the forum [Proposal: select one or more pieces, hide the others.](http://forum.freecadweb.org/viewtopic.php?f=8&t=13152)


<div class="mw-translate-fuzzy">

## Version

ver 00.02 12/11/2015 **macro Macro_SelectVisible** : hidden the objects not selected, if not object selected displayed all objects, hidden all objects. This version include the tree macro in one


</div>

ver 00.02 12/11/2015 **macro Macro_SelectVisible** : hidden the objects not selected, if not object selected displayed all objects, hidden all objects. This version include the tree macro in one



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro Toggle Visibility/it
