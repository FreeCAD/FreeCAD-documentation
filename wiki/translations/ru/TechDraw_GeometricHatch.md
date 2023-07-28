---
- GuiCommand:/ru
   Name/ru:Применить геометрическую штриховку к грани
   Name:TechDraw_GeometricHatch
   MenuLocation:TechDraw → Применить геометрическую штриховку к грани
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   SeeAlso:[Штриховать грань, используя файл изображения](TechDraw_Hatch/ru.md), [Штриховка](TechDraw_Hatching/ru.md)
---

# TechDraw GeometricHatch/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Инструмент GeometricHatch заполняет замкнутый регион внутри вида шаблоном, базирующимся на спецификации AutoDesk PAT hatching. **В качестве альтернативы**, инструмент [Hatch](TechDraw_Hatch/ru.md) использует качестве рисунка штриховки файл в формате [SVG](SVG/ru.md) или [растровый](bitmap/ru.md), подробности см. в [Hatching](TechDraw_Hatching/ru.md).


</div>

<img alt="" src=images/TechDraw_GeomHatch_example.png  style="width:300px;"> 
*Геометрический узор штриховки на грани*



## Применение

1.  Select a closed region in a View.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_GeometricHatch.svg" width=16px> [TechDraw GeometricHatch](TechDraw_GeometricHatch.md)** button.
    -   Select the **TechDraw → Hatching → <img src="images/TechDraw_GeometricHatch.svg" width=16px> Apply Geometric Hatch to Face** option from the menu.
3.  The **Apply Geometric Hatch to Face** task panel opens.
4.  Optionally change the **Pattern File**, the **Pattern Name**, the **Pattern Scale**, the **Line Weight** and the **Line Color**.
5.  Press the **OK** button.



## Примечания

-   Hatching objects are vulnerable to the \"[topological naming problem](Topological_naming_problem.md)\". See [TechDraw LengthDimension](TechDraw_LengthDimension.md) for more information. It is recommended that hatching be one of the last steps in your drawing process.

A small set of sample patterns are available in:


```python
$INSTALL_DIR/data/Mod/TechDraw/PAT/FCPAT.pat
```


`$INSTALL_DIR`

is the directory where FreeCAD was installed, for example


```python
/usr/share/freecad/data/Mod/TechDraw/PAT/FCPAT.pat
```



## Свойства

-    **Source**: The View and Face to receive the hatch pattern.

-    **File Pattern**: The location of the PAT file to use.

-    **Name Pattern**: The name of the PAT specification within File Pattern.

-    **Scale Pattern**: The scale to be applied to the pattern (must be \> 0.0).

-    **Weight Pattern**: The thickness of the pattern lines.

-    **Color Pattern**: The color for the pattern lines.



## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

A GeometricHatch can be created with [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
hatch = FreeCAD.ActiveDocument.addObject("TechDraw::DrawGeomHatch", "GeomHatch")
hatch.Source = (view1, ["Face0"])
hatch.FilePattern = "path/to/myPATfile.pat"
hatch.NamePattern = "Diamond"
page.addView(hatch)
```

It is also possible to use TechDraw\'s geometric hatch engine to produce a compound object in the 3D space. One must take care that the base face lies on the XY plane, as the algorithm is not tailored yet for other cases:


```python
import TechDraw
face = Part.makePlane(10, 10)
patfile = "path/to/myPATfile.pat"
pattern = "Diamond"
scale = 10
hatch = TechDraw.makeGeomHatch(face, scale, pattern, patfile)
Part.show(hatch)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw GeometricHatch/ru
