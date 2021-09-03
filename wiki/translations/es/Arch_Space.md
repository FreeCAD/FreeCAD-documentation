---
- GuiCommand:/es
   Name:Arch Space   Name/es:Arch Espacio
   MenuLocation:Arch → Space
   Workbenches:[Arch](Arch_Module/es.md)
   Shortcut:**S** **P**
   SeeAlso:[[Arch Wall/es]], [[Arch Structure/es]]
   Version:0.14
---


</div>


<div class="mw-translate-fuzzy">

## Descripción

La herramienta Espacio le permite definir un volumen vacío, ya sea basado en una forma sólida, o definiendo sus límites, o una combinación de ambos. Si se basa únicamente en los límites, el volumen se calcula comenzando desde el cuadro delimitador de todos los límites dados, y restando los espacios detrás de cada límite. El objeto espacio siempre define un volumen sólido. El área del suelo de un objeto espacio, calculado mediante la intersección de un plano horizontal en el centro de masa del volumen del espacio, también se puede visualizar, configurando el modo de visualización del objeto espacial a \"detallado\".


</div>

<img alt="" src=images/Arch_Space_example.jpg  style="width:640px;">


<div class="mw-translate-fuzzy">

*En la imagen de arriba, un objeto espacial se crea a partir de un objeto sólido existente, luego se agregan dos caras de muro como límites, y el modo de visualización se establece en \"detallado\" para mostrar el área del piso.*


</div>


<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

1.  Seleccione un objeto sólido existente o caras en objetos de contorno
2.  Presione el botón {{KEY | <img src="images/_Arch_Space.png_" width= 16px> [[Arch Space]]}}, o presione las teclas {{KEY | S}}, {{KEY | P}}


</div>


<div class="mw-translate-fuzzy">

## Limitaciones


</div>


<div class="mw-translate-fuzzy">

-   No disponible antes de la versión 0.14 de FreeCAD
-   Las propiedades de límites actualmente no se pueden editar a través de GUI
-   Ver el [anuncio del foro](http://forum.freecadweb.org/viewtopic.php?f=9&t=4275)


</div>

## Propiedades


<div class="mw-translate-fuzzy">

-    {{PropertyData/es|Base}}: El objeto base, si lo hay (debe ser un sólido)

-    {{PropertyData/es|Boundaries}}: Una lista de elementos de límite opcionales


</div>

-    **Text**: The text to show. Use \$area, \$label, \$tag, \$floor, \$walls, \$ceiling to insert the respective data

-    **FontName**: The name of the font

-    **TextColor**: The color of the text

-    **FontSize**: The size of the text

-    **FirstLine**: The size of the first line of text (multiplies the font size. 1 = same size, 2 = double size, etc..)

-    **LineSpacing**: The space between the lines of text

-    **TextPosition**: The position of the text. Leave (0,0,0) for automatic position

-    **TextAlign**: The justification of the text

-    **Decimals**: The number of decimals to use for calculated texts

-    **ShowUnit**: Show the unit suffix or not

## Options

-   To create zones that group several spaces, use a [Arch BuildingPart](Arch_BuildingPart.md) and set its IFC type to \"Spatial Zone\"
-   The space object has the same display modes as other Arch and Part objects, with one more, called **Footprint**, that displays only the bottom face of the space. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramienta de espacio se puede usar en scripts de Python y [macros/es](macros/es.md) usando la siguiente función:


</div>


```python
Space = makeSpace(objects=None, baseobj=None, name="Space")
```


<div class="mw-translate-fuzzy">

-   Crea un objeto espacio a partir de los objetos dados.
-   Los objetos pueden ser un objeto de documento, en cuyo caso se convierte en la forma básica del objeto de espacio, o una lista de objetos de selección como se devuelve por FreeCADGui.Selection.getSelectionEx(), o una lista de tuplas (object, subobjectname).
-   Devuelve el objeto espacial recién creado.


</div>

Ejemplo: 
```python
import FreeCAD, Arch

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 1000
Box.Width = 1000
Box.Height = 1000

Space = Arch.makeSpace(Box)
Space.ViewObject.LineWidth = 2
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">

Después de crear un objeto espacio, se pueden agregar caras seleccionadas con la siguiente función:


</div>


```python
import FreeCAD, FreeCADGui, Draft, Arch

points = [FreeCAD.Vector(-500, 0, 0), FreeCAD.Vector(1000, 1000, 0)]
Line = Draft.makeWire(points)
Wall = Arch.makeWall(Line, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

# Select a face of the wall
selection = FreeCADGui.Selection.getSelectionEx()
Arch.addSpaceBoundaries(Space, selection)
```


<div class="mw-translate-fuzzy">

Los límites también se pueden eliminar con:


</div>


```python
selection = FreeCADGui.Selection.getSelectionEx()
Arch.removeSpaceBoundaries(Space, selection)
```


<div class="mw-translate-fuzzy">


{{docnav/es|[Roof](Arch_Roof/es.md)|[Stairs](Arch_Stairs/es.md)|[Arch](Arch_Module/es.md)|IconL=Arch_Roof.svg |IconC=Workbench_Arch.svg |IconR=Arch_Stairs.svg}}


</div>


 
