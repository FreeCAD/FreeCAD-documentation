# <img alt="CurvedShapes Workbench icon" src=images/CurvedShapes_workbench_icon.svg  style="width:64px;"> CurvedShapes Workbench

 

## Introduction

Curved Shapes is a FreeCAD [external workbench](External_workbenches.md) that creates 3D shapes from 2D curves.

## Installation

Recommended installation is through the FreeCAD <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) via the 
**Tools → Addon Manager**

## Tools

-   <img alt="" src=images/CurvedShapes_CurvedArray.svg  style="width:24px;"> [CurvedArray](CurvedShapes_CurvedArray.md): Creates an array and resizes the items in the bounds of one or more hull curves.
-   <img alt="" src=images/CurvedShapes_CurvedSegment.svg  style="width:24px;"> [CurvedSegment](CurvedShapes_CurvedSegment.md): Interpolates between two 2D curves. The interpolated curves can be resized in the bounds of some hullcurves.
-   <img alt="" src=images/CurvedShapes_InterpolatedMiddle.svg  style="width:24px;"> [InterpolatedMiddle](CurvedShapes_InterpolatedMiddle.md): Interpolates a 2D shape into the middle between two 2D curves. The base shapes can be connected to a shape with a sharp corner.
-   <img alt="" src=images/CurvedShapes_SurfaceCut.svg  style="width:24px;"> [SurfaceCut](CurvedShapes_SurfaceCut.md): Cuts a surface to get the outline curve or a face. This tool is similar to <img alt="" src=images/Part_CrossSections.svg  style="width:24px;"> [Cross-Sections](Part_CrossSections.md) in the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part workbench](Part_Workbench.md), but it is fully parametric and has an option to reduce the complexity of the output curve. It tries to remove overlapping edges.

### Examples

-   <img alt="" src=images/CurvedShapes_HortenHIX.svg  style="width:24px;"> [HortenHIX](CurvedShapes_HortenHIX.md): A Python script that creates the shape of the [Horten Ho 229 (also called Horten H IX)](https://en.wikipedia.org/wiki/Horten_Ho_229), a stealth fighter that has been build in Germany in 1944.
-   <img alt="" src=images/CurvedShapes_FlyingWingS800.svg  style="width:24px;"> [FlyingWingS800](CurvedShapes_FlyingWingS800.md): A Python script that creates the shape of a flying wing radio-controlled model.

## References

-   Author: \@chbergmann
-   Github repo: <https://github.com/chbergmann/CurvedShapesWorkbench>

## Related

-   [Curves Workbench](Curves_Workbench.md)
-   [AirPlaneDesign Workbench](https://github.com/FredsFactory/FreeCAD_AirPlaneDesign)

## External Workbenches 

 

[<img src="images/Property.png" style="width:16px"> External Workbenches](Category_External_Workbenches.md) [<img src="images/Property.png" style="width:16px"> Addons](Category_Addons.md)

---
[documentation index](../README.md) > [External Workbenches](Category_External Workbenches.md) > CurvedShapes Workbench
