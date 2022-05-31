---
- GuiCommand   *
   Name   *PartDesign Scaled
   Workbenches   *[PartDesign](PartDesign_Workbench.md)
   MenuLocation   *None (Option within PartDesign → MultiTransform)
---

# PartDesign Scaled

## Description

The <img alt="" src=images/PartDesign_Scaled.svg  style="width   *24px;"> **PartDesign Scaled** command turns a set of transformation results within a <img alt="" src=images/PartDesign_MultiTransform.svg  style="width   *16px;"> [MultiTransform](PartDesign_MultiTransform.md) feature into a sequence of scaled objects with evenly distributed scale factors. Starting with the unscaled base feature of the predefined transformation the scale factor is growing/declining until reaching the given value on the last item.

<img alt="" src=images/PartDesign_Scaled-01.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/PartDesign_Scaled-02.png  style="width   *300px;">



*Polar patterned pointer and linear patterned prism → Scaled polar pattern with 12 steps (occurrences) and scaled linear pattern with 3 steps*

If there is no predefined transformation within the current <img alt="" src=images/PartDesign_MultiTransform.svg  style="width   *16px;"> [MultiTransform](PartDesign_MultiTransform.md) feature, a scaled item will be placed at the same position as the base feature; this may result in unexpected shapes if the base feature isn\'t covered completely by the scaled object. And thus it is not recommendet to use **Scaled** as a single or a first transformation of a MultiTransform feature.

<img alt="" src=images/PartDesign_Scaled-03.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/PartDesign_Scaled-04.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/PartDesign_Scaled-05.png  style="width   *200px;">



*A holed base feature → Scaled object with 2 occurrences → Scaled object with 4 occurrences*

This command is not available from the menu nor does it have its own toolbar icon. It is incorporated into the <img alt="" src=images/PartDesign_MultiTransform.svg  style="width   *16px;"> [MultiTransform](PartDesign_MultiTransform.md) tool (<small>(v0.15)</small> ).

## Usage

### Scaling transformed features 

1.  There are two ways to reopen a <img alt="" src=images/PartDesign_MultiTransform.svg  style="width   *16px;"> [MultiTransform](PartDesign_MultiTransform.md) feature in the [Tree view](Tree_view.md)   *
    -   Right-click on the tree item and select **Edit MultiTransform** from the context menu.
    -   Double-cklick on the tree item.
2.  The MultiTransform parameters dialog will open in the [Task panel](Task_panel.md).
3.  Right-click in the **Transformations** list view and select **Add scaled transformation** from the context menu.
4.  A **Scaled** item is added to the Transformations list and the dialog will be extended at the bottom to allow to set the [options](#Options.md) **Factor** and **Occurrences**.
5.  Click the **OK** bar at the bottom to validate the options.
6.  Click the **OK** button at the top to close the MultiTransform parameters dialog.

### Scaling a single feature 

1.  Select a feature of the current body in the [Tree view](Tree_view.md).
2.  There are two ways to create a <img alt="" src=images/PartDesign_MultiTransform.svg  style="width   *16px;"> [MultiTransform](PartDesign_MultiTransform.md) feature   *
    -   Press the **![](images/)_[MultiTransform](PartDesign_MultiTransform.md)** button.
    -   Select the **Part Design → Apply a pattern → <img src="images/PartDesign_MultiTransform.svg" width=16px> Create MultiTransform** option from the menu.
3.  The MultiTransform parameters dialog will open in the [Task panel](Task_panel.md).
4.  Right-click in the **Transformations** list view and select **Add scaled transformation** from the context menu.
5.  A **Scaled** item is added to the Transformations list and the dialog will be extended at the bottom to allow to set the [options](#Options.md) **Factor** and **Occurrences**.
6.  Click the **OK** bar at the bottom to validate the options.
7.  Click the **OK** button at the top to close the MultiTransform parameters dialog.

## Options

When creating or editing a Scaled object, the \'MultiTransform parameters\' dialogue offers the following options   *

### List of features 

The list of base features that are handled by this MultiTransform object.

   *   See <img alt="" src=images/PartDesign_MultiTransform.svg  style="width   *16px;"> [MultiTransform, Usage](PartDesign_MultiTransform#Usage.md) for details about adding and removing features.

### List of transformations 

The list of transformations that are use by this MultiTransform object.

   *   See <img alt="" src=images/PartDesign_MultiTransform.svg  style="width   *16px;"> [MultiTransform, Usage](PartDesign_MultiTransform#Usage.md) for details about adding and removing transformations.

### Parameters

-   **Factor**   * The factor to which the last feature is to be scaled.
-   **Occurrences**   * Number of steps from unscaled (1) to Factor (including base and last feature).
    -   Scaled transformations accept the number of occurrences of the predefined transformation as maximum value or any integer divisor of that number returning integer results. (12, 6, 4, 3, or 2 for 12 occurrences of a Linear or Polar Pattern)
    -   Scaled single features accept any integer number larger than 1.

## Notes

-   The centre of scaling is the item\'s centre of gravity and that may cause   *
    -   An item that is growing through the parent feature.

       *   Protruding geometry on the opposite side is not trimmed automatically.

    -   A shrinking item that is losing the contact with the parent feature.

       *   A fully detached item just disappears.

    -   A shrinking pocket that is hiding invisible inside the parent feature.

       *   Void spaces inside are hard to detect.

## Limitations

-   See [linear pattern feature](PartDesign_LinearPattern.md) for other limitations
-   See [MultiTransform](PartDesign_MultiTransform.md) for more details

## Examples

![c\|center\|800px](images/mt_example2.png ) The smallest pad was first patterned three times in X direction and then scaled to factor two (so the three occurrences have scaling factor 1.0, 1.5 and 2.0). Then a polar pattern was applied with 8 occurrences.

Since the scaling is done with respect to the center of gravity, in the case of a pad, it is necessary that the pad penetrate also in the main body, otherwise the scaled objects are floating, detached from the body. To have a pad that intersects the main body can be used \"two dimensions\" type or \"symmetric to plane\" option.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Scaled
