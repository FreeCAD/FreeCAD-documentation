---
- GuiCommand:
   Name:Path MillFace
   MenuLocation:Path → Face
   Workbenches:[Path](Path_Workbench.md)
---

# Path MillFace/pt-br

## Description

The <img alt="" src=images/Path_MillFace.svg  style="width:24px;"> [Mill Face](Path_MillFace.md) tool creates a path to perform a facing operation on a horizontal surface. This operation is generally used:

-   to smooth out a rough stock surface,
-   to mill selected face(s) to desired depth in preparation for performing subsequent clearing operations within the boundary of the regions affected by this operation,
-   or to apply a finishing surface to the selected face(s).

This operation contains a **BoundaryShape** property that allows for a modified selection area based upon the selected face(s).

<img alt="Sample image of Mill Face operation used to prepare stock surface for subsequent clearing operation." src=images/MillFace_Sample.png  style="width:600px;">

## Usage

1.  Select one or more faces to be surfaced. **Note:** If selected faces exist at different heights, then all will be milled to the Final Depth setting.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Path_MillFace.svg" width=16px> [Path MillFace](Path_MillFace.md)** button.
    -   Select the **Path → <img src="images/Path_MillFace.svg" width=16px> Face** option from the menu.
3.  Select the correct **BoundaryShape** setting to modify the milling area based on the face(s) selected as **Base Geometry**.
4.  Adjust the other properties as needed. They are listed further below.

## Caveats

-   Using it on an inclined plane may produce unexpected results: it will still produce a path to cut a horizontal surface. The extent of the cut will be the vertical projection of the inclined plane, performed at a height corresponding to the lowest point in that plane.

-   Since the path tools work on the geometry of the selected edges/faces only, and do not relate to the rest of the 3D model, the paths will not go beyond the bounds of the chosen plane, even if it is surrounded by unused stock or air. This will leave unmachined corners. These can sometimes removed with one of the dress-up tools to be found on the *Path* menu.

## Vertical face milling 

-   This tool will not work on a **vertical plane** or vertical non planar surface. Vertical operations can be achieved by using the face profile tool or edge profile tool. These will need the selection of a face or closed loop of edges *including the top or bottom edge of the vertical surface desired*). The extent of the path can then be reduced using the *Boundary Dress-up* tool to be found on the *Path* menu. With the Dress-up tool select *Create Box* option and reduce the size to limit the scope of the profile path. These settings will not allow the origin of the boundary box to be moved, however. This must be done by adjusting the Placement settings in the [tree view](Tree_view.md).
-   This will work on compound surfaces such as several vertical planes or cylindrical surfaces joined together, so long as they form one continuous surface.

## Options

Empty

## Properties

\'\'\' *Note* \'\'\': The names of some Properties in this list differ a little from the same settings used in the Task Window Editor.

### Data


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

-    **Finish Depth**: Maximum material removed on final pass.

-    **Safe Height**: The above which Rapid motions are allowed.

-    **Start Depth**: Starting Depth of Tool- first cut depth in Z

-    **Step Down**: Incremental Step Down of Tool


{{TitleProperty|Face}}

-    **BoundaryShape**: Shape to use for calculating Boundary

-    **ClearEdges**: Clear edges of surface (Only applicable to BoundBox)

-    **ExcludeRaisedAreas**: Exclude milling raised areas inside the face.

-    **Offset Pattern**: Clearing pattern to use. (Select in which manner the horizontal movements should be done.)


{{TitleProperty|Path}}

-    **Active**: make False, to prevent operation from generating code

-    **Base**: The base geometry for this operation

-    **Comment**: An optional comment for this Operation

-    **Coolant Mode**: The coolant mode for this operation.

-    **Cycle Time**: The cycle time estimation for this operation.

-    **Tool Controller**: Defines the Tool controller used in the Operation

-    **User Label**: User assigned label


{{TitleProperty|Pocket}}

-    **Cut Mode**: The direction that the toolpath should go around the part ClockWise (CW) or CounterClockWise (CCW)

-    **Extra Offset**: Extra offset to apply to the operation. Direction is operation dependent.

-    **StartAt**: Start pocketing at center or boundary

-    **Step Over**: Percent of cutter diameter to step over on each pass

-    **Zig Zag Angle**: Angle of the zigzag pattern

-    **Offset Pattern**: Clearing pattern to use

-    **Min Travel**: Use 3D Sorting of Path

-    **Keep Tool Down**: Attempts to avoid unnecessary retractions.


{{TitleProperty|Rotation}}

-    **Attempt Inverse Angle**: Automatically attempt Inverse Angle if initial rotation is incorrect.

-    **Enable Rotation**: Enable rotation to gain access to pockets or areas not normal to Z axis.

-    **Inverse Angle**: Inverse the angle of the rotation. \'\' **Example:** change a rotation from -22.5 to 22.5 degrees.\'\'

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



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path MillFace/pt-br
