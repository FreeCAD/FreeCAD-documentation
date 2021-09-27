---
- GuiCommand:/es
   Name:Draft FlipDimension
   Name/es:Draft FlipDimension
   MenuLocation:Draft → Utilities → Flip Dimension
   Workbenches:[Draft](Draft_Workbench/es.md), [Arch](Arch_Workbench/es.md)
   SeeAlso:[Dimension](Draft_Dimension/es.md)
---

# Draft FlipDimension/es


</div>

## Description


<div class="mw-translate-fuzzy">

## Descripción

Cuando está en modo 2D, el texto de [Dimensiones de borrador](Draft_Dimension.md) se muestra alineado con la línea de dimensión. La herramienta Dimensión siempre intenta mostrarle el texto de la dimensión en el lado correcto de la línea de dimensión, dependiendo de dónde lo esté viendo. En algunos casos, sin embargo, la dirección de visualización puede no reflejar la intención del espectador, y la orientación del texto de cota puede invertirse. Esta herramienta invierte esa orientación en los objetos [ dimensión](Draft_Dimension.md) seleccionados.


</div>

## Usage


<div class="mw-translate-fuzzy">

## Utilización

1.  Seleccione uno o más objetos [dimension](Draft_Dimension.md)
2.  Presione el botón **<img src="images/Draft_FlipDimension.png" width=16px> [Flip Dimension](Draft_FlipDimension.md)
**


</div>

## Notes

-   [Draft Dimensions](Draft_Dimension.md) also have a **Flip Text** property. When set to `True` the text is rotated 180° around the normal direction. This can be combined with the effect of this command.

## Scripting

See also: _.

To flip a [Draft Dimension](Draft_Dimension.md) invert its `Normal` property.

Example:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 0, 0)
p3 = App.Vector(500, 300, 0)
dimension = Draft.make_dimension(p1, p2, p3)
dimension.ViewObject.FontSize = 200

dimension.Normal = dimension.Normal.negative()
doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft FlipDimension/es
