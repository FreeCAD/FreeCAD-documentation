# Status bar/en
## Introduction

The [status bar](status_bar.md) is a simple ribbon that appears at the bottom of the FreeCAD [interface](interface.md).

When the mouse pointer is over a button or menu, the usage information of that command is displayed both in a textual popup and in the status bar.

![](images/FreeCAD_Status_bar.png )

The status bar shows the [mouse navigation](Mouse_navigation.md) mode and the zoom level on the right. The zoom level gives the size of the current [3D view](3D_view.md) in appropriate units for the current scale, for example, millimeters (mm) or meters (m).

The status bar also shows the last pre-selected object (any object under the pointer is pre-selected) or element of an object (vertex, edge, face), and the coordinates of the mouse pointer when the last pre-selection occurred; this is useful to know immediately the coordinate of specific vertices in your shapes. The 3D coordinates update automatically as long as the mouse pointer floats over a geometrical element; the update stops when the mouse pointer rests over an empty space in the [3D view](3D_view.md).

![](images/FreeCAD_Status_bar_selected.png )

## Quick measure 


<small>(v1.0)</small> 

The Quick measure feature uses the right side of the Status bar to show measurements based on the selection in 3D view:

-   Edge length
-   Face area
-   Distance between points, edges or faces
-   Angle between edges
-   Radius of circular edges or cylindrical faces


{{Interface navi

}}



---
⏵ [documentation index](../README.md) > Status bar/en
