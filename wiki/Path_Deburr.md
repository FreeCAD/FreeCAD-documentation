---
- GuiCommand:
   Name:Path Deburr
   MenuLocation:Menu: Path → Deburr <br>Toolbar: Path → Engraving options → Deburr
   Workbenches:[Path](Path_Workbench.md)
---

# Path Deburr

## Description

The <img alt="" src=images/Path_Deburr.svg  style="width:24px;"> [Path Deburr](Path_Deburr.md) tool is primarily for Deburring an edge.

## Usage

Use for de-burring edges.

Start feature → select face or edge → configure options.

## Options

After starting the feature you have to select the face or edge you want to de-burr in the Base Geometry tab in the Deburr feature menu. As seen in below:

:   <img alt="Base Geometry tab within the Deburr feature menu" src=images/Path_Deburr_Base_Geometry-tab.png  style="width:337" height="559px;">

After you selected the geometry you can press **Apply** to see the tool-path as set by the default options.
When you have everything selected you can check your depths/step down and heights just like other path functions.

Final step is the menu that as seen below, you can configure the feature as follows:

-    `Tool controller`: The tool a 90 degree V-bit

-    `Coolant Mode`: Do you want coolant? (On/Off)

-    `Directions`: **CW** (clockwise) or **CCW** (counter-clockwise)

-    `W`: is the dimension of your edge.

-    `h`: is the offset from the bottom of the V-bit. It\'s a safety feature because if the tip gets above the edge it won\'t cut anymore.

:   <img alt="Deburring interface with the options" src=images/Path_Deburr_Operations-tab.png  style="width:337" height="599px;">

## Properties

### Data


{{TitleProperty|Base Geometry}}

-    **Placement**:

-    **Label**: User name of the object (UTF-8)


{{TitleProperty|Deburr}}

-    **Direction**: CCW or CW

-    **Entry Point**: Change this to change Entry point, if set to 2 it will go in 2 corners from the default.

-    **Extra depth**: Extra depth or h in the menu.

-    **Join**: How to join chamfer segments, Round or Miter. \[example needed\]

-    **Side**: Can change sides. \[example needed\]

-    **Width**: The width you fill in in the menu by W.


{{TitleProperty|Depth}}

-    **Clearance Height**: The height needed to clear clamps and obstructions (set by default to `OpStockZMax + SetupSheet.ClearanceHeightOffset`)

-    **Safe Height**: The above which Rapid motions are allowed. (set to `OpStockZMax + SetupSheet.SafeHeightOffset`)

-    **Start Depth**: Starting Depth of Tool- first cut depth in Z

-    **Step Down**: Incremental Step Down of Tool


{{TitleProperty|Path}}

-    **Active**: Make False, to prevent operation from generating code

-    **Base**: The base geometry for this operation, edges or a face

-    **Comment**: An optional comment for this operation

-    **Coolant Mode**: Coolant mode for this operation

-    **Cycle Time**: Estimated cycle time for this operation

-    **Start Vertex**: The vertex index to start the path from

-    **Tool Controller**: The tool controller that will be used to calculate the path

-    **User Label**: User assigned label

### View

Empty Example:





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Deburr
