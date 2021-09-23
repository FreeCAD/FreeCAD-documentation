# PartDesign Revolution/ro
---
- GuiCommand:   Name:PartDesign Revolution   Workbenches:[[PartDesign Workbench   PartDesign]], Complete|MenuLocation:PartDesign → Revolution---


</div>

## Description


<div class="mw-translate-fuzzy">

## Introducere

Instrumentul **Revolution** crează un solid prin rotirea schiței selectate sau a unui obiect 2D în jurul unei axe date.


</div>

![](images/PartDesign_Revolution_example.svg )


<div class="mw-translate-fuzzy">

*Deasupra: schița (A) este rotită cu 270 grade în sens antiorar/trigonometric în jurul axei (B); rezultând un solid (C), care este afișat în dreapta.*


</div>


<div class="mw-translate-fuzzy">

## Cum se foloseste 


</div>


<div class="mw-translate-fuzzy">

1.  Select the sketch to be revolved. v0.17 and above A face on the existing solid can alternatively be used.
2.  Press the **<img src="images/PartDesign_Revolution.png" width=24px> '''Revolution'''** button.
3.  Set the Revolution parameters (see next section).
4.  Press **OK**.


</div>

## Options


<div class="mw-translate-fuzzy">

## Opțiuni

Atunci când este crrată o revoluție, dialogul privind **REveolution parameters** oferă câteva variante de parametrii care specifică cum schița poate fi rotită.


</div>

+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ![](images/partdesign_revolution_parameters.png ) | ### Axis                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                  | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                  | +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+ |
|                                                                                  | | ![](images/partdesign_revolution_parameters.png ) | ### Axis                                                                                                                                                                                                                                                                                                                                                            | |
|                                                                                  | |                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              | |
|                                                                                  | |                                                                                  | This option specifies the axis about which the sketch is to be revolved.                                                                                                                                                                                                                                                                                                     | |
|                                                                                  | |                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              | |
|                                                                                  | |                                                                                  | -   **Vertical sketch axis**: selects the vertical sketch axis.                                                                                                                                                                                                                                                                                                              | |
|                                                                                  | |                                                                                  | -   **Horizontal sketch axis**: selects the horizontal sketch axis.                                                                                                                                                                                                                                                                                                          | |
|                                                                                  | |                                                                                  | -   **Sketch axis**: v0.16 and below selects a construction line contained in the sketch used by the Revolution. The first construction line created in the sketch will be labelled *Sketch axis 0*. The drop down list will contain one custom sketch axis for each construction line.                 | |
|                                                                                  | |                                                                                  | -   **Construction line**: v0.17 and above selects a construction line contained in the sketch used by the Revolution. The drop down list will contain an entry for each construction line. The first construction line created in the sketch will be labelled *Construction line 1*.                  | |
|                                                                                  | |                                                                                  | -   **Base (X/Y/Z) axis**: v0.17 and above selects the X, Y or Z axis of the Body\'s Origin;                                                                                                                                                                                                           | |
|                                                                                  | |                                                                                  | -   **Select reference\...**: v0.17 and above allows selection in the 3D view of an edge on the Body, or a [datum line](PartDesign_Line.md).                                                                                                                                                   | |
|                                                                                  | |                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              | |
|                                                                                  | |                                                                                  |                                                                                                                                                                                                                                                                                                                                                                    | |
|                                                                                  | |                                                                                  | </div>                                                                                                                                                                                                                                                                                                                                                                       | |
|                                                                                  | |                                                                                  |                                                                                                                                                                                                                                                                                                                                                                           | |
|                                                                                  | |                                                                                  | ### Angle                                                                                                                                                                                                                                                                                                                                                          | |
|                                                                                  | |                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              | |
|                                                                                  | |                                                                                  |                                                                                                                                                                                                                                                                                                                                                                    | |
|                                                                                  | |                                                                                  | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                                                                                                                             | |
|                                                                                  | |                                                                                  |                                                                                                                                                                                                                                                                                                                                                                           | |
|                                                                                  | |                                                                                  | ### Unghi                                                                                                                                                                                                                                                                                                                                                          | |
|                                                                                  | |                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              | |
|                                                                                  | |                                                                                  | This controls the angle through which the revolution is to be formed, e.g. 360° would be a full, contiguous revolution. The images in the [examples](#Examples.md) section demonstrate some of the possibilities with specifying different angles. It is not possible to specify negative angles (use the **Reversed** option instead) or angles greater than 360° . | |
|                                                                                  | |                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              | |
|                                                                                  | |                                                                                  | ### Simetric față de Plan                                                                                                                                                                                                                                                                                                                          | |
|                                                                                  | |                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              | |
|                                                                                  | |                                                                                  | If checked, the revolution will extend half of the specified angle in both directions from the sketch plane.                                                                                                                                                                                                                                                                 | |
|                                                                                  | |                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              | |
|                                                                                  | |                                                                                  | ### Inversat                                                                                                                                                                                                                                                                                                                                                    | |
|                                                                                  | |                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              | |
|                                                                                  | |                                                                                  | If checked, the direction of revolution is reversed from default clockwise to counterclockwise.                                                                                                                                                                                                                                                                              | |
|                                                                                  | +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+ |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                  | </div>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                  | ### Symmetric to plane                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                  | If checked, the revolution will extend half of the specified angle in both directions from the sketch plane.                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                  | ### Reversed                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                  | If checked, the direction of revolution is reversed from default clockwise to counterclockwise.                                                                                                                                                                                                                                                                                                                                                                     |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## Proprietăți

Mai jos sunt proprietăți care pot fi definite după crearea funcției. Proprietățile de date \"Base\" și \"Axis\" nu pot fi modificate.

-    **Angle**: angle of rotation. See [Angle](#Angle.md).

-    **Label**: label given to the operation, can be changed at convenience.

-    **Midplane**: true or false. See [Symmetric to plane](#Symmetric_to_plane.md).

-    **Reversed**: true or false. See [Reversed](#Reversed.md).

-    **Refine**: v0.17 and above true or false. If set to true, cleans the solid from residual edges left by features. See [Part RefineShape](Part_RefineShape.md) for more details.

## Exemple


<div class="mw-translate-fuzzy">

![Example revolution using a construction line as the Revolution axis: In this image the angle is 75°, revolution is about the construction line (Sketch axis 0)](images/PartDesign_Revolution_axis_fromconstructionlines1.jpg ) 


</div>

## Useful links 


<div class="mw-translate-fuzzy">

## Link uri utile 

Un exemplu [detailed example of use](http://forum.freecadweb.org/viewtopic.php?f=3&t=3674) are partea practică pe forum.


</div>





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Revolution/ro
