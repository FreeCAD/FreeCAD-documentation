---
- GuiCommand:/ru
   Name:Arch Panel Cut
   Name/ru:Arch Panel Cut
   MenuLocation:Arch → Panel Tools → Нарезка панелей
   Workbenches:[Arch](Arch_Workbench/ru.md), [Path](Path_Workbench/ru.md)
   Shortcut:**P** **C**
   SeeAlso:[Arch Panel](Arch_Panel/ru.md), [Arch Panel Sheet](Arch_Panel_Sheet/ru.md), [Arch Nest](Arch_Nest/ru.md)
---


</div>

## Описание


<div class="mw-translate-fuzzy">

Этот инструмент создает в 3D-документе плоский 2D-просмотр [Arch Panel](Arch_Panel.md), который должен быть включен в [Arch Panel Sheet](Arch_Panel_Sheet.md) или напрямую экспортирован в [ DXF](Draft_DXF.md). Объекты Panel Cut также поддерживаются [Path Workbench](Path_Workbench.md).


</div>

<img alt="" src=images/Arch_Wikihouse_02.jpg  style="width:1024px;">

## Использование

1.  Select one or more [Arch Panel](Arch_Panel.md) objects.
2.  Press the **<img src="images/Arch_Panel_Cut.svg" width=16px> [Arch Panel Cut](Arch_Panel_Cut.md)** button, or press **P** then **C** keys.
3.  Adjust the desired properties.

## Options

-   If the panel is not flat (corrugated, for example), the relief won\'t appear in the Panel cut. This tool is useful mainly for flat panels
-   The panel cut can display a tag. This tag can be a custom line of text or can automatically show the Tag, Label or Description of its linked Panel.
-   To be useful for CNC machining, the tag should be written using a sticky font, where letters are simple polylines that are easy for the machine to follow. Upon creation, the Panel Cut object will automatically use the font specified in Edit → Preferences → Draft → Texts and Dimensions → ShapeString Font
-   Double-clicking on the panel cut in the tree view after it is created allows you to enter edit mode and modify the position of the tag
-   When you need to layout different Panel Cuts together, Panel Cuts can display a margin, that is useful to make sure a certain space is always present between a cut and another

## Properties

### Data

-    **Source**: The [Arch Panel](Arch_Panel.md) object shown by this Cut

-    **Tag Text**: The text to display. Can be %tag%, %label% or %description% to display the panel tag or label

-    **Tag Size**: The size of the tag text

-    **Tag Position**: The position of the tag text. Keep (0,0,0) for automatic center position

-    **Tag Rotation**: The rotation of the tag text

-    **Font File**: The font of the tag text

-    **Make Face**: If True, the panel is a Part Face, otherwise a Part Wire

### View

-    **Margin**: A margin that can be displayed outside the panel cut shape

-    **Show Margin**: Turns the display of the margin on/off

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Panel Cut tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function: 
```python
View = makePanelCut(panel, name="PanelView")```

-   Creates a `View` object (2D projection) from the existing `panel`.

Example: 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(500, 0, 0)
p3 = FreeCAD.Vector(500, 50, 0)
p4 = FreeCAD.Vector(550, 50, 0)
p5 = FreeCAD.Vector(600, 0, 0)
p6 = FreeCAD.Vector(1000, 0, 0)
p7 = FreeCAD.Vector(1000, 400, 0)
p8 = FreeCAD.Vector(600, 400, 0)
p9 = FreeCAD.Vector(600, 350, 0)
p10 = FreeCAD.Vector(550, 350, 0)
p11 = FreeCAD.Vector(500, 400, 0)
p12 = FreeCAD.Vector(0, 400, 0)

Wire = Draft.makeWire([p1, p2, p3, p4, p5, p6,
                       p7, p8, p8, p9, p10, p11, p12], closed=True)
Panel = Arch.makePanel(Wire, thickness=36)
FreeCAD.ActiveDocument.recompute()

View = Arch.makePanelCut(Panel)
View.ViewObject.LineWidth = 3
FreeCAD.ActiveDocument.recompute()
```

## Tutorials

-   [Wikihouse porting tutorial](Wikihouse_porting_tutorial.md)


<div class="mw-translate-fuzzy">


{{docnav/ru|[Panel](Arch_Panel.md)|[Panel Sheet](Arch_Panel_Sheet.md)|[Arch](Arch_Workbench/ru.md)|IconL=Arch_Panel.svg |IconC=Workbench_Arch.svg |IconR=Arch_Panel_Sheet.svg}}


</div>


 
