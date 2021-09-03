---
- GuiCommand:/ru
   Name:PartDesign Pocket
   Name/ru:PartDesign Pocket
   Workbenches:[PartDesign](PartDesign_Workbench/ru.md), Complete
   MenuLocation:PartDesign → Карман
---


</div>

## Description

The **Pocket** tool cuts out a solid by extruding a sketch (or a face of the solid) in a straight path and subtracting it from the solid.

![](images/PartDesign_Pocket_example.svg ) \'\'Sketch profile (A) was mapped to the top face of base solid (B); result after pocketing through on the right. \'\'

## Usage

1.  Select the sketch to be pocketed.

    :   The sketch must be mapped to the planar face of an existing solid or Part Design feature, or an error message will appear. {{VersionMinus|0.16}}
2.  Press the **<img src="images/PartDesign_Pocket.svg" width=16px> '''Pocket'''** button.
3.  Set the Pocket parameters (see next section).
4.  Click OK.

## Options

![](images/Pocket_options.png )

When creating a pocket, the **Pocket parameters** dialogue offers five different ways of specifying the length (depth) to which the pocket will be extruded:

### Dimension

Enter a numeric value for the depth of the pocket. The default direction for extrusion is into the support. Extrusions occur [normal](http://en.wikipedia.org/wiki/Surface_normal) to the defining sketch plane. Negative dimensions are not possible. Use the **Reversed** option instead.

### To first {#to_first}

The pocket will extrude up to the first face of the support in the extrusion direction. In other words, it will cut through all material until it reaches an empty space.

### Through all {#through_all}

The pocket will cut through all material in the extrusion direction. With the option **Symmetric to plane** the pad will cut through all material in both directions.**Note:** For technical reasons, *Through All* is actually a 10 meter deep pocket. If you need deeper pockets, use *Dimension*.

### Up to face {#up_to_face}

The pocket will extrude up to a face in the support that can be chosen by clicking on it.

### Two dimensions {#two_dimensions}

This allows to enter a second length in which the pocket should extend in the opposite direction (into the support). Again can be changed by ticking the **Reversed** option. <small>(v0.17)</small> 

## Limitations

-   Use the type **Dimension** or **Through All** wherever possible because the other types sometimes give trouble when they are being patterned
-   Otherwise, the pocket feature has the same [limitations](PartDesign_Pad#Limitations.md) as the pad feature.

## Useful links {#useful_links}

An [example](http://forum.freecadweb.org/viewtopic.php?f=3&t=3733&start=10) with the practice on the forum.





{{PartDesign Tools navi

}} 
