---
- GuiCommand   *
   Name   *PartDesign AdditiveCylinder
   MenuLocation   *Part Design → Create an additive primitive → Additive Cylinder
   Workbenches   *[PartDesign](PartDesign_Workbench.md)
   Version   *0.17
   SeeAlso   *[PartDesign CompPrimitiveAdditive](PartDesign_CompPrimitiveAdditive.md), [PartDesign SubtractiveCylinder](PartDesign_SubtractiveCylinder.md)
---

# PartDesign AdditiveCylinder/en

## Description

Inserts a primitive cylinder in the active Body as the first feature, or fuses it to the existing feature(s).

<img alt="" src=images/PartDesign_AdditiveCylinder_example.png  style="width   *200px;">

## Usage

1.  Press the **<img src="images/PartDesign_AdditiveCylinder.svg" width=24px> '''Additive Cylinder'''** button. **Note**   * the Additive Cylinder is part of an icon menu labelled *Create an additive primitive*. After launching FreeCAD, the Additive Box is the one displayed in the toolbar. To get to the Cylinder button, click on the down arrow besides the visible icon and select Additive cylinder in the menu.
2.  Set the Primitive parameters and [Attachment](Part_EditAttachment.md).
3.  Click **OK**.
4.  A Cylinder feature appears under the active Body.

## Options

It is possible to create skewed cylinders by specifying angles in respect to the normal vector of the chosen attachment. <small>(v0.20)</small> 

The Cylinder can be edited after its creation in two ways   *

-   Double-clicking it in the Model tree, or by right-clicking and selecting **Edit primitive** in the contextual menu; this brings up the Primitive parameters.
-   Via the [Property editor](Property_editor.md).

## Properties

-    **Attachment**   * defines the attachment mode as well as the Attachment Offset. See [Part EditAttachment](Part_EditAttachment.md).

-    **Label**   * label given to the Cylinder object. Change to suit your needs.

-    **Radius**   * the radius value of the cylinder.

-    **Angle**   * angle of rotation of the cross section (360 degrees forms a full cylinder).

-    **Height**   * the height of the cylinder along its axis.

-    **First Angle**   * angle in first direction. <small>(v0.20)</small> 

-    **Second Angle**   * angle in second direction. <small>(v0.20)</small> 





{{PartDesign_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveCylinder/en
