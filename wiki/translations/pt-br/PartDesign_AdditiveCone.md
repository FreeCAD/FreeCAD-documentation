---
- GuiCommand:
   Name:PartDesign AdditiveCone
   MenuLocation:Part Design → Create an additive primitive → Additive Cone
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   Version:0.17
   SeeAlso:[PartDesign Create an additive primitive](PartDesign_CompPrimitiveAdditive.md), [PartDesign Subtractive Cone](PartDesign_SubtractiveCone.md)
---

# PartDesign AdditiveCone/pt-br

## Description

Inserts a primitive cone in the active Body as the first feature, or fuses it to the existing feature(s).

<img alt="" src=images/PartDesign_AdditiveCone_example.png  style="width:200px;">

## Usage

1.  Press the **<img src="images/PartDesign_AdditiveCone.svg" width=24px> '''Additive Cone'''** button. **Note**: the Additive Cone is part of an icon menu labelled *Create an additive primitive*. After launching FreeCAD, the Additive Box is the one displayed in the toolbar. To get to the Cone button, click on the down arrow besides the visible icon and select Additive Cone in the menu.
2.  Set the Primitive parameters (for a complete cone, set one of the radii to zero) and the [Attachment](Part_EditAttachment.md).
3.  Click **OK**.
4.  A Cone feature appears under the active Body.

## Options

The Cone can be edited after its creation in two ways:

-   Double-clicking it in the Model tree, or by right-clicking and selecting **Edit primitive** in the contextual menu; this brings up the Primitive parameters.
-   Via the [Property editor](Property_editor.md).

## Properties

-    **Attachment**: defines the attachment mode as well as the Attachment Offset. See [Part EditAttachment](Part_EditAttachment.md).

-    **Label**: label given to the Cone object. Change to suit your needs.

-    **Radius1**: the radius value at the cone\'s base.

-    **Radius2**: the radius value at the cone\'s top. A non-zero value creates a truncated cone.

-    **Height**: the height of the cone along its axis.

-    **Angle**: angle of rotation of the cross section (360 degrees in a full cone).





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveCone/pt-br
