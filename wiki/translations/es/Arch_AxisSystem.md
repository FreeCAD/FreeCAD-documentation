---
- GuiCommand:/es
   Name:Arch AxisSystem
   Name/es:Arch AxisSystem
   MenuLocation:Arch → Axis System
   Workbenches:[Arch](Arch_Workbench/es.md)
   SeeAlso:[Arch Axis](Arch_Axis/es.md), [Grid](Arch_Grid/es.md)
---

# Arch AxisSystem/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

La herramienta Sistema de ejes le permite combinar 2 o 3 objetos [Arch Axis](Arch_Axis/es.md). La función principal de esta herramienta es calcular los puntos de intersección entre los diferentes ejes incluidos en este sistema. Los objetos de Arch pueden usar este sistema para duplicar su forma en los diferentes puntos de intersección.


</div>

This is useful to define the intersection points between the different axes. Arch objects can then use this system to duplicate their shape on the different intersection points.

<img alt="" src=images/Arch_AxisSystem_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

*La imagen de arriba muestra tres objetos [Arch Axis](Arch_Axis/es.md) combinados en un Sistema de Eje. A continuación, un objeto de columna utiliza este sistema como su propiedad **Eje**, para tener su forma duplicada en cada punto de intersección.*


</div>


<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

1.  Opcionalmente, seleccione los objetos [Arch Axis](Arch_Axis/es.md) que desea incluir en este sistema
2.  Presione el botón **<img src="images/_Arch_AxisSystem.png" width=16px> [Arch AxisSystem](Arch_AxisSystem/es.md)
**
3.  Haga clic con el botón derecho en el objeto del sistema de ejes recién creado en la vista de árbol para agregar / editar los objetos [Arch Axis](Arch_Axis.md) incluidos en este sistema
4.  Seleccione cualquier [Arch Axis](Arch_Axis/es.md) existente y presione los botones Agregar o Eliminar para agregarlo o eliminarlo de / a este sistema
5.  Establecer la propiedad **Eje** de cualquier objeto Arch para que apunte a este sistema, para que su forma se duplique en los puntos de intersección de este sistema


</div>

## Opciones

-   Un mismo objeto [Arch Axis](Arch_Axis/es.md) puede ser parte de más de un sistema
-   Cualquier objeto basado en una forma también se puede usar como la propiedad **Eje** de los objetos Arch. En este caso, la forma del objeto se duplicará a lo largo de los vértices del objeto ejes


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramienta del sistema ejes puede utilizarse en [macros](macros/es.md) y desde la consola de Python mediante la siguiente función:


</div>


```python
AxisSystem = makeAxisSystem(axes, name="Axis System")
```


<div class="mw-translate-fuzzy">

Hace un sistema de eje basado en la lista dada de [Arch Axis](Arch_Axis/es.md)


</div>

Ejemplo: 
```python
import Draft, Arch

Axes = Arch.makeAxis(5, 1000)

Axes.ViewObject.LineWidth = 3
Axes.ViewObject.BubbleSize = 200
Axes.ViewObject.FontSize = 150

Axes2 = Arch.makeAxis(6, 500)

Axes2.ViewObject.LineWidth = 2
Axes2.ViewObject.BubbleSize = 200
Axes2.ViewObject.FontSize = 150
Axes2.ViewObject.NumberingStyle = "A,B,C"
FreeCAD.ActiveDocument.recompute()

Axes2.Length = 6000
Draft.rotate(Axes2, -90)
Draft.move(Axes2, FreeCAD.Vector(-1000, 2500, 0))
FreeCAD.ActiveDocument.recompute()

AxisSystem = Arch.makeAxisSystem([Axes, Axes2])

Structure = Arch.makeStructure(length=200, width=200, height=100)
Draft.move(Structure, FreeCAD.Vector(-100, 0, 0))
Structure.Axis = AxisSystem
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


{{docnav|[Axis](Arch_Axis.md)|[Grid](Arch_Grid.md)|[Arch](Arch_Workbench/es.md)|IconL=Arch_Axis.svg |IconC=Workbench_Arch.svg |IconR=Arch_Grid.svg}}


</div>

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch AxisSystem/es
