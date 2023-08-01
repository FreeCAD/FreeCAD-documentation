---
- GuiCommand:/ru
   Name/ru:Вставить размер знака
   Name:TechDraw_LandmarkDimension
   MenuLocation:TechDraw → Размеры → Вставить размер знака
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   Version:0.19
   SeeAlso:[Указать горизонтальный размер](TechDraw_HorizontalDimension/ru.md), [Указать вертикальный размер](TechDraw_VerticalDimension/ru.md)
---

# TechDraw LandmarkDimension/ru


</div>



## Описание

The **TechDraw LandmarkDimension** tool adds a linear dimension to a View. The dimension is based on two Point **feature** (Draft.Point or Part.Vertex) from the 3D model. Note that the points must be **feature** objects that appear in the model [tree view](Tree_view.md). Random vertexes from a shape will not work.

The purpose of this tool is to provide a workaround to the corruption of dimension caused by \"[topological naming](Topological_naming_problem.md)\" issues. The source points should use [Expressions](Expressions.md) or other containing mechanism to establish their position. Since the points are [Document Objects](App_DocumentObject.md), and not shape components, their name does not change with recomputes, and hence they are easily found.

See [TechDraw LengthDimension](TechDraw_LengthDimension#Limitation.md) for more on dimensions and topological naming.

The Landmark Dimension generally behaves like any other Dimension.



## Применение

1.  Select 2 Point objects in the [tree view](Tree_view.md) or the [3D view](3D_view.md).
2.  Select also the View to which the dimension is to be added.
3.  Press the **<img src="images/TechDraw_LandmarkDimension.svg" width=16px> [Insert Landmark Dimension  - EXPERIMENTAL](TechDraw_LandmarkDimension.md)
** button or **TechDraw → Insert Landmark Dimension  - EXPERIMENTAL**
4.  A dimension will be added to the View. The dimension text may be dragged to the desired position.



## Ограничения

The Landmark Dimension tool is initially limited to \"Distance\" dimensions. Other types may be added if demand warrants.



## Свойства

Landmark Dimension does not introduce any new properties.



## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

The Landmark Dimension tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::LandmarkDimension','Landmark')
dim1.Type = "Distance"
dim1.References2D=[(TDView, 'Vertex1')]
dim1.References3D=[(Point3d1, 'Vertex1')]
dim1.References3D=[(Point3d2, 'Vertex1')]
rc = page.addView(dim1)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LandmarkDimension/ru
