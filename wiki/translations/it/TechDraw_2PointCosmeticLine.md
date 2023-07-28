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


<div class="mw-translate-fuzzy">

Lo strumento **Linea tra 2 punti** aggiunge una linea cosmetica tra due vertici (punti). I vertici possono essere 2d o 3d. La linea risultante può essere utilizzata per il dimensionamento. L\'aspetto della linea può essere modificato utilizzando lo strumento [Rimuovi oggetto cosmetico](TechDraw_CosmeticEraser/it.md).


</div>

<img alt="" src=images/CosLine2PointsSample.png  style="width:200px;">


<div class="mw-translate-fuzzy">



*Linea tra 2 punti*


</div>




<div class="mw-translate-fuzzy">

## Utilizzo


</div>

1.  Select two points in a TechDraw View or two points in the [3D view](3D_view.md).
2.  If you have selected points in the 3D view: add the correct TechDraw View to the selection by selecting it in the [Tree view](Tree_view.md).
3.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_2PointCosmeticLine.svg" width=16px> [Add Cosmetic Line Through 2 points](TechDraw_2PointCosmeticLine.md)** button.
    -   Select the **TechDraw → Add Lines → <img src="images/TechDraw_2PointCosmeticLine.svg" width=16px> Add Cosmetic Line Through 2 points** option from the menu.
4.  A task panel opens.
5.  Optionally adjust the coordinates of the points.
6.  Press the **OK** button.
7.  A cosmetic line connecting the two points is added. In the case of 3D points, the line connects the projection of the points.

## Usage edit 

To change the endpoints of a cosmetic line:

1.  Select the cosmetic line.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_2PointCosmeticLine.svg" width=16px> [Add Cosmetic Line Through 2 points](TechDraw_2PointCosmeticLine.md)** button.
    -   Select the **TechDraw → Add Lines → <img src="images/TechDraw_2PointCosmeticLine.svg" width=16px> Add Cosmetic Line Through 2 points** option from the menu.
3.  A task panel opens.
4.  Adjust the coordinates of the points.
5.  Press the **OK** button.

## Notes

-   To delete a cosmetic line use <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:16px;"> [TechDraw CosmeticEraser](TechDraw_CosmeticEraser.md).
-   To change the appearance of a cosmetic line use <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:16px;"> [TechDraw DecorateLine](TechDraw_DecorateLine.md).



## Proprietà

Cosmetic lines have no properties of their own, as they are not document objects.



## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>

Cosmetic lines can be created using the {{Incode|makeCosmeticLine(v1, v2)}} or {{Incode|makeCosmeticLine3d(v1, v2)}} methods of DrawViewPart.


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 2PointCosmeticLine/it
