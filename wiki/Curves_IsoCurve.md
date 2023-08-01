---
- GuiCommand:
   Name:Curves IsoCurve
   MenuLocation:Surfaces - IsoCurve
   Workbenches:[Curves](Curves_Workbench.md)
   SeeAlso:[Curves JoinCurves](Curves_JoinCurve.md)
---

# Curves IsoCurve

## Description

The <img alt="" src=images/Curves_IsoCurve.svg  style="width:24px;"> [Curves IsoCurve](Curves_IsoCurve.md) tool applies a UV oriented lattice on to a selected surface. This tool is part of the [external workbench](External_workbenches.md) called [Curves](Curves_Workbench.md).

<img alt="" src=images/Curves_IsoCurve_Demo.jpg  style="width:600" height="400px;"> 
*Above: shows the before (left) and after (right) surface applied IsoCurve*

## Usage

1.  Switch to the <img alt="" src=images/Curves_workbench_icon.svg  style="width:24px;"> [Curves](Curves_Workbench.md) workbench (install from <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) is necessary, if not previously installed)
2.  Select an unique surface on the [3D view](3D_view.md)
3.  To invoke the command, do one of the following:
    -   Press the <img alt="" src=images/Curves_IsoCurve.svg  style="width:24px;"> button
    -   Use the **Surfaces → IsoCurve** entry from the Curves menu
4.  A UV oriented lattice on the surface is created.
5.  Change `NumberU` or/and `NumberV` to get more curves.

## Notes

-   Curves can be extracted as a subelement (e.g: with [Curves JoinCurves](Curves_JoinCurve.md)) for others uses or just to help to visualize the shape.

## Limitations

## Properties

## Scripting




 {{Curves Tools navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Curves](Category_Curves.md) > Curves IsoCurve
