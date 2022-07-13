# Design456 Workbench
**This workbench is under heavy development**

## Introduction

<img alt="Design456 External workbench icon" src=images/Design456_workbench_icon.svg  style="width   *128px;"> {{TOCright}}

The Design456 workbench is an [External workbench](external_workbenches.md) that plans to implement a Direct Modeling methodology in FreeCAD. Think \'push and pull geometry\' that one finds in CAD suites like SketchUp and Fusion360. The original idea came to live when the developer of Design456 wanted to do the basic tasks which is simple and easy to do in 123D Design. FreeCAD could do the same job but the tools aren\'t interfaced in that way. This workbench will not keep track of old shapes. It tries to clean up the garbage which might be produced during running under commands. It tries to make the tree as simple as possible. Parameters must be decided during the desired manipulations which cannot be changed later.

This Wikipage is not updated regularly. To get the latest tool-list, you need to look at Design456 github or youtube videos. Only one developer is working on this project, and time to update these all documents is missing unfortunately.

## Background

Traditionally, FreeCAD employs a Parametric Modeling methodology which is a powerful and scalable approach. It is also has been an industry standard. But I wish to have another approach. My workbench will try to implement direct modeling which is not provided at the moment by FreeCAD.

## Installation

Download the Design456 workbench via the <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Addon Manager](Std_AddonMgr.md) 
**Tools → Addon Manager**

##### Note   *

If the above is not working for you please consider    *

-   Addon manager no longer works in FreeCAD 0.18 due to changes in Github use FreeCAD 0.20 instead.
-   Invoke the Addon Manager - Tools \| Adddon manager.
-   Select Configure..Into Custom repositories enter <https   *//github.com/MariwanJ/Design456>.
-   Then OK.
-   Restart FreeCAD.

## References

-   Developer   * \@MariwanJ (Mariwan Jalal)
-   Youtube channel    * [(used to announce new updates 2022-01-20)](https   *//www.youtube.com/user/BestofMyDream)
-   Github   * <https   *//github.com/MariwanJ/Design456> (used to announce new updates 2022-01-20)
-   Discussion   * <https   *//forum.freecadweb.org/viewtopic.php?f=8&t=54893> (Not used anymore 2022-01-20)

## Tools

### 2D Drawing and manipulation tools 

-   <img alt="" src=images/Design456_3Point.svg  style="width   *32px;"> [Design456 Arc3Points](Design456_3Point.md)   * Use this tool to create an Arc from 3 vertices.
-   <img alt="" src=images/Design456_MultiPointsToWireClose.svg  style="width   *32px;"> [Design456 MultiPointsToWireClose](Design456_MultiPointsToWireClose.md)   * Use this tool to create a series of lines between points selected in series(closed).
-   <img alt="" src=images/Design456_MultiPointsToWireOpen.svg  style="width   *32px;"> [Design456 MultiPointsToWireOpen](Design456_MultiPointsToWireOpen.md)   * Use this tool to create a series of lines between points selected in series (open).
-   <img alt="" src=images/Design456_2DTrimLine.svg  style="width   *32px;"> [Design456 Trim a line](Design456_2DTrim.md)   * Use this tool delete a line/wire.
-   <img alt="" src=images/2D_ExtendLine.svg  style="width   *32px;"> [Design456 Extend a line or a wire](Design456_2DExtend.md)   * Use this tool to extend any wire or line .

### 3D Drawing and manipulation tools 

-   <img alt="" src=images/Design456_Extrude.svg  style="width   *32px;"> [Design456 Extrude](Design456_Extrude.md)   * Use this tool to extrude any face of 2D or 3D object.
-   <img alt="" src=images/Design456_Extract.svg  style="width   *32px;"> [Design456 Extract Face](Design456_Extract.md)   * Use this tool to extract a face, edge or vertex from any object.
-   <img alt="" src=images/Design456_PartMerge.svg  style="width   *32px;"> [Design456 3D PartMerge](Design456_PartMerge.md)   * Use this tool to merge 3D objects.
-   <img alt="" src=images/simplifyCompound.svg  style="width   *32px;"> [Design456 Simplify Compound Obects](Design456_SimplifyCompound.md)   * Use this tool to simplify faces of 3D objects.
-   <img alt="" src=images/Design456_PartSubtract.svg  style="width   *32px;"> [Design456 3D PartSubtract](Design456_PartSubtract.md)   * Use this tool to subtract/cut 3D objects.
-   <img alt="" src=images/Design456_PartIntersect.svg  style="width   *32px;"> [Design456 3D Parts Intersect](Design456_PartIntersect.md)   * Use this tool to create new object which is common between two shapes intersecting each other.
-   <img alt="" src=images/Design456_LoftOnDirection.svg  style="width   *32px;"> [Design456 Loft on direction](Design456_LoftOnDirection.md)   * Use this tool create new 3D object based on the face you select and the scale you choose.
-   <img alt="" src=images/Design456_PartGroup.svg  style="width   *32px;"> [Design456 3D Part Grouping](Design456_PartGroup.md)   * Use this tool to collect several parts in one group.
-   <img alt="" src=images/Design456_PartCompound.svg  style="width   *32px;"> [Design456 3D Part Compound](Design456_PartCompound.md)   * Use this tool to compound different parts.
-   <img alt="" src=images/PartDesign_Shell.svg  style="width   *32px;"> [Design456 3D Part Shell](Design456Part_Shell.md)   * Use this tool to make Shell.
-   <img alt="" src=images/DivideObject.svg  style="width   *32px;"> [Design456 3D Divide Object](Design456_DivideObject.md)   * Use this tool to divide 3D object faces.
-   <img alt="" src=images/Design456_SplitObject.svg  style="width   *32px;"> [Design456 Split a 3D object](Design456_SplitObject.md)   * Use this tool to split any 3D object.
-   <img alt="" src=images/PartDesign_Fillet.svg  style="width   *32px;"> [Design456 3D Fillet](Design456Part_Fillet.md)   * Use this tool to create fillet.
-   <img alt="" src=images/PartDesign_Chamfer.svg  style="width   *32px;"> [Design456 3D Chamfer](Design456Part_Chamfer.md)   * Use this tool to create Chamfer.
-   <img alt="" src=images/LoftBetweenFaces.svg  style="width   *32px;"> [Design456 3D loft between faces](Design456_LoftBetweenFaces.md)   * Use this tool to fill gap between faces by creating a loft between them.
-   <img alt="" src=images/UnifySplitFuse2.svg  style="width   *32px;"> [Design456 3D unify or split and then fuse](Design456_unifySplitFuse2.md)   * Use this tool create diff shapes. (Might be removed in the future)
-   <img alt="" src=images/Design456_Colorize.svg  style="width   *32px;"> [Design456 Colorize 3D object-faces](Design_ColorizeObject.md)   * Use this colorize randomly 3D object (each face will get a random color).

### Alignment tools 

-   <img alt="" src=images/Design456_PartMagnet.svg  style="width   *32px;"> [Design456 Magnet](Design456_PartMagnet.md)   * Use this tool align an object on another one by selecting the target face.
-   <img alt="" src=images/Design456_AlignToPlane.svg  style="width   *32px;"> [Design456 Align to plane](Design456_AlignToPlane.md)   * Use this tool to align object(s) on the surface of the plane.
-   <img alt="" src=images/Design456_TopSideView.svg  style="width   *32px;"> [Design456 Top Side View](Design456_TopSideView.md)   * Use this tool align camera and working plane to the Top side.
-   <img alt="" src=images/Design456_BottomSideView.svg  style="width   *32px;"> [Design456 Bottom Side View](Design456_BottomView.md)   * Use this tool align camera and working plane to the Bottom side.
-   <img alt="" src=images/LeftSideView.svg  style="width   *32px;"> [Design456 Left Side View](Design456_LeftSideView.md)   * Use this tool align camera and working plane to the Left side.
-   <img alt="" src=images/Design456_RightSideView.svg  style="width   *32px;"> [Design456 Right Side View](Design456_RightSideView.md)   * Use this tool align camera and working plane to the Right side.
-   <img alt="" src=images/FrontSideView.svg  style="width   *32px;"> [Design456 Front Side View](Design456_FrontSideView.md)   * Use this tool align camera and working plane to the Front side.
-   <img alt="" src=images/BackSideView.svg  style="width   *32px;"> [Design456 Back Side View](Design456_BackSideView.md)   * Use this tool align camera and working plane to the Back side.
-   <img alt="" src=images/Design456_MoveObject.svg  style="width   *32px;"> [Design456 Move Object](Design456_MoveObject.md)   * Move, rotate 3D Objects.
-   <img alt="" src=images/Design456_MoveObjectDetails.svg  style="width   *32px;"> [Design456 Move Object in details](Design456_MoveObjectDetails.md)   * Move, rotate 3D and 2D Objects.
-   <img alt="" src=images/Design456_SmartAlignment.svg  style="width   *32px;"> [Design456 Align multiple objects](Design456_SmartAlignment.md)   * Do 9 alignments based on shapes bound boxes.

### [FreeCAD Direct Modeling](FreeCAD_Direct_Modeling.md) 

Main goal of Design456 is to provide Direct Modeling tool set. There are some tools that are partially finished or ready to use. Please try them and report your comments at the github pages. This wiki will be updated whenever I have time. It is almost certain that the github has more info than these pages (at the moment due to lack of time for updating the wiki pages)

-   smart Scale
-   smart DirectScale
-   smart Fillet
-   smart Chamfer
-   smart Extrude
-   smart Extrude Rotate
-   smart Edge Extend
-   smart Face Extend
-   smart Alignment
-   Extend Edge
-   Extend Face
-   Paint
-   Hole
-   Reset Placement
-   Simplify Edges
-   Simplify Faces

##### Note   * 

-   Please notice that there is no released version yet for this workbench. Intensively development is ongoing and bug is expected for the tools. Don\'t use it on serious document yet. Make a copy of you object and apply my tools. By that you know if it works for you or not without taking risk.

### [FreeCAD GUI Widgets toolkit](FreeCAD_GUI_Widgets_toolkit.md) 

Fr\_Widget system is a work for providing easy to use Coin3D drawing GUI toolkit. The toolkit will make it easy to draw and should provide an interactive way to manipulate FreeCAD e objects. The simplicity of the toolkit should make it easy to use it.

Widgets gives you the ability to get callbacks, and are inspired by the well known multi-platform toolkit www.fltk.org. Almost all smart tools must have a widget from this toolkit.

### Defeaturing WB added to Design456 

I added the workbench to my workbench and further development of the tools will continue. It was necessary to add the de-featuring tools to Design456. More tools must be added to the tool set in the feature.

-   Tobe continued!

### Microelly2 Tools (Nurbs WB) converted 

I did the conversion for the Nurbs and fixed many bugs. In the beginning I added the project to my WB, but since the tools are not working well, I remove it. The work is huge and there were places where I didn\'t know how to solve the issues. More time required and more understanding of Microlley\'s work is required that is why the work on the project is suspended. Some good works are done and you can find the project at    * <https   *//github.com/MariwanJ/nurbs> Unfortunately, the code is more experimental code that is not made to be a tool in a workbench. Due to that, I wasn\'t able to retrieve all tools and it is hard to understand the tools. Most of the code are undocumented. There are good things there but not structured in a way a workbench requires. Note   * Due to what I described, further developing Nurbs WB is not possible, at least for now.


{{Design456 Tools navi

}} 

[Category   *External Workbenches](Category_External_Workbenches.md) [Category   *Addons](Category_Addons.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [External Workbenches](Category_External Workbenches.md) > [Addons](Category_Addons.md) > [Design456](Category_Design456.md) > Design456 Workbench
