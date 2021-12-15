# PartDesign Pocket/ro
---
- GuiCommand:   Name:PartDesign Pocket   Workbenches:[[PartDesign Workbench   PartDesign]], Complete|MenuLocation:PartDesign → Pocket---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Instrumentul **Pocket** așchiază un solid prin extrudarea unei schițe în traiectorie dreaptă și extrăgând-o din solid.


</div>

![](images/PartDesign_Pocket_example.svg ) \'\'Sketch profile (A) was mapped to the top face of base solid (B); result after pocketing through on the right. \'\'

## Usage


<div class="mw-translate-fuzzy">

## Cum se foloseșste 

1.  Select the sketch to be pocketed.

    :   v0.16 and below The sketch must be mapped to the planar face of an existing solid or Part Design feature, or an error message will appear.
2.  Press the **<img src="images/PartDesign_Pocket.png" width=16px> '''Pocket'''** button.
3.  Set the Pocket parameters (see next section).
4.  Click OK.


</div>


<div class="mw-translate-fuzzy">

## Opțiuni

![](images/Pocket_options.png )


</div>

When creating a pocket, the the **Pocket parameters** dialog will be shown. It offers the following settings:

![](images/pocket_parameters_cropped.png )

### Type

Type offers four different ways of specifying the length to which the pocket will be extruded:

### Dimension


<div class="mw-translate-fuzzy">

Atunci când se creează un pocket, dialogul **Pocket parameters** oferă cinci căi diferite de specificare a lungimii(adâncimii) la care buzunarul va fi extrudat:

### Dimension 

Enter a numeric value for the depth of the pocket. The default direction for extrusion is into the support. Extrusions occur [normal](http://en.wikipedia.org/wiki/Surface_normal) to the defining sketch plane. Negative dimensions are not possible. Use the **Reversed** option instead.

### To first 

The pocket will extrude up to the first face of the support in the extrusion direction. In other words, it will cut through all material until it reaches an empty space.

### Through all 

The pocket will cut through all material in the extrusion direction. With the option **Symmetric to plane** the pad will cut through all material in both directions.

### Up to face 

The pocket will extrude up to a face in the support that can be chosen by clicking on it.

### Two dimensions 

v0.17 and above This allows to enter a second length in which the pad should extend in the opposite direction (into the support). Again can be changed by ticking the **Reversed** option.


</div>

#### Through all 

The pocket will extrude through all objects in the extrusion direction. With the option **Symmetric to plane** the pad will cut through all material in both directions.**Note:** For technical reasons, *Through All* is actually a 10 meter deep pocket. If you need deeper pockets, use the type **Dimension**.

#### To first 

The pocket will extrude up to the first face of the support in the extrusion direction. In other words, it will cut through all material until it reaches an empty space.

#### Up to face 

The pocket will extrude up to a face in the model that can be chosen by clicking on it.

#### Two dimensions 

This allows to enter a second length in which the pocket should extend in the opposite direction (into the support). The directions can be switched by ticking the **Reversed** option.

### Length

Defines the length of the pocket. Multiple units can be used independently of the user\'s units preferences (m, cm, mm, nm, ft or \', in or \"). This option is only available when **Type** is either **Dimension** or **Two dimensions**.

### Offset to face 

Offset from face at which the pocket will end. This option is only available when **Type** is either **Through all**, **To first** or **Up to face**.

### Direction


<small>(v0.20)</small> 

#### Direction/edge

You can select the direction of the extrusion:

-   **Face/Sketch normal** The sketch or face is extruded along its normal. If you have selected several sketches or faces to be extruded, the normal of the first one will be used. <small>(v0.20)</small> 
-   **Select reference\...** The sketch is extruded along an edge of the 3D model. When this is method selected, you can click on any edge in the 3D model and it becomes the direction vector for the extrusion.
-   **Custom direction** The sketch is extruded along a direction that can be specified via vector values.

#### Show direction 

If checked, the pocket direction will be shown. In case the pocket uses a **Custom direction**, it can be changed.

#### Length along sketch normal 

If checked, the pocket length is measured along the sketch normal, otherwise along the custom direction.

### Symmetric to plane 

Tick the checkbox to extrude half of the given length to either side of the sketch or plane.

### Reversed

Reverses the direction of the pocket.

## Properties

-    **Type**: Type of ways how the pocket will be extruded, see [Options](#Options.md).

-    **Length**: Defines the length of the pocket, see [Options](#Options.md).

-    **Length2**: Second pocket length in case the **Type** is **TwoLengths**, see [Options](#Options.md).

-    **Use Custom Vector**: <small>(v0.20)</small>  If checked, the pocket direction will not be the normal vector of the sketch but the given vector, see [Options](#Options.md).

-    **Direction**: <small>(v0.20)</small>  Vector of the pocket direction if **Use Custom Vector** is used.

-    **Along Sketch Normal**: <small>(v0.20)</small>  If *true*, the pocket length is measured along the sketch normal. Otherwise and if **Use Custom Vector** is used, it is measured along the custom direction.

-    **Up To Face**: A face the pocket will extrude up to, see [Options](#Options.md).

-    **Refine**: True or false. Cleans up residual edges left after the operation. This property is initially set according to the user\'s settings (found in **Preferences → Part design → General → Model settings**). It can be manually changed afterwards. This property will be saved with the FreeCAD document.

## Limitations


<div class="mw-translate-fuzzy">

## Limitări

-   Use the type **Dimension** or **Through All** wherever possible because the other types sometimes give trouble when they are being patterned
-   Otherwise, the pocket feature has the same [limitations](PartDesign_Pad#Limitations.md) as the pad feature.


</div>





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pocket/ro
