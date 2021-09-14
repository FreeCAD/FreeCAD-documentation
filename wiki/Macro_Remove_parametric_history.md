# Macro Remove parametric history

  {{Macro
|Name=Remove parametric history
|Icon=Macro_Remove_parametric_history.png
|Description=This will remove all parametric associativity from an object, leaving it as a "dumb" shape
|Author=Yorik
|Version=1.0
|Date=2011-08-01
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/b/b7/Macro_Remove_parametric_history.png ToolBar Icon]
}}

## Description

This will remove all parametric associativity from an object, leaving it as a \"dumb\" shape

Before and after:

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




