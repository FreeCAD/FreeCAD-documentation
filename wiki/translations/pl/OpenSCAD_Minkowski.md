---
- GuiCommand:
   Name:OpenSCAD Minkowski
   MenuLocation:OpenSCAD → Minkowski
‏‎   Workbenches:[OpenSCAD](OpenSCAD_Workbench.md)
---

# OpenSCAD Minkowski/pl

## Description

Applies a Minkowski sum to selected shapes.

### Mathematical Definition 

Add each element of subset A to each element of subset B to get Minkowski sum.

### Geometrical Definition 

Sweep element A along all boundaries of element B. Resulting space which is occupied by both elements is Minkowski sum.

![An example of a Minkowski sum](images/Minkowski_example.jpg )

Example of Minkowski sum applied to cylinder and cube. Note: that the height of minkowski sum is height of cylinder plus height of cube.

## Usage

1.  Select shapes in [Tree view](Tree_view.md) or in [3D view](3D_view.md)
2.  Click on <img alt="" src=images/OpenSCAD_Minkowski.svg  style="width:32px;"> or choose ** OpenSCAD** → **<img src="images/OpenSCAD_Minkowski.svg" width=32px> Minkowski** from the top menu.

## Limitations

Feature needs OpenSCAD installed and configured in **Edit** → **Preferences**

## Notes





{{OpenSCAD_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD Minkowski/pl
