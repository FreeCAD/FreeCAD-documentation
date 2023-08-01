---
- GuiCommand:/ru
   Name/ru:Вставить знак
   Name:TechDraw_Symbol
   MenuLocation:TechDraw → Вставить SVG знак
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   SeeAlso:[Шаблоны](TechDraw_Templates/ru.md), [Draft SVG](Draft_SVG/ru.md)
---

# TechDraw Symbol/ru


</div>



## Описание

The **TechDraw Symbol** tool inserts an [SVG](SVG.md) file into the page. This symbol can be anything that helps annotating your drawing, and that doesn\'t need to be further modified.

<img alt="" src=images/TechDraw_SymbolSVG_sample.png  style="width:250px;"> 
*Compass rose added to the drawing page; this symbol is available by installing the "symbols_library" addon with the [Addon Manager](Std_AddonMgr.md)*



## Применение

1.  If there are multiple drawing pages in the document: optionally activate the desired page by selecting it in the [Tree view](Tree_view.md).
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_Symbol.svg" width=16px> [Insert SVG Symbol](TechDraw_Symbol.md)** button.
    -   Select the **TechDraw → TechDraw Views → <img src="images/TechDraw_Symbol.svg" width=16px> Insert SVG Symbol** option from the menu.
3.  If there are multiple drawing pages in the document and you have not yet activated a page, the **Page Chooser** dialog box opens: <small>(v0.20)</small> 
    1.  Select the desired page.
    2.  Press the **OK** button.
4.  A file dialog opens.
5.  Select a location and file name.
6.  The symbol is inserted.
7.  Optionally change its **Scale** property to adjust its size.



## Примечания

-    **Scale Type**for Symbols is always set to *Custom* at creation. This is for convenience, since symbols are almost always scaled differently from the rest of the objects on the page.

## Properties

See also [TechDraw View](TechDraw_View#Properties.md).


{{TitleProperty|Drawing view}}

-    **Editable Texts**: List of editable texts, if any.



## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

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
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Symbol/ru
