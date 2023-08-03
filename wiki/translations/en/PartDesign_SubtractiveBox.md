---
 GuiCommand:
   Name: PartDesign SubtractiveBox
   MenuLocation: Part Design , Create a subtractive primitive , Subtractive box
   Workbenches: PartDesign_Workbench
   Version: 0.17
   SeeAlso: PartDesign_CompPrimitiveSubtractive, PartDesign_AdditiveBox
---

# PartDesign SubtractiveBox/en

## Description

Inserts a subtractive box in the active Body. Its shape is subtracted from the existing solid.

![](images/PartDesign_SubtractiveBox_example.png ) *On the left: active body (A) shown in grey and subtractive box (B) shown in transparent red; result on the right.*

## Usage

1.  Press the **<img src="images/PartDesign_SubtractiveBox.svg" width=24px> '''Subtractive Box'''** button. **Note**: the Subtractive Box is part of an icon menu labelled *Create a subtractive primitive*. After launching FreeCAD, the Subtractive Box is the one displayed in the toolbar. If a different primitive is displayed, click on the down arrow besides the icon and select Subtractive Box in the menu.
2.  Set the Primitive parameters and [Attachment](Part_EditAttachment.md).
3.  Click **OK**.
4.  A Box feature appears under the active Body.

## Options

The Box can be edited after its creation in two ways:

-   Double-clicking it in the Model tree, or by right-clicking and selecting **Edit primitive** in the contextual menu; this brings up the Primitive parameters.
-   Via the [Property editor](Property_editor.md).

## Properties

-    **Attachment**: defines the attachment mode as well as the Attachment Offset. See [Part EditAttachment](Part_EditAttachment.md).

-    **Label**: Label given to the Box object. Change to suit your needs.

-    **Length**: the Box\'s dimension in the X-direction.

-    **Width**: the Box\'s dimension in the Y-direction.

-    **Height**: the Box\'s dimension in the Z-direction.





{{PartDesign_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveBox/en
