---
 GuiCommand:Addon/es
   Name: Arch Rebar Helical
   Name/es: Arch Rebar Helical
   MenuLocation: Arch , Rebar tools
   Workbenches: Arch_Workbench/es
   Addon: Reinforcement
   Shortcut: None
   SeeAlso: Arch_Rebar/es
---

# Reinforcement HelicalRebar/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

La herramienta {{KEY | <img src="images/_Arch_Rebar_Helical.png_" width= 16px> Helical Rebar}} permite al usuario crear una barra de refuerzo helicoidal en el elemento estructural.


</div>

This tool is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md).

:   <img alt="" src=images/Arch_Rebar_Helical_example.png  style="width:80px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/HelicalRebar.png  style="width:800px;">


</div>




<div class="mw-translate-fuzzy">

## Como utilizar 


</div>


<div class="mw-translate-fuzzy">

1.  Crear un elemento [structure](Arch_Structure/es.md)
2.  Seleccione cualquier cara de la estructura
3.  A continuación, seleccione **<img src="images/_Arch_Rebar_Helical.png" width=16px> Helical Rebar** desde las herramientas de la barra de refuerzo
4.  Aparecerá un panel de tareas en el lado izquierdo de la pantalla como se muestra a continuación <img alt="" src=images/_HelicalRebarDialog.png  style="width:250px;">
5.  Seleccione la orientación deseada
6.  Proporcione las entradas como la cubierta frontal, la cubierta lateral derecha, la cubierta lateral izquierda, la cubierta inferior y el diámetro de la barra de refuerzo
7.  Seleccione el modo de distribución, ya sea cantidad o espaciado
8.  Si se selecciona el espaciado, un usuario también puede optar por [espaciado personalizado](Custom_Spacing/es.md)
9.  La selección de la cara seleccionada se usa para verificar o cambiar la cara de la distribución de barras de refuerzo
10. Haga clic en **OK** o **Apply** para generar las barras de refuerzo
11. Haga clic en **Cancel** para salir del panel de tareas


</div>

<img alt="" src=images/HelicalRebarDialog.png  style="width:250px;"> 
*Task panel for the tool*



## Propiedades

-    {{PropertyData/es|Side Cover}}: la distancia entre las barras de refuerzo a la cara curva.

-    {{PropertyData/es|Top Cover}}: la distancia entre barras de refuerzo desde la cara superior de la estructura.

-    {{PropertyData/es|Bottom Cover}}: la distancia entre las barras de refuerzo desde la cara inferior de la estructura.

-    {{PropertyData/es|Pitch}}: el pitch de una hélice es la altura de un giro completo de hélice, medido en paralelo al eje de la hélice.

-    {{PropertyData/es|Diameter}}: Diámetro de la barra de refuerzo.




<div class="mw-translate-fuzzy">

## Programación


</div>


**See also:**

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

La herramienta **<img src="images/_Arch_Rebar_Helical.png" width=16px> Helical Rebar** puede utilizarse en [macros](macros/es.md) y desde la consola de python utilizando la siguiente función:


</div>


```python
Rebar = makeHelicalRebar(s_cover, b_cover, diameter, t_cover, pitch, structure=None, facename=None)
```


<div class="mw-translate-fuzzy">

-   Agrega un objeto de barra de refuerzo recto al objeto estructural dado.
-   Si no se proporciona Estructura y nombre de cara, tomará la cara seleccionada por el usuario como entrada.
-   Aquí el argumento de CoverAlong es del tipo tupla.
-   Devuelve el nuevo objeto de refuerzo.


</div>

### Example


```python
import FreeCAD, Draft, Arch, HelicalRebar

Circle = Draft.makeCircle(radius=250)
Structure = Arch.makeStructure(Circle)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = HelicalRebar.makeHelicalRebar(10, 50, 8, 50, 50, structure, "Face2")
```

### Edition of the rebar 

You can change the properties of the rebar with the following function


```python
editHelicalRebar(Rebar, s_cover, b_cover, diameter, t_cover, pitch, structure=None, facename=None)
```

-    `Rebar`is a previously created `HelicalRebar` object.

-   The other parameters are the same as required by the `makeHelicalRebar()` function.

-    `structure`and `facename` may be omitted so that the rebar stays in the original structure.


```python
import HelicalRebar

HelicalRebar.editHelicalRebar(Rebar, 20, 100, 20, 20, 100)
```


<div class="mw-translate-fuzzy">


</div>



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > [BIM](Category_BIM.md) > Reinforcement HelicalRebar/es
