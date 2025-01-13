---
 GuiCommand:
   Name: PartDesign Revolution
   MenuLocation: Part Design , Create an additive feature , Revolution
   Workbenches: PartDesign_Workbench
   SeeAlso: PartDesign_Groove
---

# PartDesign Revolution/pt-br

## Description

The **Revolution** tool creates a solid by revolving a selected sketch or 2D object about a given axis.

![](images/PartDesign_Revolution_example.svg )



*Above: sketch (A) is revolved 270 degrees counter-clockwise around axis (B); resulting solid (C) is shown right.*



## Utilização

1.  Select a single sketch or one or more faces from the Body.
2.  Press the **<img src="images/PartDesign_Revolution.svg" width=24px> [Revolution](PartDesign_Revolution.md)** button.
3.  Set the Revolution parameters, see [Options](#Options.md) below.
4.  Press the **OK** button.

## Options

When creating a revolution, or after double-clicking an existing revolution in the [Tree view](Tree_view.md), the **Revolution parameters** task panel is shown. It offers the following settings:

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

-   **Vertical sketch axis**: selects the vertical sketch axis.
-   **Horizontal sketch axis**: selects the horizontal sketch axis.
-   **Construction line**: selects a construction line from the sketch used by the revolution. The dropdown list will contain an entry for each construction line. The first construction line will be labelled *Construction line 1*.
-   **Base (X/Y/Z) axis**: selects the X, Y or Z axis of the Body\'s origin.
-   **Select reference\...**: allows the selection of a straight edge or a [datum line](PartDesign_Line.md) from the Body.

Note that when changing the axis, the **Reversed** option may be (un)checked automatically.

### Angle

Defines the angle of the revolution. This option is only available if **Type** is **Dimension** or **Two dimensions**. Angles larger than 360° are not possible. Nor are negative values, use the **Reversed** option instead.

### Symmetric to plane 

Check this option to extend the revolution half the given angle to either side of the sketch or face. This option is only available if **Type** is **Dimension**.

### Reversed

Reverses the direction of the revolution.

### 2nd angle 


<small>(v1.0)</small> 

Defines the angle of the revolution in the opposite direction. This option is only available if **Type** is **Two dimensions** and **Angle** is smaller than 360°.




<div class="mw-translate-fuzzy">

## Propriedades


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
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Revolution/pt-br
