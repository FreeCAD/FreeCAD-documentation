# Macro VisibleAlls/fr

 {{Macro/fr
|Name=Macro VisibleAlls
|Icon=Macro_VisibleAlls.png
|Description=Cette macro affiche tous les objets du document (Visibility True).
|Author=Mario52
|Version=00.01
|Date=2015-11-12
|FCVersion=Toutes versions
|Download=[https://www.freecadweb.org/wiki/images/1/19/Macro_VisibleAlls.png ToolBar Icon]
|SeeAlso=[Macro_Toggle_Visibility2](Macro_Toggle_Visibility2/fr.md)<br />[Macro_Toggle_Visibility](Macro_Toggle_Visibility/fr.md)<br />[Macro Cache tous les Objets](Macro_HiddenAlls/fr.md)<br />[Macro Si sélectionné reste si non efface](Macro_If_Selected_Stay_If_Not_Then_Delete/fr.md)
}}

## Description

Cette macro affiche tous les objets du document (Visibility True).

## Script

ToolBar Icon <img alt="" src=images/Macro_VisibleAlls.png  style="width:64px;">

**Macro\_VisibleAlls.FCMacro**


{{MacroCode|code=
import FreeCAD
#Macro_VisibleAlls
__title__="Macro_DisplayAllObjects"
__author__ = "Mario52"
__url__     = "http://www.freecadweb.org/index-fr.html"
__version__ = "00.00"
__date__    = "11/11/2015"

try:
    for ShapeNameObj in FreeCAD.ActiveDocument.Objects:   # displyed alls objects
        #print ShapeNameObj.Name
        FreeCADGui.ActiveDocument.getObject(ShapeNameObj.Name).Visibility = True
except Exception:
    None
}}




