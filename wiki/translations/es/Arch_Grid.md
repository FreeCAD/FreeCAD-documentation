---
- GuiCommand:/es
   Name:Arch Grid
   Name/es:Arch Grid
   MenuLocation:Arch → Axis tools → Grid
   Workbenches:[Arch](Arch_Workbench/es.md)
   SeeAlso:[[Arch Axis/es]], [[Arch AxisSystem/es]]
---

# Arch Grid/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

La herramienta Grid/Grilla le permite colocar un objeto similar a una cuadrícula en el documento. Este objeto sirve como base para construir objetos Arch que necesitan un marco regular pero complejo, como ventanas, muros cortina, rejillas de columnas, barandas, etc. El objeto Grilla se puede editar como una hoja de cálculo, donde puede agregar o eliminar columnas y filas, definir su tamaño y combinar celdas.


</div>


<div class="mw-translate-fuzzy">

La grilla es un objeto 2D y, por lo tanto, puede utilizarse en cualquier lugar donde se necesite una forma 2D como [Draft](Draft_Workbench/es.md) o [Sketch](Sketcher_Workbench/es.md), pero también puede comportarse como un [Arch AxisSystem](Arch_AxisSystem/es.md), y se usará para propagar la ubicación de otros objetos de Arch.


</div>

<img alt="" src=images/Arch_Grid_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

*La imagen de arriba muestra una grilla de columnas, un sistema de barandillas y una ventana, cada una basada en un objeto grilla.*


</div>


<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

1.  Presione el botón **<img src="images/_Arch_Grid.png_" width= 16px> [Arch Grid](Arch_Grid/es.md)
**
2.  Establezca el **Ancho** y **Altura** de la grilla en las propiedades
3.  Ingrese al modo de edición haciendo doble clic en el objeto de la grilla en la vista de árbol
4.  Agregar filas y columnas
5.  Establezca el ancho y el alto deseados de filas y columnas haciendo doble clic en los encabezados de fila o columna


</div>

## Opciones


<div class="mw-translate-fuzzy">

-   Un ancho de columna o una altura de fila de 0 significa que su tamaño se adaptará automáticamente para ajustarse al ancho / alto total de la grilla
-   Las celdas se pueden fusionar y no fusionar seleccionándolas y haciendo clic en el botón apropiado
-   Cuando se usa como la propiedad **Eje** de otros objetos Arch, la grilla controlará el posicionamiento de estos objetos. La propiedad **Salida de puntos** define cómo se colocan los otros objetos en la grilla: en vértices, puntos medios del borde o centros de caras
-   Al establecer las propiedades **Auto Height** o **Auto Width** en un valor distinto de cero, se ignora el número total de filas / columnas y sus alturas / anchuras individuales. En cambio, se crea automáticamente la cantidad máxima de columnas o filas del auto especificado ancho / alto


</div>

## Propiedades

-    {{PropertyData/es|Rows}}: el número de filas

-    {{PropertyData/es|Columns}}: el número de columnas

-    {{PropertyData/es|Row Size}}: los tamaños para las filas

-    {{PropertyData/es|Column Size}}: los tamaños de las columnas

-    {{PropertyData/es|Points Output}}: el tipo de puntos 3D producidos por este objeto de cuadrícula

-    {{PropertyData/es|Width}}: el ancho total de esta grilla

-    {{PropertyData/es|Height}}: la altura total de esta grilla

-    {{PropertyData/es|Auto Width}}: crea divisiones de columna automáticas (se establece en 0 para deshabilitar)

-    {{PropertyData/es|Auto Height}}: crea divisiones de filas automáticas (establecido en 0 para deshabilitar)

-    {{PropertyData/es|Reorient}}: cuando está en el modo de punto medio de borde, si esta grilla debe reorientar sus hijos a lo largo de las normales de borde o no

-    {{PropertyData/es|Hidden Faces}}: los índices de caras para ocultar

## Scripting


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramienta grilla se puede usar en [macros](macros/es.md) y desde la consola de python mediante la siguiente función:


</div>


```python
Grid = makeGrid(name="Grid")
```

-   Creates a `Grid` object.

Its `Width`, `Height`, `Rows`, and `Columns` attributes can be changed directly to define the appearance of the grid.


```python
import FreeCAD, Draft, Arch
Grid = Arch.makeGrid()

Grid.Width = 5000
Grid.Height = 5000
Grid.Rows = 4
Grid.Columns = 6
FreeCAD.ActiveDocument.recompute()

Structure = Arch.makeStructure(length=200, width=200, height=100)
Draft.move(Structure, FreeCAD.Vector(-100, 0, 0))
Structure.Axis = Grid
FreeCAD.ActiveDocument.recompute() 
```


<div class="mw-translate-fuzzy">


{{docnav/es
|[Axes system](Arch_AxisSystem/es.md)
|[Roof](Arch_Roof/es.md)
|[Arch](Arch_Workbench/es.md)
|IconL=Arch_AxisSystem.png
|IconC=Workbench_Arch.svg
|IconR=Arch_Roof.svg
}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Grid/es
