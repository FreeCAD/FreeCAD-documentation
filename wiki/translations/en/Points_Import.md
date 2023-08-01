---
- GuiCommand:
   Name: Points Import
   MenuLocation: Points - Import points...
   Workbenches: [Points](Points_Workbench.md)
   SeeAlso: [Import Export](Import_Export.md)
---

# Points Import/en

## Description

The **Points Import** command imports a point cloud from a file.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Points_Import.svg" width=16px> [Points Import](Points_Import.md)** button.
    -   Select the **Points → <img src="images/Points_Import.svg" width=16px> Import Points...** option from the menu.
2.  Select a point cloud file.
3.  Press the **Open** button.

## Properties

See [Points Convert](Points_Convert.md).

## Point cloud file format 

-   A point cloud file must have the **.asc**, **.pcd** or **.ply** extension.
-   Each line in the file must list the X, Y and Z coordinates of a point.
-   The coordinates must be separated by spaces.
-   The coordinates must use a decimal point, not a decimal comma.

## Sample point cloud file 

0 0 0
1.4562 -7.2354 12.2367
5.9423 3.1728 -17.6439

For testing you can use [this file](https://raw.githubusercontent.com/FreeCAD/Examples/master/Point_cloud_ExampleFiles/PointCloud-Data_Stanford-Bunny.asc), which is a low polygon version of the [Stanford Bunny](http://graphics.stanford.edu/data/3Dscanrep/).





{{Points Tools navi

}}



---
⏵ [documentation index](../README.md) > [Points](Points_Workbench.md) > Points Import/en
