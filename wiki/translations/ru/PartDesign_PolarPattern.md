---
- GuiCommand:/ru
   Name:PartDesign PolarPattern
   Name/ru:PartDesign PolarPattern
   Workbenches:[PartDesign](PartDesign_Workbench/ru.md), Complete
   MenuLocation:PartDesign -> Круговой массив
---

# PartDesign PolarPattern/ru


</div>

## Description

The **polar pattern** tool takes a selected feature and creates a set of copies rotated around a chosen axis. Starting with v0.17, it can pattern multiple features.

![](images/PartDesign_PolarPattern_example.png )

*Above: a slot-shaped pocket (B) made on top of a base solid (A, also referred to as support) is used for a polar pattern. The result (C) is shown on the right.*

## Usage

#### To create a pattern 

1.  (Optional) Select the feature (<small>(v0.19)</small>  or several features) to be patterned.
2.  Press the **<img src=images/PartDesign_PolarPattern.svg style="width:24px">** **PolarPattern** button.
    -   If you didn\'t initially select any features, you\'ll be able to select a *single* base feature
3.  Define the **Axis**. See [Options](#Options.md).
4.  Define the **Angle** between the last copied occurrence and the original feature.
5.  Set the number of **Occurrences**.
6.  If you have several features in the pattern, their order can be important, see the image below.
7.  Press **OK**.

#### Ordering features 

![](images/PartDesign_feature-order.gif ) 
*Effect of the feature order*


<small>(v0.19)</small> 

You can change the order by dragging the feature in the list and you will see the result immediately as preview.

#### Adding features 

###### v0.18

1.  Press **Add feature** to add a feature to be patterned. The feature must be visible in the [3D view](3D_view.md):
2.  Switch to the Model tree;
3.  Select in the tree the feature to be added and press **Spacebar** to make it visible in the [3D view](3D_view.md);
4.  Switch back to the Tasks panel;
5.  Select the feature in the 3D view; it will be added to the list.
6.  Repeat to add other features.

###### v0.19

1.  Press **Add feature** to add a feature to be patterned.
2.  Switch to the Model tree;
3.  Select in the tree the feature to be added.
4.  Repeat to add other features.

#### Removing features 

-   Right-click on the feature in the list and select *Remove*.

or

###### v0.18 

1.  Press **Remove feature** to remove a feature from the list. The feature must be visible in the [3D view](3D_view.md):
2.  Switch to the Model tree;
3.  Select in the tree the feature to be removed and press **Spacebar** to make it visible in the [3D view](3D_view.md);
4.  Switch back to the Tasks panel;
5.  Select the feature in the 3D view; it will have been removed from the list.
6.  Repeat to remove other features.

###### v0.19 

1.  Press **Remove feature** to remove a feature from the list.
2.  Switch to the Model tree;
3.  Select in the tree the feature to be removed.
4.  Repeat to remove other features.

## Options

![](images/Polarpattern_parameters.png )

### Axis

When creating a polar pattern feature, the *PolarPattern parameters* dialogue offers different ways of specifying the pattern rotation axis.

#### Normal sketch axis 

An axis being normal to the sketch and starting in the origin of the sketch of the feature being used is taken as axis for the polar pattern.
The pattern direction can be reversed by ticking \'Reverse direction\'.

#### Horizontal sketch axis 

Uses the horizontal axis of the sketch for axis.

#### Vertical sketch axis 

Uses the vertical axis of the sketch for axis.

#### Custom Sketch Axis 

If the sketch which defines the feature to be patterned also contains a construction line (or lines), then the drop down list will contain one custom sketch axis for each construction line. The first construction line will be labelled *Sketch axis 0*.

#### Base (X/Y/Z) axis 


<small>(v0.17)</small> 

Select one of the Body Origin\'s standard axis (X, Y or Z) as axis.

#### Select reference\... 

Allows you to select either a DatumLine or an edge of an object or a line of a sketch to use for axis.

### Angle and Occurrences 

Specifies the angle to be covered by the pattern, and the total number of pattern shapes (including the original feature). For example, four occurrences in an angle of 180 degrees would give a spacing of 60 degrees between patterns. There is one exception: If the angle is 360 degrees, since first and last occurrence are identical, four occurrences will be spaced 90 degrees apart. 


## Limitations

-   See [linear pattern feature limitations](PartDesign_LinearPattern#Limitations.md).








{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign PolarPattern/ru
