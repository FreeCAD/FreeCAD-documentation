---
- GuiCommand:
   Name:Path Deburr
   MenuLocation:Path → Deburr
   Workbenches:[Path](Path_Workbench.md)
   Version:0.18
---

# Path Deburr

## Description

The <img alt="" src=images/Path_Deburr.svg  style="width:24px;"> **Path Deburr** tool is primarily for Deburring an edge.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Path_Deburr.svg" width=16px> [Deburr](Path_Deburr.md)** button.
    -   Select the **Path → <img src="images/Path_Deburr.svg" width=16px> Deburr** option from the menu.
2.  The **Deburr** task panel opens. See [Options](#Options.md).
3.  Select **Base Geometry**.
4.  Specify the required parameters.
5.  Press the **OK** button.

## Options

After selecting the geometry in the **Base Geometry** section of the task panel you can press **Apply** to see the tool path as defined by the default options.

Next you can check your depths/step down and heights, just like with other path commands.

The Final step is to activate the **Operation** section where you can specify the following:

-    **Tool controller**: Select the tool to use.

-    **Coolant Mode**: Select {{Value|None}}, {{Value|Flood}} or {{Value|Mist}}.

-    **Directions**: Select {{Value|CW}} (clockwise) or {{Value|CCW}} (counter-clockwise).

-    **W**: The dimension of your edge.

-    **h**: The offset from the bottom of the tool. It\'s a safety feature because if the tip gets above the edge it won\'t cut anymore.



:   <img alt="Deburring interface with the options" src=images/Path_Deburr_Operations-tab.png  style="width:300px;">



## Properties

### Data


{{TitleProperty|Base}}

-    **Placement**:

-    **Label**: User name of the object (UTF-8)


{{TitleProperty|Deburr}}

-    **Direction**: {{Value|CCW}} or {{Value|CW}}.

-    **Entry Point**: Entry point of the operation, if set to 2 it will go in 2 corners from the default.

-    **Extra depth**: Extra depth (**h** in the task panel).

-    **Join||Hidden**: How to join chamfer segments, {{Value|Round}} or {{Value|Miter}}.

-    **Side||Hidden**: Side of the operation, {{Value|Outside}} or {{Value|Inside}}.

-    **Width**: The width of the chamfer (**W** in the task panel).


{{TitleProperty|Depth}}

-    **Clearance Height**: The height needed to clear clamps and obstructions (set by default to `OpStockZMax + SetupSheet.ClearanceHeightOffset`).

-    **Safe Height**: The height above which rapid motions are allowed. (set to `OpStockZMax + SetupSheet.SafeHeightOffset`).

-    **Start Depth**: Starting depth of of the tool, first cut depth in Z.

-    **Step Down**: Incremental step down of the tool.


{{TitleProperty|Op Values}}

-    **Op Stock ZMax**: The maximum Z value of the stock.

-    **Op Stock ZMin**: The minimum Z value of the stock.

-    **Op Tool Diameter**: The diameter of the tool.


{{TitleProperty|Path}}

-    **Active**: Make `False`, to prevent operation from generating code.

-    **Base**: The base geometry for this operation, edges or a face.

-    **Comment**: An optional comment for this operation.

-    **Coolant Mode**: Coolant mode for this operation.

-    **Cycle Time**: Estimated cycle time for this operation.

-    **Tool Controller**: The tool controller that will be used to calculate the path.

-    **User Label**: User assigned label.




 {{Path_Tools_navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Deburr
