---
 GuiCommand:
   Name: Points Structure
   MenuLocation: Points , Structured point cloud
   Workbenches: Points_Workbench
---

# Points Structure/pt-br

## Description

The **Points Structure** command creates a structured point cloud from the points of an existing scattered point cloud. A structured point cloud has the advantage that tessellation is much easier.

The command only works for point clouds whose points, when viewed from a certain direction, are organized in a regular 2D grid. These point clouds are typically produced by [structured-light 3D scanners](https://en.wikipedia.org/wiki/Structured-light_3D_scanner) and do not have undercuts. For complex objects, point clouds from many different view directions have to be combined.

## Usage

1.  The command assumes that the view direction of the point cloud is parallel to the Z axis of the global coordinate system. If this is not the case: adjust the point cloud object\'s **Placement** accordingly.
2.  Select the point cloud object.
3.  There are several ways to invoke the command:
    -   Press the **<img src="images/Points_Structure.svg" width=16px> [Structured point cloud](Points_Structure.md)** button.
    -   Select the **Points → <img src="images/Points_Structure.svg" width=16px> Structured point cloud** option from the menu.

## Properties

See [Points Convert](Points_Convert.md).





{{Points Tools navi

}}



---
⏵ [documentation index](../README.md) > [Points](Points_Workbench.md) > Points Structure/pt-br
