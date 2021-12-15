# Macro VisibleAlls/fr
{{Macro/fr
|Name=Macro VisibleAlls
|Icon=Macro_VisibleAlls.png
|Description=Cette macro affiche tous les objets du document (Visibility True).
|Author=Mario52
|Version=00.01
|Date=2015-11-12
|FCVersion=Toutes
|Download=[https://www.freecadweb.org/wiki/images/1/19/Macro_VisibleAlls.png Icône de la barre d'outils]
|SeeAlso=[Macro Toggle Visibility2 1-2](Macro_Toggle_Visibility2_1-2/fr.md)<br>[Macro Toggle Visibility2 2-2](Macro_Toggle_Visibility2_2-2/fr.md)<br>[Macro_Toggle_Visibility](Macro_Toggle_Visibility.md)<br>[Macro_HiddenAlls](Macro_HiddenAlls/fr.md)<br>[Macro If Selected Stay If Not Then Delete](Macro_If_Selected_Stay_If_Not_Then_Delete/fr.md)
}}

## Description

Cette macro affiche tous les objets du document (Visibility True).

## Script

Icône de la barre d\'outils <img alt="" src=images/Macro_VisibleAlls.png  style="width:64px;">

**Macro\_VisibleAlls.FCMacro**


```python
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
```

---
[documentation index](../README.md) > Macro VisibleAlls/fr
