# TechDraw Symbol/ro
---
- GuiCommand   *   Name   *TechDraw  Symbol   Workbenches   *[[TechDraw Workbench   TechDraw]]|MenuLocation   *TechDraw → Symbol   Shortcut   *   SeeAlso   *---


</div>


<div class="mw-translate-fuzzy">

## Descriere

Instrumentul Simbol inserează un fișier SVG în pagină ca vizualizare


</div>

The Symbol tool inserts an [SVG](SVG.md) file into the page. This symbol can be anything that helps annotating your drawing, and that doesn\'t need to be further modified.

<img alt="" src=images/TechDraw_SymbolSVG_sample.png  style="width   *250px;"> 
*Compass rose added to the drawing page; this symbol is available by installing the "symbols_library" addon with the [Addon Manager](Std_AddonMgr.md)*


<div class="mw-translate-fuzzy">

## Cum se utilizează 

1.  Apăsați butonul Press the **<img src="images/Symbol.png" width=24px> [Symbol](TechDraw_Symbol.md)
**
2.  Se va deschide un dialog de salvare a fișierelor. Selectați o locație și un nume de fișier.


</div>

1.  Press the **<img src="images/TechDraw_Symbol.svg" width=16px> [Insert SVG Symbol](TechDraw_Symbol.md)** button
2.  A File dialog will open.
3.  Select a location and file name.
4.  Press **OK**

If the symbol appears larger than expected, use the scale property to adjust its size.

## Notes

-    **Scale Type**for Symbols is always set to *Custom* at creation. This is for convenience, since symbols are almost always scaled differently from the rest of the objects on the page.

## Properties

See also [TechDraw View](TechDraw_View#Properties.md).


{{TitleProperty|Drawing view}}

-    **Editable Texts**   * List of editable texts, if any.


<div class="mw-translate-fuzzy">

## Script

SVG pot fi inserate într-o pagină de desen folosind Python.


</div>


**See also   ***

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Symbol tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions   *


```python
sym = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewSymbol','TestSymbol')
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
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Symbol/ro
