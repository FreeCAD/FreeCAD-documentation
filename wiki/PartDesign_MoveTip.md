---
- GuiCommand:
   Name:PartDesign MoveTip
   MenuLocation:Contextual menu → Set tip
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   Version:0.17
   SeeAlso:[PartDesign Move object to other body](PartDesign_MoveFeature.md), [PartDesign Move object after other object](PartDesign_MoveFeatureInTree.md)
---

# PartDesign MoveTip

## Description

<img alt="" src=images/PartDesign_MoveTip.svg  style="width:24px;"> [Set tip](PartDesign_MoveTip.md), as this command is labeled in the context menu, redefines the tip, which is the feature exposed outside of the Body. By default, the tip is the last feature added to the Body; but sometimes it can be useful to temporarily set the tip to a feature earlier in the tree. This may be done to add a sketch, datum geometry or a feature which in retrospect should have been created earlier in the Body\'s history.

The tip is visually distinguished in the Model tree by a small white down arrow in a green circle overlayed on the feature\'s icon. For example, the following feature is the tip:

 ![](images/PartDesign_Body_tree-04.png ) 

## Usage

1.  In the Model tree, right-click on the feature to set as tip.
2.  Select from the list in the context menu <img alt="" src=images/PartDesign_MoveTip.svg  style="width:24px;"> **Set tip**.
3.  The new tip is set to visible, and all elements below the tip are hidden from view. Elements newly created from that point will be placed under the tip, and above the other existing elements.

**Note**: It is important not to forget to set the tip again to the last feature at the bottom of the Body tree.




 {{PartDesign Tools navi}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign MoveTip
