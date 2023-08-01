---
- GuiCommand:
   Name:PartDesign SubtractiveWedge
   MenuLocation:Part Design - Create a subtractive primitive - Subtractive Wedge
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   Version:0.17
   SeeAlso:[PartDesign CompPrimitiveSubtractive](PartDesign_CompPrimitiveSubtractive.md), [PartDesign AdditiveWedge](PartDesign_AdditiveWedge.md)
---

# PartDesign SubtractiveWedge/pt-br

## Description

Inserts a subtractive wedge in the active Body. Its shape is subtracted from the existing solid.

![](images/PartDesign_SubtractiveWedge_example.svg ) *On the left: active body (A) shown in grey and subtractive wedge (B) shown in transparent red; result on the right.*

## Usage

1.  Press the **<img src="images/PartDesign_SubtractiveWedge.svg" width=24px> '''Subtractive Wedge'''** button. **Note**: the Subtractive Wedge is part of an icon menu labelled *Create an additive primitive*. After launching FreeCAD, the Subtractive Box is the one displayed in the toolbar. To get the Wedge, click on the down arrow besides the visible icon and select Subtractive Wedge in the menu.
2.  Set the Primitive parameters and [Attachment](Part_EditAttachment.md).
3.  Click **OK**.
4.  A Wedge feature appears under the active Body.

## Options

The Wedge can be edited after its creation in two ways:

-   Double-clicking it in the Model tree, or by right-clicking and selecting **Edit primitive** in the contextual menu; this brings up the Primitive parameters.
-   Via the [Property editor](Property_editor.md).

## Properties

Using the default placement, the below inputs are:

-    **X min/max**: Base face X axis span

-    **Y min/max**: Wedge height span

-    **Z min/max**: Base face Z axis span

-    **X2 min/max**: Top face X axis span

-    **Z2 min/max**: Top face Z axis span

## Pyramids

Wedges can be used to create pyramids by setting **X2 min/max** and **Z2 min/max** each so that min = max.





{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveWedge/pt-br
