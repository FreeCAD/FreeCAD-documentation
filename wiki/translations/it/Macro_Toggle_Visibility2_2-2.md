# Macro Toggle Visibility2 2-2/it
{{Macro
|Name=Macro Toggle Visibility2 2-2
|translate=Macro Toggle Visibility2 2-2
|Icon=Macro_VisibleAlls2.png
|Description={{ColoredParagraph|DarkRed|Yellow|Questa macro lavora con '''Macro_Toggle_Visibility2_1-2'''}}<br/>Questa macro rende visibili tutti gli oggetti rispettando gli oggetti visibili e nascosti originali dopo l'uso di [Macro Toggle Visibility2 1-2](Macro_Toggle_Visibility2_1-2/it.md)
|Author=openfablab
|Version=00.02b
|Date=2017-07-27
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/e/ec/Macro_VisibleAlls2.png ToolBar Icon]
|SeeAlso=[Macro Toggle Visibility2 1-2](Macro_Toggle_Visibility2_1-2/it.md)<br/>[Macro Toggle Visibility](Macro_Toggle_Visibility/it.md)
}}

## Description


{{ColoredText|Uesta macro lavora con '''[Macro Toggle Visibility2 1-2](Macro_Toggle_Visibility2_1-2/it.md)'''}}

Questa macro rende visibili tutti gli oggetti rispettando gli oggetti visibili e nascosti originali dopo l\'uso di [Macro Toggle Visibility2 1-2](Macro_Toggle_Visibility2_1-2/it.md)

## Utilizzo

Copia le macro e le icone nelle macro delle cartelle ed esegui (vedi [Comme installare una macro](How_to_install_macros/it.md))

## Script

Questa macro rende visibili tutti gli oggetti rispettando gli oggetti visibili e nascosti originali dopo l\'uso di [Macro_Toggle_Visibility2_1-2](Macro_Toggle_Visibility2_1-2/it.md) macro.

ToolBar Icon <img alt="" src=images/Macro_VisibleAlls2.png  style="width:64px;">

**Macro_DisplayAllObjects2_2-2.FCMacro**


{{MacroCode|code=

import FreeCAD
#original name "Macro_VisibleAlls" pratical name "Macro_Toggle_Visibility2_2-2" "Macro_Toggle_Visibility2_1-2" associate with "Macro_Toggle_Visibility2_2-2"
__title__="Macro_DisplayAllObjects2_2-2"
__author__ = "openfablab"
__url__     = "http://www.freecadweb.org/index-fr.html"
__version__ = "00.00b"
__date__    = "27/07/2017"

try:
    for ShapeNameObj in FreeCAD.actual:   # displyed alls objects
        #print ShapeNameObj
        FreeCADGui.ActiveDocument.getObject(ShapeNameObj).Visibility = True
except Exception:
    None }}



---
⏵ [documentation index](../README.md) > Macro Toggle Visibility2 2-2/it
