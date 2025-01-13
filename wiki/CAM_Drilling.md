---
 GuiCommand:
   Name: CAM Drilling
   MenuLocation: CAM , Drilling
   Workbenches: CAM_Workbench
---

# CAM Drilling

## Description

The <img alt="" src=images/CAM_Drilling.svg  style="width:16px;"> [Drilling](CAM_Drilling.md) tool generates a drilling Operation in the Job.

 <img alt="" src=images/Path_Drilling_Sample.png  style="width:400px;">  
*Above: CAM Drilling operation sample*

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/CAM_Drilling.svg" width=16px> [CAM Drilling](CAM_Drilling.md)** button.
    -   Select the **CAM → <img src="images/CAM_Drilling.svg" width=16px> Drilling** option from the menu.
2.  In the **Operation** section:
    -   Select a **ToolController**.
    -   Select a **Coolant Mode**.
    -   Optionally enable and adjust the following:
        -   
            **Peck**
            
            set the **Depth**.

        -   
            **Dwell**
            
            set the **Time** in seconds.

        -   
            **Extended Depth**
            
            .
3.  In the **Base Geometry** section confirm that the list matches the holes that are intended for processing, and adjust add, enable, or disable, as necessary. Holes can be added by selecting the wall faces of the Holes.
4.  In the **Depths** section check, and if required adjust, the **Start Depth** and **Final Depth**.
5.  In the **Heights** section check, and if required adjust, the **Safe Height** and the **Clearance Height**.
6.  Press the **OK** button to generate the drilling path(s).

## Notes

-   When using edges for Base Geometry, always select the bottom edge of the hole.
-   Always verify the tool chosen is the correct diameter for the hole(s) selected.
-   **Peck disabled** generates (G81 canned drill cycles). **Peck enabled** generates (G83 canned drill cycles).
-   **Dwell enabled** is currently unsupported, but is intended to generate (G82 canned drill cycles).

## Properties

***Note***: Not all of these Properties are available in the Task Window Editor. Some are only accessible in the Data tab of the Properties View panel for this Operation.


{{TitleProperty|Base}}

Note: It is suggested that you do not edit the Placement property of path operations. Rather, move or rotate the CAM Job model as needed.

-    **Placement**: Overall placement\[position and rotation\] of the object - with respect to the origin (or origin of parent object container)

    -   
        **Angle**
        
        : Angle in degrees applied to rotation of the object around Axis property value

    -   
        **Axis**
        
        : Axis (one or multiple) around which to rotate the object, set in sub-properties: X, Y, Z

        -   
            **X**
            
            : X axis value

        -   
            **Y**
            
            : Y axis value

        -   
            **Z**
            
            : Z axis value

    -   
        **Position**
        
        : Position of the object, set in sub-properties: X, Y, Z - with respect to the origin (or origin of parent object container)

        -   
            **X**
            
            : X distance value

        -   
            **Y**
            
            : Y distance value

        -   
            **Z**
            
            : Z distance value

-    **Label**: User-provided name of the object (UTF-8)

-    **Disabled**: List of disabled features


{{TitleProperty|Depth}}

-    **Clearance Height**: The height needed to clear clamps and obstructions

-    **Final Depth**: Final Depth of Tool- lowest value in Z

-    **Safe Height**: The height above which Rapid motions are allowed. (Rapid safety height between locations)

-    **Start Depth**: Starting depth of Tool - *first cut depth in Z*


{{TitleProperty|Drill}}

-    **Add Tip Length**: Calculate the tip length and subtract from final depth

-    **Dwell Enabled**: Enable dwell

-    **Dwell Time**: The time to dwell between peck cycles

-    **Peck Depth**: Incremental Drill depth before retracting to clear chips

-    **Peck Enabled**: Enable pecking

-    **Retract Height**: The height where feed starts and height during retract tool when path is finished

-    **Return Level**: Controls how tool retracts Default=G98


{{TitleProperty|Path}}

-    **Active**: Make False, to prevent operation from generating code

-    **Comment**: An optional comment for this Operation

-    **User Label**: User assigned label

-    **Tool Controller**: Defines the Tool controller used in the Operation


{{TitleProperty|Rotation}}

(*when available*)

-    **Attempt Inverse Angle**: Automatically attempt Inverse Angle if initial rotation is incorrect.

-
-    **Enable Rotation**: Enable rotation to gain access to holes not normal to Z axis.

-    **Inverse Angle**: Inverse the angle of the rotation. ***Example:** change a rotation from -22.5 to 22.5 degrees.*

-    **Reverse Direction**: Reverse orientation of Operation by 180 degrees.

## Tasks Window Editor Layout 

*Descriptions for the settings are provided in the Properties list above.*

This section is simply a layout map of the settings in the window editor for the Operation.

### Base Geometry 

-   **Add**: Adds selected element(s) which should be the base(s) for the path(s).
-   **Delete**: Delete the selected item(s) in the Base Geometry list.
-   **Clear**: Clear all items in the Base Geometry list.

### Base Location 

-   **Add**: Add an (X,Y) coordinate location to the current drilling operation.
-   **Remove**: Remove the selected location item(s) from the Base Location list.
-   **Edit**: Edit the selected location item.

### Depths

-   **Start Depth**:
-   **Final Depth**:

### Heights

-   **Safe Height**:
-   **Clearance Height**:

### Operation

-   **Tool Controller**:
-   **Retract Height**:
-   **Peck**:
-   **Peck Depth**:
-   **Dwell**:
-   **Dwell Time**:
-   **Use Tip Length**:

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

Example:

 
```python
#Place code example here.
```




 {{CAM_Tools_navi}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Drilling
