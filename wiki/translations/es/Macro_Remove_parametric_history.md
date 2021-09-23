# Macro Remove parametric history/es
{{Macro/es
|Name=Remove parametric history
|Icon=Macro_Remove_parametric_history.png
|Translate=Remove parametric history
|Description=Esta macro eliminará toda la asociatividad paramétrica de un objeto, dejándolo como una forma "tonta"
|Author=Yorik
|Version=0.1
|Date=2011-08-01
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/b/b7/Macro_Remove_parametric_history.png ToolBar Icon]
}}

## Descripción

Esta macro eliminará toda la asociatividad paramétrica de un objeto, dejándolo como una forma \"tonta\"

Antes y después de:

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
[documentation index](../README.md) > Macro Remove parametric history/es
