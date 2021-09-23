---
- GuiCommand:
   Name:PartDesign AdditiveTorus
   MenuLocation:Part Design → Create an additive primitive → Additive Torus
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   Version:0.17
   SeeAlso:[PartDesign CompPrimitiveAdditive](PartDesign_CompPrimitiveAdditive.md)
---

# PartDesign AdditiveTorus/pl

## Description

Inserts a primitive torus in the active Body as the first feature, or fuses it to the existing feature(s).

<img alt="" src=images/PartDesign_AdditiveTorus_example.png  style="width:200px;">

## Usage

1.  Press the **<img src="images/PartDesign_AdditiveTorus.svg" width=24px> '''Additive Torus'''** button. **Note**: the Additive Torus is part of an icon menu labelled *Create an additive primitive*. After launching FreeCAD, the Additive Box is the one displayed in the toolbar. To get the Torus, click on the down arrow besides the visible icon and select Additive Torus in the menu.
2.  Set the Primitive parameters and [Attachment](Part_EditAttachment.md).
3.  Click **OK**.
4.  A Torus feature appears under the active Body.

## Options

The Torus can be edited after its creation in two ways:

-   Double-clicking it in the Model tree, or by right-clicking and selecting **Edit primitive** in the contextual menu; this brings up the Primitive parameters.
-   Via the [Property editor](Property_editor.md).

## Properties

-    **Attachment**: defines the attachment mode as well as the Attachment Offset. See [Part EditAttachment](Part_EditAttachment.md).

-    **Label**: Label given to the Torus object. Change to suit your needs.

-    **Radius1**: Radius of the imaginary orbit around which the circular cross-section revolves. (The distance between the center of the torus and the center of the revolving cross section)

-    **Radius2**: Radius of the circular cross-section defining the form of the torus.

-    **Angle1**: (labelled *V parameter* in the Primitive parameters) lower truncation of the torus, parallel to the circular cross section (-180 degrees in a full torus). A bug in the sources causes unexpected results at changing Angle1.

-    **Angle2**: (unlabelled in the Primitive parameters) upper truncation of the ellipsoid, parallel to the circular cross section (180 degrees in a full torus). A bug in the sources causes unexpected results at changing Angle2.

-    **Angle3**: (labelled *U parameter* in the Primitive parameters) angle of rotation of the circular cross section (360 degrees in a full torus).





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveTorus/pl
