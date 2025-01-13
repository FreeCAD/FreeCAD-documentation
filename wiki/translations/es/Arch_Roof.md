---
 GuiCommand:
   Name: Arch Roof
   Name/es: Arch Techo
   MenuLocation: Arquitectura , Techo
   Workbenches: Arch_Workbench/es
   Shortcut: **R** **F**
---

# Arch Roof/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

La herramienta Techo le permite crear un techo inclinado a partir de un wire seleccionado. El objeto del techo creado es paramétrico, manteniendo su relación con el objeto base. Tenga en cuenta que esta herramienta todavía está en desarrollo y puede fallar con formas muy complejas. El principio es que cada borde se ve asignando un perfil de techo (pendiente, ancho, saliente, espesor\...).


</div>

**Note:** This tool is still in development, and might fail with very complex shapes.

<img alt="" src=images/RoofExample.png  style="width:600px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/RoofExample.png  style="width:600px;">


</div>




<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

1.  Crea un wire siguiendo la dirección en sentido contrario a las agujas del reloj y selecciónalo.
2.  \* ![ 600px](images/_CounterclockwiseWire.png )
3.  Presiona el botón **<img src="images/_Arch_Roof.png" width=16px> [Arch Roof](Arch_Roof/es.md)
**, o presiona **R** luego las teclas **F**
4.  El objeto de techo predeterminado podría tener una forma extraña, es porque la herramienta no tiene toda la información necesaria.
5.  Después de crear el techo predeterminado, haga doble clic en el objeto en la vista de árbol para acceder y editar todas las propiedades. El ángulo debe estar entre 0 y 90.
6.  \* ![](images/_RoofTable.png )
7.  Cada línea corresponde a un panel de techo. Entonces puede establecer las propiedades que desea para cada panel de techo.
8.  Para ayudarlo, puede establecer Ángulo o Run en 0 y definir un Id relativo, esto hace cálculos automáticos para encontrar los datos relativos al Id relativo.
9.  Funciona así:
    1.  Si Angle = 0 y Run = 0, el perfil es idéntico al perfil relativo.
    2.  Si Angle = 0, el ángulo se calcula de modo que la altura sea la misma que el perfil relativo.
    3.  Si Run = 0, Run se calcula para que la altura sea la misma que el perfil relativo.
10. Al final, establece un ángulo de 90 ° para hacer un frontón.
11. \* ![ 600px](images/_RoofProfil.png )
12. **También puedes consultar este video**: <https://www.youtube.com/watch?v=4Urwru71dVk>


</div>

## Usage (solid base) 

If your roof has a complex shape (e.g. contains pitched windows or other non-standard features) you can create a custom solid object using various other FreeCAD workbenches ([Part](Part_Workbench.md), [Sketcher](Sketcher_Workbench.md) etc.). And then use this solid as the **Base** object of your roof:

1.  Select the solid base object.
2.  Press the **<img src="images/Arch_Roof.svg" width=16px> [Arch Roof](Arch_Roof.md)** button, or press **R** then **F** keys.

## Subtracting a roof 

Roofs have an automatically generated subtraction volume (<small>(v1.0)</small>  for roofs with a solid base). When a roof is [removed](Arch_Remove.md) from the walls of a building, both the roof itself as well as everything above it is subtracted from the walls.


<small>(v1.0)</small> 

: It is possible to override the automatic subtraction volume by setting the **Subvolume** property of the roof to a custom solid object.

<img alt="" src=images/Arch_Roof_Subtract_Default.png  style="width:" height="150px;"> <img alt="" src=images/Arch_Roof_Subtract_Subvolume.png  style="width:" height="150px;"> <img alt="" src=images/Arch_Roof_Subvolume_Example.png  style="width:" height="150px;"> 
*Solid-based roof before (1st image) and after (2nd image) [removing](Arch_Remove.md) it from walls.<br>
The 3rd image shows the generated subtraction volume.*



## Opciones


<div class="mw-translate-fuzzy">

-   Los techos comparten las propiedades y comportamientos comunes de todos los [Arch Components](Arch_Component/es.md)


</div>



## Propiedades

### Data


{{TitleProperty|Roof}}


<div class="mw-translate-fuzzy">

-    {{PropertyData/es|Angles}}: Lista del ángulo de inclinación del panel de techo (un ángulo para cada borde en el wire).

-    {{PropertyData/es|Runs}}: Lista del ancho del panel del techo (una ejecución para cada borde en el wire).

-    {{PropertyData/es|IdRel}}: Lista de la relación Id El ángulo de inclinación del techo

-    {{PropertyData/es|Thickness}}: Lista de espesores del panel de techo. (un espesor para cada borde en el wire).

-    {{PropertyData/es|Overhang}}: Lista del saliente del panel del techo (un saliente para cada borde en el wire).

-    {{PropertyData/es|Face}}: El índice de la cara del objeto base que se utilizará #No realmente utilizado


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramientas techo se puede utilizar en [macros](macros/es.md) y desde la consola de Python utilizando las siguientes funciones:


</div>


```python
Roof = makeRoof(baseobj=None, facenr=0, angles=[45.,], run=[], idrel=[0,], thickness=[50.,], overhang=[100.,], name="Roof")
```


<div class="mw-translate-fuzzy">


:   Hace un techo basado en un wire cerrado. Puede proporcionar una lista de ángulos, ejecutar, idrel, espesor, voladizo para cada borde en el wire para definir la forma del techo. El valor predeterminado para el ángulo es 45 y la lista se completa automáticamente para que coincida con el número de bordes en el wire.


</div>

Ejemplo:


```python
import FreeCAD as App
import Arch, Draft

doc = App.newDocument()

rect = Draft.makeRectangle(3000, 4000)
doc.recompute()

roof = Arch.makeRoof(rect, angles=[30.,])

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(0, 2000, 0)

wire = Draft.make_wire([p1, p2, p3], closed=True)
doc.recompute()

roof1 = Arch.makeRoof(wire)

doc.recompute()
```


<div class="mw-translate-fuzzy">


</div>


{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Roof/es
