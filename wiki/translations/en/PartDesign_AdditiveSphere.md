---
- GuiCommand:
   Name:PartDesign AdditiveSphere
   MenuLocation:Part Design → Create an additive primitive → Additive Sphere
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   Version:0.17
   SeeAlso:[PartDesign CompPrimitiveAdditive](PartDesign_CompPrimitiveAdditive.md)
---

# PartDesign AdditiveSphere/en

## Description

Inserts a primitive sphere in the active Body as the first feature, or fuses it to the existing feature(s).

<img alt="" src=images/PartDesign_AdditiveSphere_example.png  style="width:200px;">

## Usage

1.  Press the **<img src="images/PartDesign_AdditiveSphere.svg" width=24px> '''Additive Sphere'''** button. **Note**: the Additive Sphere is part of an icon menu labelled *Create an additive primitive*. After launching FreeCAD, the Additive Box is the one displayed in the toolbar. To get the Sphere, click on the down arrow besides the visible icon and select Additive Sphere in the menu.
2.  Set the Primitive parameters and [Attachment](Part_EditAttachment.md).
3.  Click **OK**.
4.  A Sphere feature appears under the active Body.

## Options

The Sphere can be edited after its creation in two ways:

-   Double-clicking it in the Model tree, or by right-clicking and selecting **Edit primitive** in the contextual menu; this brings up the Primitive parameters.
-   Via the [Property editor](Property_editor.md).

## Properties

-    **Attachment**: defines the attachment mode as well as the Attachment Offset. See [Part EditAttachment](Part_EditAttachment.md).

-    **Label**: Label given to the Sphere object. Change to suit your needs.

-    **Radius**: Radius of the sphere.

-    **Angle1**: (labelled *V parameter* in the Primitive parameters) lower truncation of the sphere, parallel to the circular cross section (-90 degrees in a full sphere)

-    **Angle2**: (unlabelled in the Primitive parameters) upper truncation of the ellipsoid, parallel to the circular cross section (90 degrees in a full sphere).

-    **Angle3**: (labelled *U parameter* in the Primitive parameters) angle of rotation of the cross section (360 degrees in a full sphere).





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveSphere/en
