---
- GuiCommand:
   Name:PartDesign MoveFeatureInTree
   MenuLocation:Context menu - Move object after other object
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   Version:0.17
   SeeAlso:[PartDesign Set tip](PartDesign_MoveTip.md), [PartDesign Move object to other body](PartDesign_MoveFeature.md)
---

# PartDesign MoveFeatureInTree

## Description

<img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width:24px;"> [Move object after other object](PartDesign_MoveFeatureInTree.md), as this command is labeled in the context menu, allows reordering of objects under a Body. Sketches, datum geometry and features are supported.

## Usage

1.  In the Model tree, select the object(s) to be moved then right-click to open the context menu.
2.  Select **Move object after other object**.
3.  In the **Select feature** dialog, select the object under which to move the object(s).
4.  Press **OK**.

## Example

The following three pictures show the same model with a pocket defined on a sketch attached to the datum plane. The features are reordered from one picture to the other. This has the effect that the pocket makes either no hole or make holes in different pads, depending on the order of the features in the model tree.

 ![](images/PD_move_feature0.png ) ![](images/Hole_Pad002.png ) ![](images/PD_move_feature2.png ) 




 {{PartDesign Tools navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign MoveFeatureInTree
