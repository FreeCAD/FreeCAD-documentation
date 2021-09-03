---
- GuiCommand:/it   Name:Path Pocket   Name/it:Tasca   Workbenches:[[Path Workbench/it   Path]]|MenuLocation:Path → Tasca   Shortcut:P,O   SeeAlso:---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento crea un\'operazione di scavo basato sulle facce o sulle pareti inferiori selezionate in una o più tasche dell\'oggetto in lavorazione.


</div>


<div class="mw-translate-fuzzy">

L\'oggetto Tasca di Path è fatto per essere parte di una [Lavorazione](Path_Job/it.md).


</div>

<img alt="" src=images/Path_Pocket_Shape_example.png  style="width:600px;">

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare una faccia o una parete inferiore di una tasca. Mentre di solito è più facile selezionare il fondo, le parete devono essere selezionati quando una tasca passa attraverso tutto.
2.  Premere il pulsante **<img src="images/Path_Pocket.png" width=16px> [Tasca](Path_Pocket_Shape/it.md)
**
3.  Regolare le proprietà desiderate


</div>

## Proprietà

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

#### Depth


<div class="mw-translate-fuzzy">

![](images/Path-DepthsAndHeights.gif ) *Descrizione delle proprietà dello strumento tasca*


</div>

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Visual reference for Depth properties (settings)*

#### Extension

-    **Extension Corners**: When enabled connected extension edges are combined to wires.

-    **Extension Length Default**: Default length of extensions.

#### Face

-    **Offset Pattern**: Clearing pattern to use. (Select in which manner the horizontal movements should be done.)

#### Path

-    **Active**: make False, to prevent operation from generating code

-    **Comment**: An optional comment for this Operation

-    **User Label**: User assigned label

-    **Tool Controller**: Defines the Tool controller used in the Operation

#### Pocket

-    **Cut Mode**: Specifies a CW or CCW move for the cut

-    **Extra Offset**: Extra offset to apply to the operation. Direction is operation dependent. (Extra value to stay away from final profile- *good for roughing toolpath*)

-    **Keep Tool Down**: Attempts to avoid unnecessary retractions.

-    **Min Travel**: Use 3D Sorting of Path (when multiple base geometries used).

-    **Start At**: Start pocketing at center or boundary

-    **Step Over**: Select the horizontal step over (**Percent** of tool diameter: 100% = tool diameter)

-    **Use Outline**: Uses the outline of the base geometry.

-    **Zig Zag Angle**: Angle of the zigzag pattern. (Select the path angle relative to X axis.)

#### Rotation

-    **Attempt Inverse Angle**: Automatically attempt Inverse Angle if initial rotation is incorrect.

-
-    **Enable Rotation**: Enable rotation to gain access to pockets or areas not normal to Z axis.

-    **Inverse Angle**: Inverse the angle of the rotation. \'\' **Example:** change a rotation from -22.5 to 22.5 degrees.\'\'

-    **Reverse Direction**: Reverse orientation of Operation by 180 degrees.

#### Start Point 

-    **Start Point**: The start point of this path

-    **Use Start Point**: make True, if manually specifying a Start Point, then enter Start Points in the property data Start Points field

## Tasks Window Editor Layout 

*Descriptions for the settings are provided in the Properties list above.* This section is simply a layout map of the settings in the window editor for the Operation.

#### Base Geometry 

-   **Add**: adds selected element(s) which should be the base(s) for the path(s)
-   **Delete**: delete the selected item(s) in the Base Geometry list
-   **Clear**: clear all items in the Base Geometry list

#### Extensions

-    **Show All**: If selected, all potential extensions are visualized. Enabled extensions in purple, disabled extensions in yellow.

-    **Extension Corners**
    

-    **Extension Length Default**
    

-   **Enable**

-   **Disable**

-   **Clear**

#### Depth 

-    **Start Depth**
    

-    **Final Depth**
    

-    **Step Down**
    

#### Height

-    **Safe Height**
    

-    **Clearance Height**
    

#### Operation

-    **Tool Controller**
    

-    **Cut Mode**
    

-    **Pattern**(Offset Pattern)

-    **Angle**(Zig Zag Angle)

-    **Step Over Percent**(Step Over)

-    **Pass Extension**: The distance the facing operation will extend beyond the boundary shape (base geometry)

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


```python
#Place code example here.
```


<div class="mw-translate-fuzzy">





</div>


{{Path_Tools_navi

}} 
