---
- GuiCommand:   Name:Std MeasureDistance   MenuLocation:[[Std View Menu   View]] → Measure distance‏‎||Workbenches:All   Shortcut:   SeeAlso:---


</div>


<div class="mw-translate-fuzzy">

## Introducere

Acest instrument măsoară și afișează distanța absolută dintre două puncte din spațiul 3D.


</div>

The **Std MeasureDistance** command creates a distance object that measures and displays the distance between two points.


<div class="mw-translate-fuzzy">

## Utilizare

1.  Click pe <img alt="" src=images/Std_MeasureDistance.png  style="width:32px;"> or choose ** Tools** → **<img src="images/Std_MeasureDistance.png" width=32px> Measure Distance** din meniul principal.
2.  Selectați primul punct din vizualizarea 3D.
3.  Selectați al doile apunct din vizualizarea 3D.
4.  Distanța absolută dintre două puncte va fi calculată și afișată în vizualizarea 3D .
5.  o distanță obiect va fi creată în vizualizarea arborescentă.


</div>

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_MeasureDistance.svg" width=16px> [Std MeasureDistance](Std_MeasureDistance.md)** button.
    -   Select the **Tools → <img src="images/Std_MeasureDistance.svg" width=16px> Measure distance** option from the menu.
2.  Select the first dimension point anywhere on an object in the [3D view](3D_view.md).
3.  Select the second dimension point anywhere on an object in the 3D view.
4.  The selection order of the points can have an impact on the position of the dimension line.
5.  Optionally flip the position of the dimension line by changing the **Mirror** property of the distance object.


<div class="mw-translate-fuzzy">

## Note

Pentru mai multe posibilități de măsurare / dimensionare puteți utiliza

1.  [Measure-Tools](Std_Measure_Menu.md) din Atelierul Part
2.  [Draft Dimension](Draft_Dimension.md)-Tool din Atelierul Draft
3.  [Arch Survey](Arch_Survey.md)-Tool din atelierul Arch


</div>

-   You cannot use the [Draft](Draft_Workbench.md) snap tools with this command.
-   To add dimensions to drawings use the dimension tools from the [TechDraw Workbench](TechDraw_Workbench.md).
-   For more comprehensive measuring tools, install the <img alt="" src=images/Manipulator_workbench_icon.svg  style="width:24px;"> [Manipulator Workbench](Manipulator_Workbench.md) (an [external workbench](External_workbenches.md)).

## Properties

### Data


{{TitleProperty|Base}}

-    **Label**: by default the label contains the measured distance, but this distance is not updated when P1 or P2 are later changed.


{{TitleProperty|Measurement}}

-    **P1**: the first dimension point.

-    **P2**: the second dimension point.

-    **Distance**: (read-only) the measured distance between P1 and P2.

### View


{{TitleProperty|Base}}

-    **Dist Factor**: this factor, multiplied by the measured distance, determines the dimension line offset.

-    **Font Size**: the height of the letters (line height in pixels).

-    **Mirror**: if set to `True` the position of the dimension line relative to P1 and P2 is flipped.





{{Std Base navi

}}  
