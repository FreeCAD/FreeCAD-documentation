# Design456 Workbench
**This workbench is under heavy development**

## Introduction

<img alt="Design456 External workbench icon" src=images/Design456_workbench_icon.svg  style="width:128px;"> {{TOCright}}

The Design456 workbench is an [External workbench](external_workbenches.md) that plans to implement a Direct Modeling methodology in FreeCAD. Think \'push and pull geometry\' that one finds in CAD suites like SketchUp and Fusion360. The original idea came to live when the developer of Design456 wanted to do the basic tasks which is simple and easy to do in 123D Design. FreeCAD could do the same job but the tools aren\'t interfaced in that way. This workbench will not keep track of old shapes. It tries to clean up the garbage which might be produced during running under commands. It tries to make the tree as simple as possible. Parameters must be decided during the desired manipulations which cannot be changed later.

## Background

Traditionally, FreeCAD employs a Parametric Modeling methodology which is a powerful and scalable approach. It is also has been an industry standard. But I wish to have another approach. My workbench will try to implement direct modeling which is not provided at the moment by FreeCAD.

## Installation

Download the Design456 workbench via the <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Addon_Manager.md) 
**Tools → Addon Manager**

##### Note:

If the above is not working for you please consider :

-   Addon manager no longer works in FreeCAD 0.18 due to changes in Github use FreeCAD 0.19 instead.
-   Invoke the Addon Manager - Tools \| Adddon manager.
-   Select Configure..Into Custom repositories enter <https://github.com/MariwanJ/Design456>.
-   Then OK.
-   Restart FreeCAD.

## References

-   Developer: \@MariwanJ (Mariwan Jalal)
-   Github: <https://github.com/MariwanJ/Design456>
-   Discussion: <https://forum.freecadweb.org/viewtopic.php?f=8&t=54893>

## Tools

### 2D Drawing and manipulation tools 

-   <img alt="" src=images/Design456_3Point.svg  style="width:32px;"> [Design456 Arc3Points](Design456_3Point.md): Use this tool to create an Arc from 3 vertices.
-   <img alt="" src=images/Design456_MultiPointsToWireClose.svg  style="width:32px;"> [Design456 MultiPointsToWireClose](Design456_MultiPointsToWireClose.md): Use this tool to create a series of lines between points selected in series(closed).
-   <img alt="" src=images/Design456_MultiPointsToWireOpen.svg  style="width:32px;"> [Design456 MultiPointsToWireOpen](Design456_MultiPointsToWireOpen.md): Use this tool to create a series of lines between points selected in series (open).
-   <img alt="" src=images/Design456_2DTrimLine.svg  style="width:32px;"> [Design456 Trim a line](Design456_2DTrim.md): Use this tool delete a line/wire.
-   <img alt="" src=images/2D_ExtendLine.svg  style="width:32px;"> [Design456 Extend a line or a wire](Design456_2DExtend.md): Use this tool to extend any wire or line .

### 3D Drawing and manipulation tools 

-   <img alt="" src=images/Design456_Extrude.svg  style="width:32px;"> [Design456 Extrude](Design456_Extrude.md): Use this tool to extrude any face.
-   <img alt="" src=images/Design456_Extract.svg  style="width:32px;"> [Design456 Extract Face](Design456_Extract.md): Use this tool to extract a face from a 3D object.
-   <img alt="" src=images/Design456_ExtrudeFace.svg  style="width:32px;"> [Design456 Extrude Face](Design456_ExtrudeFace.md): Use this tool to extract a face from a 3D object and extrude it.
-   <img alt="" src=images/Design456_Tweak.svg  style="width:32px;"> [Design456 Tweak](Design456_Tweak.md): Use this tool to move a subshape of the object.
-   <img alt="" src=images/Design456_SplitObject.svg  style="width:32px;"> [Design456 Split a 3D object](Design456_SplitObject.md): Use this tool to split any 3D object.
-   <img alt="" src=images/Design456_LoftOnDirection.svg  style="width:32px;"> [Design456 Loft on direction](Design456_LoftOnDirection.md): Use this tool create new 3D object based on the face you select and the scale you choose.
-   <img alt="" src=images/Design456_PartMerge.svg  style="width:32px;"> [Design456 3D PartMerge](Design456_PartMerge.md): Use this tool to merge 3D objects.
-   <img alt="" src=images/Design456_PartSubtract.svg  style="width:32px;"> [Design456 3D PartSubtract](Design456_PartSubtract.md): Use this tool to subtract/cut 3D objects.
-   <img alt="" src=images/Design456_PartIntersect.svg  style="width:32px;"> [Design456 3D Parts Intersect](Design456_PartIntersect.md): Use this tool to create new object which is common between two shapes intersecting each other.
-   <img alt="" src=images/Design456_PartGroup.svg  style="width:32px;"> [Design456 3D Part Grouping](Design456_PartGroup.md): Use this tool to collect several parts in one group.
-   <img alt="" src=images/Design456_PartCompound.svg  style="width:32px;"> [Design456 3D Part Compound](Design456_PartCompound.md): Use this tool to compound different parts.

### Alignment tools 

-   <img alt="" src=images/Design456_PartMagnet.svg  style="width:32px;"> [Design456 Magnet](Design456_PartMagnet.md): Use this tool align an object on another one by selecting the target face.
-   <img alt="" src=images/Design456_AlignToPlane.svg  style="width:32px;"> [Design456 Align to plane](Design456_AlignToPlane.md): Use this tool to align object(s) on the surface of the plane.
-   <img alt="" src=images/Design456_TopSideView.svg  style="width:32px;"> [Design456 Top Side View](Design456_TopSideView.md): Use this tool align camera and working plane to the Top side.
-   <img alt="" src=images/Design456_BottomSideView.svg  style="width:32px;"> [Design456 Bottom Side View](Design456_BottomView.md): Use this tool align camera and working plane to the Bottom side.
-   <img alt="" src=images/Design456_LeftSideView.svg  style="width:32px;"> [Design456 Left Side View](Design456_LeftSideView.md): Use this tool align camera and working plane to the Left side.
-   <img alt="" src=images/Design456_RightSideView.svg  style="width:32px;"> [Design456 Right Side View](Design456_RightSideView.md): Use this tool align camera and working plane to the Right side.
-   <img alt="" src=images/Design456_FrontSideView.svg  style="width:32px;"> [Design456 Front Side View](Design456_FrontSideView.md): Use this tool align camera and working plane to the Front side.
-   <img alt="" src=images/Design456_BackSideView.svg  style="width:32px;"> [Design456 Back Side View](Design456_BackSideView.md): Use this tool align camera and working plane to the Back side.
-   <img alt="" src=images/Design456_MoveObject.svg  style="width:32px;"> [Design456 Move Object](Design456_MoveObject.md): Move, rotate 3D Objects.
-   <img alt="" src=images/Design456_MoveObjectDetails.svg  style="width:32px;"> [Design456 Move Object in details](Design456_MoveObjectDetails.md): Move, rotate 3D and 2D Objects.

### [FreeCAD Direct Modeling](FreeCAD_Direct_Modeling.md) 

The main WB development is on this part at the moment. There are some (almost- finished) commands developed, and the development of this part is ongoing. The following are available ..

-   smart Scale
-   smart DirectScale
-   smart Fillet
-   samrt Chamfer
-   smart Extrude

##### Note: 

Please notice that there is no version released yet for this workbench. Intensively development is ongoing and bug is expected on the tools. Don\'t use it on serious document yet.

### [FreeCAD GUI Widgets toolkit](FreeCAD_GUI_Widgets_toolkit.md) 

Fr\_Widget system is a beginning work for the Coin3D and the QT drawing GUI toolkit. The toolkit will make it easy to make drawing and provides an interactive way to manipulate the objects. The simplicity of the toolkit should make it easy to use it. It will be well documented. Looking at the Devbranch at my github, you will find some widget that are already made. But it is just the beginning. More details will come after finishing the Nurbs tools. The toolkit will be a flavor of FLTK toolkit.

### Microelly2 Tools converted 

I did the conversion for the Nurbs and fixed many bugs. In the begning I added the project to my WB, but since the tools are not working well, I remove it. The work is huge and there were places where I didn\'t know how to solve the issues. More time required and more understanding of Microlley\'s work is required that is why the work on the project is suspended. Some good works are done and you can find the project at : <https://github.com/MariwanJ/nurbs>

-   Tobe continued!


{{Design456 Tools navi

}} 

[Category:External Workbenches](Category:External_Workbenches.md) [Category:Addons](Category:Addons.md)

---
[documentation index](../README.md) > Design456 Workbench
