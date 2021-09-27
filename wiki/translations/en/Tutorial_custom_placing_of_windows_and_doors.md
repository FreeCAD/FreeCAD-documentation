# Tutorial custom placing of windows and doors/en
{{TutorialInfo
|Topic=Architecture
|Level=Intermediate
|Time=60 minutes
|Author=[https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=21943 vocx]
|FCVersion=0.18 or greater
|Files=none
}}

## Introduction

This tutorial shows how to place custom designed [Arch Windows](Arch_Window.md) and [Arch Doors](Arch_Door.md) in a building model. It uses the [Draft Workbench](Draft_Workbench.md), the [Arch Workbench](Arch_Workbench.md), and the [Sketcher Workbench](Sketcher_Workbench.md).

Common tools used are: [Draft Grid](Draft_Snap_Grid.md), [Draft Snap](Draft_Snap.md), [Draft Wire](Draft_Wire.md), [Arch Wall](Arch_Wall.md), [Arch Window](Arch_Window.md), and [Sketcher NewSketch](Sketcher_NewSketch.md). The user should be familiar with constraining sketches.

This tutorial was inspired by the tutorials by jpg87 posted in the [FreeCAD forums](https://forum.freecadweb.org/viewforum.php?f=36).

-   [Arch Create a custom window](https://forum.freecadweb.org/viewtopic.php?f=36&t=32883)
-   [Arch : How to use your custom Window](https://forum.freecadweb.org/viewtopic.php?f=36&t=32982)

See also the following thread for more information on the position of windows and doors.

-   [Discussion: Orientation of Windows and Doors](https://forum.freecadweb.org/viewtopic.php?t=35368)

See also the following page for some videos on how to align windows.

-   [The workbench used to create architectural projects is called Arch](http://help-freecad-jpg87.fr/04_arch_ind.php)

## Setup

1\. Open FreeCAD, create a new empty document, and switch to the [Arch Workbench](Arch_Workbench.md).

2\. Make sure your units are set correctly in the menu **Edit → Preferences → General → Units**. For example, `MKS (m/kg/s/degree)` is good for dealing with distances in a typical building; moreover, set the number of decimals to `4`, to consider even the smallest fractions of a meter.

3\. Use the [Draft ToggleGrid](Draft_ToggleGrid.md) button to show a grid with enough resolution. You can change the grid appearance in the menu **Edit → Preferences → Draft → Grid and snapping → Grid**. Set lines at every `50 mm`, with major lines every `20` lines (every meter), and `1000 lines` in total (the grid covers an area of 50 m x 50 m).

4\. [Zoom out](Zoom_out.md) of the 3D view if you are too close to the grid.

Now we are ready to create a simple wall on which we can position windows and doors.

## Placing a wall 

5\. Use the [Draft Wire](Draft_Wire.md) tool to create a wire. Go counterclockwise.

:   5.1. First point in (0, 4, 0); in the dialog enter **0** **m** **Enter**, **4** **m** **Enter**, **0** **m** **Enter**.
:   5.2. Second point in (2, 0, 0); in the dialog enter **2** **m** **Enter**, **0** **m** **Enter**, **0** **m** **Enter**.
:   5.3. Third point in (4, 0, 0); in the dialog enter **4** **m** **Enter**, **0** **m** **Enter**, **0** **m** **Enter**.
:   5.4. Fourth point in (6, 2, 0); in the dialog enter **6** **m** **Enter**, **2** **m** **Enter**, **0** **m** **Enter**.
:   5.4. Fifth point in (6, 5, 0); in the dialog enter **6** **m** **Enter**, **5** **m** **Enter**, **0** **m** **Enter**.
:   5.5. In the number pad press **A** to finish the wire.
:   5.6. In the number pad press **0** to get an [axonometric view](axonometric_view.md) of the model.
:   
    **Note:**make sure the **Relative** checkbox is disabled if you are giving absolute coordinates.
:   
    **Note 2:**the points can also be defined with the mouse pointer by choosing intersections on the grid, with the help of the [Draft Snap](Draft_Snap.md) toolbar and the [Draft Grid](Draft_Snap_Grid.md) method.
:   
    **Note 3:**you can also create shapes programmatically by scripting in [Python](Python.md). Beware that most functions expect their input in millimeters.


```python
import FreeCAD
import Draft

p = [FreeCAD.Vector(0.0, 4000.0, 0),
FreeCAD.Vector(2000.0, 0.0, 0.0),
FreeCAD.Vector(4000.0, 0.0, 0.0),
FreeCAD.Vector(6000.0, 2000.0, 0.0),
FreeCAD.Vector(6000.0, 5000.0, 0.0)]

w = Draft.makeWire(p, closed=False)
```

6\. Select the `DWire` and click the [Arch Wall](Arch_Wall.md) tool; the wall is immediately created with a default width (thickness) of 0.2 m, and height of 3 m.

<img alt="" src=images/01_T02_wire_wall.png  style="width:600px;">


*align=center|Base wire for the wall*

<img alt="" src=images/02_T02_just_wall.png  style="width:600px;">


*align=center|Wall constructed from the wire*

## Placing preset doors and windows 

7\. Click the [Arch Window](Arch_Window.md) tool; as preset select `Simple door`, and change the height to 2 m.

:   7.1. Change the snapping to [Draft Midpoint](Draft_Snap_Midpoint.md), and try selecting the bottom edge of the frontal wall; rotate the [standard view](standard_view.md) as necessary to help you pick the edge and not the wall face; when the midpoint is active, click to place the door.
:   7.2. Click the [Arch Window](Arch_Window.md) tool again, and place another door, but this time in the midpoint of the rightmost wall; rotate the [standard view](standard_view.md) as necessary.

<img alt="" src=images/03_T02_wall_place_doors.png  style="width:600px;">


*align=center|Snapping to the midpoint of the bottom edge of the wall to place the door*


:   
    **Note:**the `Sill height` is the distance from the floor to the lower edge of the element. For doors the `Sill height` is usually 0 m as doors are normally touching the floor; on the other hand, windows have a usual separation of 0.5 m to 1.5 m from the floor. The `Sill height` can only be set when initially creating the window or door from a preset. Once the window or door is inserted, modify its placement by editing the **Position** vector `[x, y, z]` of the underlying [Sketcher Sketch](Sketcher_Sketch.md).

## Creating custom doors and windows 

8\. Switch to the [Sketcher Workbench](Sketcher_Workbench.md); select the part of the wall to the right that has no door; click on the [Sketcher NewSketch](Sketcher_NewSketch.md); select **FlatFace** as attachment method. If the existing geometry obstructs your view, click on [Sketcher ViewSection](Sketcher_ViewSection.md) to remove it.

9\. Draw a fancy sketch containing three closed wires. Make sure to provide constraints to all wires.

:   9.1. The outside wire is the biggest one, and will define the main dimensions of the window object, and the size of the hole created when it\'s embedded in an [Arch Wall](Arch_Wall.md). Make sure the dimensions are named appropriately, for example, `Width` and `Height`. A constraint also defines the curvature of the outer wire; give it an appropriate name, like `HeightCurve`.
:   9.2. The second wire is offset from the outer wire, and together with it, they define the width of the fixed frame of the window. Name the offset appropriately, for example, `FrameFixedOffset`. It will be used for both the top vertical and horizontal offsets. The bottom offset, if set to zero, will result in the fixed frame touching the bottom of the window; this can be used to model a door instead of a window. Give it an appropriate name, like `FrameFixedBottom`.
:   9.3. The third, innermost wire is offset from the second wire, and together with it, they define the frame of the window that can open. The innermost wire also defines the size of the glass panel. Again, give meaningful names to these offsets, for example, `FrameInnerOffset` and `FrameInnerBottom`.
:   9.4. In order to build succesfully the sketch, use horizontal ([Sketcher ConstrainHorizontal](Sketcher_ConstrainHorizontal.md)) and vertical ([Sketcher ConstrainVertical](Sketcher_ConstrainVertical.md)) constraints for the straight sides; use auxiliary construction geometry ([Sketcher ToggleConstruction](Sketcher_ToggleConstruction.md)), and tangential constraints ([Sketcher ConstrainTangent](Sketcher_ConstrainTangent.md)) to correctly place the circular arcs at the top. As in this case the window is symmetrical, consider equality ([Sketcher ConstrainEqual](Sketcher_ConstrainEqual.md)), symmetrical ([Sketcher ConstrainSymmetric](Sketcher_ConstrainSymmetric.md)), and point on object ([Sketcher ConstrainPointOnObject](Sketcher_ConstrainPointOnObject.md)) constraints where it makes sense.

![](images/04_T02_window_constraints_outer_frame.png )


*align=center|Constraints for the outer wires of the sketch that form the window*

![](images/05_T02_window_constraints_inner_frame.png )


*align=center|Constraints for the inner wires of the sketch that form the window*

10\. Once the sketch is fully constrained, press **Close** to exit the sketch ([Sketcher LeaveSketch](Sketcher_LeaveSketch.md)).

:   10.1. Since a face of the wall was selected during the initial step of creating the sketch, the sketch is co-planar with that face; however, it may be in the wrong position, away from the wall. If this is the case, adjust **Position** within **Attachment Offset**. Set **Position** to `[4 m, 1 m, 0 m]` so the sketch is centered in the wall, and it is one meter above the floor level.
:   10.2. You can see the named constraints under **Constraints**. The values can be modified to see the sketch change dimensions immediately.

<img alt="" src=images/07_T02_window_sketch_in_wall.png  style="width:600px;">


*align=center|Window sketch moved to the desired position on the wall*

<img alt="" src=images/06_T02_window_sketch_properties_constraints.png  style="width:600px;">


*align=center|Named constraints of the sketch, which can be modified without going inside the sketch*

11\. Change back to the [Arch Workbench](Arch_Workbench.md) and, with the new `Sketch002` selected, use [Arch Window](Arch_Window.md). A window will be created, and will make a hole in the wall. The window is made from a custom sketch, and not from a preset, so it needs to be edited in order to correctly display its components, that is, the fixed frame, the inner frame, and the glass panel.

<img alt="" src=images/08_T02_window_basic_in_wall.png  style="width:600px;">


*align=center|Custom window created from the sketch; it still doesn't have a proper frame, nor glass*

## Setting up the custom window 

12\. In the tree view select `Sketch002` underlying `Window`, and press **Space**, or change the property **Visibility** to `True`.

13\. Double click `Window` in the tree view to start editing it.

:   13.1. Inside the `Window elements` dialog there are two panes, `Wires` and `Components`. There are three wires, `Wire0`, `Wire1`, and `Wire2`, and one component, `Default`. The wires refer to the closed loops that were drawn in the sketch; the components define the areas in the sketch that will be extruded to create frame or glass panels with real thicknesses; these areas are delimited by the wires. A window created from a preset already has two components, `OuterFrame` and `Glass`. The custom window needs to be edited to have a similar structure.

![](images/09_T02_window_edit_default.png )


*align=center|Dialog to edit a window or a door*


:   13.2. Click on `Default`, and click the **Remove** button to eliminate it.





:   13.3. Click **Add**; this shows the properties of a new component like `Name`, `Type`, `Wires`, `Thickness`, `Offset`, `Hinge`, and `Opening mode`. Give a name, such as `OuterFrame`, choose `Frame` for `Type`, and click on `Wire0` and then `Wire1`; they should highlight in the 3D viewport. Add a small value for `Thickness`, `15 mm`, and check the checkbox to add the default value. This default value is the length assigned to the **Frame** property; a similar default can be assigned to the **Offset** property. Click the **+Create/update component** button to finish editing the component.





:   13.4. Click **Add**; give another name, such as `InnerFrame`, choose `Frame` for `Type`, and click on `Wire1` and then `Wire2`. Add a sensible `Thickness`, `60 mm`, and `Offset`, `15 mm`. Then click the **+Create/update component** button.





:   13.5. Click **Add**; give another name, such as `Glass`, choose `Glass panel` for `Type`, and click on `Wire2`. Add a sensible `Thickness`, `10 mm`, and `Offset`, `40 mm`. Then click the **+Create/update component** button. If any of the three components needs to be modified, select it and press **Edit**; modifications are only saved after pressing the **+Create/update component** button.

![](images/10_T02_window_edit_components.png )


*align=center|Editing a previously defined component of a window or a door*


:   13.6. If everything is set, click **Close** to finish editing the window. The sketch may become hidden again, but the window will show distinct solid elements for the `OuterFrame`, the `InnerFrame`, and the `Glass`. Give a value of `100 mm` to **Frame** to assign a default thickness, which will be added to the value specified in the `OuterFrame` component.

![](images/11_T02_window_property_view.png )


*align=center|Property view of the window to add default Frame length, Offset length, and other options*

<img alt="" src=images/12_T02_window_finished.png  style="width:600px;">


*align=center|Finished window with appropriate components embedded in the wall*

## Duplicating the custom window 

14\. In the tree view, select `Window` and its underlying `Sketch002`. Then go to **Edit → Duplicate selection**, and answer **No** if asked to duplicate unselected dependencies. A new `Window001` and `Sketch003` will appear in the same position as the original elements.

15\. Select the new `Sketch003`. Go to the **Map Mode** property, and click on the ellipsis next to the `FlatFace` value. In the 3D viewport select the left side of the wall which doesn\'t have any element; rotate the [standard view](standard_view.md) as necessary. Change the `Attachment offset` to \[-1 m, 0 m, 0 m\] to center the window, and click **OK**. The sketch and the window should appear in a new position.

:   
    **Note:**the [attachment operation](Part_EditAttachment.md) can also be performed by changing to the [Part Workbench](Part_Workbench.md), and then using the menu **Part → Attachment**.

![](images/13_T02_sketch_attachment_edit.png )


*align=center|Dialog to edit the attachment plane of the sketch*

16\. You may adjust the dimensions of the new window by changing the named parameters in `Sketch003` under **Constraints**, for example, set `Height` to `2 m`, and `Frame Fixed Bottom` to `0 m`. Then press **Ctrl**+**R** to [recompute](recompute.md) the model. If the wall doesn\'t show a bigger hole for the new window, select the wall in the tree view, right click and choose `Mark to recompute`, then press **Ctrl**+**R** again.

17\. These operations have changed the position of the new window, but the opening in the wall doesn\'t look correct. It is slanted, that is, the hole is not perpendicular to the face of the wall, and it may even cut other parts of the wall. The problem is that `Window001` has retained the **Normal** information of the original `Window`.

<img alt="" src=images/14_T02_sketch_2_attached_slanted.png  style="width:600px;">


*align=center|Incorrect opening in the wall due to bad Normal of the window*

## Normals of doors and windows 

18\. Each [Arch Window](Arch_Window.md) object controls the extrusion of its body and the opening that is created in its host wall by means of the **Normal**.

The normal is a vector `[x, y, z]` that indicates a direction perpedicular to a wall. When a window or door preset is created with the [Arch Window](Arch_Window.md) tool directly over an [Arch Wall](Arch_Wall.md), the normal is automatically calculated, and the resulting window or door is correctly aligned; the first two objects, `Door` and `Door001`, were created in this way.

In similar way, when a sketch is created by selecting a planar surface, it is oriented on this plane. Then when the [Arch Window](Arch_Window.md) tool is used, the window will use as normal the perpendicular direction to the sketch. This was the case with the third object, the custom `Window`.

If the window already exists and needs to be moved, as was the case with the duplicated `Window001` object, the sketch needs to be remapped to another plane; doing this moves both the sketch and the window, but the latter doesn\'t automatically update its normal, so it has incorrect extrusion information. The normal needs to be calculated manually and written to **Normal**.

The three values of the normal vector are calculated as following. 
```python
x = -sin(angle)
y = cos(angle)
z = 0
``` Where `angle` is the angle of the local Z axis of the sketch with respect to the global Y axis.

When a sketch is created, it always has two axes, a local X (red) and a local Y (green). If the sketch is mapped to the global XY working plane, then these axes are aligned; but if the sketch is mapped on the global XZ or global YZ planes, as is common with windows and doors (the sketches are \"standing up\"), then the local Z (blue) forms an angle with the global Y axis; this angle varies from -180 to 180 degrees. The angle is considered positive if it opens counterclockwise, and it is negative if it opens clockwise, starting from the global Y axis.

<img alt="" src=images/15_T02_sketch_local_coordinates.png  style="width:600px;">


*align=center|Local coordinates of a sketch that is "standing up", that is, mapped to the global XZ plane*

<img alt="" src=images/16_T02_sketch_correct_normal_direction.png  style="width:600px;">


*align=center|Intended directions of the normals for each door and window*

If we look at the geometry created so far, we see the following normals.

`Door`
:   The local Z is aligned with the global Y, therefore, the `angle` is zero. The normal vector is


```python
x = -sin(0) = 0
y = cos(0) = 1
z = 0
```

or **Normal** is `[0, 1, 0]`.

`Door001`
:   The local Z is rotated 90 degrees from the global Y, therefore, the `angle` is 90 (positive, because it opens counterclockwise). The normal vector is


```python
x = -sin(90) = -1
y = cos(90) = 0
z = 0
```

or **Normal** is `[-1, 0, 0]`.

`Window`
:   The local Z is rotated 45 degrees from the global Y, therefore, the `angle` is 45 (positive, because it opens counterclockwise). The normal vector is


```python
x = -sin(45) = -0.7071
y = cos(45) = 0.7071
z = 0
```

or **Normal** is `[-0.7071, 0.7071, 0]`.

`Window001`
:   The local Z direction is found by using the [Draft Dimension](Draft_Dimension.md) tool and measuring the angle that the wall trace (`Wire`) makes with the global Y axis, or any line aligned to it. This angle is `26.57`; the desired angle is the complement to this, so 90 - 26.57 = 63.43.

This means the local Z axis is rotated 63.43 degrees from the global Y, therefore, the `angle` is -63.46 (negative, because it opens clockwise). The normal vector is 
```python
x = -sin(-63.43) = 0.8943
y = cos(-63.43) = 0.4472
z = 0
``` Therefore **Normal** should be changed to `[0.8943, 0.4472, 0]`.

After doing these changes, recompute the model with **Ctrl**+**R**. If the wall doesn\'t update the hole, select it in the tree view, right click and choose `Mark to recompute`, then press **Ctrl**+**R** again.

19\. The orientation of the extrusion of the window is resolved, together with the opening in the wall.

<img alt="" src=images/17_T02_sketch_2_attached_correctly.png  style="width:600px;">


*align=center|Correct opening in the wall due to proper Normal of the window*

## Final remarks 

20\. As demonstrated, the initial placement of the [Arch Window](Arch_Window.md) is very important. The user should either

-   use the [Arch Window](Arch_Window.md) tool to insert and automatically align a preset to a wall, or
-   map a sketch to the desired wall, and build the window after that.

If a window already exists, and it needs to be moved, the supporting sketch should be remapped to a new plane, and the **Normal** of the window needs to be recalculated.

The new normal direction can be obtained by measuring the `angle` of the new wall with respect to the global Y axis, considering whether this angle is positive (counterclockwise) or negative (clockwise), and using a simple formula. 
```python
x = -sin(angle)
y = cos(angle)
z = 0
```

To confirm that the operations are correct, the absolute magnitude of the normal vector should be one. That is, 
```python
abs(N) = 1 = sqrt(x^2 + y^2 + z^2)
abs(N) = 1 = sqrt(sin^2(angle) + cos^2(angle) + z^2)
```


{{Tutorials navi

}}   {{Sketcher Tools navi}}

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > Tutorial custom placing of windows and doors/en
