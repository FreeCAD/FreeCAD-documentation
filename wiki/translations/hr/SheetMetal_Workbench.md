# SheetMetal Workbench/hr
}

<img alt="Sheet Metal External workbench icon" src=images/Sheetmetal_workbench_icon.svg  style="width:128px;">




## Introduction

<img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:32px;"> [Sheet Metal](SheetMetal_Workbench.md) is an [external workbench](External_workbenches.md) and does not belong to the standard FreeCAD installation. It has been developed to supply tools to create and unfold sheet metal objects.

Characteristics of sheet metal objects are:

-   They have a constant thickness
-   They can be unfolded, if they are made of planar walls and cylindrical connections only

The unfolding tool in both of its versions is not restricted to parts made with tools from this workbench, but can handle [Part](Part_Workbench.md) and [PartDesign](PartDesign_Workbench.md) objects as well, as long as they meet above characteristics.

<img alt="" src=images/SheetMetal_Example.png  style="width:600px;"> 
*The sheet metal model built with the Sheet Metal add-on (rear); in front of it, the unfolded solid; at the forefront, the unfold sketch with bending lines for export to DXF.*

If the export in DXF is used to control machines (Lasercut for example), you have to modify the DXF to remove the lines showing the folds, as these lines may be used for cutting by the machine.

## Installation

This workbench can be installed from the [Addon Manager](Std_AddonMgr.md). For manual installation see [Installing more workbenches](Installing_more_workbenches.md).

## Tools

A detailed description of the tools can be found [on the author\'s blog](http://theseger.com/projects/2015/06/sheet-metal-addon-for-freecad/). It\'s a bit outdated now, since some new tools have been added.

-   <img alt="" src=images/SheetMetal_AddBase.svg  style="width:32px;"> [Make Base Wall](SheetMetal_AddBase.md): Creates a sheet metal base object from a sketch, either a profile or a plate.

-   <img alt="" src=images/SheetMetal_AddWall.svg  style="width:32px;"> [Make Wall](SheetMetal_AddWall.md): Adds a flange on each selected edge of a base plate. (The flange can be turned into a hem by modifying its angle.)

-   <img alt="" src=images/SheetMetal_Extrude.svg  style="width:32px;"> [Extend Face](SheetMetal_Extrude.md): Extends a sheet metal plate at a selected edge face along its normal. (By adding an outline sketch it can be used to create interlocking geometry.)

-   <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:32px;"> [Fold a Wall](SheetMetal_AddFoldWall.md): Folds a face at a chosen line with a specified bend radius.

-   <img alt="" src=images/SheetMetal_Unfold.svg  style="width:32px;"> [Unfold](SheetMetal_Unfold.md): Flattens a folded sheet metal object and generates an unfold solid and an outline sketch with bend lines (provides a dialog to set parameters).

-   <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:32px;"> [Unattended Unfold](SheetMetal_UnattendedUnfold.md): Flattens a folded sheet metal object and generates an unfold solid and an outline sketch with bend lines (if parameters have already been set).

-   <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:32px;"> [Add Corner Relief](SheetMetal_AddCornerRelief.md): Adds a corner relief to a corner.

-   <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:32px;"> [Make Relief](SheetMetal_AddRelief.md): 1st step to convert a shell object into an unfoldable sheet metal object, adds a relief (cutout) to a corner.

-   <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:32px;"> [Make Junction](SheetMetal_AddJunction.md): 2nd step to convert a shell object into an unfoldable sheet metal object, creates an open junction on the edge of two walls.

-   <img alt="" src=images/SheetMetal_AddBend.svg  style="width:32px;"> [Make Bend](SheetMetal_AddBend.md): 3rd step to convert a shell object into an unfoldable sheet metal object, replaces sharp edges with round bends.

-   <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:32px;"> [Sketch On Sheet metal](SheetMetal_SketchOnSheet.md): Cuts a sketch based hole pattern along the folded walls of a sheet metal object.

-   <img alt="" src=images/SheetMetal_Forming.svg  style="width:32px;"> [Make Forming in Wall](SheetMetal_Forming.md): Embosses shapes with or without holes into a sheet metal plate.

-   <img alt="" src=images/SheetMetal_BaseShape.svg  style="width:32px;"> [Add base shape](SheetMetal_BaseShape.md): Adds a basic sheet metal object from parameters.

## Brief description 

This workbench provides tools for the two main tasks:

-   Create sheet metal objects
-   Unfold sheet metal objects

This section is meant to give a rough idea of how to use the supplied tools. More detailed information can be found on each tool\'s own page (see above) or in the linked tutorials (see below).

### Create a sheet metal object 

#### Start with a profile 

1.  Create an open polyline (preferably with the sketcher)
2.  Use the <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Make Base Wall](SheetMetal_AddBase.md) command to create a sheet metal profile.

#### Start with a blank 

1.  Create a closed polyline (preferably with the sketcher)
2.  Use the <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Make Base Wall](SheetMetal_AddBase.md) command to create a sheet metal blank.

#### Start with a PartDesign Pad 

1.  Create a closed polyline (preferably with the sketcher)
2.  Use the <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [PartDesign Pad](PartDesign_Pad.md) command to create a prismatic body.
3.  The <img alt="" src=images/PartDesign_Thickness.svg  style="width:16px;"> [PartDesign Thickness](PartDesign_Thickness.md) command will make it an object of constant thickness.
4.  To make it unfoldable it needs some gaps or connections between the walls:
    1.  The <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> [Make Relief](SheetMetal_AddRelief.md) command will cut off selected corners.
    2.  The <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> [Make Junction](SheetMetal_AddJunction.md) command will create junctions with gaps between adjoining walls that need to be disjoined.
    3.  The <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> [Make Bend](SheetMetal_AddBend.md) command will create cylindrical connections for the remaining walls that need to stay joined.

Some parameters will be inherited from the parent object(s) but it is better to check the relevant parameters at each stage.

It should now be checked if the resulting sheet metal object can be unfolded. (see [Unfold\...](#Unfold_a_sheet_metal_object.md) below).

#### Adding more features 

The unfoldable basic sheet metal objects can be extended:

1.  Use the <img alt="" src=images/SheetMetal_Extrude.svg  style="width:16px;"> [Extend Face](SheetMetal_Extrude.md) command to enlarge walls.
2.  The <img alt="" src=images/SheetMetal_AddWall.svg  style="width:16px;"> [Make Wall](SheetMetal_AddWall.md) command will add new flanges or hems to the existing object.
3.  Use the <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:16px;"> [Add Corner Relief](SheetMetal_AddCornerRelief.md) command to add or reshape corner reliefs.
4.  The <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:16px;"> [Fold a Wall](SheetMetal_AddFoldWall.md) command will fold a wall at a chosen line, i.e. it will trimm a wall at said line, relocate the cut away side, and rejoin them with a cylindrical connection.
5.  Use the <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:16px;"> [Sketch on Sheet metal](SheetMetal_SketchOnSheet.md) command to cut holes into the object starting on a chosen wall and then following the adjoined walls and connections.
6.  The <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> [Make Forming in Wall](SheetMetal_Forming.md) command will stamp a shape into a plate (wall).

:   

    :   After the creation of a WallForming feature the SheetMetal object is **no longer unfoldable**!

Several tools from other workbenches can be used to add holes or to reshape edges.

### Unfold a sheet metal object 

To unfold a sheet metal object activate the <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Unfold](SheetMetal_Unfold.md) or the <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:16px;"> [Unattended Unfold](SheetMetal_UnattendedUnfold.md) tool.

The result will be a 3D object with an optional outline sketch including bend lines.

### Examples

Until tutorial pages are available on this wiki there is an [Examples](SheetMetal_Examples.md) page.

<img alt="" src=images/SheetMetal_Example-01.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-02.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-03.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-04.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-05.png  style="width:100px;">

It contains some hints about [properties](SheetMetal_Examples#SheetMetal_properties.md) as well.

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

-   Open the Sheet_metal workbench.
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

## Videos


<div class="mw-translate-fuzzy">





</div>

## Links

-   [Macro Sheet Metal Unfolder](Macro_Sheet_Metal_Unfolder.md), the original macro the Unfold tool is based on.
-   [An English and French tutorial in PDF format](https://forum.freecadweb.org/viewtopic.php?f=3&t=25002) on the FreeCAD forum.
-   Report bugs/Request features: <https://github.com/shaise/FreeCAD_SheetMetal/issues>.

## References

-   Author:
    -   Folding tools: Copyright 2015-2018 by Shai Seger
    -   Unfolding tool: Copyright 2014 by Ulrich Brammer
-   License: [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)
-   Source code on github: <https://github.com/shaise/FreeCAD_SheetMetal>



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Workbench/hr
