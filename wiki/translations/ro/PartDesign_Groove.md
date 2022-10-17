# PartDesign Groove/ro
---
- GuiCommand   *   Name   *PartDesign Groove   Workbenches   *[[PartDesign Workbench   PartDesign]], Complete|MenuLocation   *PartDesign → Groove---


</div>

## Descriere

Instrumentul Canelură/ **Groove**, învârte o schiță sau un profil selectat pe o anumită axă, tăind materialul din suport.

![](images/PartDesign_Groove_example.svg )


<div class="mw-translate-fuzzy">

*Above   * sketch (A) is revolved around axis (B); resulting groove on solid (C) is shown right.*


</div>

## Cum se folosește 


<div class="mw-translate-fuzzy">

1.  Selectați schița care va fi rotită.

       *   v0.17 and above A face on the existing solid can alternatively be used.
       *   v0.16 and below The sketch must be mapped to the planar face of an existing solid or Part Design feature, or an error message will appear .
2.  Press the **<img src="images/PartDesign_Groove.png" width=24px> '''Groove'''** button.
3.  Set the Groove parameters (see next section).
4.  Press **OK**.


</div>

## Opţiuni

Atunci când este crată o canelură, dialogul privind **Groove parameters** oferă câteva variante de parametrii care specifică cum schița profilului canelurii poate fi rotită.

+++
| ![](images/partdesign_groove_parameters.png ) | ### Axe                                                                                                                                                                                                                                                                                                                                                  |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                |
|                                                                          | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                                                                                                         |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                       |
|                                                                          | This option specifies the axis about which the sketch is to be revolved.                                                                                                                                                                                                                                                                                 |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | -   **Vertical sketch axis**   * selects the vertical sketch axis .                                                                                                                                                                                                                                                                                         |
|                                                                          | -   **Horizontal sketch axis**   * selects the horizontal sketch axis.                                                                                                                                                                                                                                                                                      |
|                                                                          | -   **Sketch axis**   * v0.16 and below selects a construction line contained in the sketch used by the Groove. The first construction line created in the sketch will be labelled *Sketch axis 0*. The drop down list will contain one custom sketch axis for each construction line. |
|                                                                          | -   **Construction line**   * v0.17 and above selects a construction line contained in the sketch used by the Groove. The drop down list will contain an entry for each construction line. The first construction line created in the sketch will be labelled *Construction line 1*.  |
|                                                                          | -   **Base (X/Y/Z) axis**   * v0.17 and above selects the X, Y or Z axis of the Body\'s Origin;                                                                                                                                                                                       |
|                                                                          | -   **Select reference\...**   * v0.17 and above allows selection in the 3D view of an edge on the Body, or a [datum line](PartDesign_Line.md).                                                                                                                               |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                |
|                                                                          | </div>                                                                                                                                                                                                                                                                                                                                                   |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                       |
|                                                                          | ### Unghiul                                                                                                                                                                                                                                                                                                                                              |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | This controls the angle through which the groove is to be formed, e.g. 360° would be a full, contiguous revolution. It is not possible to specify negative angles (use the **Reversed** option instead) or angles greater than 360° .                                                                                                                    |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | ### Planul simetric                                                                                                                                                                                                                                                                                                                    |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | If checked, the groove will extend half of the specified angle in both directions from the sketch plane .                                                                                                                                                                                                                                                |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | ### Reversed                                                                                                                                                                                                                                                                                                                                             |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | If checked, the direction of revolution is reversed from default clockwise to counterclockwise .                                                                                                                                                                                                                                                         |
+++

### Proprietăți

Mai jos sunt proprietăți care pot fi definite după crearea funcției. Proprietățile de date \"Base\" și \"Axis\" nu pot fi modificate.


<div class="mw-translate-fuzzy">

-    **Angle**   * angle of rotation. See [Angle](#Angle.md) .

-    **Label**   * label given to the operation, can be changed at convenience.

-    **Midplane**   * true or false. See [Symmetric to plane](#Symmetric_to_plane.md).

-    **Reversed**   * true or false. See [Reversed](#Reversed.md).

-    **Refine**   * v0.17 and above true or false.

Dacă este setat la true, curăță solidul de margini reziduale lăsate de funcții(onalități). Consultați [Part RefineShape](Part_RefineShape.md) pentru mai multe detalii.


</div>





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Groove/ro
