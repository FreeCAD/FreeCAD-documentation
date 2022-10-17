---
- GuiCommand   *
   Name   *Path Surface
   MenuLocation   *Path → 3D Surface
   Workbenches   *[Path](Path_Workbench.md)
   Version   *0.19
---

# Path Surface/ru

## Описание

This tool creates a new **<img src="images/Path_Surface.svg" width=24px> [3D Surface](Path_Surface.md)** operation which is capable of generating G-Code paths for the entire top surface of a 3D model (or is able to work with selected faces) and allows for faces to be avoided. This operation offers multiple cut patterns   * Line, Zigzag, Circular, Circular Zigzag, Offset, and Spiral (similar to an adaptive pattern). As of version 0.19, this operation offers many customizations to allow for greater productivity.

The **<img src="images/Path_Surface.svg" width=24px> [3D Surface](Path_Surface.md)** operation is also capable of generating basic rotational 3D surfacing paths. The rotational capabilities are limited to the entire model, and do not allow for specific faces or regions to be isolated. The rotational paths are also limited to line cut patterns.

The 3D Surface Tool interfaces to OCL.pyd, a 3rd party Open Source module titled [OpenCamLib](OpenCamLib.md), that generates tool paths from a 3D model. OpenCamLib is not integrated directly into FreeCAD.

**Note   *** In order to use the 3D Surface operation you must   *

1.  Properly install [OpenCamLib](OpenCamLib.md).
2.  Enable [Experimental Features](Path_experimental.md) for the Path Workbench.
3.  Check **Edit → Preferences... → Path → Advanced → Enable OCL dependent features**.

## Применение

Usage instructions for multiple variations of the [3D Surface](Path_Surface.md) operation are presented here.

#### Простая операция 

1.  Press the **<img src="images/Path_Surface.svg" width=24px> [3D Surface](Path_Surface.md)** icon, or select **Path → 3D Surface** from the dropdown menu.
2.  Select the tool controller for the Operation from the Tool controller dialogue pop up window, if presented.
3.  In the Base Geometry tab, select any specific faces you wish to focus on and/or avoid for the operation.
4.  Adjust the operation depths as needed in the Depths tab   * Start Depth, Finish Depth, Step Down.
5.  Make adjustments in Heights tab if needed.
6.  Configure settings in the Operations tab as needed   *
    -   Choose your Coolant Mode.
    -   Choose the BoundBox   * Stock or BaseBoundBox
    -   Set the Scan Type for the operation   * Planar or Rotational
    -   Select the Layer Mode for the operation   * Single-pass or Multi-pass
        1.  Single-pass is for a finishing pass
        2.  Multi-pass could be used for clearing in combination with the use of Depth Offset to leave a thin surface layer for a finish pass
    -   Add additional BoundBox Extra Offset to X and Y as desired (*Rotational scans only*)
    -   Set the Drop Cutter Direction   * X or Y. This is the linear direction the cutter(spindle) will travel. (*Rotational scans only*)
    -   Add a Depth Offset value if you wish to leave a specified thickness of material on the surface, for say a final finish pass
    -   Set the Sample Interval used for the OCL scan.
    -   Set the Step Over value as a percentage of the diameter of the Tool.
    -   Check the Use Start Point box if you wish to provide a start point for the operation in the properties view of the data tab for the operation.
    -   Boundary Enforcement is enabled by default. This forces the cutter to remain inside the boundaries of the feature geometry for the operation, like a pocketing operation. Disable to allow the cutter to extend to the outside of the feature geometry. The Boundary Adjustment property supersedes this property.
    -   Optimize Linear Paths is enabled by default. Disabling will yield a longer gcode result and likely increase cut time.
7.  If you wish to preview the result before accepting the settings, click **Apply**
8.  Click **OK** button to confirm and generate paths.

To achieve different, or more complex, effects, adjust additional operation properties within the Data tab of the Properties View for the operation.

#### Rotational Scans (4th-axis) 

1.  Initiate a [Basic Operation](#Basic_Operation.md) as described above and set the **Scan Type** to **Rotational**.
2.  **Note   *** Face selection is unavailable for Rotational scans, so changes to Base Geometry are ignored.
3.  Locate the Data tab and Properties View for the new [3D Surface](Path_Surface.md) operation. A **Rotation** section should be available with additional properties to adjust, listed below.
    It is recommended that you set the desired rotation properties all at once before recomputing. This is done by clicking the ENTER key immediately after changing a property setting. This process will allow you to change and save multiple properties before recomputing the operation.
4.  Adjust the following settings as needed   *
    -   Set **Cutter Tilt** to the offset index(angle) \[0-90\]. (Used for ball mill cutters)
    -   Change **Drop Cutter Dir** to the axis of travel for the cutter(spindle).
    -   Change **Drop Cutter Extra Offset** to extend the BoundBox in the X and Y directions.
    -   Set **Rotation Axis** to the desired axis.
    -   Adjust **Start Index** to start index(angle) \[0-360\].
    -   Adjust **Stop Index** to stop index(angle) \[0-360\].
5.  Click the **[<img src=images/View-refresh.svg style="width   *16px"> [Refresh](Std_Refresh.md)** icon in the tool bar.
6.  Wait for the results\...

##### Notes About Rotational Scans 

-   **Rotational** scans require much more time and processing than **Planar** scans. Factors affecting processing time include   * Sample Interval, Step Over, tool diameter, and model size. Again, rotational scans can take a long time. Some might take 3, 5 or 10 minutes or longer.
-   For time purposes, it is better that you not recompute a rotational scan after every property change; rather, consider one of the following   *
    -   use the \' *change all settings with ENTER key* \' technique mentioned in Step 2 above, then **[<img src=images/View-refresh.svg style="width   *16px"> [Refresh](Std_Refresh.md)** the operation.
    -   deactivate the operation with the **<img src="images/Path_OpActiveToggle.svg" width=16px> [Active](Path_OpActiveToggle.md)** toggle tool, make your changes to the operation\'s properties, then click the **<img src="images/Path_OpActiveToggle.svg" width=16px> [Active](Path_OpActiveToggle.md)** icon again to re-activate the operation - which triggers a recompute internally.
-   The **<img src="images/Path_Surface.svg" width=16px> [3D Surface](Path_Surface.md)** operation is still considered an *experimental feature* as of 2019-06-25. As such, it may contain a few bugs yet to be clearly identified. Please report bugs and issues in the [FreeCAD Path/CAM Forum](https   *//forum.freecadweb.org/viewforum.php?f=15).
-   The built in **<img src="images/Path_Simulator.svg" width=16px> [CAM Simulator](Path_Simulator.md)** does NOT support 4th-axis simulation. You will need to use a third party simulator to inspect or verify paths visually. See the [Resources](#Resources.md) section below for suggestions.
-   You will likely see red rotational lines around your model in the viewport. This is normal in FreeCAD for the time being.

##### Notes About Scans of complex models 

Excessively long processing times (longer than 10 minutes) can occur when processing large complex models. In addition to the factors already mentioned the following steps could help identify potential causes and solutions.

**\'\'Low Memory**\'\'
Check how much memory is available while the scan is running using a tool such as the Windows **Task Manager, Memory tab**. If more than 90% of memory is consistently being used then a small **Linear Deflection** parameter could be generating a mesh that is too large for the available memory.
To confirm this \...

1.  Create a new **<img src="images/Path_Surface.svg" width=24px> [3D Surface](Path_Surface.md)** operation.
2.  Switch to the Model tab and increase the **Linear Deflection** value. For example change from 2.5um to 20um
3.  Switch back to the Tasks tab to complete setting up the operation.
4.  Click **OK** button to confirm and generate paths.

To make this value the default for all new **<img src="images/Path_Surface.svg" width=24px> [3D Surface](Path_Surface.md)** operations, change the **GeometryTolerance** parameter.
**Tools → Edit Parameters ... → Preferences → Mod → Path → GeometryTolerance **.
Note as of version 0.19 the **Linear Deflection** default = GeometryTolerance / 4

**\'\'Invalid Geometry**\'\'
If a model contains invalid geometry the scanning time can increase significantly. A model can be checked using the [Part CheckGeometry](Part_CheckGeometry.md) function in <img alt="" src=images/Workbench_Part.svg  style="width   *24px;">**Part Workbench**.
To run the tool   *

1.  Switch to the <img alt="" src=images/Workbench_Part.svg  style="width   *24px;">**Part Workbench** and select the model to check
2.  Click on the **<img src="images/Part_CheckGeometry.svg" width=16px> [Part CheckGeometry](Part_CheckGeometry.md)** button available in the Part workbench toolbar OR use the **Part → <img src="images/Part_CheckGeometry.svg" width=16px> Check geometry** entry from the top menu.
3.  Click the **Run Check** button and review the results.

If the results includes items like *BOPAlgo SelfIntersect* then the geometry is invalid and should be corrected by adjusting the model.
(Hint   * Boolean operations and Loft commands can sometimes introduce *Self Intersections*)

#### Available Tool (Cutter) Shapes 

This 3D Surface op currently uses [OpenCamLib](OpenCamLib.md) to extract paths from the part base. As such, a tool setting translation is required between the FreeCAD tool controller and OCL in order to complete the scan with your chosen tool(cutter) shape.

These tool shapes are respected and available for this 3D Surface operation   *

-   End mill
-   Ball end mill
-   Bull nose end mill
-   Chamfer bit
-   Engraver

Should you choose to run the path simulator in the Path Workbench, it only uses the standard end mill to simulate paths. Therefore, you will not see tool-shape-specific material removal. Material removal is shown using the end mill shape.

NOTE   * As of May 2019, only the End Mill has any type of testing to determine accuracy of the FreeCAD-to-OCL tool settings translation. Please post any feedback for non-end-mill usage to the [Path/CAM](https   *//forum.freecadweb.org/viewforum.php?f=15) section in the FreeCAD forums.

## Properties   * Version 0.19 

***Note***   * Not all of these Properties are available in the Task Window Editor. Some are only accessible in the Data tab of the Properties View panel for this Operation.


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


{{TitleProperty|Clearing Options}}

-    **Bound Box**   * Should the operation be limited by the stock object or by the bounding box of the base object

-    **Cut Mode**   * The direction that the toolpath should go around the part   * Climb(ClockWise) or Conventional(CounterClockWise)

-    **Cut Pattern**   * Clearing pattern to use

-    **Cut Pattern Reversed**   * Reverse the cut order of the stepover paths. For circular cut patterns, begin at the outside and work toward the center

-    **Depth Offset**   * Z-axis offset from the surface of the object

-    **Layer Mode**   * The completion mode for the operation   * single or multi-pass

-    **Pattern Center At**   * Choose location of the center point for starting the cut pattern

-    **Pattern Center Custom**   * Set the start point for the cut pattern

-    **Profile Edges**   * Profile the edges of the selection

-    **Sample Interval**   * The Sample Interval. Small values cause long wait times

-    **Step Over**   * Step over percentage of the drop cutter path


{{TitleProperty|Depth}}

-    **Clearance Height**   * The height needed to clear clamps and obstructions

-    **Final Depth**   * Final Depth of Tool- lowest value in Z

-    **Safe Height**   * The above which Rapid motions are allowed.

-    **Start Depth**   * Starting Depth of Tool- first cut depth in Z

-    **Step Down**   * Incremental Step Down of Tool


{{TitleProperty|Mesh Conversion}}

-    **Angular Deflection**   * Smaller values yield a finer, more accurate mesh. Smaller values increase processing time a lot

-    **Linear Deflection**   * Smaller values yield a finer, more accurate mesh. Smaller values do not increase processing time much but can increase memory comsumption


{{TitleProperty|Optimization}}

-    **Circular Use G2 G3**   * Convert co-planar arcs to G2/G3 gcode commands for \Circular\ and \CircularZigZag\ cut patterns

-    **Gap Sizes**   * Feedback   * three smallest gaps identified in the path geometry

-    **Gap Threshold**   * Collinear and co-radial artifact gaps that are smaller than this threshold are closed in the path

-    **Optimize Linear Paths**   * Enable optimization of linear paths (co-linear points). Removes unnecessary co-linear points from G-Code output

-    **Optimize Step Over Transitions**   * Enable separate optimization of transitions between, and breaks within, each step over path


{{TitleProperty|Path}}

-    **Active**   * make False, to prevent operation from generating code

-    **Base**   * The base geometry for this operation

-    **Comment**   * An optional comment for this Operation

-    **Coolant Mode**   * Coolant mode for this operation

-    **Cycle Time**   * Operations Cycle Time Estimation

-    **Tool Controller**   * Defines the Tool controller used in the Operation

-    **User Label**   * User assigned label


{{TitleProperty|Rotation}}

-    **Cutter Tilt**   * Set the cutter (spindle) tilt angle.

-    **Drop Cutter Dir**   * The direction along which dropcutter lines are created

-    **Drop Cutter Extra Offset**   * Additional offset to the selected bounding box - use sub-properties to set values

    -   
        **X**
        
           * x distance value

    -   
        **Y**
        
           * y distance value

    -   
        **Z**
        
           * z distance value

-    **Rotation Axis**   * Set the axis for model rotation.

-    **Start Index**   * Start index(angle) for rotation

-    **Stop Index**   * Stop index(angle) for rotation


{{TitleProperty|Selected Geometry Settings}}

-    **Avoid Last X Faces**   * Avoid cutting the last \'N\' faces in the Base Geometry list of selected faces

-    **Avoid Last X Internal Features**   * Do not cut internal features on avoided faces

-    **Boundary Adjustment**   * Positive values push the cutter toward, or beyond, the boundary. Negative values retract the cutter away from the boundary

-    **Boundary Enforcement**   * If true, the cutter will remain inside the boundaries of the model or selected face(s)

-    **Handle Multiple Features**   * Choose how to process multiple Base Geometry features

-    **Internal Features Adjustment**   * Positive values push the cutter toward, or into, the feature. Negative values retract the cutter away from the feature

-    **Internal Features Cut**   * Cut internal feature areas within a larger selected face


{{TitleProperty|Start Point}}

-    **Start Point**   * The custom start point for the path of this operation, set in sub-properties   * x, y, z

    -   
        **X**
        
           * x axis value

    -   
        **Y**
        
           * y axis value

    -   
        **Z**
        
           * z axis value

-    **Use Start Point**   * Make True, if specifying a Start Point


{{TitleProperty|Surface}}

-    **Scan Type**   * Planar   * Flat, 3D surface scan. Rotational   * 4th-axis rotational scan.


{{TitleProperty|Waste}}

-    **Ignore Waste**   * Ignore areas that proceed below specified depth.

-    **Ignore Waste Depth**   * Depth used to identify waste areas to ignore.

-    **Release From Waste**   * Cut through waste to depth at model edge, releasing the model.

## Tasks Window Editor Layout 

*Descriptions for the settings are provided in the Properties list above.* This section is simply a layout map of the settings in the window editor for the Operation.

### Base Location 

-   **Base Geometry import selection**   * Use this list to select Base Geometry to be imported from the selected, existing operation
-   **Import**   * imports the selected operation\'s Base Geometry into the current operations Base Geometry list
-   **Base Geometry list for current operation**   * List of Base Geometry for current operation, if any selected
-   **Add**   * adds selected element(s) which should be the base(s) for the path(s)
-   **Remove**   * remove the selected item(s) in the Base Location list
-   **Edit**   * clear all items in the Base Location list

### Depth

-    **Start Depth**
    

-    **Final Depth**
    

-    **Step Down**
    

### Height

-    **Safe Height**
    

-    **Clearance Height**
    

### Operation

-    **Tool Controller**
    

-    **Coolant Mode**
    

-    **BoundBox**
    

-    **Scan Type**
    

-    **Layer Mode**
    

-    **BoundBox extra offset X**
    

-    **BoundBox extra offset Y**
    

-    **Drop Cutter Direction**
    

-    **Depth Offset**
    

-    **Step Over**
    

-    **Sample Interval**
    

-    **Optimize Output Enabled**
    

-    **Use Start Point**
    

-    **Boundary Enforcement**
    

-    **Optimize Linear Paths**
    

## Resources

-   G-code(path) simulator   * [NCViewer](https   *//ncviewer.com/)
-   G-code(path) simulator   * [CAMotics](https   *//www.camotics.org/)





{{Path Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Surface/ru
