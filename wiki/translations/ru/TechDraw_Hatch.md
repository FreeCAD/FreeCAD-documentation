---
- GuiCommand:/ru
   Name/ru:Штриховка
   Name:TechDraw_Hatch
   MenuLocation:TechDraw → Штриховать грань, используя файл изображения
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   SeeAlso:[Применить геометрическую штриховку к грани](TechDraw_GeometricHatch/ru.md), [Штриховка](TechDraw_Hatching/ru.md)
---

# TechDraw Hatch/ru

## Описание

The <img alt="" src=images/TechDraw_Hatch.svg  style="width:24px;"> **TechDraw Hatch** tool fills a closed region in a View with a tiled [SVG](SVG.md) or bitmap (<small>(v1.0)</small> ) based hatch pattern. Alternatively the <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:16px;"> [TechDraw GeometricHatch](TechDraw_GeometricHatch.md) tool uses PAT based hatch patterns. See [Hatching](TechDraw_Hatching.md) for details.

<img alt="" src=images/TechDraw_Hatch_example.png  style="width:300px;">



*SVG hatch pattern on a face*

## Применение

1.  Select a closed region in a View.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_Hatch.svg" width=16px> [TechDraw Hatch](TechDraw_Hatch.md)** button.
    -   Select the **TechDraw → <img src="images/TechDraw_Hatch.svg" width=16px> Hatch a Face using Image File** option from the menu.
3.  The **Apply Hatch to Face** task panel opens.
4.  Optionally change the **Pattern File**.
5.  Optionally change the **Pattern Scale** and the **Line Color**. These settings are ignored for bitmap patterns.
6.  Press the **OK** button.

## Примечания

-   Hatching objects are vulnerable to the \"[topological naming problem](Topological_naming_problem.md)\". See [TechDraw LengthDimension](TechDraw_LengthDimension.md) for more information. It is recommended that hatching be one of the last steps in your drawing process.
-   Sample [SVG](SVG.md) patterns are available locally in:

:   
    
```python
    $INSTALL_DIR/data/Mod/TechDraw/Patterns
    
```
    

:   Where `$INSTALL_DIR` is the directory where FreeCAD was installed, for example:

:   
    
```python
    /usr/share/freecad/data/Mod/TechDraw/Patterns
    
```
    

:   They are also available on [GitHub](https://github.com/FreeCAD/FreeCAD/tree/master/src/Mod/TechDraw/Patterns).

## Свойства

-    **Source**: The View and Face to receive the hatch pattern.

-    **Hatch Pattern**: Full path and filename to an SVG pattern file.

-    **Hatch Color**: Hatch pattern will be displayed in this color.

-    **Hatch Scale**: Hatch pattern size modifier.

## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

The Hatch tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
hatch = FreeCAD.ActiveDocument.addObject('TechDraw::DrawHatch','Hatch')
hatch.Source = (view1,["Face0"])
hatch.HatchPattern = hatchFileSpec
rc = page.addView(hatch)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Hatch/ru
