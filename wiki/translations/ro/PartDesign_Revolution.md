# PartDesign Revolution/ro
---
 GuiCommand:   Name: PartDesign Revolution   Workbenches: PartDesign Workbench   PartDesign, Complete|MenuLocation: PartDesign , Revolution---


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

![](images/partdesign_revolution_parameters.png )

### Type


<small>(v1.0)</small> 

Type offers five different ways of specifying the angle of the revolution:

#### Dimension

Enter a numeric value for the **Angle** of the revolution. With the option **Symmetric to plane** the revolution will extend half the given angle to either side of the sketch or face.

#### To last 

The revolution will extend up to the last face of the support it encounters in its direction. If there is no support, an error message will appear.

#### To first 

The revolution will extend up to the first face of the support it encounters in its direction. If there is no support, an error message will appear.

#### Up to face 

The revolution will extend up to a face. Press the **Face** button and select a face or a [datum plane](PartDesign_Plane.md) from the Body.

#### Two dimensions 

This allows to enter a second angle in which the revolution should extend in the opposite direction. The directions can be switched by checking the **Reversed** option.

### Axis

Specifies the axis of the revolution:


<div class="mw-translate-fuzzy">

+++
| ![](images/partdesign_revolution_parameters.png ) | ### Axis                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  | This option specifies the axis about which the sketch is to be revolved.                                                                                                                                                                                                                                                                                                     |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  | -   **Vertical sketch axis**: selects the vertical sketch axis.                                                                                                                                                                                                                                                                                                              |
|                                                                                  | -   **Horizontal sketch axis**: selects the horizontal sketch axis.                                                                                                                                                                                                                                                                                                          |
|                                                                                  | -   **Sketch axis**: v0.16 and below selects a construction line contained in the sketch used by the Revolution. The first construction line created in the sketch will be labelled *Sketch axis 0*. The drop down list will contain one custom sketch axis for each construction line.                 |
|                                                                                  | -   **Construction line**: v0.17 and above selects a construction line contained in the sketch used by the Revolution. The drop down list will contain an entry for each construction line. The first construction line created in the sketch will be labelled *Construction line 1*.                  |
|                                                                                  | -   **Base (X/Y/Z) axis**: v0.17 and above selects the X, Y or Z axis of the Body\'s Origin;                                                                                                                                                                                                           |
|                                                                                  | -   **Select reference\...**: v0.17 and above allows selection in the 3D view of an edge on the Body, or a [datum line](PartDesign_Line.md).                                                                                                                                                   |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                  | </div>                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                  | Note that when changing the axis, the **Reversed** option may be (un)checked automatically.                                                                                                                                                                                                                                                                                  |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  | ### Angle                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                  | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                                                                                                                             |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                  | ### Unghi                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  | This controls the angle through which the revolution is to be formed, e.g. 360° would be a full, contiguous revolution. The images in the [examples](#Examples.md) section demonstrate some of the possibilities with specifying different angles. It is not possible to specify negative angles (use the **Reversed** option instead) or angles greater than 360° . |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  | ### Simetric față de Plan                                                                                                                                                                                                                                                                                                                            |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  | If checked, the revolution will extend half of the specified angle in both directions from the sketch plane.                                                                                                                                                                                                                                                                 |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  | ### Inversat                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  | If checked, the direction of revolution is reversed from default clockwise to counterclockwise.                                                                                                                                                                                                                                                                              |
+++





</div>

### Symmetric to plane 

Check this option to extend the revolution half the given angle to either side of the sketch or face. This option is only available if **Type** is **Dimension**.

### Reversed

Reverses the direction of the revolution.

### 2nd angle 


<small>(v1.0)</small> 

Defines the angle of the revolution in the opposite direction. This option is only available if **Type** is **Two dimensions** and **Angle** is smaller than 360°.




<div class="mw-translate-fuzzy">

## Proprietăți


</div>

### Data


{{TitleProperty|Part Design}}

-    **Refine|Bool**
    


{{TitleProperty|Revolution}}

-    **Type|Enumeration**
    

-    **Base|Vector**: (read-only)

-    **Axis|Vector**: (read-only)

-    **Angle|Angle**
    

-    **Up To Face|LinkSub**
    

-    **Angle2|Angle**
    

-    **Reference Axis|LinkSub**
    


{{TitleProperty|Sketch Based}}

-    **Profile|LinkSub**
    

-    **Midplane|Bool**
    

-    **Reversed|Bool**
    

-    **Allow Multi Face|Bool**
    

## Notes

-   A <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:16px;"> [ShapeBinder](PartDesign_ShapeBinder.md) cannot be used for the profile.
-   When using a <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:16px;"> [SubShapeBinder](PartDesign_SubShapeBinder.md) for the profile, selecting the binder in the [Tree view](Tree_view.md) will fail, instead the binder\'s face has to be selected in the [3D view](3D_view.md).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Revolution/ro
