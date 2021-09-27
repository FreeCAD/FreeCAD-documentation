---
- GuiCommand:/es
   Name:Arch Rebar UShape
   Name/es: Arch Barra de Refuerzo en Forma de U
   MenuLocation:Arch → Rebar tools
   Workbenches:[Arch](Arch_Workbench/es.md)
   Shortcut:None
   SeeAlso:[LShape Rebar](Arch_Rebar_LShape/es.md)
   Addon:Reinforcement
---

# Arch Rebar Straight/es


</div>


<div class="mw-translate-fuzzy">

## Descripción

La herramienta {{KEY | <img src="images/_Arch_Rebar_Straight.png_" width= 16px> Straight Rebar}} permite al usuario crear una barra de refuerzo recta en el elemento estructural.


</div>

The [Arch Straight Rebar](Arch_Rebar_Straight.md) tool is also integrated into [BIM Workbench](BIM_Workbench.md).

This command is part of the _ via the **Tools → Addon manager → Reinforcement** menu.

<img alt="" src=images/Arch_Rebar_Straight_example.png  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/StraightRebar.png  style="width:800px;">


</div>

## Utilización


<div class="mw-translate-fuzzy">

1.  Crear un elemento [ structure](Arch_Structure.md)
2.  Seleccione cualquier cara de la estructura
3.  A continuación, seleccione {{KEY | <img src="images/_Arch_Rebar_Straight.png_" width= 16px> Straight Rebar}} de las herramientas de la barra de refuerzo
4.  Aparecerá un panel de tareas en el lado izquierdo de la pantalla como se muestra a continuación ![ 250px](images/_StraightRebarDialog.png )
5.  Seleccione la orientación deseada
6.  Proporcione las entradas como la cubierta frontal, la cubierta lateral derecha, la cubierta lateral izquierda, la cubierta inferior y el diámetro de la barra de refuerzo
7.  Seleccione el modo de distribución, ya sea cantidad o espaciado
8.  Si se selecciona el espaciado, un usuario también puede optar por [ espaciado personalizado](Custom_Spacing.md)
9.  Coger cara seleccionada es usado para verificar o cambiar la cara para la distribución de barras de refuerzo
10. Haga clic en {{KEY | OK}} o {{KEY | Apply}} para generar las barras de refuerzo
11. Haga clic en {{KEY | Cancel}} para salir del panel de tareas


</div>

<img alt="" src=images/StraightRebarDialog.png  style="width:250px;"> 
*Taskview panel for the Arch Rebar Straight tool*

## Propiedades

-    {{PropertyData/es | Orientation}}: Decide la orientación de la barra de refuerzo (como una parte inferior, superior, derecha e izquierda).

-    {{PropertyData/es | Front Cover}}: la distancia entre la barra de refuerzo y la cara seleccionada.

-    {{PropertyData/es | Right Cover}}: la distancia entre el extremo derecho de la barra de refuerzo a la derecha de la estructura.

-    {{PropertyData/es | Left Cover}}: la distancia entre el extremo izquierdo de la barra de refuerzo a la cara izquierda de la estructura.

-    {{PropertyData/es | Cover along}}: estas propiedades le permiten al usuario especificar la tapa superior o inferior.

-    {{PropertyData/es | Bottom Cover}}: la distancia entre las barras de refuerzo desde la cara inferior de la estructura.

-    {{PropertyData/es | Top Cover}}: la distancia entre barras de refuerzo desde la cara superior de la estructura.

-    {{PropertyData/es | Amount}}: la cantidad de barras de refuerzo.

-    {{PropertyData/es | Spacing}}: la distancia entre los ejes de cada barra.


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramienta {{KEY | <img src="images/_Arch_Rebar_Straight.png_" width= 16px> Straight Rebar}} puede usarse en [macros/es](macros/es.md) y desde la consola de python utilizando la siguiente función:


</div>


```python
Rebar = makeStraightRebar(f_cover, coverAlong, rt_cover, lb_cover,
                          diameter, amount_spacing_check, amount_spacing_value, orientation="Horizontal",
                          structure=None, facename=None)
```

-   Creates a `Rebar` object from the given `structure`, which is an [Arch Structure](Arch_Structure.md), and `facename`, which is a face of that structure.
    -   If no `structure` nor `facename` are given, it will take the user selected face as input.

-    `f_cover`, `coverAlong`, `rt_cover`, and `lb_cover` are inner offset distances for the rebar elements with respect to the faces of the structure.

    -   
        `f_cover`
        
        is the frontal cover offset.

    -   
        `coverAlong`
        
        is a tuple `(position, value)` that defines the offset value in one position (top, bottom, left, right) depending on the `orientation`.

    -   
        `rt_cover`
        
        is either the right or the top cover offset, depending on the value of `coverAlong` and `orientation`.

    -   
        `lb_cover`
        
        is either the left or the bottom cover offset, depending on the value of `coverAlong` and `orientation`.

-    `diameter`is the diameter of the reinforcement bars inside the structure.

-    `amount_spacing_check`if it is `True` it will create as many reinforcement bars as given by `amount_spacing_value`; if it is `False` it will create reinforcement bars separated by the numerical value of `amount_spacing_value`.

-    `amount_spacing_value`specifies the number of reinforcement bars, or the value of the separation between them, depending on `amount_spacing_check`.

-    `orientation`specifies the orientation of the rebar; it can be `"Horizontal"` or `"Vertical"`.

Depending on the orientation of the rebar, the function can be called in two general ways by setting `coverAlong` appropriately.

### The rebar is horizontal 


```python
Rebar = makeStraightRebar(f_cover, ("Top Side", value), right_cover, left_cover, ...)
Rebar = makeStraightRebar(f_cover, ("Bottom Side", value), right_cover, left_cover, ...)
```

-    `coverAlong`is a tuple with either a `"Top Side"` or a `"Bottom Side"` offset `value`.

-   In this case `rt_cover` refers to the `right_cover` offset, and `lb_cover` refers to the `left_cover` offset.

### The rebar is vertical 


```python
Rebar = makeStraightRebar(f_cover, ("Left Side", value), top_cover, bottom_cover, ...)
Rebar = makeStraightRebar(f_cover, ("Right Side", value), top_cover, bottom_cover, ...)
```

-    `coverAlong`is a tuple with either a `"Left Side"` or a `"Right Side"` offset `value`.

-   In this case `rt_cover` refers to the `top_cover` offset, and `lb_cover` refers to the `bottom_cover` offset.

### Example horizontal 


```python
import Arch, Draft, StraightRebar

Structure = Arch.makeStructure(length=1000, width=1000, height=400)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = StraightRebar.makeStraightRebar(50, ("Bottom Side", 20), 100, 100,
                                        12, True, 5, "Horizontal", Structure, "Face4")
Rebar.ViewObject.ShapeColor = (0.9, 0.0, 0.0)

Rebar2 = StraightRebar.makeStraightRebar(50, ("Bottom Side", 50), 100, 100,
                                         12, True, 5, "Horizontal", Structure, "Face6")
Rebar2.ViewObject.ShapeColor = (0.0, 0.0, 0.9)
```

### Example vertical 


```python
import Arch, Draft, StraightRebar

Structure2 = Arch.makeStructure(length=1000, width=1000, height=400)
Structure2.ViewObject.Transparency = 80
Draft.move(Structure2, FreeCAD.Vector(1500, 0, 0))
FreeCAD.ActiveDocument.recompute()

Rebar3 = StraightRebar.makeStraightRebar(50, ("Left Side", 20), 100, 100,
                                         12, True, 5, "Vertical", Structure2, "Face4")
Rebar3.ViewObject.ShapeColor = (0.9, 0.5, 0.0)

Rebar4 = StraightRebar.makeStraightRebar(50, ("Left Side", 50), 100, 100,
                                         12, True, 5, "Vertical", Structure2, "Face6")
Rebar4.ViewObject.ShapeColor = (0.0, 0.5, 0.5)
```


<div class="mw-translate-fuzzy">

Cambiando las propiedades de la barra de refuerzo recta.


</div>


```python
editStraightRebar(Rebar, f_cover, coverAlong, rt_cover, lb_cover,
                  diameter, amount_spacing_check, amount_spacing_value, orientation,
                  structure=None, facename=None)
```

-    `Rebar`is a previously created `StraightRebar` object.

-   The other parameters are the same as required by the `makeStraightRebar()` function.

-    `structure`and `facename` may be omitted so that the rebar stays in the original structure.

Example: 
```python
import StraightRebar

StraightRebar.editStraightRebar(Rebar, 50, ("Top Side", 20), 100, 100,
                                24, True, 7, "Horizontal")

StraightRebar.editStraightRebar(Rebar2, 50, ("Top Side", 50), 100, 100,
                                24, True, 7, "Horizontal")

StraightRebar.editStraightRebar(Rebar3, 50, ("Right Side", 20), 100, 100,
                                24, True, 7, "Vertical")

StraightRebar.editStraightRebar(Rebar4, 50, ("Right Side", 50), 100, 100,
                                24, True, 7, "Vertical")
```


<div class="mw-translate-fuzzy">


{{docnav/es|[Arch CompRebarStraight](Arch_CompRebarStraight/es.md)|[UShape Rebar](Arch_Rebar_UShape/es.md)|[Arch](Arch_Workbench/es.md)|IconL=Arch_CompRebarStraight.png|IconC=Workbench_Arch.svg|IconR=Arch_Rebar_UShape.png}}


</div>


 

_

---
[documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar Straight/es
