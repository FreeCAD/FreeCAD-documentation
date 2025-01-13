# PartDesign Groove/cs
---
 GuiCommand:   Name: PartDesign_Groove   Name/cs: PartDesign Groove   Workbenches: PartDesign Workbench/cs   Návrh dílu, Complete|MenuLocation: PartDesign -> Groove---


</div>




<div class="mw-translate-fuzzy">

## Úvod

Tento nástroj otáčí náčrtem nebo 2D objektem podle zadané osy a odebírá materiál z podkladu. Například, obrázek ukazuje drážku vyříznutou na hřídeli. <img alt="" src=images/Groove_example.png  style="width:500px;"> 


</div>

The **Groove** tool revolves a selected sketch or profile about a given axis, cutting out material from the support .

![](images/PartDesign_Groove_example.svg )



*Above: sketch (A) is revolved around axis (B); resulting groove on solid (C) is shown right.*

## Usage

1.  Select a single sketch or one or more faces from the Body.
2.  Press the **<img src="images/PartDesign_Groove.svg" width=16px> [Groove](PartDesign_Groove.md)** button.
3.  Set the Groove parameters, see [Options](#Options.md) below.
4.  Press the **OK** button.




<div class="mw-translate-fuzzy">

## Volby

![](images/partdesign_groove_parameters.png ) Při vytváření drážky, dialogové okno \'parametry drážky\' nabízí několik parametrů, které specifikují jak by se náčrt měl otáčet. Mají stejný význam jako u vlastnosti [otáčení](PartDesign_Revolution#Options.md).


</div>

When creating a groove, or after double-clicking an existing groove in the [Tree view](Tree_view.md), the **Groove parameters** task panel is shown. It offers the following settings:

![](images/partdesign_groove_parameters.png )

### Type


<small>(v1.0)</small> 

Type offers five different ways of specifying the angle of the groove:

#### Dimension

Enter a numeric value for the **Angle** of the groove. With the option **Symmetric to plane** the groove will extend half the given angle to either side of the sketch or face.

#### Through all 

The groove will extend up to the last face of the support it encounters in its direction. With the option **Symmetric to plane** the groove will cut through all material in both directions.

#### To first 

The groove will extend up to the first face of the support it encounters in its direction.

#### Up to face 

The groove will extend up to a face. Press the **Face** button and select a face or a [datum plane](PartDesign_Plane.md) from the Body.

#### Two dimensions 

This allows to enter a second angle in which the groove should extend in the opposite direction. The directions can be switched by checking the **Reversed** option.

### Axis

Specifies the axis of the groove:

-   **Vertical sketch axis**: selects the vertical sketch axis.
-   **Horizontal sketch axis**: selects the horizontal sketch axis.
-   **Construction line**: selects a construction line from the sketch used by the groove. The dropdown list will contain an entry for each construction line. The first construction line will be labelled *Construction line 1*.
-   **Base (X/Y/Z) axis**: selects the X, Y or Z axis of the Body\'s origin.
-   **Select reference\...**: allows the selection of a straight edge or a [datum line](PartDesign_Line.md) from the Body.

Note that when changing the axis, the **Reversed** option may be (un)checked automatically.

### Angle

Defines the angle of the groove. This option is only available if **Type** is **Dimension** or **Two dimensions**. Angles larger than 360° are not possible. Nor are negative values, use the **Reversed** option instead.

### Symmetric to plane 

Check this option to extend the groove half the given angle to either side of the sketch or face, if **Type** is **Dimension**, or **Through all** if that is the **Type**.

### Reversed

Reverses the direction of the groove.

### 2nd angle 


<small>(v1.0)</small> 

Defines the angle of the groove in the opposite direction. This option is only available if **Type** is **Two dimensions** and **Angle** is smaller than 360°.

## Properties

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
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Groove/cs
