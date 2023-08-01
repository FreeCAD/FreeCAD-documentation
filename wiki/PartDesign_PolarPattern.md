---
- GuiCommand:
   Name:PartDesign PolarPattern
   MenuLocation:Part Design - Apply a pattern - PolarPattern
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   SeeAlso:[PartDesign MultiTransform](PartDesign_MultiTransform.md)
---

# PartDesign PolarPattern

## Description

The <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:24px;"> **PartDesign PolarPattern** tool creates a polar pattern of one or more features.

 ![](images/PartDesign_PolarPattern_example.png )  
*A slot-shaped pocket (B) made on top of a base pad (A, also referred to as support) is used for a polar pattern. The result (C) is shown on the right.*

## Usage

### Create

1.  Optionally [activate](PartDesign_Body#Active_status.md) the correct Body.
2.  Optionally select one or more features in the [Tree view](Tree_view.md) or the [3D view](3D_view.md).
3.  There are several ways to invoke the tool:
    -   Press the **<img src="images/PartDesign_PolarPattern.svg" width=16px> [PolarPattern](PartDesign_PolarPattern.md)** button.
    -   Select the **Part Design → Apply a pattern → <img src="images/PartDesign_PolarPattern.svg" width=16px> PolarPattern** option from the menu.
4.  If there is no active Body, and there are two or more Bodies in the document, the **Active Body Required** dialog will open and prompt you to activate one. If there is a single Body it will be activated automatically.
5.  If no features were selected the **Select feature** [task panel](Task_panel.md) opens: select one or more (hold down the **Ctrl** key) from the list and press the **OK** button.
6.  The **PolarPattern parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
7.  Press the **OK** button to finish.

### Edit

1.  Do one of the following:
    -   Double-click the PolarPattern object in the [Tree view](Tree_view.md).
    -   Right-click the PolarPattern object in the [Tree view](Tree_view.md) and select **Edit PolarPattern** from the context menu.
2.  The **PolarPattern parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
3.  Press the **OK** button to finish.

## Options

-   To add features:
    1.  Press the **Add feature** button.
    2.  Select a feature in the [Tree view](Tree_view.md) or the [3D view](3D_view.md).
    3.  Repeat to add more features.
-   To remove features:
    1.  Press the **Remove feature** button.
    2.  Do one of the following:
        -   Select a feature in the [Tree view](Tree_view.md) or the [3D view](3D_view.md).
        -   Select a feature in the list and press the **Del** key.
        -   Right-click a feature in the list and select **Remove** from the context menu.
    3.  Repeat to remove more features.
-   If there are several features in the pattern, their order can be important. See [Ordering features](#Ordering_features.md).
-   Specify the **Axis** of the pattern:
    -   
        **Normal sketch axis**
        
        : The Z axis of the sketch (only available for sketch-based features).

    -   
        **Vertical sketch axis**
        
        : The Y axis of the sketch (idem).

    -   
        **Horizontal sketch axis**
        
        : The X axis of the sketch (idem).

    -   
        **Construction line #**
        
        : A separate entry for each construction line in the sketch (idem).

    -   
        **Base X axis**
        
        : The X axis of the Body.

    -   
        **Base Y axis**
        
        : The Y axis of the Body.

    -   
        **Base Z axis**
        
        : The Z axis of the Body.

    -   
        **Select reference...**
        
        : Select a [Datum Line](PartDesign_Line.md) in the [Tree view](Tree_view.md) or a [Datum Line](PartDesign_Line.md) or edge in the [3D view](3D_view.md).
-   Check the **Reverse direction** checkbox to reverse the pattern.
-   Specify the **Angle** to be covered by the pattern. If the angle is less than 360°, the instances are evenly distributed from 0° (first instance) to the given angle (last instance). If the angle is a full 360° circle, the instances are evenly distributed around the circle. This means that for n instances an angle of 360° is equivalent to an angle of 360°\*(1-1/n).
-   Specify the number of **Occurrences** (including the original feature).
-   If the **Update view** checkbox is checked the view will update in real time.

## Ordering features 

If some of the selected features are additive and others subtractive, their order can have have an impact on the final result. You can change the order by dragging individual features in the list.

 ![](images/PartDesign_feature-order.gif )  
*Effect of the feature order*

## Limitations

-   Any shape in the pattern that does not overlap the parent feature will be excluded. This ensures that a PartDesign Body always consists of a single, connected solid.
-   The PartDesign patterns are not yet as optimized as their Draft counterparts. So for a large number of instances you should consider using a [Draft PolarArray](Draft_PolarArray.md) instead, combined with a Part boolean operation. This may require major changes to your model as you are leaving PartDesign and therefore cannot simply continue with further PartDesign features in the same body. An example is shown in [this Forum topic](https://forum.freecadweb.org/viewtopic.php?f=3&t=55192).
-   A pattern cannot be applied directly to another pattern, be it polar, linear or a mirror. For this you need a [PartDesign MultiTransform](PartDesign_MultiTransform.md).




 {{PartDesign Tools navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign PolarPattern
