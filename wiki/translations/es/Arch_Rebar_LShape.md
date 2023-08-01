---
- GuiCommand:Addon/es
   Name:Arch Rebar LShape   Name/es:Arch Barra de Refuerzo en forma de L
   MenuLocation:Arch - Rebar tools
   Workbenches:[Arch](Arch_Workbench/es.md), [BIM](BIM_Workbench/es.md)
   Shortcut:None
   SeeAlso:[Barra de refuerzo doblada](Arch_Rebar_BentShape/es.md), [[Arch Rebar/es]]
   Version:0.17
   Addon:Reinforcement
---

# Arch Rebar LShape/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

La herramienta {{KEY | <img src="images/_Arch_Rebar_LShape.png_" width= 16px> L'Shaped Rebar}} permite al usuario crear la barra de refuerzo en forma de L en el elemento estructural.


</div>

The [LShape Rebar](Arch_Rebar_LShape.md) tool is also integrated into [BIM Workbench](BIM_Workbench.md).

This command is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) via the **Tools → Addon manager → Reinforcement** menu.

<img alt="" src=images/Arch_Rebar_LShape_example.png  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/LShapeRebarNew.png  style="width:800px;">


</div>



## Como utilizar 


<div class="mw-translate-fuzzy">

1.  Crear un elemento [ structure](Arch_Structure.md)
2.  Seleccione cualquier cara de la estructura
3.  A continuación, seleccione {{KEY | <img src="images/_Arch_Rebar_LShape.png_" width= 16px> LShape Rebar}} desde las herramientas de la barra de refuerzo
4.  Aparecerá un panel de tareas en el lado izquierdo de la pantalla como se muestra a continuación ![ 250px](images/_LShapeDialog.png )
5.  Seleccione la orientación deseada
6.  Proporcione las entradas como la cubierta frontal, la cubierta lateral izquierda, la cubierta lateral derecha, la cubierta inferior, la cubierta superior, el redondeo y el diámetro de la barra de refuerzo
7.  Seleccione el modo de distribución, ya sea cantidad o espaciado
8.  Si se selecciona el espaciado, un usuario también puede optar por [ espaciado personalizado](Custom_Spacing.md)
9.  La selección de la cara seleccionada se usa para verificar o cambiar la cara de la distribución de barras de refuerzo
10. Haga clic en {{KEY | OK}} o {{KEY | Apply}} para generar las barras de refuerzo
11. Haga clic en {{KEY | Cancel}} para salir del panel de tareas


</div>


:   <img alt="" src=images/LShapeDialog.png  style="width:250px;">



*Taskview panel for the Arch Rebar LShape tool*



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


**See also:**

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

La herramienta {{KEY | <img src="images/_Arch_Rebar_LShape.png_" width= 16px> L'Shaped Rebar}} puede utilizarse en [macros/es](macros/es.md) y desde la consola de python mediante la siguiente función:


</div>


```python
Rebar = makeLShapeRebar(f_cover, b_cover, l_cover, r_cover,
                        diameter, t_cover, rounding, amount_spacing_check, amount_spacing_value, orientation="Bottom Left",
                        structure=None, facename=None):
```


<div class="mw-translate-fuzzy">

-   La barra de refuerzo LShape tiene cuatro orientaciones diferentes:
    -   Abajo a la derecha
    -   Abajo a la izquierda
    -   Parte superior derecha
    -   Arriba a la izquierda
-   Agrega un objeto de barra de refuerzo LShape al objeto estructural dado.
-   Si no se proporciona Estructura y Facename, tomará la cara seleccionada por el usuario como entrada.
-   Aquí el argumento de CoverAlong es tener tipo tupla.
-   Devuelve el nuevo objeto Rebar.


</div>

### Example


```python
import FreeCAD, Arch, LShapeRebar

Structure = Arch.makeStructure(length=1000, width=1000, height=400)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = LShapeRebar.makeLShapeRebar(50, 20, 20, 20,
                                    8, 50, 4, True, 6, "Bottom Left", Structure, "Face4")
Rebar.ViewObject.ShapeColor = (0.9, 0.0, 0.0)

Rebar2 = LShapeRebar.makeLShapeRebar(50, 50, 20, 20,
                                     8, 50, 4, True, 6, "Bottom Left", Structure, "Face6")
Rebar2.ViewObject.ShapeColor = (0.0, 0.0, 0.9) 
```

### Edition of the rebar 

You can change the properties of the rebar with the following function 
```python
editLShapeRebar(Rebar, f_cover, b_cover, l_cover, r_cover,
                diameter, t_cover, rounding, amount_spacing_check, amount_spacing_value, orientation,
                structure=None, facename=None)
```

-    `Rebar`is a previously created `LShapeRebar` object.

-   The other parameters are the same as required by the `makeLShapeRebar()` function.

-    `structure`and `facename` may be omitted so that the rebar stays in the original structure.


```python
import LShapeRebar

LShapeRebar.editLShapeRebar(Rebar, 50, 50, 20, 20,
                            12, 50, 6, True, 5, "Top Right")

LShapeRebar.editLShapeRebar(Rebar2, 50, 50, 20, 20,
                            12, 70, 6, True, 5, "Top Right")
```


<div class="mw-translate-fuzzy">


{{docnav/es
|[UShape Rebar](Arch_Rebar_UShape/es.md)
|[Bent Shape Rebar](Arch_Rebar_BentShape/es.md)
|[Arch](Arch_Workbench/es.md)
|IconL=Arch_Rebar_UShape.svg
|IconC=Workbench_Arch.svg
|IconR=Arch_Rebar_BentShape.svg
}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar LShape/es
