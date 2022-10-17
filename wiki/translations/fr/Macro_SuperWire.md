# Macro SuperWire/fr
{{Macro/fr
|Name=SuperWire
|Icon=Macro_SuperWire.png
|Description=Cette macro crée un fil d'objets sélectionnés (lignes et arcs) même lorsque les méthodes de création du fil normal (par exemple avec l'outil de mise à niveau) échouent.
|Author=Yorik
|Version=0.1
|Date=2012-05-22
|FCVersion=All
|Download=[https   *//www.freecadweb.org/wiki/images/e/e3/Macro_SuperWire.png ToolBar Icon]
}}

## Description

Cette macro crée un fil d\'objets sélectionnés (lignes et arcs) même lorsque les méthodes de création du fil normal (par exemple avec l\'outil de mise à niveau) échouent.

Attention, vous devez avoir une version récente de FreeCAD pour ce travail

## Script

Icône de la barre d\'outils ![](images/Macro_SuperWire.png )

**Macro_SuperWire.FCMacro**


{{MacroCode|code=
import FreeCAD,FreeCADGui,Part
try   *
    import DraftGeomUtils as fcgeo
except   *
    from draftlibs import fcgeo

sel = FreeCADGui.Selection.getSelection()
if not sel   *
   FreeCAD.Console.PrintWarning("Select something first!")
else   *
   elist = []
   for obj in sel   *
       if hasattr(obj,"Shape")   *
           elist.append(obj.Shape.Edges[0])
   wire = fcgeo.superWire(elist)
   if wire   *
       Part.show(wire)
   else   *
       FreeCAD.Console.PrintError("SuperWire operation failed!")
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro SuperWire/fr
