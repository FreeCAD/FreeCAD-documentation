---
- GuiCommand   */es
   Name   *Arch Frame
   Name/es   *Arch Frame
   MenuLocation   *Arch → Frame
   Workbenches   *[Arch](Arch_Workbench/es.md)
   Shortcut   ***F** **R**
   SeeAlso   *[[Arch Wall/es]], [[Arch Structure/es]]
---

# Arch Frame/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

La herramienta armazón se usa para construir todo tipo de objetos de armazón basados en un perfil y un diseño. El perfil se extruye a lo largo de los bordes del diseño, que puede ser cualquier objeto 2D como un [sketch](Sketcher_Workbench/es.md), o un [draft object](Draft_Workbench/es.md). Es especialmente útil crear barandas o muros de armazón. Los objetos de armazón pueden convertirse fácilmente en objetos [wall](Arch_Wall/es.md) o [structure](Arch_Structure/es.md) .


</div>

<img alt="" src=images/Arch_Frame_example.jpg  style="width   *640px;">


<div class="mw-translate-fuzzy">

*En la imagen de arriba, un [line](Draft_Line/es.md) se ha convertido en un [array](Draft_Array/es.md), y un objeto de armazón se ha hecho usando el arreglo como layout, y un [circle](Draft_Circle/es.md) como perfil.*


</div>


<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

1.  Crear un layout objeto y un objeto de perfil, por ejemplo con el [Draft Workbench](Draft_Workbench/es.md) o el [Sketcher Workbench](Sketcher_Workbench/es.md)
2.  Seleccione primero el objeto de layout, luego, con **CTRL** presionado, seleccione el objeto perfil
3.  Presiona el botón **<img src="images/_Arch_Frame.png" width=16px> [Arch Frame](Arch_Frame/es.md)
**, o presiona **F** y luego la tecla **R**


</div>

## Opciones


<div class="mw-translate-fuzzy">

-   Los armazones comparten las propiedades y los comportamientos comunes de todos [Arch Components](Arch_Component/es.md)
-   El objeto de armazón se puede colocar a cierta distancia del objeto de layout, estableciendo su propiedad de Desplazamiento/Offset
-   El perfil se copiará en la base de cada borde del objeto de layout y luego se extruirá a lo largo de él. Puede controlar cómo se coloca el perfil en la base de cada borde con las propiedades Alinear y Rotación.


</div>

## Propiedades

-    {{PropertyData/es|Base}}   * el layout en el que se basa este armazón.

-    {{PropertyData/es|Profile}}   * el perfil en el que se basa este armazón.

-    {{PropertyData/es|Align}}   * Especifica si el perfil debe girarse para que su eje normal esté alineado con cada borde.

-    {{PropertyData/es|Offset}}   * una distancia opcional entre el objeto de layout y el objeto de armazón.

-    {{PropertyData/es|Rotation}}   * la rotación del perfil alrededor de su eje de extrusión.

## Scripting


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramienta Armazón se puede utilizar en [macros](macros/es.md) y desde la consola de Python mediante la siguiente función   *


</div>


```python
Frame = makeFrame(baseobj, profile)
```


<div class="mw-translate-fuzzy">

-   Crea un objeto de armazón a partir de un Sketch base (o cualquier otro objeto que contenga wires cerrados) y un objeto de perfil (un objeto 2D extruible que contiene caras o wires cerrados)
-   Devuelve el nuevo objeto de armazón, o ninguno si la operación falló.


</div>

Ejemplo   * 
```python
import Draft, Arch

Line = Draft.makeLine(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 2000))
baseobj = Draft.makeArray(Line, FreeCAD.Vector(1000, 0, 0), FreeCAD.Vector(0, 1, 0), 6, 1)

profile = Draft.makeCircle(200)
Frame = Arch.makeFrame(baseobj, profile)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


{{docnav/es|[Nest](Arch_Nest.md)|[Fence](Arch_Fence.md)|[Arch](Arch_Workbench.md)|IconL=Arch_Nest.svg |IconC=Workbench_Arch.svg |IconR=Arch_Fence.svg}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Frame/es
