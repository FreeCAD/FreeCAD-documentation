---
- GuiCommand:/ru
   Name/ru:Выдавливание
   Name:PartDesign_Pad
   MenuLocation:Part Design → Create an additive feature → Выдавливание
   Workbenches:[PartDesign](PartDesign_Workbench/ru.md)
   SeeAlso:[Вырез](PartDesign_Pocket/ru.md)
---

# PartDesign Pad/ru

## Описание

The **<img src="images/PartDesign_Pad.svg" width=16px> [PartDesign Pad](PartDesign_Pad.md)** tool extrudes a sketch into a solid in a direction normal to the sketch plane. As of <small>(v0.17)</small>  faces on the solid can also be used.

![](images/PartDesign_Pad_example.svg )

*Sketch (A) shown on the left; end result after pad operation (B) on the right.*

**Note:** {{VersionMinus|0.16}} If the selected sketch is mapped to the face of an existing solid or another Part Design feature, the pad will be fused to it.

## Применение

1.  Select the sketch to be padded. **Note:** As of <small>(v0.17)</small>  a face on the existing solid can alternatively be used.
2.  Press the **<img src="images/PartDesign_Pad.svg" width=16px> '''Pad'''** button.
3.  Set the Pad parameters, see the [Options](#Options.md) below.
4.  Click **OK**.

## Опции

When creating a pad, the Combo view automatically switches to the Tasks pane, showing the **Pad parameters** dialog.

![](images/pad_parameters_cropped.png )

### Type

Type offers five different ways of specifying the length to which the pad will be extruded.

#### Dimension

Enter a numeric value for the length of the pad. The default direction for extrusion is away (outside of) the support, but it can be changed by ticking the **Reversed** option. Extrusions occur [normal](http://en.wikipedia.org/wiki/Surface_normal) to the defining sketch plane. With the option **Symmetric to plane** the pad will extend half of the given length to either side of the sketch plane. Negative dimensions are not possible. Use the **Reversed** option instead.

#### Two dimensions 

This allows to enter a second length in which the pad should extend in the opposite direction (into the support). Again can be changed by ticking the **Reversed** option.

#### To last 

The pad will extrude up to the last face of the support in the extrusion direction. If there is no support, an error message will appear.

#### To first 

The pad will extrude up to the first face of the support in the extrusion direction. If there is no support, an error message will appear.

#### Up to face 

The pad will extrude up to a face in the support that can be chosen by clicking on it. If there is no support, no selections will be accepted.

### Length

Defines the length of the pad. Multiple units can be used independently of the user\'s units preferences (m, cm, mm, nm, ft or \', in or \").

### Use custom direction 


<small>(v0.19)</small> 

If checked, the pad direction will not be the normal vector of the sketch but the given vector. The pad length is however set according to the normal vector direction.

### Length along sketch normal 

If checked, the pad length is measured along the sketch normal, otherwise along the custom direction. <small>(v0.20)</small> 

### Offset to face 

Offset from face in which the pad will end. This option is only available when **Type** is either **To last**, **To first** or **Up to face**.

### Symmetric to plane 

Tick the checkbox to extend half of the given length to either side of the sketch plane.

### Reversed

Reverses the direction of the pad.

## Свойства

-    **Type**: Type of ways how the pad will be extruded, see [Options](#Options.md).

-    **Length**: Defines the length of the pad, see [Options](#Options.md).

-    **Length2**: Second pad length in case the **Type** option **TwoLengths** is used, see [Options](#Options.md).

-    **Use Custom Vector**: <small>(v0.19)</small>  If checked, the pad direction will not be the normal vector of the sketch but the given vector, see [Options](#Options.md).

-    **Direction**: <small>(v0.19)</small>  Vector of the pad direction if **Use Custom Vector** is used.

-    **Along Sketch Normal**: <small>(v0.20)</small>  If *true*, the pad length is measured along the sketch normal. Otherwise and if **Use Custom Vector** is used, it is measured along the custom direction.

-    **Up To Face**: A face the pad will extrude up to, see [Options](#Options.md).

-    **Offset**: Offset from face in which the pad will end. This is only taken into account if the **Type** option **UpToLast**, **UpToFirst** or **UpToFace** is used.

-    **Refine**: <small>(v0.17)</small>  true or false. Cleans up residual edges left after the operation. This property is initially set according to the user\'s settings (found in *Preferences → Part design → General → Model settings*). It can be manually changed afterwards. This property will be saved with the FreeCAD document.

## Ограничения

-   Like all Part Design features, Pad creates a solid, thus the sketch must include a closed profile or it will fail with a *Failed to validate broken face* error. There can be multiple enclosed profiles inside a larger one, provided none intersect each other (for example, a rectangle with two circles inside it).
-   The algorithm used for **To First** and **To Last** is:
    -   Create a line through the centre of gravity of the sketch
    -   Find all faces of the support cut by this line
    -   Choose the face where the intersection point is nearest/furthest from the sketch

:   This means that the face that is found might not always be what you expected. If you run into this problem, use the **Up to face** type instead, and pick the face you want.
:   For the very special case of extrusion to a concave surface, where the sketch is larger than this surface, extrusion will fail. This is a unresolved bug.

-    {{VersionMinus|0.16}}There is no automatic cleanup, e.g. of adjacent planar surfaces into a single surface. You can fix this manually in the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> _ which creates a parametric feature.





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pad/ru
