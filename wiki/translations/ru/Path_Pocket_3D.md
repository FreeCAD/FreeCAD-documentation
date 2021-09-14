---
- GuiCommand:
   Name:Path Pocket 3D
   MenuLocation:Path → 3D Pocket
   Workbenches:[Path](Path_Workbench.md)
---

## Описание

This command inserts a path <img alt="" src=images/Path_3DPocket.svg  style="width:24px;"> [3D Pocket](Path_Pocket_3D.md) object into the Job. This operation takes into account the bottom surface of the pocket, as well as selected walls that are not vertical. In its current state, this operation is used to rough out a pocket with non-vertical walls and/or non-horizontal bottom. A common finishing technique is to use a ball end mill with the experimental <img alt="" src=images/Path_3DSurface.svg  style="width:24px;"> [3D Surface](Path_3DSurface.md) operation. <img alt="Sample image of 3D Pocket operation used to clear cylindrical battery holder." src=images/Path_3D_Pocket_Sample.png  style="width:600px;">

## Применение

### Creating a 3D Pocket 

1.  From within a Job, select one or more Faces from the Job Model to include as the Base Geometry.
2.  Invoke the **<img src="images/Path_3DPocket.svg" width=16px> [Pocket 3D](Path_Pocket_3D.md)** or select ** Path** → **<img src="images/Path_3DPocket.svg" width=16px> [Pocket 3D](Path_Pocket_3D.md)** command from the top menu.
3.  Choose a Tool controller from the pop up selection dialogue window.
4.  Add or subtract Base Geometry elements as needed to configure the Operation.
5.  Check the Depths tab to ensure the Start Depth, Finish Depth, and Step Down percentage are correct. The Final Depth is determined by the Body Geometry selection and is not modifiable.
6.  Check the Heights tab to ensure the Safe and Clearance Heights are appropriate.
7.  Check the Operation tab where the Tool controller can be re-selected, the Cut mode can be configured for Climb or Conventional milling, the Pattern can be set, the Step Over percentage can be adjusted, and Pass Extension can be applied.
8.  Click **Apply** to observe the milling path for the passes of the Operation. Adjust parameters until satisfied with the Operation.
9.  Click **OK** to save the Operation.

## Примечания

-   All paths generated from this operation are based on a standard end mill using the diameter of the tool you selected for this 3D Pocket operation.
-   Ball end mills and other shapes are not respected for path generation even if selected as the tool for this operation.

## Options

-   Use the **Adaptive Pocket Finish** property to attempt to minimize air milling below a 3D Pocket in cases where the pocket is a hole through the model.
-   Use the **Adaptive Pocket Start** property to attempt to minimize air milling upon entry to the pocket. For example, look at the sample image above in the [Description](Path_Pocket_3D#Description.md) section of this page. In order to reduce the air milling above that 3D Pocket, toggle this property to True and the paths will begin closer to the pocket, much nearer to where the pocket actually begins. See the following image and note the difference in the path start height. The air milling is reduced.

<img alt="Sample image of 3D Pocket operation used to clear cylindrical battery holder with the Adaptive Pocket Start enabled in order to reduce air milling upon entry." src=images/3D_Pocket_Sample_Adaptive_Start.png  style="width:600px;">

-   If you wish to process the entire model and stock as a whole, use the **Process Stock Area** property set to True with no Base Geometry selected.

## Properties

### Data Tab 

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

#### Depth

-    **Clearance Height**: The height needed to clear clamps and obstructions

-    **Final Depth**: Final Depth of Tool- lowest value in Z

-    **Finish Depth**: Maximum material removed on final pass.

-    **Safe Height**: The above which Rapid motions are allowed.

-    **Start Depth**: Starting Depth of Tool- first cut depth in Z

-    **Step Down**: Incremental Step Down of Tool

#### Face

-    **Offset Pattern**: Clearing pattern to use. (Select in which manner the horizontal movements should be done.)

#### Path

-    **Active**: make False, to prevent operation from generating code

-    **Base**: The base geometry for this operation

-    **Comment**: An optional comment for this Operation

-    **Coolant Mode**: The coolant mode for this operation.

-    **Cycle Time**: The cycle time estimation for this operation.

-    **Tool Controller**: Defines the Tool controller used in the Operation

-    **User Label**: User assigned label

#### Pocket

-    **Adaptive Pocket Finish**: Use adaptive algorithm to eliminate excessive air milling below planar pocket bottom.

-    **Adaptive Pocket Start**: Use adaptive algorithm to eliminate excessive air milling above planar pocket top.

-    **Cut Mode**: The direction that the toolpath should go around the part ClockWise (CW) or CounterClockWise (CCW)

-    **Extra Offset**: Extra offset to apply to the operation. Direction is operation dependent.

-    **Handle Multiple Features**: Choose how to process multiple Base Geometry features.

-    **Keep Tool Down**: Attempts to avoid unnecessary retractions.

-    **Min Travel**: Use 3D Sorting of Path

-    **Process Stock Area**: Process the model and stock in an operation with no Base Geometry selected.

-    **Start At**: Start pocketing at center or boundary

-    **Step Over**: Percent of cutter diameter to step over on each pass

-    **Zig Zag Angle**: Angle of the zigzag pattern

#### Rotation

Note: Rotation is not available for 3D Pocket as of 0.19.

-    **Enable Rotation**: Enable rotation to gain access to pockets or areas not normal to Z axis.

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

-    **Use Start Point**: Make True, if manually specifying a Start Point. Set the start point in the property data Start Point field.

### View

Empty

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

Example:


```python
#Place code example here.
```





{{Path_Tools_navi

}} 
