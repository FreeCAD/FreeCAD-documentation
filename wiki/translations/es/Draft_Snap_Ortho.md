# Draft Snap Ortho/es
---
 GuiCommand:   Name: Draft Snap Ortho   Workbenches: Draft Workbench   Draft, Arch Workbench , Ortho|Shortcut:    SeeAlso: ---


</div>



### Descripción

The <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:24px;"> **Draft Snap Ortho** option snaps to imaginary lines that cross the previous point at multiples of 45°. The lines and angles are relative to the XY plane of the [working plane](Draft_SelectPlane.md) coordinate system.

![](images/Draft_Snap_Ortho_example.png ) 
*Snapping the second point of a line to an imaginary line that has an angle of 45° with the X axis. The small magenta circles indicate all possible directions.*

## Usage

For general information about snapping see [Draft Snap](Draft_Snap.md).

1.  Make sure snapping is enabled. See <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Snap Lock](Draft_Snap_Lock.md).
2.  If **Draft Snap Ortho** is not active do one of the following:
    -   Press the **<img src="images/Draft_Snap_Ortho.svg" width=16px> [Snap ortho](Draft_Snap_Ortho.md)** button in the Draft snap toolbar.
    -   [Draft](Draft_Workbench.md): Press the **<img src="images/Draft_Snap_Ortho.svg" width=16px> [Snap ortho](Draft_Snap_Ortho.md)** button in the [Draft snap widget](Draft_snap_widget.md).
    -   [BIM](BIM_Workbench.md): Select the **Snapping → <img src="images/Draft_Snap_Ortho.svg" width=16px> Snap ortho** option from the menu, or from the [3D view](3D_view.md) context menu.
3.  Choose a Draft or BIM command to create your geometry.
4.  Note that you can also change snap options while a command is active.
5.  Pick a first point. This snap option requires a previous point.
6.  If you move the cursor around the previous point you will notice a \"magnetic\" effect when the cursor is on an imaginary infinite line crossing that point at an angle of 0°, 45°, 90° or 135°.
7.  The point is marked and the <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:16px;"> icon is displayed near the cursor.
8.  Click to confirm the point.

## Preferences

See [Draft Snap](Draft_Snap#Preferences.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Ortho/es
