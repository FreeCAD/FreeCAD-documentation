---
- GuiCommand   *
   Name   *PartDesign SubtractiveCone
   MenuLocation   *Part Design → Create a subtractive primitive → Subtractive Cone
   Workbenches   *[PartDesign](PartDesign_Workbench.md)
   Version   *0.17
   SeeAlso   *[PartDesign CompPrimitiveSubtractive](PartDesign_CompPrimitiveSubtractive.md), [PartDesign AdditiveCone](PartDesign_AdditiveCone.md)
---

# PartDesign SubtractiveCone/en

## Description

Inserts a subtractive cone in the active Body. Its shape is subtracted from the existing solid.

![](images/PartDesign_SubtractiveCone_example.png )

*On the left   * active body (A) shown in grey and subtractive cone (B) shown in transparent red; result on the right.*

## Usage

1.  Press the **<img src="images/PartDesign_SubtractiveCone.svg" width=24px> '''Subtractive Cone'''** button. **Note**   * the Subtractive Cone is part of an icon menu labelled *Create a subtractive primitive*. After launching FreeCAD, the Subtractive Box is the one displayed in the toolbar. To get to the Cone button, click on the down arrow besides the visible icon and select Subtractive Cone in the menu.
2.  Set the Primitive parameters (for a complete cone, set one of the radii to zero) and the [Attachment](Part_EditAttachment.md).
3.  Click **OK**.
4.  A Cone feature appears under the active Body.

## Options

The Cone can be edited after its creation in two ways   *

-   Double-clicking it in the Model tree, or by right-clicking and selecting **Edit primitive** in the contextual menu; this brings up the Primitive parameters.
-   Via the [Property editor](Property_editor.md).

## Properties

-    **Attachment**   * defines the attachment mode as well as the Attachment Offset. See [Part EditAttachment](Part_EditAttachment.md).

-    **Label**   * label given to the Cone object. Change to suit your needs.

-    **Radius1**   * the radius value at the cone\'s base.

-    **Radius2**   * the radius value at the cone\'s top. A non-zero value creates a truncated cone.

-    **Height**   * the height of the cone along its axis.

-    **Angle**   * angle of rotation of the cross section (360 degrees in a full cone).





{{PartDesign_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveCone/en
