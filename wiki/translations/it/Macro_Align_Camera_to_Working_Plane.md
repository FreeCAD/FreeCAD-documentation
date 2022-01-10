# Macro Align Camera to Working Plane/it
{{Macro/it
|Name=Macro Align Camera to Working Plane
|Icon=Macro_Align_Camera_to_Working_Plane.png
|Translate=Allinea la camera al piano di lavoro
|Description=Questa macro allinea la fotocamera al corrente [Piano di lavoro di Draft](Draft_SelectPlane/it.md) |Author=yorik
|Version=0.1
|Date=2017-03-16
|Download=[https://www.freecadweb.org/wiki/images/f/fd/Macro_Align_Camera_to_Working_Plane.png ToolBar Icon]
|FCVersion=All
|SeeAlso=<img src=images/Macro_Align_Working_Plane_to_Camera.png style="width:Macro Align Working Plane to Camera](Macro_Align_Working_Plane_to_Camera/it.md) [24px"> 
}}

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Questa macro allinea la fotocamera al corrente [Piano di lavoro di Draft](Draft_SelectPlane/it.md)


</div>

## Usage


<div class="mw-translate-fuzzy">

## Utilizzo

-   Impostare il [Piano di lavoro di Draft](Draft_SelectPlane/it.md) desiderato
-   Eseguire la macro


</div>

## Script

ToolBar Icon ![](images/Macro_Align_Camera_to_Working_Plane.png )

**Macro\_Align\_Camera\_to\_Working\_Plane.FCMacro**


{{MacroCode|code=
import FreeCAD,FreeCADGui
c = FreeCADGui.ActiveDocument.ActiveView.getCameraNode()
r = FreeCAD.DraftWorkingPlane.getRotation().Rotation.Q
c.orientation.setValue(r)
}}

---
[documentation index](../README.md) > Macro Align Camera to Working Plane/it
