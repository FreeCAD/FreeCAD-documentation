---
- GuiCommand:
   Name:TechDraw Symbol
   MenuLocation:TechDraw → Insert SVG Symbol
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   SeeAlso:[TechDraw Templates](TechDraw_Templates.md), [Draft SVG](Draft_SVG.md)
---

# TechDraw Symbol/pl

## Description

The Symbol tool inserts an [SVG](SVG.md) file into the page. This symbol can be anything that helps annotating your drawing, and that doesn\'t need to be further modified.

<img alt="" src=images/TechDraw_SymbolSVG_sample.png  style="width:250px;"> 
*Compass rose added to the drawing page; this symbol is available by installing the "symbols_library" addon with the [Addon Manager](Std_AddonMgr.md)*

## Usage

1.  Press the **<img src="images/TechDraw_Symbol.svg" width=16px> [Insert SVG Symbol](TechDraw_Symbol.md)** button
2.  A File Save dialog will open.
3.  Select a location and file name.
4.  Press **OK**

If the symbol appears larger than expected, use the scale property to adjust its size.

## Notes

-    **Scale Type**for Symbols is always set to *Custom* at creation. This is for convenience, since symbols are almost always scaled differently from the rest of the objects on the page.

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Symbol tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
sym = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewSymbol','TestSymbol')
rc = page.addView(anno)
f = open(unicode(symbolFileSpec,'utf-8'),'r')
svg = f.read()
f.close()
sym.Symbol = svg
rc = page.addView(sym)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Symbol/pl
