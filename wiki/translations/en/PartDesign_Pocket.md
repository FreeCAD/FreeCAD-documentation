---
- GuiCommand:
   Name: PartDesign Pocket
   MenuLocation: Part Design -> Create a substractive feature -> Pocket
   Workbenches: PartDesign_Workbench
   SeeAlso: PartDesign_Pad
---

# PartDesign Pocket/en

## Description

The **Pocket** tool cuts solids by extruding a sketch or a face of a solid along a straight path.

![](images/PartDesign_Pocket_example.svg ) *Sketch profile (A) was mapped to the top face of base solid (B); result after pocketing through on the right.*

## Usage

1.  Select the sketch or face to be pocketed. <small>(v0.20)</small> : Alternatively you can select several sketches or faces.
2.  Press the **<img src="images/PartDesign_Pocket.svg" width=16px> '''Pocket'''** button.
3.  Set the Pocket parameters, see the [Options](#Options.md) below.
4.  Click **OK**.

When selecting a single sketch, it can have multiple enclosed profiles inside a larger one, for example a rectangle with two circles inside it. But the profiles may not intersect each other. <small>(v0.20)</small> 

## Options

When creating a pocket, the the **Pocket parameters** dialog will be shown. It offers the following settings:

![](images/pocket_parameters_cropped.png )

### Type

Type offers five different ways of specifying the length to which the pocket will be extruded:

#### Dimension

Enter a numeric value for the length of the pocket. The default direction for extrusion is into the support, but it can be changed by ticking the **Reversed** option. Extrusions occur by default [normal](http://en.wikipedia.org/wiki/Surface_normal) to the defining sketch plane. This can be changed by specifying another **Direction** <small>(v0.20)</small> . With the option **Symmetric to plane** the pocket will extend half of the given length to either side of the plane. Negative dimensions are not possible. Use the **Reversed** option instead.

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

### Taper angle 


<small>(v0.20)</small> 

Tapers the pocket in the extrusion direction by the given angle. A positive angle means the outer pocket border gets wider. This option is only available if **Type** is either **Dimension** or **Two dimensions**. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts.

Limitations:

-   Sketches containing [B-Splines](B-Splines.md) often cannot be properly tapered. This is a limitation of the [OpenCASCADE](OpenCASCADE.md) kernel that FreeCAD uses.
-   For larger angles tapering will fail if the end face of the pocket would have fewer edges than the start face/sketch.

### 2nd length 

Defines the length of the pocket in the opposite extrusion direction. Multiple units can be used independently of the user\'s units preferences (m, cm, mm, nm, ft or \', in or \"). This option is only available if **Type** is **Two dimensions**.

### 2nd taper angle 


<small>(v0.20)</small> 

Tapers the pocket in the opposite extrusion direction by the given angle. A positive angle means the outer pocket border gets wider. This option is only available if **Type** is **Two dimensions**. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts.

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

-   Use the type **Dimension** or **Through All** wherever possible because the other types sometimes give trouble when they are being patterned
-   Otherwise, the pocket feature has the same [limitations](PartDesign_Pad#Limitations.md) as the Pad feature.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pocket/en
