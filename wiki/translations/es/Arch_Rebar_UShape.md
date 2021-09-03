---
- GuiCommand:Addon/es   Name:Arch Rebar UShape   Name/es: Arch Barra de Refuerzo en Forma de U   Workbenches:[Addon:Reinforcement   MenuLocation:Arch → Rebar tools   Shortcut:None   SeeAlso:[[Arch_Rebar_LShape/es|LShape Rebar](Arch_Module/es___Arch]].md)---


</div>

## Descripción


<div class="mw-translate-fuzzy">

La herramienta {{KEY | <img src="images/_UShapeRebar.png_" width= 16px> UShape Rebar}} permite al usuario crear una barra de refuerzo de forma de U en el elemento estructural.


</div>

The **<img src="images/Arch_Rebar_UShape.svg" width=16px> [UShape Rebar](Arch_Rebar_UShape.md)** tool is also integrated into [BIM Workbench](BIM_Workbench.md).

This command is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Addon_Manager.md) via the **Tools → Addon manager → Reinforcement** menu.

<img alt="" src=images/Arch_Rebar_UShape_example.png  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Footing_UShapeRebar.png  style="width:800px;">


</div>

## Utilización


<div class="mw-translate-fuzzy">

1.  Crear un elemento [ structure](Arch_Structure.md)
2.  Seleccione cualquier cara de la estructura
3.  A continuación, seleccione {{KEY | <img src="images/_UShapeRebar.png_" width= 16px> UShape Rebar}} desde las herramientas de la barra de refuerzo
4.  Aparecerá un panel de tareas en el lado izquierdo de la pantalla como se muestra a continuación ![ 250px](images/_UShapeDialog.png )
5.  Seleccione la orientación deseada
6.  Proporcione las entradas como la cubierta frontal, la cubierta lateral derecha, la cubierta lateral izquierda, la cubierta inferior, la cubierta superior, el factor de redondeo y el diámetro de la barra de refuerzo
7.  Seleccione el modo de distribución, ya sea cantidad o espaciado
8.  Si se selecciona el espaciado, un usuario también puede optar por [ espaciado personalizado](Custom_Spacing.md)
9.  La selección de la cara seleccionada se usa para verificar o cambiar la cara de la distribución de barras de refuerzo
10. Haga clic en {{KEY | OK}} o {{KEY | Apply}} para generar las barras de refuerzo
11. Haga clic en {{KEY | Cancel}} para salir del panel de tareas


</div>


:   <img alt="" src=images/UShapeDialog.png  style="width:250px;">


*Taskview panel for the Arch Rebar UShape tool*

## Propiedades

-    {{PropertyData/es | Orientation}}: Decide la orientación de la barra de refuerzo (como una parte inferior, superior, derecha e izquierda).

-    {{PropertyData/es | Front Cover}}: la distancia entre la barra de refuerzo y la cara seleccionada.

-    {{PropertyData/es | Right Cover}}: la distancia entre el extremo derecho de la barra de refuerzo a la derecha de la estructura.

-    {{PropertyData/es | Left Cover}}: la distancia entre el extremo izquierdo de la barra de refuerzo a la cara izquierda de la estructura.

-    {{PropertyData/es | Bottom Cover}}: la distancia entre las barras de refuerzo desde la cara inferior de la estructura.

-    {{PropertyData/es | Top Cover}}: la distancia entre barras de refuerzo desde la cara superior de la estructura.

-    {{PropertyData/es | Rounding}}: Un valor de redondeo que se aplicará a las esquinas de las barras, expresado en veces el diámetro.

-    {{PropertyData/es | Amount}}: la cantidad de barras de refuerzo.

-    {{PropertyData/es | Spacing}}: la distancia entre los ejes de cada barra.


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramienta **<img src="images/_UShapeRebar.png" width=16px> UShape Rebar** puede utilizarse en [macros](macros/es.md) y desde la consola de python utilizando la siguiente función:


</div>


```python
Rebar = makeUShapeRebar(f_cover, b_cover, r_cover, l_cover,
                        diameter, t_cover, rounding, amount_spacing_check, amount_spacing_value, orientation="Bottom",
                        structure=None, facename=None)
```


<div class="mw-translate-fuzzy">

-   La barra de refuerzo de forma de U tiene cuatro orientaciones diferentes:
    -   Fondo
    -   Parte superior
    -   Correcto
    -   Izquierda
-   Agrega un objeto de barra de refuerzo de forma de US al objeto estructural dado.
-   Si no se proporciona Estructura y Facename, tomará la cara seleccionada por el usuario como entrada.
-   Devuelve el nuevo objeto Rebar.


</div>


<div class="mw-translate-fuzzy">

Ejemplo: Creando la barra de refuerzo de forma de U.


</div>


```python
import FreeCAD, Arch, UShapeRebar

Structure = Arch.makeStructure(length=1000, width=1000, height=400)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = UShapeRebar.makeUShapeRebar(50, 20, 20, 20,
                                    8, 50, 4, True, 6, "Bottom", Structure, "Face4")
Rebar.ViewObject.ShapeColor = (0.9, 0.0, 0.0)

Rebar2 = UShapeRebar.makeUShapeRebar(50, 50, 20, 20,
                                     8, 50, 4, True, 6, "Bottom", Structure, "Face6")
Rebar2.ViewObject.ShapeColor = (0.0, 0.0, 0.9)
```


<div class="mw-translate-fuzzy">

Cambio de propiedades de la barra de refuerzo de forma de U.


</div>


```python
editUShapeRebar(Rebar, f_cover, b_cover, r_cover, l_cover,
                diameter, t_cover, rounding, amount_spacing_check, amount_spacing_value, orientation,
                structure=None, facename=None) 
```

-    `Rebar`is a previously created `UShapeRebar` object.

-   The other parameters are the same as required by the `makeUShapeRebar()` function.

-    `structure`and `facename` may be omitted so that the rebar stays in the original structure.


```python
import UShapeRebar

UShapeRebar.editUShapeRebar(Rebar, 50, 50, 20, 20,
                            16, 20, 5, True, 5, "Top")

UShapeRebar.editUShapeRebar(Rebar2, 70, 50, 20, 20,
                            16, 70, 5, True, 5, "Top")
```


<div class="mw-translate-fuzzy">


</div>


 

[Category:Arch/es](Category:Arch/es.md) [Category:Reinforcement{{\#translation:}}](Category:Reinforcement.md)
