# Macro Remove parametric history/it
{{Macro/it
|Name=Remove parametric history
|Icon=Macro_Remove_parametric_history.png
|Translate=Rimozione della cronologia
|Description=Questa operazione rimuove tutte le associazioni parametriche da un oggetto, lasciandolo come  ''muto''
|Author=Yorik
|Version=0.1
|Date=2011-08-01
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/b/b7/Macro_Remove_parametric_history.png ToolBar Icon]
}}

## Descrizione

Questa operazione rimuove tutte le associazioni parametriche da un oggetto, lasciandolo come *muto*.

Prima e dopo :

![](images/RPH_before.png )

![](images/RPH_after.png )

## Script

ToolBar Icon ![](images/Macro_Remove_parametric_history.png )

**Remove parametric history.FCMacro**


{{MacroCode|code=

originalObject = FreeCAD.ActiveDocument.ActiveObject
newShape = originalObject.Shape.copy()
newName = FreeCAD.ActiveDocument.ActiveObject.Name
FreeCAD.ActiveDocument.removeObject(newName)
newObject = FreeCAD.ActiveDocument.addObject("Part::Feature",newName)
newObject.Shape = newShape

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Remove parametric history/it
