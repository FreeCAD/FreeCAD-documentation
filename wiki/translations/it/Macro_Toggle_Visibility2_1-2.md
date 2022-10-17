# Macro Toggle Visibility2 1-2/it
{{Macro/it
|Name=Toggle Visibility2 1-2
|Translate=Commuta visibilità
|Icon=Macro SelectVisible2.png
|Description={{ColoredParagraph|DarkRed|Yellow|Questa macro lavora con '''Macro Toggle Visibility2 2-2'''}}<br/>Nasconde tutti gli oggetti selezionati.
|Author=openfablab
|Version=00.02b
|Date=2017-07-27
|FCVersion=All
|Download=[https   *//www.freecadweb.org/wiki/images/d/d7/Macro_SelectVisible2.png ToolBar Icon]
|SeeAlso=[Macro Toggle Visibility2 2-2](Macro_Toggle_Visibility2_2-2/it.md)<br/>[Macro_Toggle_Visibility](Macro_Toggle_Visibility/it.md)
}}

## Descrizione


{{ColoredText|Questa macro lavora con [Macro Toggle Visibility2 2-2](Macro_Toggle_Visibility2_2-2/it.md)}}

Questo è un insieme di tre macro correlate che servono per gestire la visibilità degli oggetti nella scheda Modello   *

1.  gli oggetti selezionati in un documento sono resi visibili, mentre gli oggetti che non sono stati selezionati vengono resi invisibili
    -   se non ci sono oggetti selezionati allora tutti gli oggetti sono nascosti
    -   se vengono selezionati tutti gli oggetti allora tutti gli oggetti vengono resi visibili
2.  rende visibili tutti gli oggetti

## Uso

Copiare le macro e le icone nella cartella delle macro ed eseguirle (vedere [Come installare le macro](How_to_install_macros/it.md))

## ToggleVisibility

Selezionare gli oggetti in una delle viste di FreeCAD. Questa macro rende visibili tutti gli oggetti selezionati e nasconde tutti gli oggetti non selezionati.

Se non ci sono oggetti selezionati tutti gli oggetti vengono nascosti

Se tutti gli oggetti sono nascosti e nella Vista Combinata non ci sono oggetti selezionati, rende visibili tutti gli oggetti

## Script 1 

ToolBar Icon <img alt="" src=images/Macro_SelectVisible2.png  style="width   *64px;">

**Macro_Toggle_Visibility2_1-2.FCMacro**


{{MacroCode|code=

import FreeCAD
# "Macro_Toggle_Visibility2_1-2" associate with "Macro_Toggle_Visibility2_2-2"
__title__="Macro_Toggle_Visibility2_1-2"
__author__ = "openfablab"
__url__     = "http   *//www.freecadweb.org/index-fr.html"
__version__ = "00.02b"
__date__    = "27/07/2017"
FreeCAD.actual=[]
try   * 
    compt = 0
    for ShapeNameObj in FreeCAD.ActiveDocument.Objects   *                                   # list alls objet for test if alls hidden
        if (FreeCADGui.ActiveDocument.getObject(ShapeNameObj.Name).Visibility == False) and (Gui.Selection.isSelected(ShapeNameObj) == False)   *
            compt += 1                                                                    # if hidden    * compt += 1
            #print "False    * ",ShapeNameObj.Name
        elif Gui.Selection.isSelected(ShapeNameObj) == False   *
            FreeCAD.actual.append(ShapeNameObj.Name)
            #print "Actual    * ",ShapeNameObj.Name
    if compt == len(FreeCAD.ActiveDocument.Objects)   *                                      # if (compt = Alls objects hidden) then Visibility = True
        for ShapeNameObj in FreeCAD.ActiveDocument.Objects   *
            FreeCADGui.ActiveDocument.getObject(ShapeNameObj.Name).Visibility = True      # Visibility = True
            #print "True     * ",ShapeNameObj.Name
        compt = 0
    else    *
        for ShapeNameObj in FreeCAD.ActiveDocument.Objects   *                               # hidde objects not selecteds
            if Gui.Selection.isSelected(ShapeNameObj) == False   *
                FreeCADGui.ActiveDocument.getObject(ShapeNameObj.Name).Visibility = False # if objects is not selected then Visibility = False (Hidden)
                #print "False    * ",ShapeNameObj.Name
            else   *
                FreeCADGui.ActiveDocument.getObject(ShapeNameObj.Name).Visibility = True  # if objects are hidden and selected then Visibility = True and hidden alls objects visibles
                #print "True     * ",ShapeNameObj.Name
except Exception   *
    None }}

## Script 2 

ToolBar <img alt="" src=images/Macro_VisibleAlls2.png  style="width   *64px;">

Seconda macro [Macro Toggle Visibility2 2-2](Macro_Toggle_Visibility2_2-2/it.md)

## Link

La discussione sul forum [Re   * Proposal   * select one or more pieces, hide the others.](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=13152&start=10#p184056)

Idea originale [Macro_Toggle_Visibility](https   *//www.freecadweb.org/wiki/index.php?title=Macro_Toggle_Visibility)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Toggle Visibility2 1-2/it
