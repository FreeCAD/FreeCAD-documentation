 {{Macro/cs
|Name=Remove parametric history
|Icon=Macro_Remove_parametric_history.png
|Translate=Remove parametric history
|Description=Odebere všechny parametrické asociace z objektu ponechajíc ho jako osamocené těleso
|Author=Yorik
|Version=0.1
|Date=2011-08-01
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/b/b7/Macro_Remove_parametric_history.png ToolBar Icon]
}}

## Popis

Odebere všechny parametrické asociace z objektu ponechajíc ho jako osamocené těleso

Před a po:

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




