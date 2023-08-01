---
- GuiCommand:/de
   Name:FEM PostCreateFunctionCylinder
   Name/de:FEM NachbereitungFunktionZylinder
   MenuLocation:Ergebnisse → Filterfunktionen → Cylinder
   Workbenches:[FEM](FEM_Workbench/de.md)
   Version:0.21
   SeeAlso:[FEM Anleitung](FEM_tutorial/de.md)
---

# FEM PostCreateFunctionCylinder/de



## Beschreibung

Die Funktion <img alt="" src=images/FEM_PostCreateFunctionCylinder.svg  style="width:24px;"> **FEM NachbereitungFunktionZylinder** legt die Geometrie fest, mit der ein Netzobjekt geschnitten wird. Sie wird von den Werkzeugen <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:16px;"> [Funktion Schnitt-Filter](FEM_PostFilterCutFunction/de.md) und <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:16px;"> [Region Ausschnitt-Filter](FEM_PostFilterClipRegion/de.md) verwendet.



## Anwendung



### Zylinderfunktion erstellen 


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Either press the **<img src="images/FEM_PostCreateFunctionCylinder.svg" width=16px> [Cylinder](FEM_PostCreateFunctionCylinder.md)** button or select the **Results → Filter functions → <img src="images/FEM_PostCreateFunctionCylinder.svg" width=16px> Cylinder** option from the menu.
2.  The Implicit function [task panel](Task_panel.md) is opened.
3.  Optionally set the values for the center and the radius of the section cylinder.
4.  Press the **OK** button to finish.


</div>



### Zylinderfunktion bearbeiten 


<div lang="en" dir="ltr" class="mw-content-ltr">

If the Cylinder object in the [tree view](Tree_view.md) is hidden, select the <img alt="" src=images/FEM_PostCreateFunctionCylinder.svg  style="width:24px;"> Cylinder object in the [3D view](3D_view.md) and press **Space** to make it visible, like in this example:


</div>

<img alt="" src=images/FEM_Cylinder-Cut-Function-Example.png  style="width:400px;">



#### Den Zylinder bewegen 


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Click and drag the big white cuboid to move the cylinder along its normal vector.
-   Click and drag the white grid.


</div>



#### Den Zylinder drehen und neigen 


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Click and drag a line that connects the small cubes with the big white cuboid to rotate and tilt the cylinder around its origin.


</div>



#### Die Zylindergröße anpassen 


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Click and drag one of the 6 small cubes to scale the cylinder.


</div>



## Hinweise

-   Vorhandene Funktionen können für unterschiedliche Filter und für unterschiedliche <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:16px;"> [Ergebnis-Pipelines](FEM_PostPipelineFromResult/de.md) genutzt werden. Es wird allerdings dazu geraten, für jede Pipeline einen separaten Satz von Funktionen zu verwenden, um den Überblick über die Elemente in der [Baumansicht](Tree_view/de.md) zu behalten.





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctionCylinder/de
