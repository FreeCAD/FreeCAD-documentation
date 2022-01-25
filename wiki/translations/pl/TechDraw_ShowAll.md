---
- GuiCommand:
   Name:TechDraw ShowAll
   MenuLocation:TechDraw → ShowAll
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   Version:0.19
   SeeAlso:[TechDraw Change Appearance of Line(s)](TechDraw_DecorateLine.md)
---

# TechDraw ShowAll/pl

## Description

The ShowAll tool shows or hide invisible lines in a View. Note that \"invisible\" is a cosmetic state, not to be confused with hidden lines which are geometric constructs.

## Usage

1.  Select a View on a Page or in the tree.
2.  Press the **<img src="images/TechDraw_ShowAll.svg" width=16px> [Show/Hide Invisible Edges](TechDraw_ShowAll.md)** button
3.  The state of the invisible lines in the View will be reversed.

## Properties

The ShowAll tool has no properties, as it is not a Document Object.

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The effect of the ShowAll tool can be duplicated in [macros](Macros.md) or the [Python](Python.md) console. 
```python
>>> v = App.ActiveDocument.View
>>> vvo = v.ViewObject
>>> vvo.ShowAllEdges = True
>>> App.activeDocument().recompute()
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ShowAll/pl
