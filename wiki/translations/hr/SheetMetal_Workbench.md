


{{UnfinishedDocu

}} <img alt="Sheet Metal External workbench icon" src=images/Sheetmetal_workbench_icon.svg  style="width:128px;">

## Overview


{{TOCright}}

<img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:32px;"> **Sheet Metal** is an [external workbench](external_workbenches.md) evolved to design and unfold sheet metal parts. Therefore, it is not part of the standard FreeCAD install.

<img alt="" src=images/SheetMetal_Example.png  style="width:600px;"> 
*The sheet metal model built with the Sheet Metal add-on (rear); in front of it, the unfolded solid; at the forefront, the unfold sketch with bending lines for export to DXF.*

If the export in DXF is used to control machines (Lasercut for example), you have to modify the DXF to remove the lines showing the folds, as these lines may be used for cutting by the machine.

## Installation

This workbench can be installed from the [Addon Manager](Std_AddonMgr.md). For manual installation see [Installing more workbenches](Installing_more_workbenches.md).

## Tools

A detailed description of the tools can be found [on the author\'s blog](http://theseger.com/projects/2015/06/sheet-metal-addon-for-freecad/).

-   <img alt="" src=images/SheetMetal_AddBase.svg  style="width:32px;"> [Make Base Wall](SheetMetal_AddBase.md): Creates a sheetmetal wall from a sketch.

-   <img alt="" src=images/SheetMetal_AddWall.svg  style="width:32px;"> [Make Wall](SheetMetal_AddWall.md): Extends a wall from a side face of the metal sheet.

-   <img alt="" src=images/SheetMetal_Extrude.svg  style="width:32px;"> [Extend Face](SheetMetal_Extrude.md): Extends a face along normal.

-   <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:32px;"> [Fold a Wall](SheetMetal_AddFoldWall.md): Folds a face at the chosen line with specified bend radius.

-   <img alt="" src=images/SheetMetal_Unfold.svg  style="width:32px;"> [Unfold](SheetMetal_Unfold.md): Flattens folded sheet metal object and generates a solid and a sketch (provides a window to set parameters).

-   <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:32px;"> [Unattended Unfold](SheetMetal_UnattendedUnfold.md): Flattens folded sheet metal object and generates a solid and a sketch (if parameters have already been set).

-   <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:32px;"> [Add Corner Relief](SheetMetal_AddCornerRelief.md): Adds corner relief to a corner.

-   <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:32px;"> [Make Relief](SheetMetal_AddRelief.md): Adds relief to a corner.

-   <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:32px;"> [Make Junction](SheetMetal_AddJunction.md): Creates gap in the corner of two walls.

-   <img alt="" src=images/SheetMetal_AddBend.svg  style="width:32px;"> [Make Bend](SheetMetal_AddBend.md): Folds a face at the chosen line.

-   <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:32px;"> [Sketch On Sheet metal](SheetMetal_SketchOnSheet.md): Cuts hole in sheetmetal based on a sketch.

-   <img alt="" src=images/SheetMetal_Forming.svg  style="width:32px;"> [Make Forming in Wall](SheetMetal_Forming.md): Creates forming tool.

## Two complementary tools 

### Create a basic profile 

Omega-shaped tool: make a part from a simple multiline created in sketcher or draft, give it height and thickness centered, left or right of this line, be careful not to create selfintersection in closed folds of lesser space as the material thickness.

### Fold along a line 

Fold a \"flat\" base plate along a line (rectangle crossed out by a line): select the face, then the line and the tool, choose the angle, the radius, the side, the position of the fold relative to the line is not very well defined; it seems that the line is the intersection edge at the extension of the 2 faces.

## Limitations

-   The workbench is affected by the [topological naming issue](Glossary#Topological_Naming.md) that is inherent to FreeCAD. If an edit of a bend earlier in the history of the part renumbers the faces, then the following bends may be affected and switch faces. If the bend features do not break, you can double-click on it to get a dialog where you can select the proper face in the [3D view](3D_view.md), and update the Bend.
-   The Unfold tool has some limitations, and will fail in certain complex situations. When it fails, try to select a different face.
-   Frequent case of crash: take a lot of precautions not to cut in the hinges (the folds) either along the faces or in the angles nor to make holes or notches through the angles.

## Tutorials


<div class="mw-collapsible mw-collapsed toccolours" style="width:800px">

### Sheet Metal Tutorial by meme2704 

The following tutorial is reproduced from the PDF tutorial mentioned in [Links](#Links.md).


<div class="mw-collapsible-content">

#### Presentation of the workbench 

After downloading the extension and install, open it. ![](images/sm1.png )

#### 1st operation 

-   Get the base: use either the workbenches \"part\" or \"draft\", make 1 sketch that will contain all holes and any cuts, extrude this base to the thickness of the sheet.
-   Bear in mind that the edges will always be in addition as well as the folding radii.

![](images/sm2.png )

#### 2nd operation 

-   Open the Sheet\_metal workbench.
-   Select 1 thickness of the edge (edge) of the base plate and click on the \"bend\" tool 90° default bend angle can be changed from 0 to 90°.
-   Edge height is 10mm by default, editable from 0.1 to xxxmm.
-   Bending radius is by default equal to thickness, editable from 0.1 to xxmm (never put 0).
-   Gap1, gap2 is the withdrawal of the folded edge from the corner of the base (0 accept).
-   Invert default: false folds to Z +, true to ZReliefd cuts the corner between the fold and the base (inactive if gap = 0).
-   Reliefw adds 1 slot between the crop and the edge (inactive if reliefd = 0).

![](images/sm3.png ) Repeat as many times as there are sides to bend.
Folding 1 return with use of \"extend\".
![](images/sm4a.png ) To add 1 back repeat the same operation by selecting the thickness of the concerned edge.
To reduce the space between the 2 edges, use \"extends\".
Select the thickness and specify the length to add.
Note that if the extension of the 1st edge is made before the fold of the return, it will not be taken into account, if 1 identical fold is added to the extension, it will appear correct but the unfolding will not be done.
Folding of 1 2nd edge:
Now we must separate the 2 edges otherwise they will merge and unfolding will be impossible.
\* 1st method: make 1 withdrawal of 1 edge.

-   -   Give 1 value slightly greater than gap1 (or gap2), at zero there is still fusion.

-   2nd method make 1 cut at 45 ° see further, use this tool.

![](images/sm5a.png )

#### Unfolding

Choose 1 reference face (here the orange face) and click on the button in the toolbar.
We obtain the blue part of which it is enough to modify the values X, Y, or Z to see it in totality.
![](images/sm6.png )

#### Cut the flaps at 45° 

After folding the flaps without having made a withdrawal, the shape thus appears. ![](images/sm7a.png ) To do it must split at 45 ° (or following the bisector flaps are unequal width).
\* Create 1 new skit related to the common part of the 2 flaps.

-   Create 1 linked stop by selecting the outer edge of the \"hinge\".
-   Draw 1 triangle whose top is constrained at the end, oriented 1 side at 45 °, give the small side 1 minimum width (0.1mm is enough), and make 1 pocket.

Be careful not to scratch the \"hinge\" where the nakedness of bound the tip of the triangle at the edge of the fold line. ![](images/sm8a.png ) Unfolding ![](images/sm9.png )

#### Piercing edges and flaps 

Make these holes and cuts after folding and before unfolding.
Always take care not to \"scratch\" the fold lines.
![](images/sm10.png )

#### Make wired flaps 

Make 1 fold on the edge of the side, at 45 ° of 0.1mm long, then 1 other reverse at 45 ° of the length of the contiguous flap, then extend the opposite side, it will pass over and they will not be merged.
![](images/sm11.png )

#### Special case of this same pierced edge 

In this particular case, unfolding only works by choosing the yellow face as a reference.
![](images/sm12.png )

#### Special case hole straddling the folds 

Previously it is said several times that it is not necessary to cut the folding lines.
How to do ?
![](images/sm13.png )

-   Make the base with its half-round hole and make the 2 half-sided and the 2 half-folds separately.
-   Then make 1 extension on 1 of the sides of the width of the opening minus 0.1mm, the 2 edges thus remain separated.
-   Then on this extension (in green) draw the contour of the cut and make 1 pocket
-   The result is the red piece above, and the unfolding works, stays the line that separated the 2 edges previously

![](images/sm14.png )


</div>


</div>


{{TOCright}}

## Links

-   [Macro Sheet Metal Unfolder](Macro_Sheet_Metal_Unfolder.md), the original macro the Unfold tool is based on.
-   [Sheet Metal Workbench](https://forum.freecadweb.org/viewtopic.php?t=11303) announcement on the FreeCAD Forum
-   [An English and French tutorial in PDF format](https://forum.freecadweb.org/viewtopic.php?f=3&t=25002) on the FreeCAD forum
-   Files:
-   Reporting bugs/Request feartures: <https://github.com/shaise/FreeCAD_SheetMetal/issues>

## References

-   Author:
    -   Folding tools: Copyright 2015-2018 by Shai Seger
    -   Unfolding tool: Copyright 2014 by Ulrich Brammer
-   License: [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)
-   Official blog: [Sheet metal Addon for FreeCAD](http://theseger.com/projects/2015/06/sheet-metal-addon-for-freecad/)
-   Source code on github: <https://github.com/shaise/FreeCAD_SheetMetal>

## External workbenches 

FreeCAD workbenches are easy to program in [Python](Python.md), there are therefore many people developing additional workbenches outside of the FreeCAD main developers.

The [external workbenches](external_workbenches.md) page has some information and tutorials on some of them, and the [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) project aims at gathering them and making them easily installable from within FreeCAD.

New workbenches are in development, stay tuned!

[Category:SheetMetal{{\#translation:}}](Category:SheetMetal.md) [Category:Addons{{\#translation:}}](Category:Addons.md) [Category:External Command Reference{{\#translation:}}](Category:External_Command_Reference.md)
