---
- GuiCommand:/ru
   Name/ru:Arch_Panel_Sheet
   Name:Arch_Panel_Sheet
   MenuLocation:Arch → Инструменты панели → Лист панелей
   Workbenches:[Arch](Arch_Workbench/ru.md)
   Shortcut:**P** **S**
   SeeAlso:[Arch Panel](Arch_Panel/ru.md), [Arch Panel Cut](Arch_Panel_Cut/ru.md), [Arch Nest](Arch_Nest/ru.md)
---

# Arch Panel Sheet/ru


</div>

## Описание

This tool allows to build a 2D sheet, including any number of [Arch Panel Cut](Arch_Panel_Cut.md) objects, or any other 2D object such as those made by the [Draft Workbench](Draft_Workbench.md) and [Sketcher Workbench](Sketcher_Workbench.md). The Panel Sheet is typically made to layout cuts to be made by a CNC machine. These sheets can then be exported to a [DXF](Draft_DXF.md) file.

<img alt="" src=images/Arch_Wikihouse_03.jpg  style="width:1024px;">

<img alt="" src=images/Arch_Wikihouse_04.jpg  style="width:1024px;">

*The above image shows how Panel Sheets appear when exported to DXF.*

## Применение

1.  Optionally, select one or more [Arch Panel Cut](Arch_Panel_Cut.md) objects or any other 2D object that lies on the XY plane.
2.  Press the **<img src="images/Arch_Panel_Sheet.svg" width=16px> [Arch Panel Sheet](Arch_Panel_Sheet.md)** button, or press **P** then **S** keys.
3.  Adjust the desired properties.

## Опции

-   After the panel sheet is created, with or without child objects, Any other child object can be added/removed to/from the panel sheet by double-clicking it in the tree view and adding or removing objects from its Group folder
-   Double-clicking on the panel in the tree view also allows you to move the objects contained in this sheet, or move its tag
-   It is possible to automatically make panels composed of more than one sheet of a material, by raising its Sheets property
-   Panel Sheets can display a margin, that is useful to make sure a certain space is always present between inner objects and the border of the sheet
-   When Panel sheets are exported to DXF, the outlines, inner holes, tags of their inner children are placed on different layers, as shown on the above image

## Свойства

### Данные

-    **Height**: The height of the sheet

-    **Width**: The width of the sheet

-    **Fill Ratio**: The percentage of the sheet area that is filled by cuts (automatic)

-    **Tag Text**: The text to display

-    **Tag Size**: The size of the tag text

-    **Tag Position**: The position of the tag text. Keep (0,0,0) for automatic center position

-    **Tag Rotation**: The rotation of the tag text

-    **Font File**: The font of the tag text

-    **Make Face**: If True, the panel is a Part Face, otherwise a Part Wire

-    **Grain Direction**: This allows you to inform the main direction of the panel fiber (clockwise direction, 0° means up)

### Вид

-    **Margin**: A margin that can be displayed inside the panel border

-    **Show Margin**: Turns the display of the margin on/off

-    **Show Grain**: Shows a fiber texture (Make Face must be set to True)

## Сценарии


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Panel sheet tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:


```python
Sheet = makePanelSheet(panels=[], name="PanelSheet")
```

-   Creates a `Sheet` object from `panels`, which is a list of [Arch Panel](Arch_Panel.md) objects.

Пример:


```python
import FreeCAD, Draft, Arch

Rect = Draft.makeRectangle(500, 200)
Polygon = Draft.makePolygon(5, 750)

p1 = FreeCAD.Vector(1000, 0, 0)
p2 = FreeCAD.Vector(2000, 400, 0)
p3 = FreeCAD.Vector(1250, 800, 0)
Wire = Draft.makeWire([p1, p2, p3], closed=True)

Panel1 = Arch.makePanel(Rect, thickness=36)
Panel2 = Arch.makePanel(Polygon, thickness=36)
Panel3 = Arch.makePanel(Wire, thickness=36)
FreeCAD.ActiveDocument.recompute()

Cut1 = Arch.makePanelCut(Panel1)
Cut2 = Arch.makePanelCut(Panel2)
Cut3 = Arch.makePanelCut(Panel3)
Cut1.ViewObject.LineWidth = 3
Cut2.ViewObject.LineWidth = 3
Cut3.ViewObject.LineWidth = 3
FreeCAD.ActiveDocument.recompute()

Sheet = Arch.makePanelSheet([Cut1, Cut2, Cut3])
```

## Учебники

-   [Wikihouse porting tutorial](Wikihouse_porting_tutorial.md)


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Panel Sheet/ru
