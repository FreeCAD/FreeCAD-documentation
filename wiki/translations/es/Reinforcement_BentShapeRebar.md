---
 GuiCommand:Addon/es
   Name: Arch Rebar BentShape
   Name/es:  Arch Barra de refuerzo doblada
   MenuLocation: Arch , Rebar tools
   Workbenches: Arch_Workbench/es
   SeeAlso: Arch_Rebar_Stirrup/es, Arch Rebar/es
   Version: 0.17
   Addon: Reinforcement
---

# Reinforcement BentShapeRebar/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

La herramienta {{KEY | <img src="images/_Arch_Rebar_BentShape.png_" width= 16px> Bent Shape Rebar}} permite al usuario crear una barra de refuerzo de forma doblada en el elemento estructural.


</div>

This tool is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md).

<img alt="" src=images/Arch_Rebar_BentShape_example.png  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/BentShapeRebar.png  style="width:800px;">


</div>



## Como utilizar 


<div class="mw-translate-fuzzy">

1.  Crear un elemento [ structure](Arch_Structure.md)
2.  Seleccione cualquier cara de la estructura
3.  Luego seleccione {{KEY | <img src="images/_Arch_Rebar_BentShape.png_" width= 16px> Bent Shape Rebar}} desde las herramientas de la barra de refuerzo
4.  Aparecerá un panel de tareas en el lado izquierdo de la pantalla como se muestra a continuación ![ 250px](images/_BentShapeDialog.png )
5.  Seleccione la orientación deseada
6.  Proporcione las entradas como cubierta frontal, cubierta izquierda, cubierta derecha, cubierta inferior, cubierta superior, longitud de anclaje, ángulo doblado, redondeado y diámetro de la barra de refuerzo
7.  Seleccione el modo de distribución, ya sea cantidad o espaciado
8.  Si se selecciona el espaciado, un usuario también puede optar por [ espaciado personalizado](Custom_Spacing.md)
9.  La selección de la cara seleccionada se usa para verificar o cambiar la cara de la distribución de barras de refuerzo
10. Haga clic en {{KEY | OK}} o {{KEY | Apply}} para generar las barras de refuerzo
11. Haga clic en {{KEY | Cancel}} para salir del panel de tareas


</div>

<img alt="" src=images/BentShapeDialog.png  style="width:250px;"> 
*Task panel for the tool*



## Propiedades

-    {{PropertyData/es | Orientation}}: Decide la orientación de la barra de refuerzo (como una parte inferior, superior, derecha e izquierda).

-    {{PropertyData/es | Front Cover}}: la distancia entre la barra de refuerzo y la cara seleccionada.

-    {{PropertyData/es | Left Cover}}: la distancia entre el extremo izquierdo de la barra de refuerzo a la cara izquierda de la estructura.

-    {{PropertyData/es | Right Cover}}: la distancia entre el extremo derecho de la barra de refuerzo a la derecha de la estructura.

-    {{PropertyData/es | Bottom Cover}}: la distancia entre las barras de refuerzo desde la cara inferior de la estructura.

-    {{PropertyData/es | Top Cover}}: la distancia entre barras de refuerzo desde la cara superior de la estructura.

-    {{PropertyData/es | Anchor Length}}: es la longitud del brazo de la barra de refuerzo de forma doblada.

-    {{PropertyData/es | Bent Angle}}: Decide el ángulo en la barra de herramientas de forma doblada.

-    {{PropertyData/es | Amount}}: la cantidad de barras de refuerzo.

-    {{PropertyData/es | Spacing}}: la distancia entre los ejes de cada barra.




<div class="mw-translate-fuzzy">

## Programación


</div>


**See also:**

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

La herramienta **<img src="images/_Arch_Rebar_BentShape.png" width=16px> Bent Shape Rebar** puede usarse en [macros](macros/es.md) y desde la consola de python mediante la siguiente función:


</div>


```python
Rebar = makeBentShapeRebar(f_cover, b_cover, l_cover, r_cover,
                           diameter, t_cover, bentLength, bentAngle, rounding, amount_spacing_check, amount_spacing_value, orientation="Bottom",
                           structure=None, facename=None)
```


<div class="mw-translate-fuzzy">

-   La barra de refuerzo doblada tiene cuatro orientaciones diferentes:
    -   Fondo
    -   Superior
    -   Izquierda
    -   Derecha
-   Agrega un objeto de barra de refuerzo doblada al objeto estructural dado.
-   Si no se proporciona Estructura y nombre de cara, tomará la cara seleccionada por el usuario como entrada.
-   Aquí el argumento de CoverAlong es tener tipo tupla.
-   Devuelve el nuevo objeto de refuerzo.


</div>

### Example


```python
import FreeCAD, Arch, BentShapeRebar

Structure = Arch.makeStructure(length=1000, width=1000, height=100)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = BentShapeRebar.makeBentShapeRebar(50, 20, 20, 20,
                                          8, 40, 100, 135, 2, True, 4, "Bottom", Structure, "Face4")
Rebar.ViewObject.ShapeColor = (0.9, 0.0, 0.0)

Rebar2 = BentShapeRebar.makeBentShapeRebar(50, 40, 20, 20,
                                           8, 20, 100, 135, 2, True, 4, "Bottom", Structure, "Face6")
Rebar2.ViewObject.ShapeColor = (0.0, 0.0, 0.9) 
```

### Edition of the rebar 

You can change the properties of the rebar with the following function:


```python
editBentShapeRebar(Rebar, f_cover, b_cover, l_cover, r_cover,
                   diameter, t_cover, bentLength, bentAngle, rounding, amount_spacing_check, amount_spacing_value, orientation,
                   structure=None, facename=None)
```

-    `Rebar`is a previously created `BentShapeRebar` object.

-   The other parameters are the same as required by the `makeBentShapeRebar()` function.

-    `structure`and `facename` may be omitted so that the rebar stays in the original structure.


```python
import BentShapeRebar

BentShapeRebar.editBentShapeRebar(Rebar, 50, 20, 20, 20,
                                  12, 20, 100, 155, 2, True, 6, "Top")

BentShapeRebar.editBentShapeRebar(Rebar2, 50, 35, 20, 20,
                                  12, 35, 100, 155, 2, True, 6, "Top")
```


<div class="mw-translate-fuzzy">


{{docnav/es|[LShape Rebar](Arch_Rebar_LShape.md)|[Stirrup Rebar](Arch_Rebar_Stirrup.md)|[Arch](Arch_Workbench/es.md)|IconL=Arch_Rebar_LShape.svg |IconC=Workbench_Arch.svg |IconR=Arch_Rebar_Stirrup.svg}}


</div>



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > [BIM](Category_BIM.md) > Reinforcement BentShapeRebar/es
