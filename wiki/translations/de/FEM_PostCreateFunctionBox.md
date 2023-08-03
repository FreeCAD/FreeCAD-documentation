---
 GuiCommand:
   Name: FEM PostCreateFunctionBox
   Name/de: FEM NachbereitungFunktionQuader
   MenuLocation: Ergebnisse , Filterfunktionen , Box
   Workbenches: FEM_Workbench/de
   Version: 0.21
   SeeAlso: FEM_tutorial/de
---

# FEM PostCreateFunctionBox/de



## Beschreibung

Die Funktion <img alt="" src=images/FEM_PostCreateFunctionBox.svg  style="width:24px;"> **FEM NachbereitungFunktionQuader** legt die Geometrie fest, mit der ein Netzobjekt geschnitten wird. Sie wird von den Werkzeugen <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:16px;"> [Funktion Schnitt-Filter](FEM_PostFilterCutFunction/de.md) und <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:16px;"> [Region Ausschnitt-Filter](FEM_PostFilterClipRegion/de.md) verwendet.



## Anwendung



### Quaderfunktion erstellen 


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Either press the **<img src="images/FEM_PostCreateFunctionBox.svg" width=16px> [Box](FEM_PostCreateFunctionBox.md)** button or select the **Results → Filter functions → <img src="images/FEM_PostCreateFunctionBox.svg" width=16px> Box** option from the menu.
2.  The Implicit function [task panel](Task_panel.md) is opened.
3.  Optionally set the values for the center and size of the section box.
4.  Press the **OK** button to finish.


</div>



### Quaderfunktion bearbeiten 


<div lang="en" dir="ltr" class="mw-content-ltr">

If the Box object in the [tree view](Tree_view.md) is hidden, select the <img alt="" src=images/FEM_PostCreateFunctionBox.svg  style="width:24px;"> Box object in the [3D view](3D_view.md) and press **Space** to make it visible, like in this example:


</div>

<img alt="" src=images/FEM_Box-Cut-Function-Example.png  style="width:400px;">



#### Den Quader bewegen 


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Click and drag a face of the box. The box is defined by blue edges.


</div>



#### Den Quader drehen und neigen 


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Click and drag one of the 3 lines that pass through the box to rotate and tilt the box around its origin.


</div>



#### Die Quadergröße anpassen 


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Click and drag one of the 8 small cubes at the box corners to scale the box.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

#### Transform the box 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Click and drag one of the 6 small cubes around the center of the box to change the shape of the box.


</div>



## Hinweise

-   Vorhandene Funktionen können für unterschiedliche Filter und für unterschiedliche <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:16px;"> [Ergebnis-Pipelines](FEM_PostPipelineFromResult/de.md) genutzt werden. Es wird allerdings dazu geraten, für jede Pipeline einen separaten Satz von Funktionen zu verwenden, um den Überblick über die Elemente in der [Baumansicht](Tree_view/de.md) zu behalten.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctionBox/de
