---
- GuiCommand:
   Name:Draft FlipDimension
   MenuLocation:Modification → Flip dimension
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
---

# Draft FlipDimension/pt-br

## Descrição

The <img alt="" src=images/Draft_FlipDimension.svg  style="width:24px;"> **Draft FlipDimension** command rotates the dimension text of selected [Draft Dimensions](Draft_Dimension.md) 180° around the dimension line. It can be used to correct dimensions whose text appears mirrored. The command does not work properly for angular dimensions.

## Utilização

1.  Select one or more [Draft Dimensions](Draft_Dimension.md).
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_FlipDimension.svg" width=16px> [Draft FlipDimension](Draft_FlipDimension.md)** button.
    -   Select the **Modification → <img src="images/Draft_FlipDimension.svg" width=16px> Flip dimension** option from the menu.

## Notas

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


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft FlipDimension/pt-br
