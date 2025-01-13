# Navigation Cube/es
## Introducción

El **Cubo de navegación** brinda información visual sobre la orientación de la cámara en la [vista 3D](3D_view/es.md) actual y se puede usar para cambiarla. De forma predeterminada, es visible y reside en la esquina superior derecha de la vista.

![](images/Navigation_Cube_Example.png )

El Cubo de Navegación consta de varias partes:

-   El [cubo principal](#Main_cube.md)
-   Seis [flechas direccionales](#Directional_arrows.md)
-   El [botón de vista inversa](#Reverse_view_button.md) (arriba a la derecha) <small>(v0.20)</small> 
-   El [menú mini-cubo](#Mini-cube_menu.md) (abajo a la derecha)
-   Indicadores de los ejes X, Y y Z.

Se puede hacer clic en todas las partes, excepto en los indicadores de eje.



## Uso



### Cubo principal 

El cubo principal tiene 26 caras: 6 caras principales, 12 caras de borde rectangulares (<small>(v0.20)</small> ) y 8 caras de esquina. Al hacer clic en cualquiera de ellos, se reorienta la cámara para que su dirección sea perpendicular a la cara seleccionada.



### Flechas Direccionales 

There are six directional arrows: four triangular arrowheads and two curved arrows. Clicking one of the triangular arrows rotates the [3D view](3D_view.md) around a line perpendicular to the direction of the arrow. Clicking a curved arrow rotates the [3D view](3D_view.md) around the view direction.

### Reverse view button 

Clicking the round button in the top right corner of the Navigation Cube rotates the [3D view](3D_view.md) 180 degrees around the vertical axis of the view.

### Mini-cube menu 

Clicking the small cube in the bottom right corner of the Navigation Cube brings up a menu with the following options:

-    **<img src="images/Std_OrthographicCamera.svg" width=16px> [Orthographic view](Std_OrthographicCamera.md)**: switches to an orthographic view.

-    **<img src="images/Std_PerspectiveCamera.svg" width=16px> [Perspective view](Std_PerspectiveCamera.md)**: switches to a perspective view.

-    **<img src="images/Std_ViewIsometric.svg" width=16px> [Isometric](Std_ViewIsometric.md)**: switches to an isometric view.

-    **<img src="images/Std_ViewFitAll.svg" width=16px> [Fit all](Std_ViewFitAll.md)**: zooms and pans the camera so that all visible objects fit inside the view.

-    **<img src="images/Std_ViewFitSelection.svg" width=16px> [Fit selection](Std_ViewFitSelection.md)**: zooms and pans the camera so that all selected objects fit inside the view. <small>(v1.0)</small> 

-    **<img src="images/Std_AlignToSelection.svg" width=16px> [Align to selection](Std_AlignToSelection.md)**: points the camera in the view in the opposite direction of the normal of a planar face, or the opposite direction of a straight edge. <small>(v1.0)</small> 

-    **Movable navigation cube**: if this checkbox (<small>(v0.21)</small> ) is checked the entire Navigation Cube can be moved by holding down the left mouse button anywhere on the main cube and dragging. This is intended to temporarily move the cube out of the way. The [advanced parameters](#Advanced_parameters.md) OffsetX and OffsetY can be used to permanently reposition the cube, see below.



## Personalización



### Preferencias

The Navigation Cube is controlled by several preferences: **Edit → Preferences... → Display → Navigation → Navigation cube**. See [Preferences Editor](Preferences_Editor#Navigation.md).



### Parámetros avanzados 

Some advanced Navigation Cube parameters cannot be changed in the [Preferences Editor](Preferences_Editor#Navigation.md). These parameters can be set manually in the [Parameter editor](Std_DlgParameter.md).

To manually set colors:

1.  Start the <img alt="" src=images/Std_DlgParameter.svg  style="width:16px;"> [Parameter editor](Std_DlgParameter.md).
2.  In the panel on the left browse to **BaseApp → Preferences → NaviCube**.
3.  Right-click the panel on the right and select **New unsigned item** from the context menu.
4.  Enter the name of one of these colors:
    -   
        **BaseColor**
        
        : the base color of all elements, the default is {{Value|3806916544}} (hex: {{Value|e2e8efc0}}). This color can be also set in the [Preferences Editor](Preferences_Editor#Navigation.md). <small>(v0.21)</small> 

    -   
        **EmphaseColor**
        
        : the color of the texts and lines, the default depends on the **BaseColor**. It is either black: {{Value|255}} (hex: {{Value|000000ff}}), or white: {{Value|4294967295}} (hex: {{Value|ffffffff}}). <small>(v0.21)</small> 

    -   
        **HiliteColor**
        
        : the color used to highlight the faces and buttons, the default is {{Value|2867003391}} (hex: {{Value|aae2ffff}}).
5.  The color value must be entered as a 32-bit unsigned integer. Translated to the hexadecimal format this integer has the form {{Value|RRGGBBAA}}. Where {{Value|AA}} stands for the alpha channel (a measure for the transparency), and the other three digit pairs stand for red, green and blue. To convert a hexadecimal value to an unsigned integer you can use the [Python console](Python_console.md), enter for example {{Incode|int("323232ff", 16)}}.
6.  Optionally set more parameters.
7.  Press the **Close** button.

The table below lists the other advanced Navigation Cube parameters that can be set in a similar manner. Use the information from the **Type** column to create a correct new item in step 3.

+++++
| Name        | Description                                                                                                                   | Type    | Default |
+=============+===============================================================================================================================+=========+=========+
| BorderWidth | The width of the edges of the cube and the borders around the buttons in pixels.                                              | Float   | 1.1     |
+++++
| ChamferSize | The size of the edges and corners as a factor of the cube size. Values should be in the 0.05 - 0.18 range.                    | Float   | 0.12    |
|             |                                                                                                                               |         |         |
|             |                                                                                                                |         |         |
|             | <small>(v0.21)</small>                                                                                                               |         |         |
|             |                                                                                                                            |         |         |
+++++
| FontStretch | The font width as a percentage of the default width. Use 0 or 100 for the default font width.                                 | Integer | 0       |
+++++
| FontWeight  | The font weight. Higher values make the font more bold. The effect may depend on the font. Use 0 for the default font weight. | Integer | 0       |
+++++
| FontZoom    | The size of the labels:                                                                                                       | Float   | 0.3     |
|             |                                                                                                                               |         |         |
|             | -                                                                                                              |         |         |
|             |     {{Value|FontZoom &#61; 1.0}}                                                                                              |         |         |
|             |                                                                                                                            |         |         |
|             |     : Make the labels as big as possible individually.                                                                        |         |         |
|             |                                                                                                                               |         |         |
|             | -                                                                                                              |         |         |
|             |     {{Value|0.0 < FontZoom < 1.0}}                                                                                            |         |         |
|             |                                                                                                                            |         |         |
|             |     : Idem but limit the maximum font size.                                                                                   |         |         |
|             |                                                                                                                               |         |         |
|             | -                                                                                                              |         |         |
|             |     {{Value|FontZoom &#61; 0.0}}                                                                                              |         |         |
|             |                                                                                                                            |         |         |
|             |     : Idem but use the same font size for all.                                                                                |         |         |
|             |                                                                                                                               |         |         |
|             | -                                                                                                              |         |         |
|             |     {{Value|FontZoom < 0.0}}                                                                                                  |         |         |
|             |                                                                                                                            |         |         |
|             |     : Use the same font size for all, but scaled down.                                                                        |         |         |
|             |                                                                                                                               |         |         |
|             |                                                                                                                |         |         |
|             | <small>(v0.21)</small>                                                                                                               |         |         |
|             |                                                                                                                            |         |         |
+++++
| OffsetX     | The offset of the cube in the X direction relative to its corner position in pixels.                                          | Integer | 0       |
+++++
| OffsetY     | The offset of the cube in the Y direction relative to its corner position in pixels.                                          | Integer | 0       |
+++++
| ShowCS      | Toggles the display of the coordinate system (the X, Y and Z axis indicators).                                                | Boolean | true    |
+++++
| TextBottom  | The text on the bottom face of the cube. The default value should be translated.                                              | String  | BOTTOM  |
+++++
| TextFront   | The text on the front face of the cube. Idem.                                                                                 | String  | FRONT   |
+++++
| TextLeft    | The text on the left face of the cube. Idem.                                                                                  | String  | LEFT    |
+++++
| TextRear    | The text on the rear face of the cube. Idem.                                                                                  | String  | REAR    |
+++++
| TextRight   | The text on the right face of the cube. Idem.                                                                                 | String  | RIGHT   |
+++++
| TextTop     | The text on the top face of the cube. Idem                                                                                    | String  | TOP     |
+++++



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Navigation Cube/es
