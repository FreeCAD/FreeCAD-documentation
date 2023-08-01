# Macro Align Camera to Working Plane/fr
{{Macro/fr
|Name=Macro Align Camera to Working Plane
|Icon=Macro_Align_Camera_to_Working_Plane.png
|Description=Cette macro aligne la caméra sur le plan courant [Draft Working Plane](Draft_SelectPlane/fr.md) 
|Author=yorik
|Version=0.1
|Date=2017-03-16
|Download=[https://www.freecadweb.org/wiki/images/f/fd/Macro_Align_Camera_to_Working_Plane.png ToolBar Icon]
|FCVersion=All
|SeeAlso=[Macro Aligne le Plan à la Camera](Macro_Align_Working_Plane_to_Camera/fr.md) [<img src=images/Macro_Align_Working_Plane_to_Camera.png style="width:24px"> 
}}

## Description

Cette macro aligne la caméra sur le [Draft Plan de travail](Draft_SelectPlane/fr.md) en cours.

## Utilisation

-   Réglez le [Draft Plan de travail](Draft_SelectPlane/fr.md) à votre convenance
-   Exécutez la macro

## Script

Icône de la barre d\'outils ![](images/Macro_Align_Camera_to_Working_Plane.png )

**Macro_Align_Camera_to_Working_Plane.FCMacro**


{{MacroCode|code=
import FreeCAD,FreeCADGui
c = FreeCADGui.ActiveDocument.ActiveView.getCameraNode()
r = FreeCAD.DraftWorkingPlane.getRotation().Rotation.Q
c.orientation.setValue(r)
}}



---
⏵ [documentation index](../README.md) > Macro Align Camera to Working Plane/fr
