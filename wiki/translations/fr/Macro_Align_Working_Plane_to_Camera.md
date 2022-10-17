# Macro Align Working Plane to Camera/fr
{{Macro/fr
|Name=Macro Align Working Plane to Camera
|Icon=Macro_Align_Working_Plane_to_Camera.png
|Description=Cette macro déplace le [Plan courant](Draft_SelectPlane/fr.md) au centre de la vue 3D
|Author=yorik
|Version=1.0
|Date=2017-05-10
|Download=[https   *//www.freecadweb.org/wiki/images/0/01/Macro_Align_Working_Plane_to_Camera.png ToolBar Icon]
|FCVersion=All
|SeeAlso=[Macro aligne la Camera sur le Plan](Macro_Align_Camera_to_Working_Plane/fr.md) [<img src=images/Macro_Align_Camera_to_Working_Plane.png style="width   *24px">
}}

## Description

Cette macro déplace le [Draft Plan de travail](Draft_SelectPlane/fr.md) au centre de la vue 3D courante. Utile lorsque vous travaillez loin du centre de la grille.

## Utilisation

-   Déplacez la vue dans la zone où vous souhaitez regarder.
-   Lancez la macro.

## Script

Icône de la barre d\'outils ![](images/Macro_Align_Working_Plane_to_Camera.png )

**Macro_Align_Working_Plane_to_Camera.FCMacro**


{{MacroCode|code=
import FreeCAD,FreeCADGui
cam = FreeCAD.Vector(FreeCADGui.ActiveDocument.ActiveView.getCameraNode().position.getValue().getValue())
pos = FreeCAD.DraftWorkingPlane.projectPoint(cam)
FreeCAD.DraftWorkingPlane.position = pos
FreeCADGui.Snapper.setGrid()
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Align Working Plane to Camera/fr
