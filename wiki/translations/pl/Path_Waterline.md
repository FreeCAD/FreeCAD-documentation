---
- GuiCommand:
   Name:Path Waterline
   MenuLocation:Path → Waterline
   Workbenches:[Path](Path_Workbench.md)
   Version:0.19
---

# Path Waterline/pl

## Description

This tool creates a new Waterline operation. As of 0.19\_pre, the Waterline operation works on the entire model to generate G-Code for the Job. Currently, within the operation\'s settings there is no functionality to select specific areas, faces, or regions of the model.

The Waterline operation has two algorithms: OCL Drop Cutter and Experimental.

-   The OCL Drop Cutter algorithm interfaces to OCL.pyd, a 3rd party Open Source module titled [OpenCamLib](OpenCamLib.md), that generates tool paths from a 3D Model. OpenCamLib is not integrated directly into FreeCAD.
-   The Experimental algorithm makes use of the built-in Path.Area() class.

\'\'\' *Note* \'\'\': In order to use the Waterline operation you must:

1.  Properly install [OpenCamLib](OpenCamLib.md).
2.  Enable [Experimental Features](Path_experimental.md) for the Path Workbench.
3.  Check **Edit → Preferences... → Path → Advanced → Enable OCL dependent features**.

## Usage

Usage instructions for multiple variations of the [Waterline](Path_Waterline.md) operation are presented here.

#### Basic Operation 

1.  Press the **<img src="images/Path_Waterline.svg" width=24px> [Waterline](Path_Waterline.md)** icon, or select the [Waterline](Path_Waterline.md) tool from the **Path** menu.
2.  Select the tool controller for the Operation from the Tool controller dialogue pop up window.
3.  Adjust the operation depths as needed in the Depths tab: Start Depth, Finish Depth, Step Down.
4.  Make adjustments in Heights tab if needed.
5.  Configure settings in the Operations tab based on the Algorithm selected:
    1.  OCL Dropcutter
        1.  Choose the BoundBox: Stock or BaseBoundBox.
        2.  Set the Layer Mode: Single-pass or Multi-pas.
        3.  Set the Sample Interval used for the OCL scan.
    2.  Experimental
        1.  Choose the BoundBox: Stock or BaseBoundBox.
        2.  Set the Layer Mode: Single-pass or Multi-pas.
        3.  Set the Cut Pattern if clearing is desired at each layer.
        4.  Set the Boundary Adjustment (material allowance).
6.  If you wish to preview the result before accepting the settings, click Apply
7.  Click **OK** button to confirm and generate paths.

To achieve different, or more complex, effects, adjust additional operation properties within the Data tab of the Properties View for the operation.

##### Notes About Experimental Algorithm 

-   It does not handle overhangs correctly.
-   It only returns paths for an End Mill type cutter (tool bit).
-   It might not correctly catch all interior features.
-   It is just that, experimental, and not ready for mainstream integration. Please inspect paths with the built-in **<img src="images/Path_Simulator.svg" width=16px> [CAM Simulator](Path_Simulator.md)**, or other 3rd-party g-code inspection tools, before cutting with your machine.

#### Available Tool (Cutter) Shapes 

When using the \'\'\' *OCL Dropcutter* \'\'\' algorithm, the Waterline operation uses OpenCamLib \[OCL\] to extract paths from the part base. As such, a tool translation is required between the FreeCAD tool controller and OCL in order to complete the scan with your chosen tool(cutter) shape. These tool shapes are(should be) respected and available for the OCL Dropcutter so long as the built-in tool shapes are used, whether Legacy or ToolBit tools:

-   End mill
-   Ball end mill
-   Bull nose end mill
-   Chamfer bit
-   Engraver

#### Additional Notes 

-   Should you choose to run the path simulator, **<img src="images/Path_Simulator.svg" width=16px> [CAM Simulator](Path_Simulator.md)**, in the Path Workbench, you might not see tool-shape-specific material removal. Be cautious. A small trial job using foam or other very non-dense material is recommended to verify paths are correct with your selected tool controller.
-   As of May 2020, only the End Mill has any type of testing to determine accuracy of the FreeCAD-to-OCL tool settings translation. Please post any feedback for non-end-mill usage to the [Path/CAM](https://forum.freecadweb.org/viewforum.php?f=15) section in the FreeCAD forums.

## Properties

\'\'\' *Note* \'\'\': Not all of these Properties are available in the Task Window Editor. Some are only accessible in the Data tab of the Properties View panel for this Operation.

#### Base

Note: It is suggested that you do not edit the Placement property of path operations. Rather, move or rotate the Path Job model as needed.

-    **Placement**: Overall placement\[position and rotation\] of the object - with respect to the origin (or origin of parent object container)

    -   
        **Angle**
        
        : Angle in degrees applied to rotation of the object around Axis property value

    -   
        **Axis**
        
        : Axis(one or multiple) around which to rotate the object, set in sub-properties: x, y, z

        -   
            **X**
            
            : x axis value

        -   
            **Y**
            
            : y axis value

        -   
            **Z**
            
            : z axis value

    -   
        **Position**
        
        : Position of the object, set in sub-properties: x, y, z - with respect to the origin (or origin of parent object container)

        -   
            **X**
            
            : x distance value

        -   
            **Y**
            
            : y distance value

        -   
            **Z**
            
            : z distance value

-    **Label**: User-provided name of the object (UTF-8)

#### Clearing Options 

-    **Algorithm**: The library to use to generate the path

-    **BoundBox**: Should the operation be limited by the stock object or by the bounding box of the base object

-    **Clear Last Layer**: Set to clear last layer in \Multi-pass\ operation.

-    **Cut Mode**: The direction that the toolpath should go around the part: Climb(ClockWise) or Conventional(CounterClockWise)

-    **Cut Pattern**: Clearing pattern to use

-    **Depth Offset**:

-    **Ignore Outer Above**:

-    **Layer Mode**: The completion mode for the operation: single or multi-pass

-    **Step Over**:

#### Depth

-    **Clearance Height**: The height needed to clear clamps and obstructions

-    **Final Depth**: Final Depth of Tool- lowest value in Z

-    **Safe Height**: The above which Rapid motions are allowed.

-    **Start Depth**: Starting Depth of Tool- first cut depth in Z

-    **Step Down**: Incremental Step Down of Tool

#### Path

-    **Active**: make False, to prevent operation from generating code

-    **Base**: The base geometry for this operation

-    **Comment**: An optional comment for this Operation

-    **Coolant Mode**:

-    **Cycle Time**:

-    **Tool Controller**: Defines the Tool controller used in the Operation

-    **User Label**: User assigned label

#### Start Point 

-    **Start Point**: The custom start point for the path of this operation.

    -   
        **X**
        
        : x distance value

    -   
        **Y**
        
        : y distance value

    -   
        **Z**
        
        : z distance value

-    **Use Start Point**: Make True, if specifying a Start Point

## Tasks Window Editor Layout 

*Descriptions for the settings are provided in the Properties list above.* This section is simply a layout map of the settings in the window editor for the Operation.

#### Base Location 

-   **Add**: adds selected element(s) which should be the base(s) for the path(s)
-   **Remove**: remove the selected item(s) in the Base Location list
-   **Edit**: clear all items in the Base Location list

#### Depths

-    **Start Depth**
    

-    **Final Depth**
    

-    **Step Down**
    

#### Heights

-    **Safe Height**
    

-    **Clearance Height**
    

#### Operation

-    **Tool Controller**
    

-    **Coolant Mode**
    

-    **Algorithm**
    

-    **BoundBox**
    

-    **Layer Mode**
    

-    **Cut Pattern**\~

-    **Boundary Adjustment**\~

-    **Sample Interval**\~

\~Visibility changes with other settings.

## Resources

-   G-code(path) simulator: [NCViewer](https://ncviewer.com/)
-   G-code(path) simulator: [CAMotics](https://www.camotics.org/)





{{Path Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Waterline/pl
