---
- GuiCommand:/it
   Name:TechDraw_2PointCosmeticLine
   Name/it:Linea tra 2 punti
   Icon:TechDraw-line2points.svg
   MenuLocation:TechDraw → Aggiungi linee → Linea tra 2 punti
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Linea a centro faccia](TechDraw_FaceCenterLine/it.md), [Linea centrale a 2 linee](TechDraw_2LineCenterLine/it.md)
   Version:0.19
---

# TechDraw 2PointCosmeticLine/it


</div>

## Descrizione

Lo strumento **Linea tra 2 punti** aggiunge una linea cosmetica tra due vertici (punti). I vertici possono essere 2d o 3d. La linea risultante può essere utilizzata per il dimensionamento. L\'aspetto della linea può essere modificato utilizzando lo strumento [Rimuovi oggetto cosmetico](TechDraw_CosmeticEraser/it.md).

<img alt="" src=images/CosLine2PointsSample.png  style="width:200px;">



*Linea tra 2 punti*

## Utilizzo

1.  Select 2 Vertexes in a View or 2 Vertexes in the 3D view.
2.  Press the **<img src="images/TechDraw-line2points.svg" width=16px> Add Cosmetic line between 2 Points** button.
3.  A dialog will open where you can adjust the coordinates of the 2 points.
4.  A line will be added to connect the 2 selected Vertices. In the case of 3d points, the line will connect the projection of the selected points.

To delete a cosmetic line, select it and use the toolbar button **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Remove Cosmetic Object](TechDraw_CosmeticEraser.md)**.

## Editing Cosmetic Lines 

To change the endpoints of a cosmetic line, **<img src="images/TechDraw-line2points.svg" width=16px> Add Cosmetic line between 2 Points
**

1.  Select the cosmetic line.
2.  Press **<img src="images/TechDraw-line2points.svg" width=16px> Add Cosmetic line between 2 Points**.
3.  A dialog will open where you can change the coordinates of the endpoints.
4.  Press **OK** to see your changes.

To change the appearance of a cosmetic line, use [Remove Cosmetic Object](TechDraw_CosmeticEraser.md).

## Proprietà

Cosmetic lines have no properties of their own, as they are not document objects.

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>

Cosmetic lines can be created using the makeCosmeticLine(v1, v2) or makeCosmeticLine3d(v1, v2) methods of DrawViewPart.


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 2PointCosmeticLine/it
