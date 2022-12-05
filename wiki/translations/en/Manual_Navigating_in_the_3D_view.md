# Manual:Navigating in the 3D view/en
{{Manual:TOC}}

### A word about the 3D space 

If this is your first contact with a 3D application, you will need to become familiar with some concepts first. If not, you can safely skip this section.

The FreeCAD 3D space is a [Euclidean space](https://en.wikipedia.org/wiki/Euclidean_space). It has an origin point and three axes: X, Y and Z. If you look at your scene from above, conventionally, the X axis points to the right, the Y axis to the back, and the Z axis upwards. In the lower right corner of the FreeCAD view, you can always see from where you are viewing the scene:

![](images/Axes_orientation.png )

The point where the three axes meet is the origin. It is the point where the value of all coordinates is zero. For any given axis, moving in one direction will increase the coordinate value and moving in the opposite direction will decrease the coordinate value. Every point of every object that exists in the 3D space can be located by its (x,y,z) coordinates. For example, a point with coordinates (2,3,1) will lie at +2 units on the X axis, +3 units on the Y axis, and +1 unit on the Z axis:

![](images/3dspace_coordinates.jpg )

You can look at that scene from any angle, as if you were holding a camera. That camera can be moved left, right, up and down (pan), rotated around what it is pointing at (rotate) and brought closer to or further from the scene (zoom).

### The FreeCAD 3D view 

#### Mouse Navigation 

Navigating in the FreeCAD [3D view](3D_view.md) can be done with a mouse, a Space Navigator device, the keyboard, a touchpad, or a combination of those. FreeCAD implements several [navigation modes](Mouse_navigation.md), which determine how the three basic view manipulation operations (pan, rotate and zoom) are done, as well as how selection of objects on the screen is performed. Navigation modes are accessed from the Preferences screen, or directly by right-clicking anywhere on the [3D view](3D_view.md):

![](images/FreeCAD-v0-18-NavigationModePopup.png )

Each of these modes allocates different mouse buttons, or mouse + keyboard combinations, or mouse gestures, to these four operations. The following table shows the principal available modes:

++++++
| Mode              | Pan                                                                                                                                                                                                                                 | Rotate                                                                                                                                                                                                 | Zoom                                                                                                                                                                                              | Select                                                                                                        |
+===================+=====================================================================================================================================================================================================================================+========================================================================================================================================================================================================+===================================================================================================================================================================================================+===============================================================================================================+
| OpenInventor      | ![Click middle button mouse](images/Pan-mouse.svg )                                                                                                                                                             | ![Click left button mouse](images/Select-mouse.svg )                                                                                                                                 | ![Roll middle button mouse](images/Zoom-mouse.svg )                                                                                                                            | Hold **Ctrl** + drag ![Click left button mouse](images/Select-mouse.svg ) |
++++++
| CAD **(default)** | ![Click middle button mouse](images/Pan-mouse.svg ) or ![Click right button mouse + CTRL key](images/Pan-mouse-CTRL.svg )                                                         | ![Hold middle then left mouse button](images/Rotate-mouse.svg ) or ![Click right button mouse + SHIFT key](images/Rotate-mouse-SHIFT.svg ) | ![Roll middle button mouse](images/Zoom-mouse.svg ) or ![Click right button mouse + CTRL + SHIFT key](images/Zoom-mouse-CTRL-SHIFT.svg ) | ![Click left button mouse](images/Select-mouse.svg )                                        |
++++++
| Blender           | Hold **Shift** + drag ![Click middle button mouse](images/Pan-mouse.svg ) or drag ![Click left + right button mouse and drag](images/Mouse_LMB%2BRMB.svg ) | ![Click middle button mouse](images/Pan-mouse.svg )                                                                                                                                | ![Roll middle button mouse](images/Zoom-mouse.svg )                                                                                                                            | ![Click left button mouse](images/Select-mouse.svg )                                        |
++++++
| Touchpad          | Hold **Shift** + drag ![Touchpad (mouse) pointer](images/Touchpad.png )                                                                                                                        |                                                                                                                                                                                         |                                                                                                                                                                                    | ![Click touchpad (mouse) left button](images/Select-touchpad.png )               |
|                   |                                                                                                                                                                                                                                     | **Alt**                                                                                                                                                                                            | **PgUp**                                                                                                                                                                                      |                                                                                                               |
|                   |                                                                                                                                                                                                                                     |                                                                                                                                                                                                     |                                                                                                                                                                                                |                                                                                                               |
|                   |                                                                                                                                                                                                                                     | \+ ![Touchpad (mouse) pointer](images/Touchpad.png )                                                                                                                                | / **PgDn**                                                                                                                                                                      |                                                                                                               |
++++++
| Gesture           | drag ![Click right button mouse](images/Pan-mouse-Ctrl.svg )                                                                                                                                                     | drag ![Click left button mouse](images/Select-mouse.svg )                                                                                                                            | ![Roll middle button mouse](images/Zoom-mouse.svg )                                                                                                                            | ![Click left button mouse](images/Select-mouse.svg )                                        |
++++++
| OpenCascade       | ![Click middle button mouse](images/Pan-mouse.svg )                                                                                                                                                             | ![Hold middle then right mouse button](images/Rotate-mouse-MMB+RMB.svg )                                                                                                 | ![Roll middle button mouse](images/Zoom-mouse.svg )                                                                                                                            | ![Click left button mouse](images/Select-mouse.svg )                                        |
++++++

#### Keyboard Navigation 

Alternatively, some keyboard controls are always available, no matter the navigation mode:

-    **Ctrl**\+ {{ASCII|43}} and **Ctrl** + {{ASCII|22}} to zoom in and out, respectively.

-   The arrow keys, {{ASCII|17}}{{ASCII|16}}{{ASCII|30}}{{ASCII|31}}, to shift the view left/right and up/down

-    **Shift**\+ {{ASCII|17}} and **Shift** + {{ASCII|16}} to rotate the view by 90 degrees

-   The numeric keys, {{ASCII|48}}{{ASCII|49}}{{ASCII|50}}{{ASCII|51}}{{ASCII|52}}{{ASCII|53}}{{ASCII|54}}, for the seven standard views: <img alt="" src=images/Std_ViewIsometric.svg  style="width:24px;"> [Isometric](Std_ViewIsometric.md), <img alt="" src=images/Std_ViewFront.svg  style="width:24px;"> [Front](Std_ViewFront.md), <img alt="" src=images/Std_ViewTop.svg  style="width:24px;"> [Top](Std_ViewTop.md), <img alt="" src=images/Std_ViewRight.svg  style="width:24px;"> [Right](Std_ViewRight.md), <img alt="" src=images/Std_ViewRear.svg  style="width:24px;"> [Rear](Std_ViewRear.md), <img alt="" src=images/Std_ViewBottom.svg  style="width:24px;"> [Bottom](Std_ViewBottom.md), and <img alt="" src=images/Std_ViewLeft.svg  style="width:24px;"> [Left](Std_ViewLeft.md)

-    **V**
    **O**will set the camera in <img alt="" src=images/View-isometric.svg  style="width:24px;"> [Orthographic view](Std_OrthographicCamera.md).

-   While **V****P** sets it in <img alt="" src=images/View-perspective.svg  style="width:24px;"> [Perspective view](Std_PerspectiveCamera.md).

-    **Ctrl**will allow you to select more than one object or element

These controls are also available from the [View menu](Std_View_Menu.md) and some from the View toolbar.

#### Using the Navigation Cluster 

In the default setup, there is a [Navigation Cluster](Navigation_Cube.md) in the upper right corner of the 3D display. This may be used to rotate the displayed object by a fixed amount, reset the display to one of several standard views, and change the display mode.

![](images/FreeCAD-v0-18-NavCube_SelectCorner.png )

When using the navigation cluster, a control point will turn light blue when the pointer is hovering over a sensitive area. If the area below the pointer does not change color, clicking on it will have no affect. As of this writing (v0.18), there are some registration issues which prevent all parts of some control points from being active.

Clicking on a face will switch the view to that face; clicking on a corner will switch to a view with that corner pointing towards you.

Clicking one of the four triangles will rotate the view 45 degrees in the indicated direction. Clicking one of the two curved arrows at the top will rotate the view 45 degrees in the indicated direction around a line pointing towards you.

The navigation cluster may be moved to any part of the 3D display by dragging. The drag (left) mouse button must be pressed inside the cube itself to initiate a drag. The structure will not begin moving until the pointer is dragged outside the cube.

There is a smaller mini-cube in the lower right of the cluster which activates a drop-down menu allowing you to switch the viewing mode.

### Selecting objects 

Objects in the 3D view can be selected by clicking them with the corresponding mouse button, depending on the navigation mode (described above). A single click will select the object and one of its subcomponents (edge, face, vertex). Double-clicking will select the object and all its subcomponents. You can select more than one subcomponent, or even different subcomponents from different objects, by pressing the CTRL key. Clicking with the selection button on an empty portion of the 3D view will deselect everything.

A panel called \"Selection view\", available from the View menu, can also be turned on, which shows you what is currently selected:

![](images/Selection_view.jpg )

You can also use the Selection View to select objects by searching for a particular object.

**Read more**

-   [The FreeCAD navigation modes](Mouse_navigation.md)
-   [Navigation Cluster](Navigation_Cube.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Manual:Navigating in the 3D view/en
