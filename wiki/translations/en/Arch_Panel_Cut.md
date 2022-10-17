---
- GuiCommand   *
   Name   *Arch Panel Cut
   MenuLocation   *Arch → Panel tools → Panel Cut
   Workbenches   *[Arch](Arch_Workbench.md), [Path](Path_Workbench.md)
   Shortcut   ***P** **C**
   Version   *0.17
   SeeAlso   *[Arch Panel](Arch_Panel.md), [Arch Panel Sheet](Arch_Panel_Sheet.md), [Arch Nest](Arch_Nest.md)
---

# Arch Panel Cut/en

## Description

This tool creates, in the 3D document, a flat, 2D view of an [Arch Panel](Arch_Panel.md), to be included in an [Arch Panel Sheet](Arch_Panel_Sheet.md) or directly exported to [DXF](Draft_DXF.md). The Panel Cut objects are also supported by the [Path Workbench](Path_Workbench.md).

<img alt="" src=images/Arch_Wikihouse_02.jpg  style="width   *1024px;">

## Usage

1.  Select one or more [Arch Panel](Arch_Panel.md) objects.
2.  Press the **<img src="images/Arch_Panel_Cut.svg" width=16px> [Arch Panel Cut](Arch_Panel_Cut.md)** button, or press **P** then **C** keys.
3.  Adjust the desired properties.

## Options

-   If the panel is not flat (corrugated, for example), the relief won\'t appear in the Panel cut. This tool is useful mainly for flat panels
-   The panel cut can display a tag. This tag can be a custom line of text or can automatically show the Tag, Label or Description of its linked Panel.
-   To be useful for CNC machining, the tag should be written using a stick font, where letters are simple polylines that are easy for the machine to follow. Upon creation, the Panel Cut object will automatically use the font specified in Edit → Preferences → Draft → Texts and Dimensions → Default ShapeString font file
-   Double-clicking on the panel cut in the tree view after it is created allows you to enter edit mode and modify the position of the tag
-   When you need to layout different Panel Cuts together, Panel Cuts can display a margin, that is useful to make sure a certain space is always present between a cut and another

## Properties

### Data

-    **Source**   * The [Arch Panel](Arch_Panel.md) object shown by this Cut

-    **Tag Text**   * The text to display. Can be %tag%, %label% or %description% to display the panel tag or label

-    **Tag Size**   * The size of the tag text

-    **Tag Position**   * The position of the tag text. Keep (0,0,0) for automatic center position

-    **Tag Rotation**   * The rotation of the tag text

-    **Font File**   * The font of the tag text

-    **Make Face**   * If True, the panel is a Part Face, otherwise a Part Wire

### View

-    **Margin**   * A margin that can be displayed outside the panel cut shape

-    **Show Margin**   * Turns the display of the margin on/off

## Scripting


**See also   ***

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Panel Cut tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function   * 
```python
View = makePanelCut(panel, name="PanelView")```

-   Creates a `View` object (2D projection) from the existing `panel`.

Example   * 
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



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Panel Cut/en
