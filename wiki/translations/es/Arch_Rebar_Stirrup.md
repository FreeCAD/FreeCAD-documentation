---
 GuiCommand:
   Name: Arch Rebar Stirrup
   MenuLocation: Arch , Rebar tools
   Workbenches: Arch Workbench/es, BIM Workbench/es
   SeeAlso: Arch_Rebar_Helical/es, Arch Rebar/es
   Version: 0.17
---

# Arch Rebar Stirrup/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

La herramienta {{KEY | <img src="images/_Arch_Rebar_Stirrup.png_" width= 16px> Stirrup Rebar}} permite al usuario crear una barra de refuerzo de estribo en el elemento estructural.


</div>

The [Stirrup Rebar](Arch_Rebar_Stirrup.md) tool is also integrated into [BIM Workbench](BIM_Workbench.md).

This command is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) via the **Tools → Addon manager → Reinforcement** menu.

<img alt="" src=images/Arch_Rebar_Stirrup_example.png  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Stirrup.png  style="width:800px;">


</div>




<div class="mw-translate-fuzzy">

## Como utilizar 


</div>


<div class="mw-translate-fuzzy">

1.  Crear un elemento [structure](Arch_Structure/es.md)
2.  Seleccione cualquier cara de la estructura
3.  A continuación, seleccione **<img src="images/Arch_Rebar_Stirrup.png" width=16px> Stirrup Rebar** desde las herramientas de la barra de refuerzo
4.  Aparecerá un panel de tareas en el lado izquierdo de la pantalla, como se muestra a continuación <img alt="" src=images/StirrupDialog.png  style="width:250px;">
5.  Seleccione la orientación deseada
6.  Proporcione las entradas como cubierta izquierda, cubierta derecha, cubierta superior, parte inferior, cubierta frontal, ángulo doblado, factor doblado, redondeo y diámetro de la barra de refuerzo
7.  Seleccione el modo de distribución, ya sea cantidad o espaciado
8.  Si se selecciona el espaciado, un usuario también puede optar por [espaciado personalizado](Custom_Spacing/es.md)
9.  La selección de la cara seleccionada se usa para verificar o cambiar la cara de la distribución de barras de refuerzo
10. Haga clic en **OK** o **Apply** para generar las barras de refuerzo
11. Haga clic en **Cancel** para salir del panel de tareas


</div>

<img alt="" src=images/StirrupDialog.png  style="width:250px;"> 
*Taskview panel for the Arch Rebar Stirrup tool*



## Propiedades

-    {{PropertyData/es|Front Cover}}: la distancia entre la barra de refuerzo y la cara seleccionada.

-    {{PropertyData/es|Right Cover}}: la distancia entre el extremo derecho de la barra de refuerzo a la derecha de la estructura.

-    {{PropertyData/es|Left Cover}}: la distancia entre el extremo izquierdo de la barra de refuerzo a la cara izquierda de la estructura.

-    {{PropertyData/es|Bottom Cover}}: la distancia entre las barras de refuerzo desde la cara inferior de la estructura.

-    {{PropertyData/es|Top Cover}}: la distancia entre barras de refuerzo desde la cara superior de la estructura.

-    {{PropertyData/es|Bent Angle}}: ángulo doblado define el ángulo en los extremos de un estribo.

-    {{PropertyData/es|Bent Factor}}: Bent Factor define la longitud del extremo del estribo.

-    {{PropertyData/es|Amount}}: la cantidad de barras de refuerzo.

-    {{PropertyData/es|Spacing}}: la distancia entre los ejes de cada barra.




<div class="mw-translate-fuzzy">

## Programación


</div>


**See also:**

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

La herramienta **<img src="images/_Arch_Rebar_Stirrup.png" width=16px> Stirrup Rebar** puede utilizarse en [macros](macros/es.md) y desde la consola de python utilizando la siguiente función:


</div>


```python
Rebar = makeStirrup(l_cover, r_cover, t_cover, b_cover, f_cover,
                    bentAngle, bentFactor, diameter, rounding, amount_spacing_check, amount_spacing_value,
                    structure=None, facename=None)
```


<div class="mw-translate-fuzzy">

-   Agrega un objeto de barra de refuerzo Estribo al objeto estructural dado.
-   Si no se proporciona Estructura y nombre de cara, tomará la cara seleccionada por el usuario como entrada.
-   Aquí el argumento de CoverAlong es tener tipo tupla.
-   Devuelve el nuevo objeto de refuerzo.


</div>




<div class="mw-translate-fuzzy">

Ejemplo: Creando la barra de refuerzo de estribo.


</div>


```python
import Draft, Arch, Stirrup

# It doesn't work if the structure is not based on a face
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = Stirrup.makeStirrup(20, 20, 20, 20, 20,
                            115, 4, 8, 2, True, 10, Structure, "Face6")
```


<div class="mw-translate-fuzzy">

Cambiando las propiedades de la barra de refuerzo de estribo.


</div>


```python
editStirrup(Rebar, l_cover, r_cover, t_cover, b_cover, f_cover,
            bentAngle, bentFactor, diameter, rounding, amount_spacing_check, amount_spacing_value,
            structure=None, facename=None)
```

-    `Rebar`is a previously created `StirrupRebar` object.

-   The other parameters are the same as required by the `makeStirrup()` function.

-    `structure`and `facename` may be omitted so that the rebar stays in the original structure.


```python
import Stirrup

Stirrup.editStirrup(Rebar, 20, 20, 20, 20, 50,
                    100, 4, 14, 8, True, 8)
```


<div class="mw-translate-fuzzy">


{{docnav/es
|[Bent Shape Rebar](Arch_Rebar_BentShape/es.md)
|[Helical Rebar](Arch_Rebar_Helical/es.md)
|[Arch](Arch_Workbench/es.md)
|IconL=Arch_Rebar_BentShape.svg
|IconC=Workbench_Arch.svg
|IconR=Arch_Rebar_Helical.svg
}}


</div>



---
⏵ [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar Stirrup/es
