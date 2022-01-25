# Macro Align Working Plane to Camera/it
{{Macro/it
|Name=Macro Align Working Plane to Camera
|Icon=Macro_Align_Working_Plane_to_Camera.png
|Translate=Allinea il piano di lavoro alla camera
|Description=Questa macro sposta il corrente [Piano di lavoro di Draft](Draft_SelectPlane/it.md) al centro della vista corrente |Author=yorik
|Version=1.0
|Date=2017-05-10
|Download=[https://www.freecadweb.org/wiki/images/0/01/Macro_Align_Working_Plane_to_Camera.png ToolBar Icon]
|FCVersion=Tutte
|SeeAlso=[Macro Align Camera to Working Plane](Macro_Align_Camera_to_Working_Plane/it.md) [24px|Macro Align Camera to Working Plane](File:Macro_Align_Camera_to_Working_Plane.png.md)
}}

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Questa macro sposta il corrente [Piano di lavoro di Draft](Draft_SelectPlane/it.md) al centro della vista corrente. È utile quando si lavora abbastanza lontano dal centro della griglia.


</div>

## Usage


<div class="mw-translate-fuzzy">

## Uso

-   Spostare la vista nella zona in cui si desidera guardare
-   Eseguire la macro


</div>

## Script

ToolBar Icon ![](images/Macro_Align_Working_Plane_to_Camera.png )

**Macro\_Align\_Working\_Plane\_to\_Camera.FCMacro**


{{MacroCode|code=
import FreeCAD,FreeCADGui
cam = FreeCAD.Vector(FreeCADGui.ActiveDocument.ActiveView.getCameraNode().position.getValue().getValue())
pos = FreeCAD.DraftWorkingPlane.projectPoint(cam)
FreeCAD.DraftWorkingPlane.position = pos
FreeCADGui.Snapper.setGrid()
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Align Working Plane to Camera/it
