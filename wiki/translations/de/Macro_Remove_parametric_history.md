# Macro Remove parametric history/de

 {{Macro/de
|Name=Remove parametric history
|Icon=Macro_Remove_parametric_history.png
|Description=Dadurch wird die gesamte parametrische Assoziativität eines Objekts entfernt und bleibt als "dumme" Form erhalten
|Author=Yorik
|Version=0.1
|Date=2011-08-01
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/b/b7/Macro_Remove_parametric_history.png ToolBar Icon]
}}

## Beschreibung

Dadurch wird die gesamte parametrische Assoziativität eines Objekts entfernt und bleibt als \"dumme\" Form erhalten.

Vorher und nachher:

![](images/RPH_before.png )

![](images/RPH_after.png )

## Skript

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




