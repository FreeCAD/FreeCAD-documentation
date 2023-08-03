---
 GuiCommand:
   Name: PartDesign AdditiveWedge
   MenuLocation: Part Design , Create an additive primitive , Additive Wedge
   Workbenches: PartDesign_Workbench
   Version: 0.17
   SeeAlso: PartDesign_CompPrimitiveAdditive, PartDesign_SubtractiveWedge
---

# PartDesign AdditiveWedge

## Description

Inserts a primitive wedge in the active Body as the first feature, or fuses it to the existing feature(s).

 <img alt="" src=images/PartDesign_AdditiveWedge_example.png  style="width:200px;"> 

## Usage

1.  Press the **<img src="images/PartDesign_AdditiveWedge.svg" width=24px> '''Additive Wedge'''** button. **Note**: the Additive Wedge is part of an icon menu labelled *Create an additive primitive*. After launching FreeCAD, the Additive Box is the one displayed in the toolbar. To get the Wedge, click on the down arrow besides the visible icon and select Additive Wedge in the menu.
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




 {{PartDesign_Tools_navi}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveWedge
