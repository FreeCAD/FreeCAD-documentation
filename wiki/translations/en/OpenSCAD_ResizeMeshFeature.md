---
- GuiCommand   *
   Name   *OpenSCAD ResizeMeshFeature
   MenuLocation   *OpenSCAD → Resize Mesh Feature
   Workbenches   *[OpenSCAD](OpenSCAD_Workbench.md)
---

# OpenSCAD ResizeMeshFeature/en

## Description

Creates a new resized mesh object with independent sizing for each axis.

## Usage

1.  Select the mesh object to be resized.
2.  Click the ** OpenSCAD** → **<img src="images/OpenSCAD_ResizeMeshFeature.svg" width=24px> Scale Resize Feature...** menu.
3.  Select the desired axis in the dialog, or enter your own custom axis to use and click OK.

-   A new mesh object is created and resized, the original object is rendered hidden.

## Limitations

-   The new mesh object is not parametric to the original mesh object, which means any changes to the original object do not get reflected in the new mirrored object.

## Notes

-   The function does not modify the existing mesh, but returns a new mesh.
-   The function can be accessed via python   *


```python
import OpenSCADUtils
import Mesh
#this assumes an existing object in the document named "Mesh" that you wish to mirror
original_mesh = App.ActiveDocument.Mesh
resized_mesh = OpenSCADUtils.resizemesh(original_mesh.Mesh, FreeCAD.Base.Vector(100,50,40))
#New mesh would be 100 mm on the x axis, 50 mm on the y axis, and 40 mm on the z axis.
Mesh.show(resized_mesh)
```





{{OpenSCAD_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD ResizeMeshFeature/en
