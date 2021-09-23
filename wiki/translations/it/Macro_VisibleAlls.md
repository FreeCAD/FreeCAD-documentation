# Macro VisibleAlls/it
{{Macro/it
|Name=Macro VisibleAlls
|Icon=Macro_VisibleAlls.png
|Description=Questa macro mostra tutti gli oggetti del documento (Visibility True).
|Author=Mario52
|Version=00.01
|Date=2015-11-12
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/1/19/Macro_VisibleAlls.png ToolBar Icon]
|SeeAlso=[Macro_Toggle_Visibility2](Macro_Toggle_Visibility2/it.md)<br />[Macro_Toggle_Visibility](Macro_Toggle_Visibility/it.md)<br />[Macro HiddenAlls](Macro_HiddenAlls/it.md)<br />[Macro If Selected Stay If Not Then Delete](Macro_If_Selected_Stay_If_Not_Then_Delete/it.md)
}}

## Descrizione

Questa macro mostra tutti gli oggetti del documento (Visibility True).

## Script

ToolBar Icon <img alt="" src=images/Macro_VisibleAlls.png  style="width:64px;">

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
[documentation index](../README.md) > Macro VisibleAlls/it
