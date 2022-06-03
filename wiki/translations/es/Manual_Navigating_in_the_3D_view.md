# Manual:Navigating in the 3D view/es
{{Manual   *TOC/es}}

### Una palabra sobre el espacio 3D 

Si este es su primer contacto con una aplicación 3D, tendrá que familiarizarse primero con algunos conceptos. Si no es así, puedes saltarte esta sección sin problemas.

El espacio 3D de FreeCAD es un [Espacio euclídeo](https   *//es.wikipedia.org/wiki/Espacio_eucl%C3%ADdeo). Tiene un punto de origen y tres ejes   * X, Y y Z. Si miras tu escena desde arriba, convencionalmente, el eje X apunta hacia la derecha, el eje Y hacia atrás, y el eje Z hacia arriba. En la esquina inferior derecha de la vista de FreeCAD, siempre puedes ver desde dónde estás viendo la escena   *

![](images/Axes_orientation.png )

El punto de encuentro de los tres ejes es el origen. Es el punto donde el valor de todas las coordenadas es cero. Para cualquier eje, el movimiento en una dirección aumentará el valor de la coordenada y el movimiento en la dirección opuesta disminuirá el valor de la coordenada. Cada punto de cada objeto que existe en el espacio 3D puede ser localizado por sus coordenadas (x,y,z). Por ejemplo, un punto con coordenadas (2,3,1) estará a +2 unidades en el eje X, +3 unidades en el eje Y y +1 unidad en el eje Z   *

![](images/3dspace_coordinates.jpg )

Puedes mirar esa escena desde cualquier ángulo, como si estuvieras sosteniendo una cámara. Esa cámara puede moverse a la izquierda, a la derecha, hacia arriba y hacia abajo (panorámica), girar alrededor de lo que está apuntando (rotación) y acercarse o alejarse de la escena (zoom).

### La vista 3D de FreeCAD 

#### Navegación del ratón 

La navegación en la [vista 3D](3D_view/es.md) de FreeCAD puede hacerse con un ratón, un dispositivo de navegación espacial, el teclado, un panel táctil, o una combinación de ellos. FreeCAD implementa varios [modos de navegación](Mouse_navigation/es.md), que determinan cómo se realizan las tres operaciones básicas de manipulación de la vista (panorámica, rotativo, zoom), así como cómo se realiza la selección de objetos en la pantalla. A los modos de navegación se accede desde la pantalla de Preferencias, o directamente haciendo clic con el botón derecho del ratón en cualquier parte de la [vista 3D](3D_view/es.md)   *

![](images/FreeCAD-v0-18-NavigationModePopup.png )

Cada uno de estos modos asigna diferentes botones del ratón, o combinaciones de ratón y teclado, o gestos del ratón, a estas cuatro operaciones. La siguiente tabla muestra los principales modos disponibles   *

++++++
| Mode              | Pan                                                                                                                                                                                                                                         | Rotate                                                                                                                                                                                                         | Zoom                                                                                                                                                                                                      | Select                                                                                                            |
+===================+=============================================================================================================================================================================================================================================+================================================================================================================================================================================================================+===========================================================================================================================================================================================================+===================================================================================================================+
| OpenInventor      | ![Click middle button mouse](images/Pan-mouse.svg )                                                                                                                                                                     | ![Click left button mouse](images/Select-mouse.svg )                                                                                                                                         | ![Roll middle button mouse](images/Zoom-mouse.svg )                                                                                                                                    | Hold **Ctrl** + drag ![Click left button mouse](images/Select-mouse.svg ) |
++++++
| CAD **(default)** | ![Click middle button mouse](images/Pan-mouse.svg ) or ![Click right button mouse + CTRL key](images/Pan-mouse-CTRL.svg )                                                         | ![Hold middle then left mouse button](images/Rotate-mouse.svg ) or ![Click right button mouse + SHIFT key](images/Rotate-mouse-SHIFT.svg ) | ![Roll middle button mouse](images/Zoom-mouse.svg ) or ![Click right button mouse + CTRL + SHIFT key](images/Zoom-mouse-CTRL-SHIFT.svg ) | ![Click left button mouse](images/Select-mouse.svg )                                            |
++++++
| Blender           | Hold **Shift** + drag ![Click middle button mouse](images/Pan-mouse.svg ) or drag ![Click left + right button mouse and drag](images/Mouse_LMB%2BRMB.svg ) | ![Click middle button mouse](images/Pan-mouse.svg )                                                                                                                                        | ![Roll middle button mouse](images/Zoom-mouse.svg )                                                                                                                                    | ![Click left button mouse](images/Select-mouse.svg )                                            |
++++++
| Touchpad          | Hold **Shift** + drag ![Touchpad (mouse) pointer](images/Touchpad.png )                                                                                                                            |                                                                                                                                                                                                 |                                                                                                                                                                                            | ![Click touchpad (mouse) left button](images/Select-touchpad.png )                   |
|                   |                                                                                                                                                                                                                                             | **Alt**                                                                                                                                                                                                    | **PgUp**                                                                                                                                                                                              |                                                                                                                   |
|                   |                                                                                                                                                                                                                                             |                                                                                                                                                                                                             |                                                                                                                                                                                                        |                                                                                                                   |
|                   |                                                                                                                                                                                                                                             | \+ ![Touchpad (mouse) pointer](images/Touchpad.png )                                                                                                                                    | / **PgDn**                                                                                                                                                                              |                                                                                                                   |
++++++
| Gesture           | drag ![Click right button mouse](images/Pan-mouse-Ctrl.svg )                                                                                                                                                         | drag ![Click left button mouse](images/Select-mouse.svg )                                                                                                                                | ![Roll middle button mouse](images/Zoom-mouse.svg )                                                                                                                                    | ![Click left button mouse](images/Select-mouse.svg )                                            |
++++++
| OpenCascade       | ![Click middle button mouse](images/Pan-mouse.svg )                                                                                                                                                                     | ![Hold middle then right mouse button](images/Rotate-mouse-MMB+RMB.svg )                                                                                                         | ![Roll middle button mouse](images/Zoom-mouse.svg )                                                                                                                                    | ![Click left button mouse](images/Select-mouse.svg )                                            |
++++++

#### Navegación del teclado 

Alternatively, some keyboard controls are always available, no matter the navigation mode   *

-    **Ctrl**\+ {{ASCII|43}} and **Ctrl** + {{ASCII|22}} to zoom in and out, respectively.

-   The arrow keys, {{ASCII|17}}{{ASCII|16}}{{ASCII|30}}{{ASCII|31}}, to shift the view left/right and up/down

-    **Shift**\+ {{ASCII|17}} and **Shift** + {{ASCII|16}} to rotate the view by 90 degrees

-   The numeric keys, {{ASCII|48}}{{ASCII|49}}{{ASCII|50}}{{ASCII|51}}{{ASCII|52}}{{ASCII|53}}{{ASCII|54}}, for the seven standard views   * <img alt="" src=images/Std_ViewIsometric.svg  style="width   *24px;"> [Isometric](Std_ViewIsometric.md), <img alt="" src=images/Std_ViewFront.svg  style="width   *24px;"> [Front](Std_ViewFront.md), <img alt="" src=images/Std_ViewTop.svg  style="width   *24px;"> [Top](Std_ViewTop.md), <img alt="" src=images/Std_ViewRight.svg  style="width   *24px;"> [Right](Std_ViewRight.md), <img alt="" src=images/Std_ViewRear.svg  style="width   *24px;"> [Rear](Std_ViewRear.md), <img alt="" src=images/Std_ViewBottom.svg  style="width   *24px;"> [Bottom](Std_ViewBottom.md), and <img alt="" src=images/Std_ViewLeft.svg  style="width   *24px;"> [Left](Std_ViewLeft.md)

-    **V**
    **O**will set the camera in <img alt="" src=images/View-isometric.svg  style="width   *24px;"> [Orthographic view](Std_OrthographicCamera.md).

-   While **V****P** sets it in <img alt="" src=images/View-perspective.svg  style="width   *24px;"> [Perspective view](Std_PerspectiveCamera.md).

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

### Seleccionar objetos 

Objects in the 3D view can be selected by clicking them with the corresponding mouse button, depending on the navigation mode (described above). A single click will select the object and one of its subcomponents (edge, face, vertex). Double-clicking will select the object and all its subcomponents. You can select more than one subcomponent, or even different subcomponents from different objects, by pressing the CTRL key. Clicking with the selection button on an empty portion of the 3D view will deselect everything.

A panel called \"Selection view\", available from the View menu, can also be turned on, which shows you what is currently selected   *

![](images/Selection_view.jpg )

You can also use the Selection View to select objects by searching for a particular object.

**Leer más**

-   [The FreeCAD navigation modes](Mouse_navigation.md)
-   [Navigation Cluster](Navigation_Cube.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Manual:Navigating in the 3D view/es
