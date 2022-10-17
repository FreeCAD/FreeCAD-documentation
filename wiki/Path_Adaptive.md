---
- GuiCommand   *
   Name   *Path Adaptive
   MenuLocation   *Path → Adaptive
   Workbenches   *[Path](Path_Workbench.md)
---

# Path Adaptive

## Description

The <img alt="" src=images/Path_Adaptive.svg  style="width   *24px;"> [Adaptive](Path_Adaptive.md) tool uses an adaptive algorithm to create clearing and profiling paths that manage cutter engagement so that engagement and material removal never exceed a maximum value.

## Usage

Usage instructions for the [Adaptive](Path_Adaptive.md) operation are presented here.

#### Basic Operation 

1.  Press the **<img src="images/Path_Adaptive.svg" width=16px> [Adaptive](Path_Adaptive.md)** icon, or select the **Path** → **<img src="images/Path_Adaptive.svg" width=24px> [Adaptive](Path_Adaptive.md)** from the top menu.
2.  Select the tool controller for the Operation from the Tool controller dialogue pop up window, if prompted.
3.  Adjust the operation depths as needed in the Depths tab   * Start Depth, Finish Depth, Step Down.
4.  Make adjustments in Heights tab if needed.
5.  Configure settings in the Operations tab   *
    1.  (**See the Properties → Adaptive section below.**)
    2.  Set the Step Over value as a percentage of the diameter of the Tool.
6.  If you wish to preview the result before accepting the settings, click **Apply**
7.  Click **OK** button to confirm and generate paths.

##### Preliminary Notes About Adaptive Clearing 

-   Depending on the size and complexity of the area for the operation, is might be better to not recompute the operation after every property change; rather, consider   *
    -   deactivate the operation with the **<img src="images/Path_OpActiveToggle.svg" width=16px> [Active](Path_OpActiveToggle.md)** toggle tool, make your changes to the operation\'s properties, then click the **<img src="images/Path_OpActiveToggle.svg" width=16px> [Active](Path_OpActiveToggle.md)** icon again to re-activate the operation - which triggers a recompute internally.
-   The **<img src="images/Path_Adaptive.svg" width=16px> [Adaptive](Path_Adaptive.md)** operation might contain a few bugs yet to be clearly identified. Please report bugs and issues in the [FreeCAD Path/CAM Forum](https   *//forum.freecadweb.org/viewforum.php?f=15).
-   All tool shapes may not be respected with this operation. Check the FreeCAD forum for further details.
-   Should you choose to run the path simulator in the Path Workbench, it only uses the standard end mill to simulate paths. Therefore, you will not see tool-shape-specific material removal. Material removal is shown using the end mill shape.

## Properties

***Note***   * The names of some Properties in this list differ a little from the same settings used in the Task Window Editor.


{{TitleProperty|Adaptive}}

-    **Force Inside-Out**   * Force plunging into material inside and clearing towards the edges

-    **Helix Angle**   * Helix ramp entry angle (degrees)

-    **Helix Cone Angle**   * Angle (degrees) of conical helix

-    **Helix Diameter Limit**   * Limit helix entry diameter, if limit larger than tool diameter or 0, tool diameter is used

-    **Keep Tool Down Ratio**   * Max length of keep tool down path compared to direct distance between points

-    **Lift Distance**   * Lift distance for rapid moves

-    **Operation Type**   * Type of adaptive operation   * Clearing or Profiling

-    **Side**   * Side of selected faces that tool should cut   * Inside or Outside

-    **Step Over**   * Percent of cutter diameter to step over on each pass

-    **Stock to Leave**   * How much stock to leave (i.e. for a separate finishing operation)

-    **Tolerance**   * Influences accuracy and performance

-    **Use Helix Arcs**   * Use Arcs (G2) for helix ramp


{{TitleProperty|Base}}

Note   * It is suggested that you do not edit the Placement property of path operations. Rather, move or rotate the Path Job model as needed.

-    **Placement**   * Overall placement\[position and rotation\] of the object - with respect to the origin (or origin of parent object container)

    -   
        **Angle**
        
           * Angle in degrees applied to rotation of the object around Axis property value

    -   
        **Axis**
        
           * Axis(one or multiple) around which to rotate the object, set in sub-properties   * x, y, z

        -   
            **X**
            
               * x axis value

        -   
            **Y**
            
               * y axis value

        -   
            **Z**
            
               * z axis value

    -   
        **Position**
        
           * Position of the object, set in sub-properties   * x, y, z - with respect to the origin (or origin of parent object container)

        -   
            **X**
            
               * x distance value

        -   
            **Y**
            
               * y distance value

        -   
            **Z**
            
               * z distance value

-    **Label**   * User-provided name of the object (UTF-8)


{{TitleProperty|Depth}}

-    **Clearance Height**   * The height needed to clear clamps and obstructions

-    **Final Depth**   * Final Depth of Tool- lowest value in Z

-    **Finish Depth**   * Maximum material removed on final pass.

-    **Safe Height**   * The above which Rapid motions are allowed.

-    **Start Depth**   * Starting Depth of Tool- first cut depth in Z

-    **Step Down**   * Incremental Step Down of Tool


{{TitleProperty|Path}}

-    **Active**   * make False, to prevent operation from generating code

-    **Comment**   * An optional comment for this Operation

-    **Tool Controller**   * Defines the Tool controller used in the Operation

-    **User Label**   * User assigned label

## Tasks Window Editor Layout 

*Descriptions for these settings are provided in the Properties list above.* This section is simply a layout map of the settings in the window editor for the Operation.

### Base Geometry 

-   **Add**   * adds selected element(s) which should be the base(s) for the path(s)
-   **Delete**   * delete the selected item(s) in the Base Geometry list
-   **Clear**   * clear all items in the Base Geometry list

### Depths

-    **Start Depth**
    

-    **Final Depth**
    

-    **Finish Depth**
    

-    **Step Down**
    

### Heights

-    **Safe Height**
    

-    **Clearance Height**
    

### Operation

-    **Tool Controller**
    

-    **Cut Region**(Side)

-    **Operation Type**
    

-    **Step Over Percent**
    

-    **Accuracy vs Performance**(Tolerance)

-    **Helix Ramp Angle**
    

-    **Helix Cone Angle**
    

-    **Helix Max Diameter**(Helix Diameter Limit)

-    **Lift Distance**
    

-    **Keep Tool Down Ratio**
    

-    **Stock to Leave**
    

-    **Force Clearing Inside-Out**
    

-    **Stop**
    

## Resources

-   Author\'s GitHub page for the original project   * [kreso-t/FreeCAD_Mod_Adaptive_Path](https   *//github.com/kreso-t/FreeCAD_Mod_Adaptive_Path)
-   Active topic in FreeCAD forums for Path Adaptive operation   * [Adaptive Path/CAM Operation](https   *//forum.freecadweb.org/viewtopic.php?f=15&t=30127)




 {{Path_Tools_navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Adaptive
