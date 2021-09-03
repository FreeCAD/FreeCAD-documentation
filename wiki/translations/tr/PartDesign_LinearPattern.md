---
- GuiCommand:
   Name:PartDesign LinearPattern
   MenuLocation:PartDesign → Apply a pattern → LinearPattern
   Workbenches:[PartDesign](PartDesign_Workbench.md)
---

## Tanım

The **<img src=images/PartDesign_LinearPattern.svg style="width:24px"> '''LinearPattern'''** tool creates evenly spaced copies of a feature in a linear direction. As of <small>(v0.17)</small>  the Linear pattern tool can pattern multiple features.

![](images/PartDesign_LinearPattern_example.svg )

\'\'Above: An L-shaped pad (B) made on top of a base pad (A, also referred to as *support*) is used for a linear pattern. The result (C) is shown on the right.\'\'

## Usage

To create a pattern:

1.  Select the feature (<small>(v0.19)</small>  or several features) to be patterned.
2.  Press the **<img src=images/PartDesign_LinearPattern.svg style="width:24px"> '''LinearPattern'''** button.
3.  Define the **Direction**. See [Options](#Options.md).
4.  Define the **Length** (distance) between the last copied occurrence and the original feature.
5.  Set the number of **Occurrences**.
6.  If you have several features in the pattern, their order can be important, see for example the image in the [PolarPattern feature](PartDesign_PolarPattern#Usage.md). <small>(v0.19)</small>  You can change the order by dragging the feature in the list and you will see the result immediately as preview.
7.  Press **OK**.

To add or remove features from an existing pattern:

1.  Press **Add feature** to add a feature to be patterned. The feature must be visible in the [3D view](3D_view.md):
    1.  Switch to the Model tree;
    2.  Select in the tree the feature to be added and press **Space** to make it visible in the [3D view](3D_view.md);
    3.  Switch back to the Tasks panel;
    4.  Select the feature in the 3D view; it will be added to the list.
    5.  Repeat to add other features.
2.  Press **Remove feature** to remove a feature from the list, or right-click on the feature in the list and select **Remove**

## Options

![LinearPattern parameters in v0.16 and below.](images/Linearpattern_parameters.png ) ![LinearPattern parameters in v0.17 and above.](images/Linearpattern_parameters_v017.png )

### Direction

When creating a linear pattern feature, the **LinearPattern parameters** dialogue offers different ways of specifying the pattern direction.

#### Horizontal sketch axis 

Uses the horizontal axis of the sketch for direction.

#### Vertical sketch axis 

Uses the vertical axis of the sketch for direction.

#### Normal sketch axis 


<small>(v0.17)</small> 

Uses the normal axis of the sketch for direction.

#### Select reference\... 

Allows you to select either a DatumLine or an edge of an object or a line of a sketch to use for direction.

#### Custom Sketch Axis 

If the sketch which defines the feature to be patterned also contains a construction line (or lines), then the drop down list will contain one custom sketch axis for each construction line. The first construction line will be labelled *Sketch axis 0*.

#### Base (X/Y/Z) axis 


<small>(v0.17)</small> 

Select one of the Body Origin\'s standard axis (X, Y or Z) as direction. 

## Limitations

-   Pattern shapes may not overlap one another except for the special case of only two occurrences (original plus one copy)
-   Any pattern shapes that do not overlap the original\'s support will be excluded. This ensures that a PartDesign feature always consists of a single, connected solid
-   The PartDesign patterns are not yet as optimized as their Draft counterparts. So for a bigger number of instances you should consider using [Draft array](Draft_OrthoArray.md) instead, combined with a Part boolean operation. This may include major changes to your model as you are leaving PartDesign, which means that you cannot simply continue with further PartDesign features in the same body. An example is shown in this [Forum topic](https://forum.freecadweb.org/viewtopic.php?f=3&t=55192)
-   For further limitations, see the [PartDesign mirrored](PartDesign_Mirrored.md) feature.





{{PartDesign Tools navi

}} 
