
{{Page in progress}}







{{TOCright}}


<div class="mw-translate-fuzzy">

La pantalla de preferencias del módulo de Croquis se encuentra en la [Ventana de Preferencias](Preferences_Editor/es.md) (Menú Editar -\> Preferencias).


</div>


<div class="mw-translate-fuzzy">

Tiene una **Configuración general**, donde puedes especificar el color de los símbolos de [ajuste](Draft_Snap/es.md), el espesor de línea y color para los nuevos objetos. Activando la casilla de verificación \"Guardar el color actual y el espesor de línea a través de las sesiones de trabajo\", cualquier cambio que hagas en la **barra de comandos de Croquis** se salvará aquí, de modo que empieces tu siguiente sesión con FreeCAD con el color y espesor de línea que estabas utilizando cuando lo cerraste.


</div>


<div class="mw-translate-fuzzy">

![](images/Draft_Preferences.jpg )


</div>

General settings allows you to set certain basic properties like the default [working plane](Draft_SelectPlane.md), the name and color of the [construction group](Draft_ToggleConstructionMode.md), a prefix to use for the [Draft Clones](Draft_Clone.md), and the internal precision of the calculations.

![](images/Preference_Draft_Tab_01.png )

## Grid and snapping {#grid_and_snapping}

Grid and snapping allows you to set properties of the **<img src="images/Draft_ToggleGrid.svg" width=16px> [visible grid](Draft_ToggleGrid.md)**, which can be used with the [Draft Snap](Draft_Snap.md) methods.

By default the option \"Always snap (disable snap mod)\" is active, which means that you don\'t need to press a modifier key to activate the snapping tools. If this option is not active, you must press a modifier key to activate snapping.

You can set three modifiers:

-    **Shift**constraint modifier, to [constraint](Draft_Constrain.md) the movement of the cursor along the X, Y, or Z axis.

-    **Ctrl**snap modifier, to snap the cursor to specific modes given by [Draft Snap](Draft_Snap.md).

-    **Alt**alternative modifier, to activate an alternative function for a Draft tool.

You can specify the space between each grid line, between each major line, and the total number of lines displayed in the working plane.

![](images/Preference_Draft_Tab_02.png )

## Visual settings {#visual_settings}

Visual settings allows you to specify the default line color and width for new objects, and the color of the [Draft Snap](Draft_Snap.md) symbols. By clicking the \"Save current color and linewidth across sessions\" checkbox, changes made in the [Draft Tray](Draft_Tray.md) will be saved and restored the next time you open FreeCAD.

![](images/Preference_Draft_Tab_03.png )

## Texts and dimensions {#texts_and_dimensions}

Texts and dimensions allows you to set default properties for the [Draft Text](Draft_Text.md), [Draft Dimension](Draft_Dimension.md), and [Draft ShapeString](Draft_ShapeString.md) tools, including default font and size, and style and size of the dimension lines. These properties can be changed in the individual text objects as well.

![](images/Preference_Draft_Tab_04.png )





 

[Category:Preferences{{\#translation:}}](Category:Preferences.md)
