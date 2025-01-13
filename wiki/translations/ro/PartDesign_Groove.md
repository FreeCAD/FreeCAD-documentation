# PartDesign Groove/ro
---
 GuiCommand:   Name: PartDesign Groove   Workbenches: PartDesign Workbench   PartDesign, Complete|MenuLocation: PartDesign , Groove---


</div>



## Descriere

Instrumentul Canelură/ **Groove**, învârte o schiță sau un profil selectat pe o anumită axă, tăind materialul din suport.

![](images/PartDesign_Groove_example.svg )


<div class="mw-translate-fuzzy">

*Above: sketch (A) is revolved around axis (B); resulting groove on solid (C) is shown right.*


</div>



## Cum se folosește 


<div class="mw-translate-fuzzy">

1.  Selectați schița care va fi rotită.

    :   v0.17 and above A face on the existing solid can alternatively be used.
    :   v0.16 and below The sketch must be mapped to the planar face of an existing solid or Part Design feature, or an error message will appear .
2.  Press the **<img src="images/PartDesign_Groove.png" width=24px> '''Groove'''** button.
3.  Set the Groove parameters (see next section).
4.  Press **OK**.


</div>



## Opţiuni


<div class="mw-translate-fuzzy">

Atunci când este crată o canelură, dialogul privind **Groove parameters** oferă câteva variante de parametrii care specifică cum schița profilului canelurii poate fi rotită.


</div>


<div class="mw-translate-fuzzy">

+++
| ![](images/partdesign_groove_parameters.png ) | ### Axe                                                                                                                                                                                                                                                                                                                                                  |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                |
|                                                                          | </div>                                                                                                                                                                                                                                                                                                                                                   |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                       |
|                                                                          | ### Type                                                                                                                                                                                                                                                                                                                                                 |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          |                                                                                                                                                                                                                                                                                                                                           |
|                                                                          | <small>(v1.0)</small>                                                                                                                                                                                                                                                                                                                                           |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                       |
|                                                                          | Type offers five different ways of specifying the angle of the groove:                                                                                                                                                                                                                                                                                   |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | #### Dimension                                                                                                                                                                                                                                                                                                                                           |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | Enter a numeric value for the **Angle** of the groove. With the option **Symmetric to plane** the groove will extend half the given angle to either side of the sketch or face.                                                                                                                                                                          |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | #### Through all                                                                                                                                                                                                                                                                                                                           |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | The groove will extend up to the last face of the support it encounters in its direction. With the option **Symmetric to plane** the groove will cut through all material in both directions.                                                                                                                                                            |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | #### To first                                                                                                                                                                                                                                                                                                                                 |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | The groove will extend up to the first face of the support it encounters in its direction.                                                                                                                                                                                                                                                               |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | #### Up to face                                                                                                                                                                                                                                                                                                                             |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | The groove will extend up to a face. Press the **Face** button and select a face or a [datum plane](PartDesign_Plane.md) from the Body.                                                                                                                                                                                     |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | #### Two dimensions                                                                                                                                                                                                                                                                                                                     |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | This allows to enter a second angle in which the groove should extend in the opposite direction. The directions can be switched by checking the **Reversed** option.                                                                                                                                                                                     |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | ### Axis                                                                                                                                                                                                                                                                                                                                                 |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | Specifies the axis of the groove:                                                                                                                                                                                                                                                                                                                        |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                |
|                                                                          | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                                                                                                         |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                       |
|                                                                          | This option specifies the axis about which the sketch is to be revolved.                                                                                                                                                                                                                                                                                 |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | -   **Vertical sketch axis**: selects the vertical sketch axis .                                                                                                                                                                                                                                                                                         |
|                                                                          | -   **Horizontal sketch axis**: selects the horizontal sketch axis.                                                                                                                                                                                                                                                                                      |
|                                                                          | -   **Sketch axis**: v0.16 and below selects a construction line contained in the sketch used by the Groove. The first construction line created in the sketch will be labelled *Sketch axis 0*. The drop down list will contain one custom sketch axis for each construction line. |
|                                                                          | -   **Construction line**: v0.17 and above selects a construction line contained in the sketch used by the Groove. The drop down list will contain an entry for each construction line. The first construction line created in the sketch will be labelled *Construction line 1*.  |
|                                                                          | -   **Base (X/Y/Z) axis**: v0.17 and above selects the X, Y or Z axis of the Body\'s Origin;                                                                                                                                                                                       |
|                                                                          | -   **Select reference\...**: v0.17 and above allows selection in the 3D view of an edge on the Body, or a [datum line](PartDesign_Line.md).                                                                                                                               |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                |
|                                                                          | </div>                                                                                                                                                                                                                                                                                                                                                   |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                       |
|                                                                          | Note that when changing the axis, the **Reversed** option may be (un)checked automatically.                                                                                                                                                                                                                                                              |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          |                                                                                                                                                                                                                                                                                                                |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | ### Unghiul                                                                                                                                                                                                                                                                                                                                              |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                |
|                                                                          | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                                                                                                         |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                       |
|                                                                          | This controls the angle through which the groove is to be formed, e.g. 360° would be a full, contiguous revolution. It is not possible to specify negative angles (use the **Reversed** option instead) or angles greater than 360° .                                                                                                                    |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                |
|                                                                          | </div>                                                                                                                                                                                                                                                                                                                                                   |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                       |
|                                                                          |                                                                                                                                                                                                                                                                                                   |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          | ### Planul simetric                                                                                                                                                                                                                                                                                                                    |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                |
|                                                                          | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                                                                                                         |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                       |
|                                                                          | If checked, the groove will extend half of the specified angle in both directions from the sketch plane .                                                                                                                                                                                                                                                |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                |
|                                                                          | </div>                                                                                                                                                                                                                                                                                                                                                   |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                       |
|                                                                          | ### Reversed                                                                                                                                                                                                                                                                                                                                             |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                          |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                |
|                                                                          | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                                                                                                         |
|                                                                          |                                                                                                                                                                                                                                                                                                                                                       |
|                                                                          | If checked, the direction of revolution is reversed from default clockwise to counterclockwise .                                                                                                                                                                                                                                                         |
+++


</div>

### 2nd angle 


<small>(v1.0)</small> 

Defines the angle of the groove in the opposite direction. This option is only available if **Type** is **Two dimensions** and **Angle** is smaller than 360°.



### Proprietăți

### Data


{{TitleProperty|Groove}}

-    **Type|Enumeration**
    

-    **Base|Vector**: (read-only)

-    **Axis|Vector**: (read-only)

-    **Angle|Angle**
    

-    **Angle2|Angle**
    

-    **Up To Face|LinkSub**
    

-    **Reference Axis|LinkSub**
    


{{TitleProperty|Part Design}}

-    **Refine|Bool**
    


{{TitleProperty|Sketch Based}}

-    **Profile|LinkSub**
    

-    **Midplane|Bool**
    

-    **Reversed|Bool**
    

-    **Allow Multi Face|Bool**
    

## Notes

-   A <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:16px;"> [ShapeBinder](PartDesign_ShapeBinder.md) cannot be used for the profile.
-   When using a <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:16px;"> [SubShapeBinder](PartDesign_SubShapeBinder.md) for the profile, selecting the binder in the [Tree view](Tree_view.md) will fail, instead the binder\'s face has to selected in the [3D view](3D_view.md).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Groove/ro
