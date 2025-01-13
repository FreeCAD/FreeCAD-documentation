# Manual:Navigating in the 3D view/es
{{Manual:TOC}}



### Una palabra sobre el espacio 3D 


<div class="mw-translate-fuzzy">

Si este es su primer contacto con una aplicación 3D, tendrá que familiarizarse primero con algunos conceptos. Si no es así, puedes saltarte esta sección sin problemas.


</div>


<div class="mw-translate-fuzzy">

El espacio 3D de FreeCAD es un [Espacio euclídeo](https://es.wikipedia.org/wiki/Espacio_eucl%C3%ADdeo). Tiene un punto de origen y tres ejes: X, Y y Z. Si miras tu escena desde arriba, convencionalmente, el eje X apunta hacia la derecha, el eje Y hacia atrás, y el eje Z hacia arriba. En la esquina inferior derecha de la vista de FreeCAD, siempre puedes ver desde dónde estás viendo la escena:


</div>


<div class="mw-translate-fuzzy">

El punto de encuentro de los tres ejes es el origen. Es el punto donde el valor de todas las coordenadas es cero. Para cualquier eje, el movimiento en una dirección aumentará el valor de la coordenada y el movimiento en la dirección opuesta disminuirá el valor de la coordenada. Cada punto de cada objeto que existe en el espacio 3D puede ser localizado por sus coordenadas (x,y,z). Por ejemplo, un punto con coordenadas (2,3,1) estará a +2 unidades en el eje X, +3 unidades en el eje Y y +1 unidad en el eje Z:


</div>

![](images/3dspace_coordinates.jpg )



### La vista 3D de FreeCAD 




<div class="mw-translate-fuzzy">

#### Navegación del ratón 


</div>


<div class="mw-translate-fuzzy">

La navegación en la [vista 3D](3D_view/es.md) de FreeCAD puede hacerse con un ratón, un dispositivo de navegación espacial, el teclado, un panel táctil, o una combinación de ellos. FreeCAD implementa varios [modos de navegación](Mouse_navigation/es.md), que determinan cómo se realizan las tres operaciones básicas de manipulación de la vista (panorámica, rotativo, zoom), así como cómo se realiza la selección de objetos en la pantalla. A los modos de navegación se accede desde la pantalla de Preferencias, o directamente haciendo clic con el botón derecho del ratón en cualquier parte de la [vista 3D](3D_view/es.md):


</div>

![](images/FreeCAD_022_NavigationMethod.png )


<div class="mw-translate-fuzzy">

Cada uno de estos modos asigna diferentes botones del ratón, o combinaciones de ratón y teclado, o gestos del ratón, a estas cuatro operaciones. La siguiente tabla muestra los principales modos disponibles:


</div>

++++++
| Style             | Select                                                                                                  | Zoom                                                                                                                                                                                                                                                                                                     | Rotate                                                                                                                                                                                                                                                                                                                                                | Pan                                                                                                                                                                                                                            |
+===================+=========================================================================================================+==========================================================================================================================================================================================================================================================================================================+=======================================================================================================================================================================================================================================================================================================================================================+================================================================================================================================================================================================================================+
| Blender           | <img alt="Click left mouse button" src=images/Mouse_LMB.svg  style="width:64px;">                         | <img alt="Roll middle mouse button" src=images/Mouse_MMB_rotate.svg  style="width:64px;">                                                                                                                                                                                                                 | <img alt="Hold middle mouse button" src=images/Mouse_MMB_hold.svg  style="width:64px;">                                                                                                                                                                                                                                                                | <img alt="Hold left + right mouse button" src=images/Mouse_LMB+RMB_hold.svg  style="width:64px;"> or **Shift** + <img alt="Hold middle mouse button" src=images/Mouse_MMB_hold.svg  style="width:64px;"> |
++++++
| CAD **(default)** | <img alt="Click left mouse button" src=images/Mouse_LMB.svg  style="width:64px;">                         | <img alt="Roll middle mouse button" src=images/Mouse_MMB_rotate.svg  style="width:64px;"> or **Ctrl** + **Shift** + <img alt="Click right mouse button" src=images/Mouse_RMB.svg  style="width:64px;">                                                                 | <img alt="Hold middle then left mouse button" src=images/Mouse_MMB+LMB_hold.svg  style="width:64px;"> or <img alt="Hold middle then right mouse button" src=images/Mouse_MMB+RMB_hold.svg  style="width:64px;"> or **Shift** + <img alt="Click right mouse button" src=images/Mouse_RMB.svg  style="width:64px;"> | <img alt="Hold middle mouse button" src=images/Mouse_MMB_hold.svg  style="width:64px;"> or **Ctrl** + <img alt="Click right mouse button" src=images/Mouse_RMB.svg  style="width:64px;">                       |
++++++
| Gesture           | <img alt="Click left mouse button" src=images/Mouse_LMB.svg  style="width:64px;">                         | <img alt="Roll middle mouse button" src=images/Mouse_MMB_rotate.svg  style="width:64px;">                                                                                                                                                                                                                 | <img alt="Hold left mouse button" src=images/Mouse_LMB_hold.svg  style="width:64px;">                                                                                                                                                                                                                                                                    | <img alt="Hold right mouse button" src=images/Mouse_RMB_hold.svg  style="width:64px;">                                                                                                                                           |
++++++
| MayaGesture       | <img alt="Click left mouse button" src=images/Mouse_LMB.svg  style="width:64px;">                         | <img alt="Roll middle mouse button" src=images/Mouse_MMB_rotate.svg  style="width:64px;"> or **Alt** + <img alt="Hold right mouse button" src=images/Mouse_RMB_hold.svg  style="width:64px;">                                                                                             |                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                 |
|                   |                                                                                                         |                                                                                                                                                                                                                                                                                                          | **Alt**                                                                                                                                                                                                                                                                                                                                           | **Alt**                                                                                                                                                                                                                    |
|                   |                                                                                                         |                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                             |
|                   |                                                                                                         |                                                                                                                                                                                                                                                                                                          | \+ <img alt="Hold left mouse button" src=images/Mouse_LMB_hold.svg  style="width:64px;">                                                                                                                                                                                                                                                                 | \+ <img alt="Hold middle mouse button" src=images/Mouse_MMB_hold.svg  style="width:64px;">                                                                                                                                      |
++++++
| OpenCascade       | <img alt="Click left mouse button" src=images/Mouse_LMB.svg  style="width:64px;">                         | <img alt="Roll middle mouse button" src=images/Mouse_MMB_rotate.svg  style="width:64px;"> or **Ctr** + <img alt="Hold left mouse button" src=images/Mouse_LMB_hold.svg  style="width:64px;">                                                                                               | <img alt="Hold middle then right mouse button" src=images/Mouse_MMB+RMB_hold.svg  style="width:64px;"> or **Ctr** + <img alt="Hold right mouse button" src=images/Mouse_RMB_hold.svg  style="width:64px;">                                                                                                                  | <img alt="Hold middle mouse button" src=images/Mouse_MMB_hold.svg  style="width:64px;"> or **Ctr** + <img alt="Hold middle mouse button" src=images/Mouse_MMB_hold.svg  style="width:64px;">                   |
++++++
| OpenInventor      |                                                                                          | <img alt="Roll middle mouse button" src=images/Mouse_MMB_rotate.svg  style="width:64px;"> or <img alt="Hold middle then left mouse button" src=images/Mouse_MMB+LMB_hold.svg  style="width:64px;">                                                                                               | <img alt="Hold left mouse button" src=images/Mouse_LMB_hold.svg  style="width:64px;">                                                                                                                                                                                                                                                                    | <img alt="Hold middle mouse button" src=images/Mouse_MMB_hold.svg  style="width:64px;">                                                                                                                                         |
|                   | **Shift**                                                                                           |                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                |
|                   |                                                                                                      |                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                |
|                   | \+ <img alt="Click left mouse button" src=images/Mouse_LMB.svg  style="width:64px;">                      |                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                |
++++++
| OpenSCAD          | <img alt="Click left mouse button" src=images/Mouse_LMB.svg  style="width:64px;">                         | <img alt="Roll middle mouse button" src=images/Mouse_MMB_rotate.svg  style="width:64px;"> or <img alt="Hold middle mouse button" src=images/Mouse_MMB_hold.svg  style="width:64px;"> or **Shift** + <img alt="Hold right mouse button" src=images/Mouse_RMB_hold.svg  style="width:64px;"> | <img alt="Hold left mouse button" src=images/Mouse_LMB_hold.svg  style="width:64px;"> or <img alt="Hold middle then right mouse button" src=images/Mouse_MMB+RMB_hold.svg  style="width:64px;">                                                                                                                                                | <img alt="Hold right mouse button" src=images/Mouse_RMB_hold.svg  style="width:64px;">                                                                                                                                           |
++++++
| Revit             | <img alt="Click left mouse button" src=images/Mouse_LMB.svg  style="width:64px;">                         | <img alt="Roll middle mouse button" src=images/Mouse_MMB_rotate.svg  style="width:64px;">                                                                                                                                                                                                                 | <img alt="Hold middle then right mouse button" src=images/Mouse_MMB+RMB_hold.svg  style="width:64px;"> or **Shift** + <img alt="Hold middle mouse button" src=images/Mouse_MMB_hold.svg  style="width:64px;">                                                                                                              | <img alt="Hold middle mouse button" src=images/Mouse_MMB_hold.svg  style="width:64px;"> or <img alt="Hold left and right mouse button" src=images/Mouse_LMB+RMB_hold.svg  style="width:64px;">                           |
++++++
| TinkerCAD         | <img alt="Click left mouse button" src=images/Mouse_LMB.svg  style="width:64px;">                         | <img alt="Roll middle mouse button" src=images/Mouse_MMB_rotate.svg  style="width:64px;">                                                                                                                                                                                                                 | <img alt="Hold right mouse button" src=images/Mouse_RMB_hold.svg  style="width:64px;">                                                                                                                                                                                                                                                                  | <img alt="Hold middle mouse button" src=images/Mouse_MMB_hold.svg  style="width:64px;">                                                                                                                                         |
++++++
| Touchpad          | <img alt="Click touchpad (mouse) left button" src=images/Touchpad_LB.svg  style="width:64px;"> |                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                 |
|                   |                                                                                                         | **Ctrl**                                                                                                                                                                                                                                                                                             | **Alt**                                                                                                                                                                                                                                                                                                                                           | **Shift**                                                                                                                                                                                                                  |
|                   |                                                                                                         |                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                             |
|                   |                                                                                                         | \+ **Shift** + <img alt="Touchpad (mouse) pointer" src=images/Touchpad.svg  style="width:64px;">                                                                                                                                                                                        | \+ <img alt="Touchpad (mouse) pointer" src=images/Touchpad.svg  style="width:64px;"> or **Shift** + <img alt="Hold touchpad (mouse) left button" src=images/Touchpad_LB_hold.svg  style="width:64px;">                                                                                                                       | \+ <img alt="Touchpad (mouse) pointer" src=images/Touchpad.svg  style="width:64px;">                                                                                                                                            |
++++++

It\'s worth noting that when a user hovers over the navigation styles menu located at the bottom right of the screen, a tooltip will appear. This tooltip provides a brief description of the highlighted navigation style, offering immediate guidance on its use.

![](images/FreeCAD_022_NavigationHover.png )




<div class="mw-translate-fuzzy">

#### Navegación del teclado 


</div>

Alternatively, some keyboard controls are always available, no matter the navigation style:

-    **Ctrl**\+ {{ASCII|43}} and **Ctrl** + {{ASCII|22}} or **PgUp** and **PgDn** to zoom in and out, respectively.

-   The arrow keys, {{ASCII|17}}{{ASCII|16}}{{ASCII|30}}{{ASCII|31}}, to pan the view left/right and up/down.

-    **Shift**\+ {{ASCII|17}} and **Shift** + {{ASCII|16}} to rotate the view by 90 degrees.

-   The numeric keys, {{ASCII|48}}{{ASCII|49}}{{ASCII|50}}{{ASCII|51}}{{ASCII|52}}{{ASCII|53}}{{ASCII|54}}, for the seven standard views: <img alt="" src=images/Std_ViewIsometric.svg  style="width:24px;"> [Isometric](Std_ViewIsometric.md), <img alt="" src=images/Std_ViewFront.svg  style="width:24px;"> [Front](Std_ViewFront.md), <img alt="" src=images/Std_ViewTop.svg  style="width:24px;"> [Top](Std_ViewTop.md), <img alt="" src=images/Std_ViewRight.svg  style="width:24px;"> [Right](Std_ViewRight.md), <img alt="" src=images/Std_ViewRear.svg  style="width:24px;"> [Rear](Std_ViewRear.md), <img alt="" src=images/Std_ViewBottom.svg  style="width:24px;"> [Bottom](Std_ViewBottom.md), and <img alt="" src=images/Std_ViewLeft.svg  style="width:24px;"> [Left](Std_ViewLeft.md)

-    **V**
    **O**will set the camera in <img alt="" src=images/View-isometric.svg  style="width:24px;"> [Orthographic view](Std_OrthographicCamera.md).

-   While **V****P** sets it in <img alt="" src=images/View-perspective.svg  style="width:24px;"> [Perspective view](Std_PerspectiveCamera.md).

-    **Ctrl**will allow you to select more than one object or element

These controls are also available from the [View menu](Std_View_Menu.md) and some from the View toolbar.

#### Using the Navigation Cube 

In the default setup, there is a [Navigation Cube](Navigation_Cube.md) in the upper right corner of the 3D view. This may be used to change the view.

![](images/FreeCAD_022_Cube.png )

Clicking on a face of the cube will switch the view to that face. Clicking one of the four triangular arrows rotates the view 45 degrees in the indicated direction. Clicking one of the two curved arrows rotates the view 45 degrees in the indicated direction around a line pointing towards you. Clicking the round button in the top right corner of the cube rotates the view 180 degrees around the vertical axis of the view.

There is a smaller mini-cube in the lower right of the Navigation Cube which activates a drop-down menu with several options, including an option to make the cube movable, which allows to temporarily move the cube to a different position by dragging.



### Seleccionar objetos 

Objects in the 3D view can be selected by clicking them with the corresponding mouse button, depending on the navigation style (described above).

-   A single click will select the object and one of its subelements (edge, face, vertex).
-   Double-clicking will select the object and all its subelements.
-   You can select more than one object and more than one subelement, from the same or different objects, by pressing the **CTRL** key.
-   Clicking with the selection button on an empty portion of the 3D view will deselect everything.

A panel called \"Selection view\", available from the View menu, can also be turned on, which shows you what is currently selected:

![](images/Selection_view.jpg )

You can also use the Selection View to select objects by searching for a particular object.

**Leer más**

-   [The FreeCAD navigation styles](Mouse_navigation.md)
-   [Navigation Cube](Navigation_Cube.md)



---
⏵ [documentation index](../README.md) > Manual:Navigating in the 3D view/es
