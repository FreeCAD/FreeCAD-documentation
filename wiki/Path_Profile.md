---
- GuiCommand:
   Name:Path Profile
   MenuLocation:Path → Profile
   Workbenches:[Path](Path_Workbench.md)
   Version:0.19
---

# Path Profile

## Description

The <img alt="" src=images/Path_Profile.svg  style="width:16px;"> [Profile](Path_Profile.md) tool creates a contour operation based on selected features of the model. The tool was introduced in version 0.19. It offers three operations that were handled by separate tools in previous versions.

All operations create objects that are made to be part of a **<img src="images/Path_Job.svg" width=24px> [Path Job](Path_Job.md)**.

These are the available operations:

### Contour operation 

A **Contour** operation is the default. It creates a simple external contour cut of complex 3D <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench.md)-based objects. The entire Job Model serves as the input for the Operation, regardless of whether any Body Geometry is selected when the Contour command is invoked.

### Profile Face operation 

A **Profile Face** operation creates a simple contour path from one ore more selected faces of an object.

### Profile Edges operation 

A **Profile Edges** operation creates a simple contour path from selected edges.

 <img alt="" src=images/Path_profile_example.jpg  style="width:600px;"> 

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Path_Profile.svg" width=16px> [Path Profile](Path_Profile.md)** button.
    -   Select the **Path → <img src="images/Path_Profile.svg" width=16px> Profile** option from the menu.
2.  Activate the Base Geometry section by clicking its tab, and select features from the Job model.
    -   If no features are selected, the command defaults to a **Contour** operation, contouring the entire model.
    -   If faces are selected, then the result is a **Profile Face** operation.
    -   If edges are selected, then the result is a **Profile Edges** operation.
        **NOTE**: This operation has received improvements to allow functionality on some open-edge (non-loop) selections. See the [Usage Notes](#Usage_Notes.md) section below for additional information on best practice for profiling open-edges.
3.  Activate the Operation section by clicking on its tab, and adjust the operation\'s settings as desired.
4.  Optionally press the **Apply** button to preview the operation with the current settings.
5.  Click the **OK** button or the **Cancel** button to create or cancel the operation.

**Important Note: Path Profile doesn\'t take care of other details of the object. You have to adjust the properties, especially the final depth, carefully, a mistake might destroy your work piece**

A Start point can be enabled from the Operation tab in the Tasks Window editor, using a location defined in the **Property View → Data → Start Point**.

Make additional adjustments to the operation by modifying the operation\'s properties in the Data tab of the Property View. Advanced properties will be located here, if any.

## Usage Notes 

-   The **<img src="images/Path_Profile.svg" width=16px> [Profile](Path_Profile.md)** operation is capable of profiling **open-edges** (one or more continuous edges that do not form a loop as seen from the *Top View*)
    -   It is best to select the top edges (highest edges) for the selection. After doing so, you will need to manually set the Final Depth for the operation. Selection of bottom edges only is unpredictable and will likely return undesirable paths in many situations; however, it will return correct paths in some situations.
    -   Selected edges must form a continual edge *as viewed from the Top View*. Selected top edges may have differing heights, so long as they connect at a common (X, Y) coordinate - differing Z-heights are acceptable in *some**\*\**** cases.
        **\*\***In certain cases, the user will need to include in their selection the straight vertical connecting edge between two adjacent edges of different heights that share a common (X, Y) coordinate.
    -   Because top edges are selected, the Final Depth for the operation will need to be set manually.
    -   When profiling open-edges, the \Side\ or \Cut Side\ property is disabled internally even though it will likely be visible within the Task editor window and the Properties list within the Data tab.
-   When profiling the entire model (a complete contour of the model) the \Side\ or \Cut Side\ property is hard coded to \Outside\ even though it might be available for user input.

## Properties

***Note***: Not all of these Properties are available in the Task Window Editor. Some are only accessible in the Data tab of the Properties View panel for this Operation.


{{TitleProperty|Base}}

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


{{TitleProperty|Depth}}

-    **Clearance Height**: The height needed to clear clamps and obstructions

-    **Final Depth**: Final Depth of Tool- lowest value in Z

-    **Finish Depth**: Maximum material removed on final pass. The height (thickness) of the last cutting level - *set for a better finish*.

-    **Safe Height**: The height above which Rapid motions are allowed. (Rapid safety height between locations)

-    **Start Depth**: Starting depth of Tool - *first cut depth in Z*

-    **Step Down**: Incremental step down of Tool during operation

 <img alt="" src=images/Path-DepthsAndHeights.gif  style="width:300px;">  
*Visual reference for Depth properties (settings)*


{{TitleProperty|Path}}

-    **Active**: make False, to prevent operation from generating code

-    **Base**: The base geometry for this operation

-    **Comment**: An optional comment for this Operation

-    **Coolant Mode**: The coolant mode for this operation.

-    **Cycle Time**: The cycle time estimation for this operation.

-    **Tool Controller**: Defines the Tool controller used in the Operation

-    **User Label**: User assigned label


{{TitleProperty|Profile}}

-    **Direction**: The direction that the tool path should go around the part: Clockwise\[CW\] or Counterclockwise\[CCW\]

-    **Expand Profile**: Extend the profile clearing beyond the Extra Offset.

-    **Expand Profile Step Over**: Set the stepover percentage, based on the tool\'s diameter.

-    **Handle Multiple Features**: Choose how to process multiple Base Geometry features.

-    **OffsetExtra**: Extra value to stay away from final profile- good for roughing toolpath

-    **Process Circles**: Check if you want this Profile Operation to also be applied to cylindrical holes, *which normally get drilled*.

-    **Process Holes**: Check if this Profile Operation should also process holes in the base geometry. **Note** that this does not include cylindrical holes.

-    **Process Perimeter**: Check if this Profile Operation should also process the outside perimeter of the base geometry shapes

-    **Side**: (Cut Side) Side of edge that tool should cut. This only matters if \Use Compensation\ is True(checked).

-    **Use Compensation**: If checked, the Profile Operation is offset by the tool radius. The offset direction is determined by the Cut Side.


{{TitleProperty|Rotation}}

-    **Attempt Inverse Angle**: Automatically attempt Inverse Angle if initial rotation is incorrect.

-    **Enable Rotation**: Enable rotation to gain access to pockets or areas not normal to Z axis.

-    **Inverse Angle**: Inverse the angle of the rotation. ***Example:** change a rotation from -22.5 to 22.5 degrees.*

-    **Limit Depth To Face**: Enforce the Z-depth of the selected face as the lowest value for final depth. Higher user values for final depth will be observed.

-    **Reverse Direction**: Reverse orientation of Operation by 180 degrees.


{{TitleProperty|Start Point}}

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

-    **Use Start Point**: Make True, if manually specifying a Start Point. Set the start point in the property data Start Point field.

## Tasks Window Editor Layout 

*Descriptions for the settings are provided in the Properties list above.* This section is simply a layout map of the settings in the window editor for the Operation.

### Base Geometry 

-   **Add**: Adds selected element(s) which should be the base(s) for the path(s)
-   **Delete**: Delete the selected item(s) in the Base Geometry list
-   **Clear**: Clear all items in the Base Geometry list

### Depths

-    **Start Depth**
    

-    **Final Depth**
    

-    **Step Down**
    

### Heights

-    **Safe Height**
    

-    **Clearance Height**
    

### Operation

-    **Tool Controller**
    

-    **Coolant Mode**
    

-    **Cut Side ****
    

-    **Direction**
    

-    **Extra Offset**
    

-    **Enable Rotation**
    

-    **Use Start Point**
    

-    **Use Compensation**
    

-    **Process Holes ****
    

-    **Process Circles ****
    

-    **Process Perimeter ****
    

**\*\*** Availability changes based on selections in Base Geometry section.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

Example:

 
```python
#Place code example here.
```




 {{Path_Tools_navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Profile
