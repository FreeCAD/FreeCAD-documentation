---
- GuiCommand:
   Name:PartDesign AdditiveBox
   MenuLocation:Part Design → Create an additive primitive → Additive Box
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   Version:0.17
   SeeAlso:[PartDesign CompPrimitiveAdditive](PartDesign_CompPrimitiveAdditive.md), [PartDesign SubtractiveBox](PartDesign_SubtractiveBox.md)
---

# PartDesign AdditiveBox/pt-br

## Description

Inserts a primitive box in the active Body as the first feature, or fuses it to the existing feature(s).

<img alt="" src=images/PartDesign_AdditiveBox_example.png  style="width:200px;">

## Usage

1.  Press the **<img src="images/PartDesign_AdditiveBox.svg" width=24px> '''Additive Box'''** button. **Note**: the Additive Box is part of an icon menu labelled *Create an additive primitive*. After launching FreeCAD, the Additive Box is the one displayed in the toolbar. If a different primitive is displayed, click on the down arrow besides the icon and select Additive Box in the menu.
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
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveBox/pt-br
