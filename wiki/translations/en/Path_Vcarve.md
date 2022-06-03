---
- GuiCommand   *
   Name   *Path Vcarve
   MenuLocation   *Path → Vcarve
   Workbenches   *[Path](Path_Workbench.md)
   Version   *0.19
---

# Path Vcarve/en

## Description

The <img alt="" src=images/Path_Vcarve.svg  style="width   *24px;"> [Path Vcarve](Path_Vcarve.md) tool is primarily for center-line engraving a <img alt="" src=images/Draft_ShapeString.svg  style="width   *24px;"> [Draft ShapeString](Draft_ShapeString.md) onto a part. However, it may be useful for other kinds of 2D.

Unlike engraving which follows the lines in the shapestring, V-carving uses a V-shaped cutter and attempts to clear the area by moving the cutter down the center of the region and varying the depth of cut. Since a v-cutter radius varies with the depth, the width of cut varies as well. The result is a more natural looking cut, particularly for serif fonts.

![](images/Engravepath.png ) ![Example Vcarving Path](images/Vcarvepath.png ) ![](images/Vcarved.png ) ![](images/Scrolltest.png )

The V-carve algorithm calculates a path down the center-line of a region using a voronoi diagram. This center-line is the path the tool will follow in the XY plane. It next calculates a \'maximum inscribed circle\' along the path. This is the largest circle that can be drawn at that point and remain entirely inside the clearing area. Using the circle radius and the tip angle of the cutter, the depth of cut is calculated.

## Usage

### Prepare the shapes to engrave 

-    **[<img src=images/Draft_ShapeString.svg style="width   *24px"> [Draft ShapeStrings](Draft_ShapeString.md)**are usable out of the box

-   SVG files require some massaging, both in the editor and in the <img alt="" src=images/Workbench_Draft.svg  style="width   *24px;"> [Draft Workbench](Draft_Workbench.md)   *
    -   In the editor (e.g. [Inkscape](https   *//www.inkscape.org))   * make sure the file only contains paths and that the paths are ungrouped; make sure there are no self-intersecting paths, (in Inkscape) use Path → Simplify and union to join paths that overlap.
    -   Switch to the <img alt="" src=images/Workbench_Draft.svg  style="width   *24px;"> [Draft Workbench](Draft_Workbench.md) in [workbench dropdown list](Std_Workbench.md)
    -   Import the SVG using **File → Import → select "SVG as geometry"**
    -   The result should look similar to this   *

           *   ![](images/Svgimport.png )
           *   
            
*Above   * Results of importing 'SVG as geometry'*
            

   *   

       *   Paths with holes (letters, the vine in the image above) are imported as 2 separate paths (named along the lines of `Path905` and `Path905001` in the [Tree view](Tree_view.md)), one of them is the hole and the other one is the outline; we\'ll deal with this in the next step

-   -   In order to get the 2D faces, [Path Vcarve](Path_Vcarve.md) needs   *
        -   For paths without holes   *
            1.  Select the path
            2.  Choose **Modification → ![](images/)_[Upgrade](Draft_Upgrade.md)**
            3.  Followed by **Modification → ![](images/)_[Downgrade](Draft_Downgrade.md)**
        -   For paths with holes   *
            1.  Select the outer path, then the inner path
            2.  Choose **Modification → ![](images/)_[Downgrade](Draft_Downgrade.md)** **twice**

           *   Some paths will behave differently, so you may need to play with **<img src="images/Draft_Upgrade.svg" width=16px> Upgrade** and **<img src="images/Draft_Downgrade.svg" width=16px> Downgrade** until you get something named   * `Face<number>`
           *   The end result should look like this   *
           *   ![](images/Svgfaces.png )

### Create the Vcarve operation 

-   Switch to the **[<img src=images/Workbench_Path.svg style="width   *16px"> [Path Workbench](Path_Workbench.md)** in the [workbench dropdown menu](Std_Workbench.md)
-   Add a job, use the objects named `Face<number>` (or the ShapeString) as a base, add a v-bit tool controller, set feeds, speeds, etc.
-   The operation only supports one object (either a single Face object, or a ShapeString) so for each object   *
    -   Select **Path  →  <img src="images/Path_Vcarve.svg" width=24px> Vcarve** from the top menu. This opens the configuration panel.
    -   Open the **Base Geometry** tab and add all faces of the ShapeString, or the face of a single Face object obtained above
    -   Press **Apply** and inspect the generated path; if necessary, adjust operation parameters (Threshold can be set higher in most situations)
    -   Press **OK** to finish

## Options

Empty

## Properties

### Data


{{TitleProperty|Base}}

-    **Placement**   * -

-    **Label**   * -


{{TitleProperty|Depth}}

-    **ClearanceHeight**   * -

-    **FinalDepth**   * -

-    **SafeHeight**   * -

-    **StartDepth**   * -

-    **StepDown**   * -


{{TitleProperty|Op Values}}

-    **OpFinalDepth**   * -

-    **OpStartDepth**   * -

-    **OpStockZMax**   * -

-    **OpStockZMin**   * -

-    **OpToolDiameter**   * -


{{TitleProperty|Path}}

-    **Active**   * -

-    **Comment**   * -

-    **CoolantMode**   * -

-    **StartVertex**   * -

-    **ToolController**   * -

-    **UserLabel**   * -

#### Hidden

-    **Base**   * -

-    **BaseObject**   * -

-    **BaseShapes**   * -

-    **ExpressionEngine**   * -

-    **Label2**   * -

-    **Path**   * -

-    **Proxy**   * -

-    **Visibility**   * -

### View

Empty

## Scripting


**See also   ***

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

Example   *


```python
#Place code example here.
```





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Vcarve/en
